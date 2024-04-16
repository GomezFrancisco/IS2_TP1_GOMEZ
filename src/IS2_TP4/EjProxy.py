from abc import ABC, abstractmethod
import os

class Ping:
    def execute(self, ip_address: str) -> None:
        if ip_address.startswith("192."):
            print(f"Pinging {ip_address}...")
            for _ in range(10):
                response = os.system(f"ping -c 1 {ip_address}")
                if response == 0:
                    print(f"{ip_address} is reachable.")
                else:
                    print(f"{ip_address} is unreachable.")
        else:
            print("Error: IP address must start with '192.'")

    def executefree(self, ip_address: str) -> None:
        print(f"Pinging {ip_address}...")
        for _ in range(10):
            response = os.system(f"ping -c 1 {ip_address}")
            if response == 0:
                print(f"{ip_address} is reachable.")
            else:
                print(f"{ip_address} is unreachable.")


class PingProxy:
    def __init__(self, ping: Ping) -> None:
        self._ping = ping

    def execute(self, ip_address: str) -> None:
        if ip_address == "192.168.0.254":
            print("Proxy: Redirecting ping to www.google.com using free execution method.")
            self._ping.executefree("www.google.com")
        else:
            print("Proxy: Redirecting ping to the original execution method.")
            self._ping.execute(ip_address)


class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)
    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
    print("")

    print("Client: Testing the Ping and PingProxy classes:")
    ping = Ping()
    ping_proxy = PingProxy(ping)
    ping_proxy.execute("192.168.0.1")
    ping_proxy.execute("192.168.0.254")
