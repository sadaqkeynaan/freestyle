from network_config_manager import NetworkConfigManager
import pytest


class Test_this:
    # def setup_method(self):
    #     self.manager = NetworkConfigManager()
    #     self.manager.connect()
    #     self.manager.update_hostname("1")
    #     self.manager.update_interface_state("down")
    #     self.manager.update_response_prefix("Standard Response")
    # def teardown_method(self):
    #     self.manager.disconnect()
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.manager = NetworkConfigManager()
        self.manager.connect()
        self.manager.update_hostname("1")
        self.manager.update_interface_state("down")
        self.manager.update_response_prefix("Standard Response")
        yield
        self.manager.disconnect()

        

    def test1(self):
        assert self.manager.show_hostname() == "hostname: 1"
    
    def test2(self):
        assert self.manager.show_interface_state() == "interface_state: down"

    def test3(self):
        assert self.manager.show_response_prefix() == "response_prefix: Standard Response"

    def test12(self):
        self.manager.update_hostname("2")
        assert self.manager.show_hostname() == "hostname: 2"
        
    def test22(self):
        self.manager.update_interface_state("up")
        assert self.manager.show_interface_state() == "interface_state: up"

    def test33(self):
        self.manager.update_response_prefix("Special Response")
        assert self.manager.show_response_prefix() == "response_prefix: Special Response"

    def testvg(self):
        try: 
            self.manager.update_interface_state("upk")
        except ValueError:
            assert True
        else:
             assert False


            
        


    