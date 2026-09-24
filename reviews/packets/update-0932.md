<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0932.txt",
      "sha256": "93796c691c4ba1ce8b24886dfd5c9d75d3e9298af6a13e439a246a5bc784fde1",
      "bytes": 14048
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6681450203593842e5605d77311ccb5614c3f0d2d466c19980908fa0889703d6",
      "bytes": 1000
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0666305ef3a14502bbfe5c72134a55888b76af6f3fad7264eaf0463c809292b0",
      "bytes": 231946
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "8a609eba0575e82dce5d757713e3060cde37ac070ee92c20c9b0ac5dfd51a2d1",
      "bytes": 1445
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "804947b9cf1251aca63714c92f6e8d11962805295e9de6e8dd001cf675b35ce2",
      "bytes": 628
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "3d5423debcad875448549d9b574ebf48f58570ed8f26f52f0502971b42e1b121",
      "bytes": 699
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5adef915a3a696260f5f96dc1bcc40cdfc06b8e310f1f6f29062babd3a42d0b0",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 9820
}
-->

# Durable State Update — Chapter 932

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
1 and safe_through 932. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 932. Profile updates may replace only one
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
  "chapter": 932,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 932,
    "continuity_sources": [932],
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
    "Taekyung has recovered consciousness and is reported to be in perfect physical condition.",
    "Hong Jin has been promoted to Eunuch Hong and is responsible for the East Depot; the Cang Gong post remains vacant.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s final instruction was to find an unspecified object at a particular place."
  ],
  "continuity_sources": [
    931
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What story has So Gyo kept to herself?",
    "Where is Ma Sanbao, and what is his current status?",
    "What object and place did the Eastern Heaven Demon Lord refer to, and what significance does the object have?"
  ],
  "safe_through": 931,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 서역 | **Western Regions** | Region from which the glasses were imported. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 정기 | **vital essence** | Energy the Wudang Sect Leader says the monster absorbs from victims. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 성경 | **Bible** | Proposed scripture containing Nanman's history and the word of God. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 931
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 929
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 929
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 930
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃932화



시스템 창 오픈.

그 짧은 명령어에, 경계를 가로막고 있던 둑이 허물어졌다.

띠링. 띠링. 띠리리링!

수없이 겹쳐지며 울려 퍼지는 종소리.

그와 동시에 거대한 파도가 되어 덮쳐 오는 무수한 홀로그램 창에, 나도 모르게 입이 벌어졌다.

‘미친. 뭐가 이렇게 많아.’

마치 초등학교 여름방학 내내 밀려 있던 숙제를 마주한 기분. 아니, 그 이상이다.

언뜻 보기에도 백여 개가 훌쩍 넘어가는 홀로그램 창이 허공을 빽빽하게 메우고 있었으니까.

‘저게 다 레벨업 알림이면 딱 좋겠는데.’

물론 허무맹랑한 나만의 바람일 뿐이고, 겨우 지난 사흘 동안 저 많은 홀로그램 창이 쌓여 있었을 리도 없다.

나는 가장 빠르게 나타난 첫 번째 시스템 메시지를 시작으로 순서에 따라 읽어 내려갔다.



- 축하합니다! [업데이트]가 완료되었습니다!

- [업데이트] 진행으로 인해 시스템 사용에 약간의 불편을 끼쳐드린 점, 심심한 유감을 표합니다.



“…….”

약간의 불편. 심심한 유감이라.

이거 시작부터 상당히 열 받네.

바로 그 ‘약간의 불편’ 때문에 생사를 넘나들었던 기억이 새록새록 떠올랐지만, 잠깐의 분노는 바로 그다음 메시지를 읽자 빠르게 누그러졌다.



- 하여, 사과의 의미로 합당한 보상을 지급하고자 합니다.



“오.”

그래, 이게 맞지.

확실히 정기 점검, 임시 점검, 연장 점검, 긴급 점검이라는 4대 명검을 전가의 보도처럼 휘두르는 똥망겜과는 근본부터가 다르다.

개고생한 만큼 합당한 보상을 주고, 유저의 쾌적한 플레이를 위해 물심양면 도와주는 것이야말로 킹갓 시스템의 순기능 아니겠나.



[업데이트 보상]이 인벤토리로 지급되었습니다.

신규 아이템을 확인하시겠습니까?

Y  /  N



보상. 신규 아이템.

저 별것 아닌 두 단어에 오랫동안 잊고 살았던 동심이 깨어난다.

일곱 살 때 받은 크리스마스 선물을 열 때보다 더 떨리는 순간.

나는 설렘과 기쁨이 공존하는 마음으로 대답했다.

“오픈.”

띠링.



아이템창



[누가 만들었는지 모를 회중시계]

종류 : 아이템

등급 : 無

제한 : 無

설명 : 알려지지 않은 누군가에 의해 제작된 회중시계. 매우 단단하다. 언뜻 보면 낡고 고장 난 시계 같지만, 자세히 보아도 낡고 고장 난 시계 같다.





“……?”

뭐여, 이게.

순간 뇌 정지가 온 나는 멍하니 손에 들린 회중시계를 내려다보았다.

아이템 설명에 적힌 그대로였다.

언뜻 보아도, 자세히 보아도 고장 난 시계다. 당장 이걸로 시 한 편 정도는 뚝딱 지을 수 있을 정도다.

제목 회중시계.

자세히 보아도 낡았다.

오래 보아도 고장 났다.

좆 같다.

“…….”

정신이 나갈 것 같다.

일곱 살 때 크리스마스 선물을 가져다준 산타 할아버지가 현관문 비밀번호를 누르고 위풍당당하게 들어온 것으로도 모자라, 엄마와 뽀뽀를 하는 광경을 보고 느꼈던 배신감에 비견될 수 있을 정도다.

‘이딴 게…… 업데이트 보상?’

뒤통수가 얼얼해진 나는 충격에서 빠져나오려 애썼다.

‘아니, 아니지. 이럴 리 없어.’

둘 중 하나다.

고단하고 힘든 상황에 지쳐있는 나를 위해 시스템이 준비한 깜짝 몰래 카메라거나, 아니면 아직 내가 모르는 특별한 무언가가 숨어 있거나.

‘알림으로 뜬 게 이거 하나니까 일단 몰카는 아니고. 그렇다면…….’

흐트러진 정신을 수습한 나는 손에 들린 회중시계를 꼼꼼하게 살폈다.

그리고 얼마 지나지 않아 누군가의 손때로 반들거리는 시계의 뒷면에서, 조금 전까지 발견하지 못했던 무언가를 확인할 수 있었다.

‘잠깐.’

아마도 평범한 사람의 눈으로는 볼 수 없었을 만큼, 거의 지워지다시피 한 흐릿한 흔적.

공력을 일으켜 눈으로 흘려보내자, 더욱 향상된 안력(眼力)을 통해 희미한 글귀를 확인할 수 있었다.

“이, 이건 설마…….”



고장 난 시계도 하루에 두 번은 맞는다.



“아무것도 아니잖아, 개새끼들아!”

쾅!

온 힘을 실어 내던진 회중시계가 대포알처럼 날아가 벽에 부딪혔다.

아니, 정확히는 벽을 박살 냈다.

쿠구궁!

산산이 허물어지는 벽. 그 너머로 입을 딱 벌린 채 이쪽을 바라보고 있는 혁무진이 있었다.

“이게 무…… 헉, 설마 암습입니까!”

어떻게 보면 암습은 암습이다.

아무런 마음의 준비도 없는 상황에서 이런 식으로 뒤통수를 맞았더니 칼에 찔린 것처럼 폐부가 욱신거리는 중이니까.

“무진아. 어지럽다. 무진아.”

“조장님! 가만히 계십시오! 제가 지켜 드리겠습니다!”

“너가? 나를?”

순간 멈칫한 혁무진이 넌지시 말을 건넸다.

“그건 그러네요. 적 대협을 모셔올까요?”

“……부르면 괜히 우리만 탈탈 털린다. 하지 마.”

“아, 뭐야. 깜짝 놀랐네. 암습 아니죠?”

“그래, 인마. 그러니까 괜히 법석 떨지 말고 거기 있는 거나 도로 주워 와.”

뿌옇게 피어오른 먼지 속에서 잔기침을 내뱉던 혁무진이 조심스럽게 회중시계를 집어 올렸다.

“그, 조장님. 혹시 말씀하신 물건이 이 철로 만들어진 쓰레기는 아니죠?”

“…….”

“죄송합니다. 맞나 보네요. 그리고 혹시 모르니 쓰레기라는 말은 취소하겠습니다.”

언럭키 십상시답게 내 불편한 심기를 간파한 혁무진이 후다닥 달려와 회중시계를 건넸다.

“그런데 이게 정확히 뭡니까?”

“고장난 시계.”

“시계요? 이 손바닥만 한 게?”

회중시계의 생소한 형태에 낯설어하는 혁무진을 향해, 나는 슬픈 목소리로 대답했다.

“그래 봤자 쓰레기지. 엄청 단단하고, 매우 쓸모없는.”

“이딴 걸 왜 갖고 계세요? 게다가 고장까지 난 걸.”

“……나도 어쩌다가 받은 거야, 이 새끼야. 말 함부로 하지 마.”

한 마디, 한 마디가 칼날이 되어 가슴을 후벼판다.

의도치 않게 회중시계의 강도를 확인하게 된 나는 차오르는 눈물을 삼켰다.

‘아이템 설명이 모두 사실이었다니.’

어떤 종류의 진실은 때때로 너무나도 가혹하게 느껴질 때가 있다. 지금의 내게는 이 회중시계가 그랬다.

‘그런데 왜 시스템은 하필 이딴 걸 준 거지?’

일반 퀘스트도 아니고, 무려 업데이트를 완료하고 얻은 보상이 이런 쓰레기라니.

마지막 희망을 걸고 설마 하는 마음을 품은 채 회중시계를 재차 살폈지만, 그런 나를 기다리고 있는 건 더욱 큰 비참함이었다.

‘진짜 고장난 시계네, 이거.’

우선 시간부터가 단단히 글러 먹었다.

이미 자정을 향해 달려가는 시각임에도 회중시계의 시침(時針)이 가리키고 있는 것은 다섯 시 어림.

그마저도 응당 적혀 있어야 할 숫자가 없어 방향을 눈대중으로 판별해야 한다.

‘분침(分針)은 어디에 팔아먹었는지 보이지도 않고.’

이쯤 되니 이걸 회중시계라고 불러도 되나 싶다.

회중시. 혹은 회중계 정도도 과분한 게 아닐까.

‘따로 시간을 조정할 수 있는 것도 아니고. 그렇다고 계속 움직이는 것 같지도 않고. 도대체 뭐야, 이거?’

이리저리 흔들고 귀에 바짝 들이대 봤지만, 째깍거리는 소리는커녕 내부 부품이 맞물리는 희미한 소음조차 없다.

그나마 장점이라고는 딱 하나. 내가 힘주어 눌러 봐도 으스러지기는커녕 흠집도 안 날 정도로 단단하다는 것뿐인데…….

‘설마 무기로 쓰라고 준 건가. 아니면 비상시를 대비한 방패막이?’

문득 전쟁 영화에서 단골손님처럼 등장하는 한 장면이 뇌리를 스쳤다.

탕, 날카로운 총성과 함께 쓰러지는 존슨 일병.

그러나 전우의 죽음을 직감하고 주위로 달려간 소대원들이 본 것은, 평소 독실한 신자였던 존슨 일병이 항상 가슴에 품고 다니던 미니 성경책에 박힌 총알…….

“와, 첫 개시부터 정신 나갈 것 같네.”

혼잣말을 중얼거리는 내 모습에, 아까부터 줄곧 눈치를 살피던 혁무진이 조심스럽게 입을 열었다.

“저어기, 조장님?”

“환관마냥 은근한 목소리로 부르지 마라. 죽는다, 진짜.”

“넵. 뭐 하나만 여쭤봐도 되겠습니까.”

“씨부려.”

“다름이 아니고, 그거 버리실 겁니까?”

내 손바닥에 놓인 회중시계를 슬쩍 가리킨 혁무진이 딴청을 피우듯 말을 이었다.

“아니, 만약 버리실 거라면 조장님의 오른팔이자 심장이며 변치 않는 충심을 가진 누군가에게 내려 주시는 게 어떤가 싶어서 조심스럽게 건의드려 봅니다.”

“조심스러운 거 맞냐. 너 지금 굉장히 당당한데.”

“뭐, 그냥 그렇다는 거죠. 안 쓰실 거면 굳이 갖고 계실 필요는 없잖습니까.”

“이딴 게 왜 갖고 싶은데?”

“그거 시계라면서요. 그것도 척 보아하니 서역(西域)에서 들어온 귀한 물건 같은데, 고장 났어도 들고 다니면 멋있지 않겠습니까?”

웬일로 논리정연한 주장을 펼치는 혁무진의 모습에, 나는 조용히 입맛을 다셨다.

‘사실 저 녀석한테 줘도 딱히 상관없을 것 같긴 한데…….’

왠지 모를 찝찝함이랄까. 목에 걸린 가시 같달까.

이대로 이 염병할 회중시계를 혁무진에게 줘 버리면, 마치 중국집에 가서 얼큰한 짬뽕 국물 없이 볶음밥을 먹은 것보다 시원찮은 기분이 될 것 같았다.

‘내가 아직 모르는 뭔가가 있을 수도 있고. 조금 더 시간을 두고 지켜본 후에 진짜 잡템이라고 생각되면 그때 줘도 늦지 않지.’

사실 시스템이 언제나 항상 엄청난 보상을 안겨 주는 것은 아니었다.

정확히 어떤 방식으로 보상을 정하는지는 자세히 모르겠지만, 지금까지 수많은 퀘스트를 완수하며 하등 쓸모없는 잡템을 받은 적도 많았다.

티끌 모아 태산이라더니, 그렇게 인벤토리에 쌓인 잡템만 어느덧 한 트럭.

다만 한 가지 마음에 걸리는 건, 지금 내 손에 들린 이 고장난 회중시계가 무려 업데이트 완료 보상이라는 것이었다.

“음.”

별다른 말 없이 고개만 끄덕이던 그때, 혁무진의 은근한 목소리가 귓가에 닿았다.

“저기, 조장님?”

“왜.”

“뭐라고 말씀을 좀…….”

“아직이니까 조금만 기다려. 한 달, 아니 보름 정도만.”

보름. 한 달의 절반.

그것이 내가 정한 마지막 심사 기간이었고, 혁무진의 얼굴이 환해졌다.

“그럼 보름 뒤에는 주시는 겁니까?”

“어. 물론 나한테 쓸모없는 물건이라는 걸 확인한 뒤라는 전제하에.”

“에이, 어차피 서역에서 만든 물건이라 고칠 수 있는 기술자도 없을 텐데요. 그냥 생긴 것이 예쁘장하니, 멋으로 갖고 다닌다면 모를까.”

혁무진이 기분 나쁘게 히죽히죽 웃으며 말을 이었다.

“그런데 이 물건은 뭐라고 부릅니까?”

“회중시발……이 아니라 회중시계.”

“캬. 이름도 예쁘네. 저 고리에 가죽끈을 끼워서 목에 달고 다니면 어딜 가든 이목이 쏠릴 것 같습니다.”

“그래?”

“예. 가죽끈 대신 반짝거리는 비단이면 더 좋을 것 같네요.”

“오. 그래?”

포목점 재벌가 집안의 장손다운 발언이었지만, 그것과는 별개로 훌륭한 의견이었기에 나는 망설임 없이 입고 있던 금빛 비단옷의 옷자락을 찢어 고리에 끼운 다음 목에 걸었다.

“어때. 나 예뻐?”

“어후, 혹시 성함이 금태양이십니까? 아주 빛이 납니다.”

“이대로 선물하면 좋아하겠지?”

“조장님 절 위해서 그렇게까지…….”

혁무진의 눈동자가 감동으로 파르르 떨리던 그때. 내가 목에 걸린 회중시계를 흐뭇하게 바라보며 말을 이었다.

“너 말고, 주 소저.”

“…….”

“주 소저도 이런 선물을 받으면 마음이 좀 풀리지 않을까? 안 그래?”

“…….”

“대답.”

“……참 좋아하시겠네요. 예.”

순식간에 짜게 식어 버린 눈빛.

혁무진이 두 눈동자로 소리 없는 비난을 퍼붓던 그 순간.

나는 전각을 향해 가까워지는 수십의 인기척을 느끼고 창밖을 향해 고개를 내밀었다.

“정지, 정지, 정지! 움직이면 벤다. 회중!”

일렁이는 횃불 속, 금의위들의 선두에서 잠시 침묵하던 정호군이 입을 열었다.

“그게 무슨 헛소리냐.”

“이 멍청한 폐급 금의위 새끼! 암구호도 숙지 안 하고 오다니!”

“아니, 그러니까 갑자기 이게 무슨…….”

“입 닥쳐! 시계라고 해! 어서!”

“……시계.”

“입 닥치라고 했지!”

“…….”

성난 복어마냥 잔뜩 독기가 오른 눈빛을 보니 이쯤에서 장난은 그만둬야 할 듯싶다.

크게 선심을 베푼 나는 입을 꾹 다문 정호군을 향해 물었다.

“그래서, 왜 왔어?”

“잠시 따라와 줘야겠다.”

“내가 오라면 오고 가라면 가는 사람이야? 그리고 나 지금 진짜 바빠. 할 일 많아.”

“폐하께서 부르신다.”

“아.”

그럼 가야지.
```

## Final English reading copy

```markdown
# Chapter 932

“Open System window.”

At that brief command, the dam blocking the floodgates came crashing down.

*Ding. Ding. D-d-ding!*

A chorus of chimes rang out, overlapping again and again.

At the same time, countless holographic windows surged toward me like a giant wave. My mouth fell open before I could stop it.

*Holy shit. Why are there so many?*

It felt like staring at all the homework I’d put off over the entire summer vacation in elementary school. No—worse than that.

Even at a glance, well over a hundred holographic windows packed the air around me.

*It’d be nice if they were all Level-up notifications.*

Of course, that was nothing but wishful thinking. And there was no way all those holographic windows had piled up in just the past three days.

I started with the first System message to appear and read them in order.

> **System**
> Congratulations! Update is complete!
>
> We sincerely regret any minor inconvenience caused by the Update.

“……”

Minor inconvenience. Sincere regret.

Well, I’m already pissed off.

The memories of coming close to death because of that very “minor inconvenience” came flooding back. But the next message quickly cooled my anger.

> **System**
> Therefore, as an apology, we would like to provide you with an appropriate Reward.

“Oh.”

Right. That’s more like it.

This System was fundamentally different from those garbage games that wielded the Four Great Swords—scheduled maintenance, unscheduled maintenance, extended maintenance, and emergency maintenance—like an heirloom blade.

Giving you a fitting reward for all your hard work and doing everything it could to make the user’s experience more enjoyable—that was the true purpose of a kingly, god-tier System.

> **System**
> Update Reward has been delivered to your Inventory.
>
> Would you like to check your new Item?
>
> **Y / N**

Reward. New Item.

Those two unremarkable words awakened the childlike wonder I’d long forgotten.

This was even more thrilling than opening the Christmas present I’d gotten when I was seven.

With excitement and joy mingling inside me, I answered.

“Open.”

*Ding.*

> **System**
> **Item Window**
>
> Pocket Watch of Unknown Make
>
> **Type:** Item  
> **Grade:** None  
> **Restriction:** None  
> **Description:** A pocket watch made by someone unknown. Very sturdy. At a glance, it looks like an old, broken watch. Even on closer inspection, it still looks like an old, broken watch.

“……?”

What the hell is this?

My brain stalled. I stared blankly at the pocket watch in my hand.

It was exactly as the Item description said.

At a glance, it looked broken. On closer inspection, it still looked broken. I could’ve written an entire poem about it on the spot.

*Title: Pocket Watch.*

*It looks old up close.*

*It stays broken no matter how long I look.*

*Fucking sucks.*

“……”

I felt like I was going insane.

It was on par with the betrayal I’d felt when Santa Claus—the old man who’d brought my Christmas present when I was seven—had punched in the front door’s passcode and strolled in like he owned the place, then kissed my mom right in front of me.

*This is my… Update Reward?*

My head still buzzing, I tried to pull myself out of the shock.

*No, no. This can’t be right.*

There were only two possibilities.

Either the System had prepared a surprise hidden-camera prank for me, exhausted as I was from everything I’d been through, or there was something special about the watch that I hadn’t figured out yet.

*There was only one notification, so it’s not a prank. Which means…*

I gathered my scattered wits and carefully examined the watch in my hand.

It didn’t take long to notice something I’d missed on the back, polished smooth by someone’s touch.

*Wait.*

The mark was so faint it had nearly vanished—probably too faint for an ordinary person to see.

I stirred up my internal energy and sent it toward my eyes. With my enhanced vision, I made out the dim inscription.

“N-no way…”

> A broken clock is right twice a day.

“It doesn't mean a damn thing, you bastards!”

*BANG!*

I hurled the pocket watch with all my strength. It flew like a cannonball and struck the wall.

Or, to be precise, it smashed through the wall.

*Rumble!*

The wall crumbled apart. Beyond it, Hyuk Mujin stood staring at me with his mouth hanging open.

“What the—Gasp! Was that an assassination attempt?!”

In a way, it was.

I’d taken a hit to the back of the head like that with absolutely no warning, and now my insides ached as if I’d been stabbed.

“Mujin. I’m dizzy. Mujin.”

“Captain! Stay still! I’ll protect you!”

“You? Protect me?”

Hyuk Mujin hesitated, then cautiously offered, “Should I bring Great Hero Jeok over?”

“……If you call him, we’re the ones who’ll get put through the wringer. Don’t.”

“Oh, come on. You scared me. It wasn’t an assassination attempt, right?”

“Yeah, idiot. So quit making a scene and go pick that thing up.”

Hyuk Mujin coughed in the cloud of dust rising around him, then cautiously picked up the pocket watch.

“C-Captain. The thing you mentioned isn’t this piece of iron junk, is it?”

“……”

“Sorry. I guess it is. And, just in case, I take back the ‘junk’ part.”

As befitting an unlucky eunuch, Hyuk Mujin had sensed my foul mood and hurried over to hand me the watch.

“But what exactly is it?”

“A broken watch.”

“A watch? This little thing?”

I answered in a mournful voice as Hyuk Mujin eyed the unfamiliar shape of the pocket watch.

“It’s still junk. Very sturdy and completely useless.”

“Why would you keep something like this? It’s even broken.”

“……I got it somehow, okay? Watch your mouth.”

Every word was a blade, digging into my heart.

I’d confirmed the watch’s durability by accident, and now I swallowed back the tears welling up inside me.

*The Item description was telling the truth after all.*

Some truths could be unbearably cruel. This pocket watch was one of them.

*But why would the System give me something like this?*

This wasn’t some ordinary Quest. It was the Reward I’d received for completing an entire Update, and it was garbage like this.

I clung to one last sliver of hope and examined the watch again. But what awaited me was an even greater humiliation.

*This thing really is broken.*

For starters, the time was completely wrong.

It was already nearing midnight, but the hour hand pointed somewhere around five.

And the numbers that should’ve been there were missing, so I had to estimate its position by eye.

*And where the hell did the minute hand go?*

At this point, I wasn’t sure I could even call it a pocket watch.

A pocket watch. Maybe a pocket dial. Even that seemed generous.

*I can’t adjust the time, either. And it doesn’t look like it’s moving. What the hell is this thing?*

I shook it this way and that, then pressed it right up to my ear. There wasn’t so much as a ticking sound—not even the faintest noise of its inner parts turning.

It had only one advantage: it was so sturdy I couldn’t crush it no matter how hard I squeezed, and couldn’t even scratch it.

*Did they give it to me as a weapon? Or a shield for emergencies?*

A familiar scene from a war movie suddenly flashed through my mind.

A sharp gunshot rang out. Private Johnson collapsed.

But when his squadmates rushed over, sure their comrade was dead, they found a bullet lodged in the little Bible he always carried over his heart—he’d been a devout believer, after all…

“Wow. This is already driving me insane.”

Hyuk Mujin, who’d been watching me warily for a while, cautiously spoke up.

“Um, Captain?”

“Don’t call me in that sly, eunuch-like voice. I’ll kill you. Seriously.”

“Yes, sir. May I ask you something?”

“Spit it out.”

“Um… are you going to throw that away?”

Hyuk Mujin pointed discreetly at the pocket watch in my palm, then kept talking as though he were making casual conversation.

“If you are, I’d like to humbly suggest giving it to someone who’s your right arm, your heart, and unwaveringly loyal to you.”

“Was that supposed to be humble? You sound pretty confident.”

“Well, I’m just saying. If you’re not going to use it, there’s no reason to keep it.”

“Why the hell do you want this thing?”

“It’s a watch, isn’t it? And judging by the look of it, it’s a rare item from the Western Regions. Even if it’s broken, wouldn’t it look cool to carry around?”

Hyuk Mujin made a surprisingly coherent argument. I quietly smacked my lips.

*I guess it wouldn’t really matter if I gave it to him…*

But something about it bothered me. Like a fish bone stuck in my throat.

If I handed this godforsaken pocket watch to Hyuk Mujin right now, I’d feel worse than if I went to a Chinese restaurant and ate fried rice without a bowl of spicy jjambbong broth.

*There might be something I don’t know about it yet. I can wait a little longer and see. If I decide it really is junk, I can give it to him then.*

It wasn’t as if the System always gave out incredible Rewards.

I didn’t know exactly how it decided what to hand out, but after completing countless Quests, I’d received plenty of useless junk Items.

They said many a little made a mickle. My Inventory was now packed with enough junk to fill a truck.

The one thing that bothered me was that this broken pocket watch in my hand was the Reward for completing an Update.

“Hmm.”

I only nodded, without saying a word. Then Hyuk Mujin’s sly voice reached my ear.

“Um, Captain?”

“What?”

“Could you give me an answer?”

“Not yet. Just wait a little. A month—or, no, half a month.”

Half a month. Half of one month.

That was the final trial period I’d decided on, and Hyuk Mujin’s face lit up.

“So you’ll give it to me in half a month?”

“Yeah. Assuming I’ve confirmed it’s useless to me, of course.”

“Come on. It came from the Western Regions. There probably isn’t a craftsman who can fix it around here. At most, you can carry it around because it looks pretty.”

Hyuk Mujin grinned unpleasantly as he went on.

“But what do you call it?”

“Pocket-watch, shi—pocket watch.”

“Wow. That’s a lovely name. You could thread a leather cord through that ring and wear it around your neck. It’d draw eyes wherever you went.”

“Yeah?”

“Yes. A shiny silk cord would look even better than leather.”

“Oh, yeah?”

It was a suggestion worthy of the eldest grandson of a wealthy textile-merchant family. And quite a good one, too. Without hesitation, I tore a strip from the gold silk robe I was wearing, threaded it through the ring, and hung the watch around my neck.

“How do I look? Pretty?”

“Whew. Is your name Mr. Golden Sun? You’re practically glowing.”

“They’d like it if I gave it to them like this, wouldn’t they?”

“Captain, you’d go that far for me…”

Hyuk Mujin’s eyes trembled with emotion. I gazed fondly at the pocket watch hanging around my neck and continued.

“Not you. Young Lady Ju.”

“……”

“Maybe Young Lady Ju would be less upset if she got a gift like this. Don’t you think?”

“……”

“Answer me.”

“……I’m sure she’d love it. Yes.”

His eyes had gone cold in an instant.

As Hyuk Mujin silently berated me with his gaze, I sensed dozens of people approaching the pavilion. I leaned out the window.

“Stop! Stop! Stop! Move and I’ll cut you down. Pocket watch!”

At the head of the Embroidered Uniform Guard, their torches flickering, Jeong Hogun fell silent for a moment before replying.

“What nonsense are you talking about?”

“You stupid, useless Embroidered Uniform Guard bastard! You showed up without even learning the password!”

“No, I mean, what is this all of a sudden…?”

“Shut up! Say ‘watch’! Hurry!”

“……Watch.”

“I said shut up!”

“……”

With that angry, venomous look in his eyes, like an enraged pufferfish, it seemed I’d better stop messing with him.

I generously decided to let him off the hook and asked Jeong Hogun, who’d clamped his mouth shut.

“So, why are you here?”

“You need to come with me for a moment.”

“Am I someone who comes and goes just because you tell me to? Besides, I’m really busy right now. I’ve got a lot to do.”

“His Majesty has summoned you.”

“Oh.”

Then I’d better go.
```
