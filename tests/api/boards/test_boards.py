import random
from http import HTTPStatus
from typing import Any

import allure
import pytest
from allure_commons.types import Severity
from faker import Faker
from pydantic import TypeAdapter

from core.api.clients.boards.boards_client import get_boards_client
from core.api.clients.boards.boards_schems import (
    BoardSchema,
    RequestCreateBoardSchema,
    RequestUpdateBoardSchema,
)
from tools.allure.allure_enum import AllureEpics, AllureFeature, AllureStory, AllureTags
from tools.assertion.base import assert_status_code, assert_equal, assert_is_true
from tools.assertion.schema import validate_json_schema

fake = Faker()


def parse_dict(
    dict_with_changes: dict[str, Any], old_dict: dict[str, Any]
) -> dict[str, Any]:
    for key, value in dict_with_changes.items():
        old_dict[key] = value
    return old_dict


@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.BOARDS)
@allure.story(AllureStory.BOARD_OPERATIONS)
@allure.tag(AllureTags.BOARD, AllureTags.CREATE_BOARD)
@allure.severity(Severity.CRITICAL)
@pytest.mark.api
@pytest.mark.regression
class TestBoards:

    @allure.title("Get all public boards")
    def test_get_public_boards(self):
        client = get_boards_client()
        response = client.get_all_public_boards()
        response_data = response.json()

        adapter = TypeAdapter(list[BoardSchema])
        adapter.validate_python(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title("Get public board by id")
    def test_get_random_public_boards_by_id(self, get_id_public_boards):
        public_board_ids = get_id_public_boards
        board_index = random.randint(0, len(public_board_ids))
        board_id = public_board_ids[board_index]
        client = get_boards_client()
        response = client.get_public_board_by_id(board_id=board_id)
        response_data = BoardSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_equal(response.json().get("id"), board_id, "Board ID")
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get all boards for current user")
    def test_get_all_current_user_boards(self):
        client = get_boards_client()
        response = client.get_current_user_boards()
        response_data = response.json()

        adapter = TypeAdapter(list[BoardSchema])
        adapter.validate_python(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_is_true(len(response_data) <= 100, "List board length")

    @allure.title("Create board (public / private)")
    @pytest.mark.parametrize("is_public", [True, False], ids=["public", "private"])
    def test_create_board(
        self,
        delete_board,
        is_public,
    ):
        board_title = fake.text(max_nb_chars=20)
        board_description = fake.text(max_nb_chars=100)
        request = RequestCreateBoardSchema(
            title=board_title,
            description=board_description,
            public=is_public,
        )
        try:
            client = get_boards_client()
            response = client.create_board(request)
            response_data = BoardSchema.model_validate_json(response.text)

            assert_status_code(response.status_code, HTTPStatus.CREATED)
            assert_equal(response.json().get("title"), board_title, "Board title")
            assert_equal(
                response.json().get("description"),
                board_description,
                "Board description",
            )
            if is_public:
                assert_is_true(response.json().get("public"), "Board public")
            else:
                assert_is_true(not response.json().get("public"), "Board private")

            validate_json_schema(response.json(), response_data.model_json_schema())
        finally:
            delete_board.append(board_title)

    @allure.title("Get board by id")
    def test_get_board_by_id(self, create_board, delete_board):
        try:
            board = create_board
            client = get_boards_client()
            response = client.get_board_by_id(board["id"])
            response_data = BoardSchema.model_validate_json(response.text)

            assert_status_code(response.status_code, HTTPStatus.OK)
            assert_equal(response.json().get("id"), board["id"], "ID")
            assert_equal(response.json().get("title"), board["title"], "Board title")
            assert_equal(
                response.json().get("description"),
                board["description"],
                "Board description",
            )
            assert_equal(response.json().get("public"), board["public"], "Board public")
            validate_json_schema(response.json(), response_data.model_json_schema())
        finally:
            delete_board.append(board["title"])

    @allure.title("Update board (partial payload)")
    @pytest.mark.parametrize(
        "dict_with_changes",
        [
            {
                "title": fake.text(max_nb_chars=20),
                "description": fake.text(max_nb_chars=20),
                "public": False,
                "archived": True,
            },
            {"title": fake.text(max_nb_chars=20)},
            {
                "description": fake.text(max_nb_chars=20),
            },
            {
                "public": False,
            },
            {"archived": True},
        ],
        ids=["all", "title", "description", "public", "archived"],
    )
    def test_update_board(self, create_board, delete_board, dict_with_changes):
        try:
            old_board = create_board
            new_board = parse_dict(dict_with_changes, old_board)
            client = get_boards_client()
            request = RequestUpdateBoardSchema(**new_board)
            response = client.update_board_by_id(request, new_board["id"])
            response_data = BoardSchema.model_validate_json(response.text)

            assert_status_code(response.status_code, HTTPStatus.OK)
            assert_equal(
                response.json().get("title"), new_board["title"], "Board title"
            )
            assert_equal(
                response.json().get("description"),
                new_board["description"],
                "Board description",
            )
            assert_equal(
                response.json().get("public"), new_board["public"], "Board public"
            )
            assert_equal(
                response.json().get("archived"), new_board["archived"], "Board archived"
            )
            validate_json_schema(response.json(), response_data.model_json_schema())
        finally:
            delete_board.append(new_board["title"])

    @allure.title("Delete board by id")
    def test_delete_board_by_id(self, create_board):
        board = create_board
        client = get_boards_client()
        response = client.delete_board_by_id(board["id"])

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)

    @allure.title("Delete board with invalid id returns not found")
    def test_delete_board_with_invalid_id(self, get_id_all_boards):
        invalid_id = get_id_all_boards[-1] + 1
        client = get_boards_client()
        response = client.delete_board_by_id(invalid_id)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)
