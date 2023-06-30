def voc(audio_data):
    import re
    import warnings
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    from transformers import BertTokenizer, BertForSequenceClassification
    import os
    import ast
    import sys
    from AI.TestCommon.conf import config
    from AI.TestCommon.conf import bcolors
    from AI.ktAiApiSDK.GENIEMEMO import GENIEMEMO
    from pathlib import Path
    import json
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    import nltk

    clientKey = "0fb26b7f-9b98-53cc-bc0f-eccf6988a793"
    clientId = "239ea532-a145-45f4-8295-ee4876877fec"
    clientSecret = "e35be7455626bde39956632c968b98df6e9d1458942f2c69888400166ca27f4e"
    
    #-------------------------------------------
    # 호출용 데이터 설정
    #-------------------------------------------
    geniememo_client = GENIEMEMO()
    geniememo_client.__init__()
    geniememo_client.setAuth(clientKey, clientId, clientSecret)
    callKey = "94"
    lastYn = "N"
    callIndex = 1
    #file_name = upload_file.read()
    #audioData = Path(file_name).read_bytes()

    audio_data = audio_data

    #-------------------------------------------
    # 호출
    #-------------------------------------------
    print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")
    print(bcolors.ENDC, "========= 호출정보 =========")
    print(bcolors.WARNING, "audioData:", "callKey:", callKey, "lastYn:", lastYn, "callIndex:", callIndex)
    response = geniememo_client.requestGENIEMEMO(audio_data, callKey, lastYn, callIndex)

    #-------------------------------------------
    # 결과 출력
    #-------------------------------------------
    print(bcolors.ENDC, "========= 응답결과 =========")
    print(bcolors.HEADER, response)

    print(bcolors.ENDC)
    text_list = []
    result = response['result'][0]  # assuming there is only one result in the list
    data_list = ast.literal_eval(result)['dataList']
    
    for item in data_list:
        text = item['text']
        text_list.append(text)

    combined_text = ' '.join(text_list)
    print(combined_text)
    model_dir = "AI/new_summary"
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

    max_input_length = 512 + 256

    text = combined_text

    inputs = ["summarize: " + text]

    inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=10, do_sample=True, min_length=10, max_length=100)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    predicted_title = nltk.sent_tokenize(decoded_output.strip())[0]

    print(predicted_title)
        
    # 감정 Step 2: 입력 텍스트 토큰화
    model_dirs = 'AI/emotion'
    tokenizer = BertTokenizer.from_pretrained(model_dirs)
    input_tokens = tokenizer.encode_plus(predicted_title, truncation=True, padding='longest', return_tensors='pt')

    # 감정 Step 3: 텍스트 분류 수행
    model = BertForSequenceClassification.from_pretrained(model_dirs)

    input_ids = input_tokens['input_ids']
    attention_mask = input_tokens['attention_mask']

    outputs = model(input_ids, attention_mask=attention_mask)

    # 가정: 이진 분류 문제를 다루는 경우
    logits = outputs.logits
    predicted_class = logits.argmax().item()

    if predicted_class == 1:
        np_emotion = 1
    else:
        np_emotion = 0
            
    print("분류:", np_emotion)
        
    # 감정 Step 2: 입력 텍스트 토큰화
    model_dirs = 'AI/emotion'
    tokenizer = BertTokenizer.from_pretrained(model_dirs)
    input_tokens = tokenizer.encode_plus(predicted_title, truncation=True, padding='longest', return_tensors='pt')

    # 감정 Step 3: 텍스트 분류 수행
    model = BertForSequenceClassification.from_pretrained(model_dirs)

    input_ids = input_tokens['input_ids']
    attention_mask = input_tokens['attention_mask']

    outputs = model(input_ids, attention_mask=attention_mask)

    # 가정: 이진 분류 문제를 다루는 경우
    logits = outputs.logits
    predicted_class = logits.argmax().item()

    if predicted_class == 1:
        np_emotion = 1
    else:
        np_emotion = 0
            
    print("분류:", np_emotion)

    from konlpy.tag import Okt

    okt = Okt()

    text = okt.nouns(combined_text)

    emergency_keywords = ['병원', '요양원', '학교', '공장', '소방서', '경찰서']
    emergency = ''

    for keyword in emergency_keywords:
        if keyword in text:
            emergency = 1
        else:
            emergency = 0

            break
            
    print("판단근거:", predicted_title)
    print("분류:", np_emotion)
    print("중요도:", emergency)
   
    return predicted_title, np_emotion, emergency
    
def construction(audio_data):
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

    from konlpy.tag import Kkma
    from dateutil.parser import parse

    import os
    import ast
    import sys
    from AI.TestCommon.conf import config
    from AI.TestCommon.conf import bcolors
    from AI.ktAiApiSDK.GENIEMEMO import GENIEMEMO
    from pathlib import Path
    import json
    import re
    import warnings
    import datetime

    clientKey = "0fb26b7f-9b98-53cc-bc0f-eccf6988a793"
    clientId = "239ea532-a145-45f4-8295-ee4876877fec"
    clientSecret = "e35be7455626bde39956632c968b98df6e9d1458942f2c69888400166ca27f4e"

    #-------------------------------------------
    # 호출용 데이터 설정
    #-------------------------------------------
    geniememo_client = GENIEMEMO()
    geniememo_client.__init__()
    geniememo_client.setAuth(clientKey, clientId, clientSecret)
    callKey = "96"
    lastYn = "N"
    callIndex = 1
    #file_name = upload_file.read()
    #audioData = Path(file_name).read_bytes()

    audio_data = audio_data
        
    #-------------------------------------------
    # 호출
    #-------------------------------------------
    print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")
    print(bcolors.ENDC, "========= 호출정보 =========")
    print(bcolors.WARNING, "audioData:", "callKey:", callKey, "lastYn:", lastYn, "callIndex:", callIndex)
    response = geniememo_client.requestGENIEMEMO(audio_data, callKey, lastYn, callIndex)

    #-------------------------------------------
    # 결과 출력
    #-------------------------------------------
    print(bcolors.ENDC, "========= 응답결과 =========")
    print(bcolors.HEADER, response)

    print(bcolors.ENDC)
    text_list = []
    result = response['result'][0]  # assuming there is only one result in the list
    data_list = ast.literal_eval(result)['dataList']
    for item in data_list:
        text = item['text']
        text_list.append(text)

    text = ' '.join(text_list)
    print(text)
    # Ignore warnings
    warnings.filterwarnings("ignore")

    # filename = "C:\\Users\\User\\Desktop\\빅프\\text_summary_auto\\geniememo.txt"
    if os.path.isfile(text):
        with open(text, "r", encoding="utf-8") as file:
            text = file.read()  
        
    data = '선로공사\n수로공사\n전기공사\n상수도공사\n하수도공사\n가스공사\n열수송공사\n통신공사\n송유공사\n지하철공사\n선로 공사\n수로 공사\n전기 공사\n상수도 공사\n하수도 공사\n가스 공사\n열수송 공사\n열 수송 공사\n통신 공사\n송유 공사\n지하철 공사'
        
    model_dir = 'AI/edit/'
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

    # 특수 문자와 공백을 제거하여 텍스트를 정리합니다.
    clean_text = re.sub(r'\W+', ' ', text.strip())

    inputs = tokenizer.encode(clean_text, return_tensors="pt")
    output = model.generate(inputs, num_beams=5,  max_length=1024, no_repeat_ngram_size=2, early_stopping=True)
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

    print(decoded_output)

    kkma = Kkma()

    # 날짜
    is_today_mentioned = any(word == '오늘' for word, pos in kkma.pos(decoded_output))
    has_no_number = not any(pos.startswith('NR') for (word, pos) in kkma.pos(decoded_output))

        
    date = None
    if is_today_mentioned or has_no_number:
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        print("\n오늘 날짜:", today)
    else:
        words = kkma.pos(decoded_output)
        num_chunks = []
        for word, pos in words:
            if pos == 'NR' or pos == 'NNM':
                num_chunks.append(word)
        if num_chunks:
            date = " ".join(num_chunks)
            date_obj = parse(date, fuzzy=True)
            formatted_date = date_obj.strftime("%m월 %d일")
            print("\n공사 날짜:", formatted_date)
        
    # 공사 내용
    content = [x for (x, y) in kkma.pos(decoded_output) if y == 'NNG' and x != '오늘' and x in data]
    print('\n내용 추출 :', ' '.join(content))
        
    content = ' '.join(content)
        
    # 장소
    location = [x for (x, y) in kkma.pos(decoded_output) if( y == 'NNG' and x != '오늘' and x not in content) or (y == 'NNP' and x != '오늘' and x not in content)]
    print('\n장소 추출 :', ' '.join(location))
        
    location = ' '.join(location)
    
    return formatted_date, content, location