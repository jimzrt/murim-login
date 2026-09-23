<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0851.txt",
      "sha256": "85182d51398d493eb69f460d3be1763c6572866910fa5231a6b033f8678c71e9",
      "bytes": 15040
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fc645c5b8af4d30d180dcc7785bda57edf2f1fd6775b7215b95997d5bf354f93",
      "bytes": 1215
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6b3a5cc8f26f77fb300434ce4eb95cd4b17da81997c54bf458d11750dd5e8a9d",
      "bytes": 227660
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "96216ff0cac68a9b03f6965434c2da1ce4937ee0b30cd4cfd6ab789d940c20fa",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "ced96a97225b1e55a84579683b78eb74dd864cf5b25e416c538bb410ff12b121",
      "bytes": 1184
    },
    {
      "path": "characters/Jang Taebo.md",
      "sha256": "424c75ba7811413384be4bb9dfc1df7e98049892067feaf561e9668f20038acd",
      "bytes": 778
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "83c8a79da4afd8e197726ddd69526d4bbe89b613c71476cb28f639228e0befae",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "82335d6715ce541f2c23044144bf6c048fb38495b07fa123b6113456963cbb71",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "f25b2e4f4b4bc7b18019893af3ae42f292c074973d0ae2eae27523323165ef4f",
      "bytes": 914
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e355e81484ae949dc8e78222090e84cb4d51822836709e9b1a9310bffea46b83",
      "bytes": 252668
    }
  ],
  "estimated_tokens": 11487
}
-->

# Durable State Update — Chapter 851

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 851. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 851. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 851,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 851,
    "continuity_sources": [851],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes episodes of madness, and eventually kills them.",
    "Namho links Blood Soul Gu to the Five Poisons Sect's ancient war with the Nanman Beast Palace; Jin believes Dark Heaven brought it from Nanman to the Central Plains.",
    "Jin suspects Dark Heaven's covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Jin considers Prince Shangshan Zhu Bao a key to the suspected scheme; the token Zhu Bao gave him seems to tremble inside the Inventory."
  ],
  "continuity_sources": [
    850
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province?",
    "Is Dark Heaven targeting the Great Nation's Emperor or imperial family, and what is its intended scheme?",
    "How is Prince Shangshan Zhu Bao connected to the suspected scheme?"
  ],
  "safe_through": 850,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 독혈지 as “Poisonblood Grounds.”",
    "Render 대국 as “Great Nation.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 영약     | **elixir**                                       |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 지부장    | **Branch Leader**                            |
| 표국     | **Escort Bureau**                            |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 진가표국 | **Jin Family Escort Bureau** | New name for the former Seongun Escort Bureau under the Jin Family. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 정기 | **vital essence** | Energy the Wudang Sect Leader says the monster absorbs from victims. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 장태보 | younger_visitor_to_elder_master | Elder | polite and persistent | Taekyung repeatedly addresses Jang Taebo as 어르신 while requesting his assistance. |
| 장태보 | 진태경 | elder_master_to_younger_visitor | you | gruff and familiar | Jang Taebo uses 자네 while questioning and dismissing Taekyung. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 850
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 155
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; he formerly served the late Emperor, who ordered him to assist Prince Shangshan, and came to the frontier in something like exile; he remains the power behind the Shanxi Provincial Office, manages the City Lord's luncheon, and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed, observant, and socially deft, candid about his fondness for bribes, and unwaveringly loyal to Prince Shangshan; he remains unashamed and matter-of-fact about having been castrated.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** The late Emperor ordered him to assist Prince Shangshan; Hong Jin has served the prince since infancy and remains loyal to him, while recognizing Taekyung as a young hero of the Jin Family of Taiyuan, increasingly enjoying his company and ruthless political methods, and forming an immediate joking rapport with Jin Wikyung.

### Jang Taebo.md

# Jang Taebo (장태보)

- **Safe through:** Chapter 500
- **Aliases:** None
- **Role:** Jang Taebo is the former Guild Leader of the Ironcraft Guild and one of the world’s renowned smiths, now the Jin Family of Taiyuan’s Master of Ironcraft Hall.
- **Personality:** Blunt, cantankerous, solitary, and proud; values an untroubled retirement and protects his anonymity, while quietly caring for the neighboring boy Hanga.
- **Voice:** Curt, gruff, and dryly teasing; rejects requests with flat finality.
- **Relationships:** His disciple is the current Guild Leader of the Ironcraft Guild; neighboring boy Hanga is his only conversational partner, and Jang Taebo gives him candy while pretending annoyance.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 849
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 849
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 850
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor's only younger full brother, and his token commands immediate deference from distant imperial relatives such as Ju Wongong; he admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃851화



유난히도 좋은 날이었다.

따스한 햇볕과 선선한 바람. 그리고 새하얀 조각구름까지.

땀 흘리며 일하는 사람들의 얼굴에는 미소가 가득했고, 잘 정돈된 대로(大路)는 수많은 인파로 붐볐다.

아마도 그래서였을 것이다.

언제나 시간에 쫓기듯 살아온 누군가가, 서둘러 출발하려는 마부에게 불현듯 한 마디를 건넨 것은.

“오늘은 좀 천천히 갈까요? 딱히 급할 거 없잖아.”

“예?”

“그냥 돌아갈 때는 천천히 가고 싶네. 바깥 구경도 하면서.”

평소와는 다른 고용주의 분위기에, 마부는 의문을 뒤로하고 고삐를 늦추었다.

어차피 하라는 대로 지시만 따르면 그만이다.

마부로서도 사람들에게 썩 비키라며 호통치는 것보다는 천천히, 안전하게 말을 모는 것이 백배 나았다.

‘그나저나, 오늘따라 이상하시네. 안에서 무슨 일이라도 있으셨나?’

마부는 슬쩍 옆을 곁눈질했다. 마치 성벽처럼 이중, 삼중으로 높게 쌓아 올린 단단한 담벼락이 그의 시야에 닿았다.

평소라면 모를까. 지금 속도대로라면 꼬박 일각(一刻)을 몰아야 저 담벼락이 끝날 것이다.

‘거참. 언제 봐도 대단하긴 하단 말이지.’

마부는 내심 혀를 내둘렀다. 저 거대한 장원이 자리 잡은 이곳은 외곽도 아니고 한 성(城)의 중심부다. 그야말로 알짜배기 중의 알짜배기.

그런 중심부에서 저 정도 면적의 땅을 차지하고 있다는 사실만으로도 어마어마한 권세가 있다는 증거였지만, 마부가 놀라워하는 점은 따로 있었다.

‘처음 봤을 때만 해도 저 정도까지는 아니었는데.’

몰락한 명가(名家).

아마도 이 이상으로 적합한 표현은 없었을 것이다.

오직 그것만이 냉정한 현실이었고, 마부뿐만 아니라 인근의 모두가 그렇게 생각했으니까.

그러나 그 누구도 짐작하지 못했다.

과거의 영광을 뒤로한 채 서서히 몰락해 가던 가문이, 불과 이 년 남짓한 짧은 시간 만에 한 성을 주름잡는 패자(霸者)로 거듭나리라는 것은.

‘이래서 세상일은 모른다니까.’

내심 중얼거린 마부는 석벽 위로 높게 솟아 있는 깃발을 바라보았다.

어디선가 불어오는 바람을 받아 펄럭이는 비단 위, 용사비등한 필체로 써 내려간 네 글자가 그의 눈에 틀어박혔다.

태원진가(太原進家).

저 거대한 장원의 주인이자, 산서성의 상징이 되어 버린 가문.

태원진가를 둘러싼 변화는 급격하고도 확실했다.

마부가 처음 보았을 때만 해도 낡고 허물어져 가던 전각과 담벼락은 마치 요새처럼 단단하게 보수되었고, 질 좋은 무기와 영약을 지원받은 무인들의 눈동자는 전에 찾아볼 수 없던 정기(正氣)로 번뜩였다.

어디 그뿐인가.

한때 망나니 삼 공자의 외상값을 요구하러 온 빚쟁이들로 붐볐던 문전은, 이제 다른 의미로 발 디딜 틈조차 없었다.

진가표국에 의뢰를 맡기고자 찾아온 타지의 거상(巨商)들. 매달 말일만 되면 상납을 위해 줄지어 늘어선 온갖 점포의 주인들과 태원진가 산하의 무림 문파 및 지부장들까지.

워낙에 산서성에서 내로라하는 온갖 거물들이 문지방이 닳도록 들락거렸기에, 어느 하릴없는 이들은 태원진가 인근을 어슬렁거리며 보고 들은 것을 떠들어 대기도 했다.

바로 지금 이 순간, 길가 옆 담벼락에 쪼그려 앉아 대화를 나누는 두 사내처럼.

“오늘도 안 왔나?”

“안 왔냐니, 누구?”

“어허, 이 사람. 내가 누굴 기다리는지 뻔히 알면서 자꾸 이러네.”

“자네, 설마 또……?”

“설마라니. 난 처음부터 일편단심이었는데.”

“헛소리 좀 작작하게. 괜히 이러다가 자네 마누라한테 걸리는 날에는 나까지 맞아 죽어.”

“괜찮네. 까짓거 한 번 죽지, 두 번 죽나.”

“아니, 내가 안 괜찮다니까. 자네 마누라 팔뚝이 내 종아리보다 굵어.”

“거참, 사내가 돼서 쫄기는. 묻는 말에나 대답하게. 오늘도 안 왔나?”

“겨우 나흘 전에 왔다 가셨는데 오늘은 당연히 안 오셨지. 그분이 뭐 우리처럼 시간이 남아도는 날백수인 줄 아나?”

“이런 제기랄. 이번에야말로 좀 가까이서 보나 했는데.”

“그냥 이쯤에서 포기하게. 자네가 가까이 봐서 뭐 하려고?”

“아니, 산서제일미(山西第一美)를 보겠다는데 다른 이유가 필요한가? 반년 전에 멀리서 한 번 본 것만으로도 침침하던 눈이 다 맑아졌다니까.”

“자네 마누라한테 한 대 얻어맞으면 눈앞이 캄캄해질 건 생각 못 하나? 그리고 말이 좋아서 산서제일미지, 여인의 몸으로 항산검문(恒山劍門)을 이끄시는 출중한 분이야. 괜히 잘못 걸리는 날에는 뼈도 못 추릴 걸세.”

몽롱한 시선으로 허공을 바라보던 사내가 문득 마른침을 꿀꺽 삼켰다.

“……하긴, 그림자처럼 따라다니는 웬 노인네가 성깔이 대단하다던데.”

“대단한 게 성깔뿐이었으면 항산호(恒山虎)라는 별호가 어찌 붙었겠나. 괜히 깝치지 말고 두 다리 멀쩡할 때 집에 들어가서 자식놈이나 돌보게.”

“돌보긴 뭘. 이미 다 컸어.”

“벌써? 세월 빠르군. 내 기억으로는 작년 이맘때쯤에 막 태어났던 것 같은데.”

“어. 맞는데.”

“……자네 미친놈인가?”

두런두런 들려오던 목소리가 서서히 멀어진다.

두 사내의 대화를 듣고 있던 마부는 피식 웃으며 잠시 느슨하게 풀어놓았던 말고삐를 잡았다.

다그닥. 다그닥.

네 마리의 준마가 이끄는 마차는 고용주의 바람대로 천천히 대로변을 가로질렀다.

예전 같았다면 사두마차 하나로도 거리의 절반을 차지했겠지만, 몇 배나 넓어진 거리에 빼곡하게 들어찬 사람들은 슬쩍 비켜서며 하던 대화를 이어 갈 뿐이었다.

그중 대부분은 신변잡기에 불과했으나, 마부의 입장에서는 꽤 귀 기울여 들을 만한 이야기들도 있었다.

“다들 소문 들었소? 그 왜, 태원진가가 운영하는 대장간에서 요새 병장기만 만들고 있다던데.”

“난 또 무슨 소리를 하려나 했네. 그거야 한참 되지 않았나? 태원진가야 무림 문파니 이상한 일도 아니고.”

“그렇긴 하지. 한데 반년 전부터는 아예 병장기만 취급하고 있다고 하오. 농기구를 사려면 적어도 고현(古縣)까지는 가야 할 것 같소.”

“허어. 고현이면 꼬박 사나흘은 걸어야겠군. 다행히 미리 들여 놓은 것들이 워낙 튼튼해서 따로 살 일은 없겠지만.”

“그야 뭐, 장 노인이 데려온 장인들의 솜씨가 좀 좋아야지.”

“예끼. 장 노인이 뭔가, 장 노인이. 태원진가에서도 믿고 중책을 맡기는 분이신데, 이제 장태보 어르신이라고 불러야지.”

“아, 하도 입버릇이 돼서 그만. 그나저나 생각할수록 걱정이오. 요새 강호의 분위기가 흉흉하다던데, 정말 무슨 큰일이라도 나려는 것인지…….”

“걱정일랑 접어 두고 바둑이나 마저 두게. 암천인지 뭔지가 날뛰어 봤자 결국 무림의 일이야. 멀게는 대국(大國)이 있고, 가까이에는 태원진가가 떡하니 버티고 있는데 무슨 걱정이 그리 많나?”

“여기저기서 들려오는 소문들이 심상찮으니 해 본 소리요. 지난 일이 년간 잠잠하던 북부 고원 쪽 상황도 그렇고. 강호의 흐름이 예사롭지 않은 것 같소.”

“북부 고원은 또 왜? 마적들이야 태원진가에서 나서서 싹 쓸어 버렸을 텐데?”

“마적이란 것들이 한번 뿌리 뽑는다고 사라지는 종자들이오? 워낙 잡초 같은 놈들이니 계속해서 생겨나는 게지. 그리고 지난달에 북부로 상행(商行)을 떠났던 상단 몇몇이…….”

제아무리 고용주의 지시라고는 해도 말을 천천히 모는 것에는 한계가 있는 법.

‘거, 빨리빨리 좀 얘기하지.’

마부가 미처 듣지 못한 뒷이야기에 대한 호기심으로 내심 입맛을 다시던 그때, 마차가 대로변을 빠져나올 때까지 줄곧 말없이 바깥 풍경만을 바라보던 고용주가 문득 입을 열었다.

“다들 걱정이 많네. 하긴, 주위에서 벌어지는 일이니 모를 수가 없긴 하겠지.”

“예, 예?”

“저 사람들 말이에요. 아까부터 귀 쫑긋 세우면서 들어 놓고 뭘 그렇게 놀라?”

“어, 그게. 그러니까…….”

마른침을 꿀꺽 삼킨 마부가 더듬더듬 말을 이었다.

“머, 먼저 이렇게 말을 거셨던 적이 없어서 저도 모르게 그만.”

“아하. 뭐, 생각해 보니 그럴 수도 있겠네.”

마부는 힐끗 등 뒤를 곁눈질했다. 진주로 이루어진 주렴(珠簾) 사이로 대수롭지 않게 고개를 끄덕이는 고용주의 모습이 언뜻 비쳤다.

새하얗게 분을 칠한 피부와 앵두처럼 붉은 입술도.

‘아무리 생각해도…… 확실히 평소와는 다르단 말이지.’

도대체 무슨 바람이 분 것일까.

벌써 일 년 가까이 모셨지만, 그간 마부가 보고 겪으면서 알게 된 고용주는 도무지 알 수 없는 사람이었다.

늘 웃고 있긴 하나 어째서인지 진짜 웃음 같지 않았고, 자신에게 먼저 말을 걸 때는 단 하나의 경우뿐이었다.

바로 목적지에 도착했을 때.

수고했어요, 라는 짤막한 인사가 그들 사이에 오가는 대화의 시작이자 끝이었다.

‘그런데 오늘은 먼저 말도 거시고, 이동 중에 죽간도 안 보셨단 말이지.’

높은 신분의 고용주는 언제나 바빴다. 처리해야 할 일도 산더미였고, 여기저기 만나야 할 사람들도 많았다.

지난 일 년간 그런 모습만을 지켜본 마부였으니, 오늘따라 고용주의 분위기가 낯설게 느껴지는 것은 당연한 일이었을지도 모른다.

그래서일까. 평소라면 절대 내비치지 않았을, 쓸데없는 호기심이 본능적으로 그의 입술을 움직였다.

“저어, 혹시 무슨 일이라도 있으십니까?”

“응?”

“아, 그게.”

마부는 질문을 내뱉는 동시에 후회했다. 자신의 고용주, 그것도 높으신 분의 심기를 거슬러서 좋을 것이 하나도 없으니까.

그러나 그런 마부의 후회가 무색하리만큼, 그의 고용주는 생각했던 것 이상으로 관대한 사람이었다.

“흠. 일이라. 있긴 하죠. 얼마 전에 썩 좋지 않은 소식을 들었거든.”

“죄, 죄송합니다.”

“아냐, 뭘 이 정도로 사과까지 해. 너무 굽신거리면 나까지 기분이 안 좋아져요. 괜히 옛날 기억이 떠오르거든.”

“예?”

“두 번 다시 돌아가고 싶지 않은 그런 기억 말이에요. 예를 들자면…….”

말꼬리를 흐린 고용주는 문득 창밖을 응시했다.

격자무늬로 이루어진 나무 창틀 너머로, 깨끗하게 정돈된 거리에서 웃고 있는 아이들이 보였다.

“꼬박 사흘을 굶고 길거리에 나와서, 비단옷 입은 사람들한테 잘 보이기 위해 노래를 부르던, 뭐 그런 기억들.”

“……!”

“아, 오해하지는 말아요. 기분 나쁘라고 한 소리도 아니고, 그냥 그런 적이 있었다는 거니까.”

마부는 저 높으신 분의 믿을 수 없는 과거에 입을 떡 벌렸고, 고용주는 천천히 지나치는 풍경 속 사람들을 바라보며 희미하게 웃었다.

“보기 좋네, 다들.”

아주 오래된, 과거의 일이다.

하지만 누군가의 기억 속에는 영원히 지워지지 않을 화인(火印)이기도 했다.

가난. 죽음. 슬픔. 분노.

태어나면서부터 목을 옥죄었던 굴레를 벗기 위해 최선을 다했던 나날들이 스쳐 지나갔다.

“어떻게든 해냈었는데…… 이번에도 그럴 수 있을까?”

작은 뇌까림이 바람을 타고 흩어진다.

마부는 더 이상 감히 입을 열지 못한 채 계속해서 말을 몰았고, 고용주는 천천히 주위를 스쳐 지나가는 그 모든 것을 눈에 담았다.

그리고 목적지에 가까워질수록 선명하게 드러나는 땅의 말발굽 자국을 보며, 마침내 때가 왔음을 깨달았다.

“부탁 하나만 해도 될까?”

“부탁…… 말씀이십니까?”

불현듯 입을 연 고용주가 반문하는 마부를 향해 고개를 끄덕였다.

“응, 부탁. 지금까지 살갑게 대하지 못한 것에 대한 사과도 겸해서.”

“그, 그런 말씀은 당치도 않습니다. 필요한 것이 있으시다면 뭐든 지시를 내려 주십시오. 도지휘동지(都指揮同知) 대감.”

고용주, 아니 산서성 도지휘동지 홍진(洪進)이 붉은 입술을 달싹였다.

“나는 이곳에서 내릴 테니. 그대는 지금 즉시 홍화루(紅花樓)로 가서 전해요. 아니, 하오문 산서지부라고 해야 하나?”

“……!”

“내가 모를 줄 알았나 보네. 하지만 그쪽에서는 이미 어느 정도 눈치챘을 거야. 금의위(錦衣衛)가 아무리 은밀하게 움직였다 해도, 그 많은 이목을 피할 수는 없을 테니까.”

홍진이 자신의 정체를 알고 있다는 사실과 황제의 명으로만 움직인다던 금의위의 존재.

마부는 이중 어느 것에 더 놀라야 하는지 가늠할 수조차 없었지만, 이내 자신이 해야 할 말을 깨달았다.

“도지휘동지께서는…… 제가 어찌하기를 원하십니까?”

“이 모든 상황을 전해요. 그리고 하오문의 모든 정보력을 동원해서라도 한 사람을 찾아줘요.”

“한 사람이라고 하신다면.”

“어떤 상황에서도 우리를, 아니 상산왕 전하를 지켜 줄 수 있는 사람. 무림인 중에서도 가장 믿을 수 있는 사람.”

홍진은 천천히, 그러나 힘주어 말을 이었다.

“열화신룡(烈火神龍) 진태경.”

“……!”

“가요, 어서.”

그것이 마지막이었다.

마차는 바람처럼 떠났고, 멀어지는 마차를 끝까지 지켜보던 홍진은 불현듯 돌아섰다.

이내 거센 말발굽 소리와 함께 일단의 무리가 들이닥쳤다.

“황명이오. 함께 가 주셔야겠소. 도지휘동지 대감.”

“상산왕 전하께서는?”

“안심하시오. 아직은 무탈하시니.”

“아직이라…… 그래, 그러지 뭐.”

홍진은 웃었다.

그리고 자신의 어린 주군을 향해 걸음을 옮겼다.
```

## Final English reading copy

```markdown
# Chapter 851

It was an especially beautiful day.

Warm sunshine, a cool breeze, and even wisps of pure white cloud.

The people working up a sweat wore smiles, and the well-kept main road bustled with crowds.

Perhaps that was why someone who was always living as though pressed for time suddenly spoke to the coachman, who was about to set off in a hurry.

“Could we take it a little slower today? There’s no particular rush.”

“Pardon?”

“I’d like to take my time on the way back. Look around outside, too.”

The coachman wondered at his employer’s uncharacteristic mood, but put the question aside and eased the reins.

All he had to do was follow orders, after all.

And as a coachman, he much preferred guiding the horses slowly and safely to shouting at people to get out of the way.

*Still, he’s acting strange today. Did something happen inside?*

The coachman glanced sideways. A sturdy wall, built high in two or three layers like a fortress, came into view.

On an ordinary day, perhaps not. But at this pace, it would take a full fifteen minutes to reach the end of that wall.

*Good grief. It’s impressive no matter how many times I see it.*

The coachman silently marveled. This enormous estate stood not on the outskirts, but right in the center of a city. Prime real estate among prime real estate.

The fact that the family owned so much land in the very heart of the city was proof enough of its tremendous power, but that wasn’t what amazed the coachman most.

*It was nothing like this when I first saw it.*

A fallen great family.

There was probably no more fitting description.

That was the cold reality, and not just the coachman but everyone nearby had thought so.

Yet no one could have guessed.

That a family slowly declining, its past glory behind it, would rise in barely more than two short years to become the power ruling over an entire city.

*Just goes to show, you never know what’ll happen in this world.*

Muttering to himself, the coachman looked up at the flag rising high above the stone wall.

The silk fluttered in a breeze from somewhere, and four characters written in a bold, flowing hand caught his eye.

Jin Family of Taiyuan.

The owner of that enormous estate, and a family that had become a symbol of Shanxi Province.

The changes surrounding the Jin Family of Taiyuan had been swift and undeniable.

The pavilions and walls, once shabby and crumbling, had been repaired until they looked as solid as a fortress. The martial artists, supplied with fine weapons and elixirs, now had a righteous spirit in their eyes the coachman had never seen before.

And that wasn’t all.

The entrance, once crowded with debt collectors demanding payment for the reckless Third Young Master’s unpaid bills, was now so packed you could hardly set foot inside—but for entirely different reasons.

There were wealthy merchants from other regions, come to entrust their business to the Jin Family Escort Bureau. There were shopkeepers of every kind, lined up to pay tribute at the end of each month, as well as martial arts sects and Branch Leaders under the Jin Family of Taiyuan.

So many important people from all over Shanxi Province came and went that the threshold was worn down. Some people with nothing better to do even loitered around the Jin Family of Taiyuan, chatting about what they’d seen and heard.

Just like the two men squatting beside the wall at the roadside right now.

“Didn’t she come today, either?”

“Didn’t who come?”

“Oh, come on. You know perfectly well who I’m waiting for. Why do you keep asking?”

“Don’t tell me you’re at it again…”

“What do you mean, ‘don’t tell me’? I’ve been devoted to her from the start.”

“Cut the nonsense. If your wife catches you, she’ll beat you to death—and then I’ll get killed, too.”

“It’s fine. You only die once, don’t you?”

“I’m telling you, it’s not fine. Your wife’s arm is thicker than my calf.”

“Good grief. You’re a man, and you’re scared? Just answer my question. Didn’t she come today, either?”

“She was here just four days ago. Of course she didn’t come today. Do you think she’s an unemployed layabout like us, with nothing but time on her hands?”

“Damn it. I thought maybe this time I’d get to see her up close.”

“Just give it up already. What would you do if you saw her up close?”

“Do I need another reason to see Shanxi’s foremost beauty? I saw her from far away once, half a year ago, and my blurry old eyes cleared right up.”

“Have you considered that one good whack from your wife might make everything go dark? And calling her Shanxi’s foremost beauty hardly does her justice. She leads the Mount Heng Sword Sect despite being a woman—and she’s formidable. If you cross her the wrong way, you won’t walk away in one piece.”

The man gazed dreamily into space, then suddenly swallowed.

“…Well, I heard she’s got some old man following her around like a shadow, and he’s got one hell of a temper.”

“If temper were all he had, would they have called him the Tiger of Mount Heng? Quit acting up and go home while both your legs still work. Take care of your kid.”

“Take care of him? He’s all grown up.”

“Already? Time flies. I remember him being born just about this time last year.”

“Yeah. That’s right.”

“…Are you insane?”

The two men’s low conversation gradually faded away.

The coachman, who’d been listening to them, gave a quiet laugh and took hold of the reins he’d let slacken for a moment.

Clip-clop. Clip-clop.

The carriage, drawn by four fine horses, crossed the main road slowly, just as his employer had asked.

In the past, a single four-horse carriage would have taken up half the street. But now the road was several times wider, and the crowds packed into it simply moved aside a little and carried on with their conversations.

Most of what they said was ordinary gossip, but from the coachman’s perspective, some of it was worth listening to.

“Have you all heard the rumors? The Jin Family of Taiyuan’s blacksmith shop has been making nothing but weapons lately.”

“I thought you were about to say something important. That’s been going on for a while, hasn’t it? The Jin Family of Taiyuan is a Murim sect. It’s hardly strange.”

“True. But for the past six months, they’ve been dealing exclusively in weapons. If you want to buy farming tools, you’ll have to go at least as far as Gohyeon.”

“Well, now. Gohyeon’s a good three or four days on foot. Luckily, the tools we bought ahead of time are sturdy enough that we won’t need to buy more.”

“That’s because the craftsmen Old Man Jang brought with him are so good.”

“Hey, don’t call him Old Man Jang. The Jin Family of Taiyuan trusts him with important work. We ought to call him Master Jang Taebo now.”

“Ah, it’s just a habit. Anyway, the more I think about it, the more worried I get. Things in the martial world are supposed to be tense these days. Do you think something big is really about to happen…?”

“Put your worries aside and finish your game of Go. Dark Heaven or whatever can make all the trouble it wants; in the end, it’s a Murim affair. The Great Nation is out there, and the Jin Family of Taiyuan is standing firm right here. What’s there to worry about?”

“I only said it because the rumors coming from all over don’t sound good. Things up in the northern plateau, which had been quiet for the past year or two, too. The currents in the martial world don’t seem normal.”

“What’s going on in the northern plateau now? The Jin Family of Taiyuan must have gone out and wiped out the mounted bandits.”

“Do mounted bandits disappear just because someone uproots them once? They’re weeds. They keep cropping up. And a few merchant caravans that headed north last month…”

Even with his employer’s instructions, there was only so long the coachman could keep the horses moving slowly.

*Come on, get to the point.*

Just as he was silently licking his lips, curious about the rest of the story he hadn’t managed to hear, his employer—who had been staring out at the scenery without a word all the way out of the main road—suddenly spoke.

“Everyone has a lot to worry about. Then again, when it’s happening around you, it’s hard not to notice.”

“Y-yes?”

“I mean those people. You’ve been listening with your ears pricked up this whole time, so why are you acting so surprised?”

“Uh, well. It’s just…”

The coachman swallowed and stammered on.

“You’ve never spoken to me first like this before, so I was caught off guard.”

“Ah. Well, when you put it that way, I suppose.”

The coachman glanced over his shoulder. Through the beaded curtain, he caught a glimpse of his employer nodding as if it were nothing.

The skin powdered pure white, and lips red as cherries, too.

*No matter how I look at it…he’s definitely acting differently than usual.*

What had gotten into him?

The coachman had served him for nearly a year, but after all he’d seen and experienced, his employer remained a mystery.

He was always smiling, but for some reason it never seemed like a genuine smile. And there was only one occasion when he ever spoke first to the coachman.

When they reached their destination.

A brief “Thank you for your hard work” was both the beginning and the end of their conversations.

*But today he spoke first, and he hasn’t even looked at his bamboo slips while we’ve been on the road.*

His high-ranking employer was always busy. There was a mountain of work to handle and people to meet everywhere.

The coachman had watched him like that for the past year, so it was only natural that his employer’s mood today felt so unfamiliar.

Maybe that was why a pointless curiosity, one he would never normally have let show, instinctively moved his lips.

“Um, has something happened?”

“Hm?”

“Ah, well…”

The coachman regretted the question as soon as he asked it. There was nothing to gain by upsetting his employer—especially when his employer was a high-ranking official.

But his employer proved far more generous than the coachman had expected.

“Hm. Something happened? Yes, it did. I heard some unpleasant news not long ago.”

“I-I’m sorry.”

“No, why apologize over something like this? When you bow and scrape too much, it makes me uncomfortable, too. It brings back memories from long ago.”

“Pardon?”

“Memories I never want to return to. For example…”

His employer’s voice trailed off, and he suddenly gazed out the window.

Beyond the wooden lattice, children were laughing in a clean, orderly street.

“Something like going out into the street after going three whole days without food, singing to impress people in silk robes.”

“……!”

“Oh, don’t get the wrong idea. I’m not saying that to make you feel bad. It’s just something that happened.”

The coachman’s mouth fell open at the unbelievable past of such a high-ranking person. His employer, meanwhile, watched the people passing slowly by and smiled faintly.

“It’s nice to see everyone looking so happy.”

It had happened a very long time ago.

But in someone’s memory, it was also a brand that would never fade.

Poverty. Death. Sorrow. Anger.

The days spent doing everything he could to escape the shackles that had gripped his throat since birth flashed past.

“I managed somehow back then…but can I do it this time, too?”

The quiet mutter was carried away by the wind.

The coachman didn’t dare say another word. He kept guiding the horses onward, while his employer took in everything slowly passing by.

And as the destination drew nearer, the hoofprints in the ground grew clearer. At last, he knew the time had come.

“Could I ask you a favor?”

“A favor…sir?”

His employer suddenly spoke, then nodded at the coachman’s question.

“Yes, a favor. And an apology, too, for not having been very kind to you until now.”

“Th-there’s no need to say that, sir. If you need anything, please just give me the order. Deputy Military Commissioner.”

His employer—or rather, Hong Jin, Deputy Military Commissioner of Shanxi Province—parted his red lips.

“I’m going to get off here. Go to Honghwaru right away and tell them. Or should I say the Lower District Sect’s Shanxi branch?”

“……!”

“You thought I wouldn’t know, didn’t you? But they’ve probably figured it out to some extent already. No matter how secretly the Embroidered Uniform Guard operates, they can’t avoid that many eyes.”

The fact that Hong Jin knew his identity, and the existence of the Embroidered Uniform Guard, said to act only on the Emperor’s orders.

The coachman couldn’t even tell which of those two things he ought to be more surprised by. Then he realized what he needed to ask.

“What would you like me to do, Deputy Military Commissioner?”

“Tell them everything that’s happened. And have them use every bit of the Lower District Sect’s information network to find one person.”

“One person, you say?”

“Someone who can protect us in any situation—or rather, His Highness Prince Shangshan. The most trustworthy person in all Murim.”

Hong Jin spoke slowly, but with emphasis.

“The Blazing Flame Divine Dragon, Jin Taekyung.”

“……!”

“Go. Hurry.”

That was all.

The carriage sped away like the wind, and Hong Jin watched it disappear before suddenly turning around.

A group arrived in a rush, the sound of their horses’ hooves growing louder.

“We have an imperial decree. You’ll have to come with us, Deputy Military Commissioner.”

“And His Highness Prince Shangshan?”

“Rest assured. He is unharmed—for now.”

“For now… Well, fine.”

Hong Jin smiled.

Then he set off toward his young lord.
```
