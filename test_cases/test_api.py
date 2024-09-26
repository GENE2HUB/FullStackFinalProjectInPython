import allure

from extensions.verifications import Verifications
from workflows.api_flows import APIFlows

team_name = 'Genetu'
team_email = 'genetu@email.com'


class Test_API:
    @allure.step('Test01: Create Team & Verify Status Code')
    @allure.step('this test creates new team in Grafana')
    def test_create_and_verify_team(self):
        actual = APIFlows.create_team(team_name, team_email)
        Verifications.verify_equals(actual, 200)

    @allure.step('Test02: verify Team Name')
    @allure.step('this test verifies the Grafana team member name')
    def test_verify_team_member_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name)

    @allure.step('Test03: Update Team & verify Status Code')
    @allure.step('this test Update Team & verify Status Code')
    def test_update_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.update_team(team_name + ' Beyene', team_email, id)
        Verifications.verify_equals(actual, 200)

    @allure.step('Test04: Update Team Name')
    @allure.step('this test verifies team member name')
    def test_verify_team_update_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name + ' Beyene')

    @allure.step('Test05: Delete Team & verify Status Code')
    @allure.step('this test delete amd verify status code')
    def test_delete_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.delete_team(id)
        Verifications.verify_equals(actual, 200)



