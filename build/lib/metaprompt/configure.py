class ConfigurationRules:
    def __init__(self, 
                 additional_rules=None, 
                 examples=None, 
                 response_format=None, 
                 sug_ques=None):
        
        self.additional_rules = """
                            Handling Specific SQL Queries:
                                - Use 'like' to search value in Column whenever required.
                                - Use word like 'Collection' instead of 'Dataset', 'database' in response.
                                """
        
        if additional_rules:
            self.additional_rules += additional_rules
        
        self.examples = [{
            "examples": [
                {"input": "", "query": ""},
            ]
        }]
        
        if examples:
            self.examples[0]["examples"].extend(examples[0]["examples"])
        
        self.response_format = """Response Format:- Here are the guidelines for your responses:
                    1. Avoid Asterisks: Do not use asterisks for bullet points or formatting. Use plain text or numbers instead.
                    2. Clean Formatting: Use clean and simple formatting to present information clearly. Use numbers or dashes for lists and headings.
                    3. Example Formatting:
                        - Instead of using multiple asterisks for bullet points, use dashes or numbers.
        """
        
        if response_format:
            self.response_format += response_format
        
        self.sug_ques = []

        default_sug_ques = [
            'What are the key insights or takeaways from this dataset?',
            'Are there any noticeable trends or changes in the data over time?',
            'What are the main categories or classifications present in this dataset?'
        ]
        
        if sug_ques is None or len(sug_ques) == 0:
            self.sug_ques = default_sug_ques
        elif len(sug_ques) < 3:
            self.sug_ques = default_sug_ques + sug_ques
        else:
            self.sug_ques = sug_ques