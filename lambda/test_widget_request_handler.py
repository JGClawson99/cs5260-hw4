from moto import mock_lambda
import unittest
from widget_request_handler import lambda_handler


class TestWidgetRequestHandler(unittest.TestCase):
    
    @mock_lambda
    def test_valid_create_widget_request(self):
        widget_request = {"message": "{\"type\":\"create\",\"requestId\":\"9ca0d18a-57ab-4ac6-89dc-146f092ea9fe\",\"widgetId\":\"ad0bb9e1-28e9-46e0-ad08-8192f4d3b6c6\",\"owner\":\"JohnJones\",\"label\":\"QQGRLNZY\",\"description\":\"JLVIEOHPQXKDXKPHOHFOXNKSYDEWRNEQWMPVPVHZVJCHCUIIWSRXITPWOKTMHULMVUNWGRREQYPQYO\",\"otherAttributes\":[{\"name\":\"size\",\"value\":\"926\"},{\"name\":\"height\",\"value\":\"828\"},{\"name\":\"height-unit\",\"value\":\"cm\"},{\"name\":\"length-unit\",\"value\":\"cm\"},{\"name\":\"rating\",\"value\":\"1.6420901\"}]}"}

        assert lambda_handler(widget_request) == [False, "error sending message"]

    @mock_lambda
    def test_valid_update_widget_request(self):
        widget_request = {"message": "{\"type\":\"update\",\"requestId\":\"d61c3e72-1a66-4cfa-9162-56712e4580d8\",\"widgetId\":\"6984abeb-5b24-42eb-93cc-3a5bef6b4b8a\",\"owner\":\"MaryMatthews\",\"description\":\"PUMMCL\",\"otherAttributes\":[{\"name\":\"size\",\"value\":\"745\"},{\"name\":\"size-unit\",\"value\":\"cm\"},{\"name\":\"height\",\"value\":\"879\"},{\"name\":\"height-unit\",\"value\":\"cm\"},{\"name\":\"width-unit\",\"value\":\"cm\"},{\"name\":\"length\",\"value\":\"793\"},{\"name\":\"price\",\"value\":\"50.96\"},{\"name\":\"quantity\",\"value\":\"311\"},{\"name\":\"note\",\"value\":\"MYEVVLRLAWVRZTQIMWRTJFDZTSJNJTWXQBFXOBABMNGJDCWRJMAGVYSWWAPYWDCHSDKFAURWSBHGABSMVKRLQZKXEXJLNXZU\"}]}"}

        assert lambda_handler(widget_request) == [False, "error sending message"]

    @mock_lambda
    def test_valid_delete_widget_request(self):
        widget_request = {"message": "{\"type\":\"delete\",\"requestId\":\"9205fcb9-7c74-4db1-8054-33bdd70ed0e8\",\"widgetId\":\"6984abeb-5b24-42eb-93cc-3a5bef6b4b8a\",\"owner\":\"MaryMatthews\"}"}

        assert lambda_handler(widget_request) == [False, "error sending message"]

    @mock_lambda
    def test_invalid_widget_request(self):
        widget_request = {"message": "{\"explode\":\"delete\",\"requestId\":\"9205fcb9-7c74-4db1-8054-33bdd70ed0e8\",\"widgetId\":\"6984abeb-5b24-42eb-93cc-3a5bef6b4b8a\",\"owner\":\"MaryMatthews\"}"}

        assert lambda_handler(widget_request)[0] == False


if __name__ == '__main__':
    unittest.main()