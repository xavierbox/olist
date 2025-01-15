
from azure.ai.translation.text import TextTranslationClient#, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError
from azure.core.credentials import AzureKeyCredential



def get_text_translation_multiple_inputs(text_translator, input_text_elements:list[str], 
                                         to_language: list[str] =['en'] ):
    # [START get_text_translation_multiple_inputs]

    results = []
    if isinstance( to_language,str): to_language = [ to_language ]
    try:
        translations = text_translator.translate(body=input_text_elements, to_language=to_language)

        for n,translation in enumerate(translations):
            #print( translation )

            language_score = translation.detected_language.score 
            language_translation = translation.translations[0].text if translation.translations else None

            results.append( { input_text_elements[n] : { 'translation': language_translation, 'laguage_score': language_score}} ) 
            
            #print(
            #    f"Detected languages of the input text: {translation.detected_language.language if translation.detected_language else None} with score: {translation.detected_language.score if translation.detected_language else None}."
            #)
            #print(
            #    f"Text was translated to: '{translation.translations[0].to if translation.translations else None}' and the result is: '{translation.translations[0].text if translation.translations else None}'."
            #)

    except HttpResponseError as exception:
        if exception.error is not None:
            print(f"Error Code: {exception.error.code}")
            print(f"Message: {exception.error.message}")

        return None 
    
    except Exception as e: 
         results.append( { input_text_elements[n] : { 'translation': 'language translation failed', 'laguage_score': language_score}} ) 
           

    # [END get_text_translation_multiple_inputs]

    return results 
  

