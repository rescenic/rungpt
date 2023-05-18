from cleo.commands.command import Command
from cleo.helpers import argument, option


class ServeCommand(Command):
    name = "serve"

    description = "Start a model serving locally."

    arguments = [argument("model_name", "The name of the model to serve.")]
    options = [
        option(
            'grpc_port',
            None,
            'The gRPC port to serve the model on.',
            flag=False,
            default=51001,
        ),
        option(
            'http_port',
            None,
            'The HTTP port to serve the model on.',
            flag=False,
            default=51002,
        ),
        option(
            "replicas", "r", "The number of replicas to serve.", flag=False, default=1
        ),
    ]

    help = """\
    This command allows you to start a model serving locally.
    
    To start a model serving locally, you can run:
        
        <comment>opengpt serve facebook/llama-7b</comment>"""

    def handle(self) -> int:
        from open_gpt.factory import create_flow

        with create_flow(
            self.argument('model_name'),
            replicas=self.option('replicas'),
            grpc_port=self.option('grpc_port'),
            http_port=self.option('http_port'),
        ) as flow:
            flow.block()

        return 0
