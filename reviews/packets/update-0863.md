<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0863.txt",
      "sha256": "c1244d2a98e4910d5b94b8f7ffbd3a619f06d15bc5c0faba5f407b3fa73c9525",
      "bytes": 13167
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "10ff3aae46a688b3f1b22f37151448da89c8285aa978df0dfa16d271ede5bd15",
      "bytes": 1058
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4c101b31c65ea71d45efd4357ef39f4e35dc7c82b77dbe6d7cdd92374a1106dc",
      "bytes": 229215
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "b4cdb4267297cfff6a714d674cf6e78b24b04981f0c4bd7c1f3e158f1c64cd50",
      "bytes": 601
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a2ad871217f4a8583c3fd88b2b5dfa8b9bf415b4e842b5da1ed1597fba12b976",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "6d46513ab0594122f93749e95680fb94db8b0156e5b8d8dd45cd50eb1d5fe56a",
      "bytes": 791
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "64ec0062c78ae4b4a5e2be771be236ef1899d027fb5242d9b2044fd43e32a5d1",
      "bytes": 1378
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "c0394aaae4ab9aabc0c235879e5119bb3c96b0d15993cb8fca1ff8cfa5b0a257",
      "bytes": 634
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "f4289f5659ee79c4d0bbf2fe06cd03ce0fefd0d1e6ff0d22446b859e55487e4c",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "5a139ff9104eaff0255350ce5503ac373f839ff6d5e90c91d736a384e31c3286",
      "bytes": 876
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c84c0036653f27312308f679e291f60453cb7f3f78592361a78728641c5a2187",
      "bytes": 254754
    }
  ],
  "estimated_tokens": 10215
}
-->

# Durable State Update — Chapter 863

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
1 and safe_through 863. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 863. Profile updates may replace only one
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
  "chapter": 863,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 863,
    "continuity_sources": [863],
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
    "Prince Shangshan and his party are at the imperial palace, where Hong Jin’s party has encountered the East Depot and Embroidered Uniform Guard.",
    "Hong Jin was formerly in the East Depot and shares an unresolved history with an old eunuch; he has been away for eleven years and nine days.",
    "Baek Yeon commands the Embroidered Uniform Guard and asserts the Emperor’s authority at the palace entrance.",
    "Prince Shangshan has asked Taekyung for candid advice on how to handle the confrontation."
  ],
  "continuity_sources": [
    861,
    862
  ],
  "open_questions": [
    "What happened between Hong Jin and the old eunuch, and why did Hong Jin leave the East Depot?",
    "What does the Emperor intend for Prince Shangshan?",
    "How will Prince Shangshan respond to Taekyung’s advice?"
  ],
  "safe_through": 862,
  "temporary_decisions": [
    "Render 동창 as “East Depot.”",
    "Render 금의위 as “Embroidered Uniform Guard” and 금위군 as “Imperial Guards.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 대한민국 | **Korea** | Country reference. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 주표 | 혁무진 | prince_to_subordinate_of_his_companion | Tenfold Man Hyuk Mujin | formal and playful | Zhu Bao takes Mujin’s boast literally and grants him the title. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 862
- **Aliases:** None
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard and a military officer trusted by the Emperor.
- **Personality:** Politically assured, he asserts imperial authority while presenting his demand to end a confrontation as formal deference.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; his relationship with Prince Shangshan is marked by conspicuous lack of deference.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 861
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 862
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, trusts Jin Taekyung to keep the prince safe, and has unresolved ties to former East Depot associates.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 862
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 862
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Commands the Embroidered Uniform Guard force confronting Jin Taekyung and serves the Emperor's command.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 862
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 862
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, and seeks candid counsel when making difficult decisions.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃863화



수백 명이 넘는 금의위와 동창의 환관들이 한자리에 모여 있다는 것은 그 자체만으로도 제법 볼만한 광경이었지만, 지금 이 순간 그들이 짓고 있는 표정만큼은 아니었다.

충격. 경악. 의문. 분노.

주위를 에워싼 수많은 얼굴들을 스쳐 지나가는 감정들.

그들은 하나같이 눈을 부릅뜨고, 멍하니 입을 벌리고, 자신의 귀를 의심하고, 마침내 현실을 인지함과 동시에 모든 얼굴 근육을 동원하여 분노를 표현했다.

단 두 사람을 제외하고.

“……진 공자?”

홍진은 흐릿한 눈으로 나를 바라보았고.

“하, 시바. 또 좆 됐네…….”

혁무진은 깊은 한숨과 함께 손바닥으로 얼굴을 쓸어내렸다.

음.

홍진이야 그렇다 치고, 혁무진 저 녀석은 나 때문에 한두 번 고생한 게 아니라 살짝 미안하긴 한데.

그래도 뭐.

‘어쩌라고.’

그럼 니가 조장 하든지.

그리고 이건 지엄하신 상산왕 전하께서 내리신 왕명(王命)이다.

나 역시 대한민국, 아니 대국의 백성으로서 성심성의껏 따르는 수밖에.

물론 내 이름으로 된 호패는 구경도 못 해 봤고 앞으로도 만들 생각조차 없지만, 아무튼 그런 거다.

쉽게 말하자면 합법적 깽판이라는 거지.

“명하신 대로 솔직하게 말씀드리긴 했는데. 제 대답이 마음에 드셨는지 모르겠습니다, 전하.”

천연덕스럽게 건넨 말에, 눈을 동그랗게 뜬 채 나를 바라보던 상산왕 주표가 장난꾸러기처럼 씩 웃었다.

“아니다. 짐이 원했던 대로 아주 솔직한 대답이었다. 약간 놀라긴 했지만.”

약간 아니라 상당히 놀란 것 같던데.

뜻밖의 대담함을 보인 저 어린 왕에게도, 내가 한 발언의 수위가 제법 강하게 와닿았던 모양이다.

하지만 딱히 별다른 후회는 없다.

우리가 지금 있는 곳이 무림이건 황궁이건, 약한 모습을 보이면 곧장 잡아먹히는 곳이 바로 이 세상이니까.

막다른 골목에 몰려 움츠러든 쥐는 그리 오래 살아남지 못한다. 고양이에 의해 그저 장난감처럼 이리저리 굴려지다가 끝내는 숨통이 끊길 뿐이다.

‘어차피 맞서야 한다면, 이빨을 드러내는 게 시간을 더 벌 수 있는 길이지.’

나 역시 아무런 생각 없이 막 들이댄 것은 아니다.

천자가 상산왕을 황도까지 데려왔다는 건, 적어도 모종의 명분을 갖춘 후에 제거하겠다는 의미니까.

그리고 그 말은, 사방에서 으르렁대고 있는 저 사냥개들도 주인의 명령이 떨어지기 전까지는 얌전할 거라는 뜻이기도 했다.

가장 날카로운 이빨을 지닌 대장 사냥개도 포함해서.

“허. 이것 참…… 뭐라고 해야 할지 모르겠군.”

수많은 금의위를 휘하에 거느린 수장이기 때문일까. 아니면 이미 초인의 영역에 든 고수이기에 보일 수 있는 여유일까.

그 이유가 뭐든 간에 백연의 반응은 확연히 달랐다.

그는 다른 이들처럼 살기에 가까운 분노를 표출하지도 않았고, 날 죽이는 게 평생 소원인 듯 병장기를 만지작거리지도 않았다.

그저 수염을 쓰다듬으며 이렇게 말할 뿐이었다.

“부디 충고하건대, 다음부터는 입조심하는 게 좋을 걸세. 이곳은 무림이 아니라 대국의 황실이니까.”

나는 턱을 긁적였다.

“전하께서 시키는 대로 했는데도 뭐라 하네. 이거 나처럼 힘없는 백성은 억울해서 살겠나.”

슬쩍 곁눈질하자, 신호를 알아차린 상산왕이 입을 열었다.

“금의위 지휘사 백연. 이 자는 짐의 명령에 충실히 따랐을 뿐이니, 그대는 더 이상 일언반구(一言半句)하지 말라.”

백연은 대답하지 않았다. 속내를 알 수 없는 묘한 눈빛으로 자신을 내려다보는 그의 시선에, 상산왕의 목소리에 힘이 실렸다.

“짐이 묻고 있거늘, 어찌하여 답하지 않는가!”

아.

내가 이런 건 또 못 참지.

“맞다. 감히 전하의 말을 씹다니! 이 무엄한 놈!”

발성 좋고. 타이밍 좋고.

스아아아.

분위기도 끝내주고.

4분의 3박자로 찰지게 치고 들어간 내 준엄한 질타에 사방에서 들끓는 기파.

홍진은 나직한 신음을 흘렸고, 혁무진은 내 소매를 잡아당기며 필사적으로 속삭였다.

“조장님. 조장님. 그만하세요, 제발.”

“지엄하신 황상 폐하의 아우이신 상산왕 전하가 묻고 계시지 않느냐! 대답 안 하면 황족 모욕이다! 역적이야!”

“진짜 머리가 어떻게 되신 것 아닙니까? 저 이런 곳에서 객사시키려고 지금까지 데리고 다녔어요?”

“이것 놓지 못하겠느냐! 이 검기도 쓸 줄 모르는 한심한 녀석 같으니! 네놈도 저것들과 한 패냐!”

“아니, 시팔. 제발 좀…….”

혁무진이 반쯤 울먹거리던 그때, 말없이 줄곧 상산왕을 응시하고 있던 백연이 불현듯 한 손을 들어 올렸다.

슥.

순식간에 흩어지는 무거운 공기.

하늘 같은 상관이 모욕당하는 모습에 분노를 금치 못하던 금의위들이 일제히 기세를 거둬들였고, 백연은 굳게 닫혀 있던 입술을 열었다.

“부디 용서하소서, 전하. 소신이 우둔한 탓에 무슨 답을 드려야 할지 몰라 잠시 망설였나이다.”

저 말을 곧이곧대로 믿는 병신은 이 자리에 단 한 사람도 없을 것이다.

설령 그것이 세상 물정 모르는 어린 왕이라 해도.

“용서한다. 허나 망설인 만큼 옳은 대답이 나와야 할 것이다.”

위엄 어린 태도로 응하는 주표의 모습을 보며, 나는 새삼 깨달았다.

그는 나이와 상관없이 고귀한 핏줄을 타고난 황족이었다. 여의주만 얻는다면 용이 될 수 있는 운명을 타고난 자.

어쩌면 오랜 세월 동안 곁을 지켰던 홍진조차도 상산왕을 과소평가했는지도 몰랐다.

무수한 숙청 속에서 간신히 살아남아, 유일하게 곁에 남은 어느 환관과 산서성으로 떠나야 했던 어린아이의 모습만을 기억하고 있던 무소불위의 권력자도.

“신, 금의위 지휘사 백연. 상산왕 전하의 명을 가슴 깊이 새기겠습니다.”

철컥.

금빛 철갑이 토해 내는 마찰음에 상산왕의 어깨가 움찔거리는 것이 보인다.

비록 나이에 걸맞지 않은 대담함과 위엄을 갖추었으나, 그럼에도 아직은 어린아이. 황도의 최고 권력자 중 하나와 맞서는 것에는 생각 이상으로 큰 용기가 필요했을 것이다.

‘그렇다면…….’

약간의 도움 정도는 괜찮겠지.

슥.

내심 중얼거린 나는, 무엄하게도 상산왕의 등을 스치듯이 짚었다.

갑작스럽게 흘러들어온 온기에 크게 뜬 눈으로 나를 올려다본 어린 왕은 이내 희미하게 웃으며 말을 이었다.

“이들은 짐이 다스리는 산서성의 백성이며, 동시에 친히 초청한 빈객(賓客)이니 일체의 소홀함이나 불상사도 있어서는 안 될 것이다. 알겠는가?”

또렷해진 목소리에 나를 힐끗 바라본 백연이 묘한 얼굴로 대답했다.

“이곳은 지엄하신 황제 폐하께서 머무르시는 황궁. 그 누가 감히 전하의 빈객들을 해하겠습니까?”

내가 혼잣말처럼 중얼거렸다.

“그거야 모르는 거지, 뭐. 막말로 전하 앞에서 검도 뽑는 마당에 뭘 못 해.”

“……!”

“어후, 요새 세상 살기가 무섭다, 무서워. 안 그렇습니까, 전하?”

내 엄살에 상산왕이 재차 백연을 응시했다.

“짐은 저 말이 옳다 여겨지는데, 그대는 어떻게 생각하는가?”

황궁 개꿀팁.

일단 왕이랑 친해지면, 황제의 오른팔이라 해도 당장은 쉽게 건드릴 수 없음.

그리고 내 예상대로, 잠시 침묵하던 백연의 대답은 이미 정해져 있는 것이나 다름없었다.

“소신 역시, 전하께서 하신 말씀에 동의하는 바입니다.”

“그렇다면 짐 또한 더는 긴말하지 않겠다.”

“……망극하옵니다.”

확실한 승자도, 패자도 없는 팽팽한 설전(舌戰)이었으나, 굳이 전황을 따지자면 확실히 득을 본 것은 우리였다.

지휘사의 이름으로 안전을 약속받았을뿐더러, 상산왕 주표가 지닌 권위가 그리 호락호락하지 않다는 것을 확인했으니.

문제는…….

‘언제까지 이 안전이 보장될지는 모른다는 거지.’

마치 수술대 위에 눕혀진다면 이런 기분일까.

나를 비롯한 일행 모두는 환자고, 친절한 간호사 대신 창칼을 든 금의위와 환관들이 사방에 도사리고 있으며, 이 수술의 집도의는 다름 아닌 천자(天子)가 될 것이다.

이곳은 황궁.

아직 모습을 드러내지 않은 그의 말 한마디에 운명이 뒤바뀔 수도 있다.

‘얼굴 한 번 못 본 누군가에 의해 운명이 결정된다라…….’

이거, 생각했던 것 이상으로 기분이 좆 같다.

물론 천자가 생사여탈권을 쥐고 있다고 해서, 곱게 당해 줄 생각 따위는 눈곱만큼도 없지만.

그나마 다행인 점은 아직 정확한 병명이 정해지지 않았다는 것이다.

그저 몇 바늘 꿰매는 가벼운 수술로 끝날지, 마취 주사와 수술 도구 대신 창칼을 든 무시무시한 간호사들에 의해 안락사당할지는 앞으로 어떻게 하느냐에 달렸다.

아니, 부디 그러길 바란다.

이미 집도의가 시한부 판정을 내린 상태라면, 그야말로 죽기 살기로 몸부림쳐야 할 테니까.

그리고 집도의를 가장 가까이에서 모시는 수간호사, 아니 백연은 그에 관한 새로운 소식을 들고 온 상태였다.

“황제 폐하의 명에 따라, 전하의 알현은 내일로 미뤄질 것입니다.”

“알현을 미룬다고? 형님께서 그리 말씀하셨단 말인가?”

“예. 전하.”

예상치도 못한 말에 주표는 물론이고 홍진까지 눈을 크게　떴다.

“하지만 도착 전에 듣기로는…….”

“감히 환관 따위가 어딜 끼어드는가, 홍 첩형. 아니, 이제는 도지휘동지겠군.”

이미 일면식이 있는 듯, 단호하게 홍진의 말을 잘라 낸 백연이 말을 이었다.

“때가 되면 기별할 터이니 그때까지 전하를 모시게.”

“……이유라도 알려 줄 수는 없나요?”

“폐하의 명이라 했을 텐데. 다른 이유가 필요한가?”

뭐라 말하려던 홍진이 입을 다물었다.

다름 아닌 황명이다.

그 단어 앞에서는 그 어떤 의문이나 반박조차 할 수 없었고, 나는 갑작스럽게 미뤄진 이 알현에 대한 의미에 대해 곱씹었다.

‘어째서지? 무슨 이유가 있나?’

이미 정해져 있던 알현이 미뤄졌다. 권력자들 특유의 변덕이야 딱히 놀라울 것도 없지만, 상황이 상황인 만큼 깊게 생각할 수밖에 없었다.

물론 희뿌연 안개에 휩싸인 듯한 현재로서는 그마저도 그리 길게 이어지지 못했지만.

“정 천호.”

“하명하십시오.”

“상산왕 전하를 안으로 모셔라. 그리고…….”

겉모습과는 달리 긴 세월의 흔적이 서린 백연의 회색빛 눈동자가 나를 향한 그 순간.

우우웅.

나는 전신을 옥죄는 백연의 기세를 느꼈다.

오직 나만을 향해 쏘아진 그 강대한 기운을.

그리고 그 사실을 인지함과 동시에, 하단전 깊숙이 잠들어 있던 공력을 일으켰다.

화아악.

보이지 않는 두 개의 기운이 허공을 격하여 맞닿는다. 찰나의 순간 수없이 충돌하고 뒤섞인 끝에, 마침내 안개처럼 흩어졌다.

다른 이들에게 들리지 않는 목소리와 함께.

- 제법이군, 젊은이.

가진 힘의 절반.

아니, 그 절반의 반도 되지 않는 기세로 벌인 신경전.

그 결과에서 아무것도 얻을 수 없었던 나는 대답 대신 입술을 핥았고, 잠시 나를 물끄러미 응시하던 백연은 미처 끝맺지 못했던 말을 이었다.

“다른 이들도 함께.”

“충!”

힘차게 군례를 올린 정호군이 수하들을 향해 고개를 끄덕이자, 다시금 황금빛 물결이 우리를 에워싸고 어딘가로 이동했다.

아니, 이동하려던 그 순간이었다.

“아, 한 가지를 잊었군.”

나직한 음성으로 모두의 발걸음을 멈춰 세운 백연이 한 금의위의 앞에 섰다. 그리고 입을 열었다.

“감히 전하의 앞에서 검을 뽑다니.”

서걱.

대답 대신 서늘한 절삭음과 함께 목이 솟구쳤다.

섬광처럼 휘두른 수도(手刀)로 수하를 베어 넘긴 백연이 상산왕을 향해 빙그레 웃어 보였다.

“수하의 죄는 곧 소신의 잘못. 부디 용서하소서, 전하.”
```

## Final English reading copy

```markdown
# Chapter 863

Hundreds of members of the Embroidered Uniform Guard and eunuchs from the East Depot gathered in one place would have been quite a sight on its own.

But not as much as the expressions on their faces at that moment.

Shock. Astonishment. Confusion. Anger.

Those emotions swept across the countless faces surrounding us.

Every last one of them stared wide-eyed, gaped in disbelief, wondered if they’d heard right, and then, finally recognizing reality, summoned every muscle in their faces to express their fury.

Except for two people.

“……Young Master Jin?”

Hong Jin looked at me with dazed eyes.

“Ha. Fuck. I’m screwed again……”

Hyuk Mujin dragged a hand down his face with a deep sigh.

Hmm.

Hong Jin was one thing, but Hyuk Mujin had suffered because of me more than once or twice. I did feel a little bad for him.

Still…

*So what?*

He could be squad leader, then.

Besides, this was a royal decree from His Highness Prince Shangshan himself.

As a citizen of Korea—no, of the Great Nation—I had no choice but to follow it with all my heart.

Of course, I’d never even seen an identity tag bearing my name, and had no intention of getting one. But anyway, that was the idea.

In short, this was a legally sanctioned rampage.

“I answered honestly, just as you ordered. I’m not sure whether my answer pleased you, Your Highness.”

At my casual remark, Prince Shangshan Zhu Bao, who’d been staring at me with round eyes, flashed a mischievous grin.

“No. That was exactly the honest answer I wanted. Though I was a little surprised.”

A little? He looked pretty damn surprised.

Even that young prince, who’d shown such unexpected boldness, seemed to have felt the force of my words.

But I didn’t particularly regret them.

Whether this was Murim or the imperial palace, this was a world where showing weakness meant getting devoured.

A rat cornered in an alley and cowering wouldn’t survive long. A cat would bat it around like a toy until it finally stopped breathing.

*If we have to fight back anyway, showing our teeth is the best way to buy ourselves more time.*

I hadn’t charged in without thinking, either.

The Son of Heaven bringing Prince Shangshan all the way to the imperial capital meant he intended to get rid of him only after establishing some kind of pretext.

And that meant the hunting dogs snarling at us from every direction would stay docile until their master gave the order.

Even the pack leader with the sharpest teeth.

“Good grief. I don’t know what to say to that.”

Was Baek Yeon so composed because he commanded so many members of the Embroidered Uniform Guard? Or because he was a master who’d already reached the realm of the superhuman?

Whatever the reason, his reaction was clearly different.

He didn’t show the near-killing-intent fury of the others, nor did he toy with his weapon as though killing me were his life’s ambition.

He merely stroked his beard and said,

“As a word of advice, you’d do well to watch your tongue next time. This is the imperial court of the Great Nation, not Murim.”

I scratched my chin.

“I did what His Highness told me to, and now I’m getting scolded for it. How’s a powerless commoner like me supposed to live with that?”

I shot a sidelong glance at the prince, who caught the signal and spoke up.

“Baek Yeon, Commander of the Embroidered Uniform Guard. This man merely followed my orders. You will say no more about it.”

Baek Yeon didn’t answer. As his inscrutable gaze looked down at the prince, Zhu Bao’s voice grew firmer.

“I asked you a question. Why aren’t you answering?”

Ah.

I couldn’t let that go.

“That’s right! How dare you ignore His Highness? You insolent bastard!”

Good projection. Good timing.

*Fwoooosh.*

And what an atmosphere.

My stern rebuke landed with a satisfying three-quarter beat, and a storm of energy boiled up all around us.

Hong Jin let out a quiet groan. Hyuk Mujin grabbed my sleeve and whispered frantically,

“Captain. Captain. Please, stop.”

“His Highness Prince Shangshan, the younger brother of His Majesty the Emperor, is asking you a question! If you don’t answer, that’s an insult to the imperial family! You’re a traitor!”

“Have you actually lost your mind? Have you been dragging me around all this time just to get me killed in a place like this?”

“Let go of me, you pathetic excuse for a man who can’t even use Sword Energy! Are you on their side, too?”

“No, shit. Please……”

Just as Hyuk Mujin was starting to sound half in tears, Baek Yeon, who’d been staring silently at Prince Shangshan the whole time, suddenly raised one hand.

*Swish.*

The oppressive air scattered in an instant.

The Embroidered Uniform Guard, who’d been furious at the sight of their heaven-high superior being insulted, all withdrew their auras at once. Baek Yeon opened his firmly shut lips.

“Please forgive me, Your Highness. I am slow-witted, and hesitated because I did not know how to answer.”

There wasn’t a single fool here who’d take that at face value.

Even if that person were a young prince who knew nothing of the world.

“I forgive you. But since you took so long to answer, it had better be the right one.”

Watching Zhu Bao respond with such dignity, I realized something anew.

Regardless of his age, he was a member of the imperial family, born to noble blood. He was someone destined to become a dragon if only he could obtain the dragon pearl.

Perhaps even Hong Jin, who’d stood by Prince Shangshan for so many years, had underestimated him. Perhaps even the all-powerful man who remembered him only as a child who had barely survived countless purges and been forced to leave for Shanxi Province with the sole eunuch left at his side had underestimated him.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard, will engrave Your Highness’s command deep in my heart.”

*Clank.*

At the metallic scrape of golden armor, I saw Prince Shangshan’s shoulders twitch.

He had a boldness and dignity beyond his years, but he was still a child. Facing one of the most powerful men in the imperial capital must have taken more courage than I’d imagined.

*In that case…*

A little help wouldn’t hurt.

*Swish.*

I murmured inwardly and, with all due insolence, brushed a hand against Prince Shangshan’s back.

The young prince looked up at me, eyes wide at the sudden warmth flowing into him. Then he gave a faint smile and continued,

“These people are citizens of Shanxi Province, which I govern, and guests whom I personally invited. There must be no neglect or mishap of any kind. Is that understood?”

Baek Yeon glanced at me at the sound of the prince’s newly clear voice, then replied with an odd expression.

“This is the imperial palace, where His Majesty the Emperor resides. Who would dare harm Your Highness’s guests?”

I muttered as if to myself,

“Who knows? I mean, someone’s already drawn a sword in front of His Highness. What wouldn’t they do?”

“……!”

“Good grief. The world’s a frightening place these days, isn’t it, Your Highness?”

At my feigned distress, Prince Shangshan looked at Baek Yeon once more.

“I believe those words are true. What do you think?”

A top tip for dealing with the imperial palace:

Get on good terms with a prince, and even the Emperor’s right-hand man can’t easily touch you—not for now, anyway.

And just as I’d expected, Baek Yeon fell silent for a moment before giving the answer that had practically been decided already.

“I, too, agree with Your Highness’s words.”

“Then I have nothing more to say.”

“……You honor me beyond measure.”

It had been a tense verbal exchange, with no clear victor or loser. But if I had to call the situation, we’d definitely come out ahead.

We’d secured a promise of safety in the Commander’s name, and confirmed that Prince Shangshan Zhu Bao’s authority wasn’t so easy to disregard.

The problem was…

*Who knows how long that safety will last.*

Was this what it felt like to lie on an operating table?

Everyone with me and I were patients. Instead of kind nurses, the place was crawling with members of the Embroidered Uniform Guard and eunuchs armed with blades and spears. And the surgeon would be none other than the Son of Heaven himself.

This was the imperial palace.

With a single word from the Emperor, who still hadn’t shown his face, our fates could change.

*To have your fate decided by someone you’ve never even seen…*

This felt a lot worse than I’d expected.

Of course, even if the Son of Heaven held the power of life and death, I had no intention of going down quietly.

The one saving grace was that they hadn’t made a firm diagnosis yet.

Maybe it would end with a few stitches. Or maybe I’d be put to sleep by terrifying nurses wielding blades and spears instead of anesthetic and surgical instruments. What happened next would depend on what we did.

No. I hoped that was how it would go.

If the surgeon had already declared us terminal, we’d have to fight for our lives with everything we had.

And Baek Yeon—the head nurse who served closest to the surgeon—had come bearing new information about that.

“By His Majesty the Emperor’s command, Your Highness’s audience has been postponed until tomorrow.”

“Postponed? Is that what my elder brother said?”

“Yes, Your Highness.”

Zhu Bao wasn’t the only one whose eyes widened at the unexpected news. Hong Jin’s did, too.

“But before we arrived, I was told…”

“How dare a mere eunuch butt in, Hong Cheophyeong. No—Deputy Military Commissioner now, is it?”

It seemed they’d met before. Baek Yeon cut Hong Jin off firmly and continued,

“You will attend to His Highness until you receive word.”

“……Can’t you at least tell us why?”

“I said it was His Majesty’s command. Do you need another reason?”

Hong Jin had been about to say something, but closed his mouth.

It was the Emperor’s command, after all.

That word left no room for questions or argument. I turned over the meaning of this sudden postponement in my mind.

*Why? Is there a reason?*

An audience that had already been arranged had been postponed. The whims of the powerful weren’t anything to be surprised about, but given the situation, I couldn’t help thinking hard about it.

Of course, with everything shrouded in a thick fog, I couldn’t get very far.

“Thousand Captain Jeong.”

“Your orders?”

“Escort His Highness Prince Shangshan inside. And…”

The moment Baek Yeon’s gray eyes, bearing the marks of many years despite his appearance, turned toward me—

*Rumble.*

I felt Baek Yeon’s aura tighten around my whole body.

That immense force had been aimed at me alone.

As soon as I realized it, I roused the internal energy sleeping deep in my lower dantian.

*Whoosh.*

Two invisible forces met across the empty air. They collided and mingled countless times in the blink of an eye, then finally dispersed like mist.

Along with a voice no one else could hear.

—Not bad, young man.

Half of one’s strength.

No—not even a quarter of it had gone into that contest of auras.

I gained nothing from the brief exchange, so instead of answering, I licked my lips. Baek Yeon gazed at me for a moment, then finished what he’d been saying.

“The others will come as well.”

“Understood!”

Jeong Hogun gave a vigorous military salute, then nodded to his subordinates. A wave of gold surrounded us once more, and we began moving somewhere.

Or rather, we were about to.

“Ah, I nearly forgot something.”

Baek Yeon’s quiet voice stopped everyone in their tracks. He walked up to one of the Embroidered Uniform Guard and spoke.

“You dared to draw your sword in front of His Highness.”

*Shhk.*

In place of an answer, a cold slicing sound rang out, and a head shot into the air.

Baek Yeon had cut down his subordinate with a hand blade faster than a flash of light. Then he turned to Prince Shangshan and smiled warmly.

“A subordinate’s crime is my own fault. Please forgive me, Your Highness.”
```
