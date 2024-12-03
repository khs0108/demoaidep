
      import os  
      from openai import AzureOpenAI  
      from azure.identity import DefaultAzureCredential, get_bearer_token_provider  
        
      endpoint = os.getenv("ENDPOINT_URL", "https://demoai0212.openai.azure.com/")
      deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo-16k")
        
      # Initialize Azure OpenAI client with Entra ID authentication  
      cognitiveServicesResource = os.getenv('AZURE_COGNITIVE_SERVICES_RESOURCE', 'YOUR_COGNITIVE_SERVICES_RESOURCE')  
      token_provider = get_bearer_token_provider(  
          DefaultAzureCredential(),  
          f'{cognitiveServicesResource}.default'  
      )  
        
      client = AzureOpenAI(  
          azure_endpoint=endpoint,  
          azure_ad_token_provider=token_provider,  
          api_version='2024-05-01-preview',  
      )  
        
      completion = client.chat.completions.create(  
          model=deployment,  
          messages=[
    {
        "role": "system",
        "content": "You are an AI assistant that helps people find information."
    },
    {
        "role": "user",
        "content": "hi"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
    },
    {
        "role": "user",
        "content": "what is paternity leave policy , and just give me the days"
    },
    {
        "role": "assistant",
        "content": "The paternity leave policy allows all married male permanent employees to avail 7 working days of paternity leave [doc3][doc4]."
    }
],  
          past_messages=10,  
          max_tokens=800,  
          temperature=0.7,  
          top_p=0.95,  
          frequency_penalty=0,  
          presence_penalty=0,  
          stop=None,  
          extra_body={  
              "data_sources": [  
                  {  
                      "type": "azure_search",  
                      "parameters": {  
                          "endpoint": os.environ["AZURE_AI_SEARCH_ENDPOINT"],  
                          "index_name": os.environ["AZURE_AI_SEARCH_INDEX"],  
                          "authentication": {  
                              "type": "azure_ad"  
                          }  
                      }  
                  }  
              ]  
          }  
      )  
        
      print(completion.model_dump_json(indent=2))  
      
