from httpx import Response

from config import settings
from core.api.clients.api_client import APIClient
from core.api.clients.boards.boards_schems import RequestCreateBoardSchema, RequestUpdateBoardSchema
from core.api.clients.private_http_builder import get_private_http_client


class BoardsClient(APIClient):
    def get_all_public_boards(self)->Response:
        return self.get(
            url=f"{settings.API_URL}/boards/public",
        )

    def get_public_board_by_id(self, board_id: int)->Response:
        return self.get(
            url=f"{settings.API_URL}/boards/public/{board_id}",
        )

    def get_current_user_boards(self, skip: int = 0, limit: int = 100, archived: bool = False)->Response:
        query_params = {
            "skip": skip,
            "limit": limit,
            "archived": archived,
        }
        return self.get(
            url=f"{settings.API_URL}/boards/",
            params=query_params,
        )

    def create_board(self, request: RequestCreateBoardSchema)->Response:
        return self.post(
            url=f"{settings.API_URL}/boards/",
            request=request,
        )

    def get_board_by_id(self, board_id: int)->Response:
        return self.get(
            url=f"{settings.API_URL}/boards/{board_id}",
        )

    def update_board_by_id(self, request: RequestUpdateBoardSchema, board_id)->Response:
        return self.put(
            url=f"{settings.API_URL}/boards/{board_id}",
            request=request,
        )
    def delete_board_by_id(self, board_id: int)->Response:
        return self.delete(
            url=f"{settings.API_URL}/boards/{board_id}",
        )

    def add_member_to_board_by_id(self, board_id: int, member_id: int)->Response:
        return self.post(
            url=f"{settings.API_URL}/boards/{board_id}/members/{member_id}"
        )

    def delete_member_from_board_by_id(self, board_id: int, member_id: int)->Response:
        return self.delete(
            url=f"{settings.API_URL}/boards/{board_id}/members/{member_id}"
        )

    def get_board_members(self, board_id: int)->Response:
        return self.get(
            url=f"{settings.API_URL}/boards/{board_id}/members",
        )
    def move_board_to_the_archive(self, board_id: int)->Response:
        return self.put(
            url=f"{settings.API_URL}/boards/{board_id}/archive",
        )

    def get_board_stats(self, board_id: int)->Response:
        return self.get(
            url=f"{settings.API_URL}/boards/{board_id}/stats",
        )

def get_boards_client(user=settings.test_admin)->BoardsClient:
    return BoardsClient(client=get_private_http_client(user))
