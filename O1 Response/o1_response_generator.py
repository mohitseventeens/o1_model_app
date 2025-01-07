import time
from helper import get_openai_api_key
from openai import OpenAI
import markdown

class O1ResponseGenerator:
    def __init__(self, o1_model="o1-mini"):
        """
        Initialize the O1ResponseGenerator with a model name.
        """
        self.o1_model = o1_model
        openai_api_key = get_openai_api_key()
        self.client = OpenAI(api_key=openai_api_key)

    def _calculate_cost(self, prompt_tokens, cached_input_tokens, output_tokens):
        """
        Internal method to calculate the total cost based on tokens used.
        """
        model_prices = {
            "o1": {
                "input_token_price": 15.00 / 1_000_000,
                "cached_input_token_price": 7.50 / 1_000_000,
                "output_token_price": 60.00 / 1_000_000,
            },
            "o1-mini": {
                "input_token_price": 3.00 / 1_000_000,
                "cached_input_token_price": 1.50 / 1_000_000,
                "output_token_price": 12.00 / 1_000_000,
            },
        }

        if self.o1_model not in model_prices:
            self.o1_model = "o1"

        prices = model_prices[self.o1_model]
        input_token_cost = (prompt_tokens - cached_input_tokens) * prices["input_token_price"]
        cached_input_token_cost = cached_input_tokens * prices["cached_input_token_price"]
        output_token_cost = output_tokens * prices["output_token_price"]

        return input_token_cost + cached_input_token_cost + output_token_cost

    def _save_response_html(self, file_name, response_time, total_cost, response_content):
        """
        Internal method to generate and save HTML from the response content.
        """
        response_html = markdown.markdown(response_content)
        html_content = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>O1 Response</title>
            <script type="text/javascript" async 
                src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
            </script>
        </head>
        <body>
            <div style="background-color: #f0fff8; padding: 10px; border-radius: 5px; border: 1px solid #d3d3d3;">
                <h2>{self.o1_model} Model Response</h2>
                <p>Response time: {response_time:.2f} seconds</p>
                <p>Total Cost: {total_cost:.2f} $</p>
            </div>

            <div style="padding: 10px;">
                {response_html}
            </div>
        </body>
        </html>
        """
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"Response saved to {file_name}")

    def generate_response(self, prompt, system_prompt, file_name="o1_response_test.html"):
        """
        Public method to generate a response using the O1 model.
        """
        start_time = time.time()

        response = self.client.chat.completions.create(
            model=self.o1_model,
            messages=[
                {
                    "role": "user",
                    "content": f"<System Prompt>{system_prompt}</System Prompt>\\n<USER Prompt>{prompt}</USER Prompt>"
                }
            ]
        )

        response_time = time.time() - start_time
        usage = response.usage

        total_cost = self._calculate_cost(
            usage.prompt_tokens,
            usage.prompt_tokens_details.cached_tokens,
            usage.completion_tokens
        )

        response_content = response.choices[0].message.content

        # Save to HTML
        self._save_response_html(file_name, response_time, total_cost, response_content)

        return response