<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0937.txt",
      "sha256": "9d79018b33ce21ce549d8db3eb5f9fe8f4e4ee2978a0e195e75608752254ae59",
      "bytes": 12361
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3728db6f6509505e9a0270697e6a8028ddd70beddc84230edae2efd919f080cb",
      "bytes": 2419
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b51f7a56cfa82ca1164fe5c2453945cbf42f0adc0ae050d159295fd4e544b433",
      "bytes": 232009
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "6e26037171c08737b10d5f4f4852155bb2ec89555e64dfb0abb1859d6c87ba00",
      "bytes": 838
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "61a37e6e624fe04ba268dc0139ec3770baed89e1088021d7d1a1c7ebd9bcd769",
      "bytes": 853
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "8d5936e0dd7c0c054fcc1ad9e728f3acf431ce9a7aa79c29dfc5c7f9d2162339",
      "bytes": 1445
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "c415739312704f8dd440cde8c0d206a5d2ba2f993a11cea9a37f248030cda0ca",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 9825
}
-->

# Durable State Update — Chapter 937

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
1 and safe_through 937. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 937. Profile updates may replace only one
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
  "chapter": 937,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 937,
    "continuity_sources": [937],
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
    "The Emperor was poisoned with Blood Soul Gu after the coup; it has reached his marrow, and he has endured its effects for more than ten years.",
    "The Divine Physician says the Emperor’s vitality is at its limit and cannot guarantee he will survive another couple of months.",
    "The Myriad-Poison Ring failed against the Emperor’s Blood Soul Gu; the gu thrashed more violently when it sensed the ring’s energy.",
    "Jin Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; the reward and failure consequence are unknown.",
    "The Emperor has prepared for his death by transferring his loyal retainers and power base to Zhu Bao, but avoids meeting his younger brother to spare him the grief of an impending farewell.",
    "Taekyung told Jeok Cheongang about the Emperor’s Blood Soul Gu poisoning, breaking his promise to keep the matter secret.",
    "The System update reward is a very durable pocket watch that appears broken and bears the faint inscription, “A broken clock is right twice a day”; its significance is unknown.",
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin.",
    "Hong Jin is Eunuch Hong, responsible for the East Depot; the Cang Gong post remains vacant.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s final instruction was to find an unspecified object at a particular place.",
    "The Emperor has publicly exposed Dark Heaven and declared his intent to crush it; war against Dark Heaven has begun."
  ],
  "continuity_sources": [
    935,
    936
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What object and place did the Eastern Heaven Demon Lord refer to, and what significance does the object have?",
    "What is the significance, if any, of the broken pocket watch given as the System update reward?"
  ],
  "safe_through": 936,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 습득               | **Acquired**                   |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |
| 앵속 | **poppy** | The dried poppy sap Hong Jin describes; Taekyung identifies it as opium. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 혁무진 | 홍진 | martial artist addressing a senior official and political ally | Comrade Hong | casual and coaxing | Hyuk Mujin addresses Hong Jin as 홍 동지님 while trying to calm him and de-escalate the confrontation. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |

## Listed compact profiles

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 936
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 936
- **Aliases:** None
- **Role:** Hong Jin is Eunuch Hong, a former Deputy Military Commissioner of Shanxi Province and East Depot member who is now responsible for the East Depot and remains a trusted aide to Prince Shangshan.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential with Prince Shangshan, but warm, familiar, and playfully forthright with trusted allies.
- **Relationships:** Hong Jin is devoted to Prince Shangshan and is trusted by the Emperor to take responsibility for the East Depot; he is a longtime friend of Ma Sanbao and a trusted ally of Jin Taekyung.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 936
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 932
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃937화



“중요한 일이라기에 최대한 빠르게 처리했…… 어머, 분위기 왜 이래요?”

방 안에 들어서자마자 이상 기류를 감지한 홍진의 물음에, 나는 착잡한 표정으로 대답했다.

“아무 일도 아닙니다.”

“아무 일도 아니긴. 척 봐도 무슨 일이 있었던 것 같은데?”

나와 혁무진을 번갈아 바라보던 홍진이 문득 진중해진 표정으로 중얼거렸다.

“아, 그거구나? 음. 그런데 그 문제는 어쩔 수 없죠.”

“……?”

“괜찮으니까 너무 상심하진 마요. 사람이 살다 보면 그럴 수도 있지, 뭘.”

뭐지. 설마 홍진도 알고 있었나?

돌이켜 생각해 보면 현재의 그는 동창 태감이니, 황제의 병환을 파악하고 있었을 가능성은 충분하다.

‘지난 사흘 동안 신나게 역적들 주리를 틀어 대면서 그에 관한 정보를 들었을 수도 있고.’

합리적인 사고방식으로 결론을 도출해 낸 나는 조심스럽게 입을 열었다.

“이미 알고 계셨습니까?”

잠시 머뭇거리던 홍진이 고개를 끄덕였다.

“응. 어쩌다 보니 들었어요.”

“극비 사항인데…… 생각보다 아는 사람이 많네요.”

“눈과 귀는 어디에나 있으니까요. 아무리 꽁꽁 싸매고 감추려고 해도 결국에는 새어 나가기 마련이죠.”

하긴. 황제만 입을 다문다고 모든 비밀이 지켜지는 것은 아니다.

모든 사건에는 피해자와 가해자가 나뉘어 있고, 가해자에게도 입은 달려 있으니까.

이미 죽거나 혹은 죽을 날만을 기다리고 있는 역적들.

홍진과 금의위의 손을 거친 그들 중에는 동천마군의 최측근으로서 황제가 혈혼고에 중독되었다는 사실을 아는 자들도 있었을 것이다.

“죄인들을 문초하는 과정에서 알게 된 모양이군요. 그중 누구누구였습니까?”

“네?”

“그 사실을 알고 있던 죄인들 말입니다. 동천마군과 분명 밀접한 연관이 있었을 텐데요.”

“어, 그게…….”

아무래도 언급하기에는 민감한 사항이었을까.

뒤늦게 실수를 깨달은 내가 손사래를 치려던 그때, 조용히 눈을 깜빡이던 홍진이 말을 이었다.

“나는 태산 소협한테 들었는데?”

“아. 그렇구…… 잠깐만. 누구요?”

“태산 소협이요. 덩치 엄청나게 큰 그 사람.”

“……?”

아니, 이거 뭔가 이상한데.

침묵하는 나를 대신해서 혁무진이 입을 열었다.

“제가 아는 그 태산이 맞습니까?”

“응.”

“이름만큼이나 덩치가 산만 하고.”

“그렇지.”

“평소에는 멍청하다가 먹는 얘기만 나오면 똑똑해지고.”

“그것까진 모르겠는데.”

“오향장육에 미쳐 있는.”

“그건 확실해요. 사실 어제 첩보가 하나 들어왔는데, 수하들이 하는 말에 의하면 황실 숙수들이 그 사람 음식에 독을 타려고 했다더라고.”

황실 숙수 선정 암살 일 순위라면 내가 아는 그놈이 맞다.

나는 극심한 혼란을 느끼며 물었다.

“아니, 걔가 그걸 어떻게 알아요?”

“어떻게 알긴. 봤으니까 알지.”

“그럴 리가요. 못 봤을 텐데?”

“똑똑히 봤다던데?”

“……도대체 지금 무슨 얘기를 하시는 겁니까?”

“……그건 오히려 내가 묻고 싶은 말이에요. 갑자기 죄인은 뭐고, 문초 얘기는 왜 나온 거지?”

눈살을 찌푸린 채 나를 바라보던 홍진이 말을 이었다.

“진 공자가 막 깨어났을 때 있었던, ‘그 일’을 얘기하는 거 아니었어요?”

“예, 예?”

“지금 많이 불안정해 보이는데, 설마 그것 때문에 그래요? 진심으로 괜찮다니까 자꾸 왜 그래. 그저 남들보다 조금 더 기운이 넘치는 것뿐인데.”

“……!”

아니, 미친.

삽시간에 눈앞이 캄캄해진 나는 몸을 부르르 떨었다.

“그걸, 그걸 어떻게.”

“이미 소문이 파다해요. 몰랐어?”

“소문이 파다……?”

“그나마 나는 잠시 자리를 비운 탓에 늦게 안 편이에요. 진 공자 깨어나고 두 시진도 안 되어서 내궁(內宮) 사람 절반은 그 소식을 들었을걸.”

숨이 막힌다. 손발이 벌벌 떨리고 눈물이 날 것 같았다.

마치 어느 날 심심해서 TV를 틀었더니, 공중파 채널에서 내 몽정 파티를 열어 주고 있는 것 같은 기분.

병에 걸린 사람처럼 경련하던 나는 간신히 목소리를 쥐어 짜냈다.

“태산이, 태산이 그 새끼 당장 잡아 와.”

입을 딱 벌린 채 굳어있던 혁무진이 대답했다.

“이런 말씀드리기 정말 죄송한데, 태산이가 저보다 더 센데요.”

“어떻게든 잡아 와!”

“아니, 조장님도 아시잖아요. 걔는 두 손으로 사람을 찢어요.”

“나는 한 손으로도 널 찢어.”

“앗. 아앗.”

짧은 탄성을 흘린 혁무진이 후다닥 달려나가자, 무거워진 공기를 느낀 홍진이 착잡한 표정으로 입을 열었다.

“진 공자님. 너무 그러지 마.”

혈혼고 치료에 관한 근심도 지금만큼은 머릿속에서 깨끗하게 지워진 상황.

위로를 건네는 홍진에게, 나는 탄식하듯 대답했다.

“남 일이라고 말 함부로 하지 마십시오.”

“괜찮다니까.”

“뭐가 괜찮아요. 나 같은 상황이 되어 본 적이나 있어요?”

내 날카로운 물음에, 홍진이 슬픈 미소를 띤 얼굴로 대답했다.

“그런 상황이 있을 리가 없지. 난 이미 오래전에 잘랐잖아.”

“…….”

“그냥 좋게 생각해요. 난 오히려 진 공자가 부러운걸. 특히 장마철에는 거기가 쑤셔서 앵속 없이는 제대로 걷기도 힘들 때가…….”

“알겠어요. 알겠으니까 그만하세요. 제발.”

심심할 때마다 꺼내는 고자 가불기로 내 입을 닥치게 만든 홍진이 품에 들고 있던 뭔가를 내밀며 말을 이었다.

“안 그래도 그러려고 했어요. 나도 바쁜 몸이라 부탁받은 물건만 건네주고 가려고 온 거야.”

그리고 탈룰라의 덫에 걸려 정신이 번쩍 든 나는, 그제야 홍진의 손에 들린 자그마한 철궤(鐵櫃)를 발견하고 그가 이곳을 다시 방문한 목적을 떠올릴 수 있었다.

동천마군이 마지막 순간 알려 주었던 의미불명의 장소.

그곳에서 찾으라고 했던 물건.

“이건…….”

“보이는 대로 철궤예요. 안에 들어 있는 물건이 뭔지, 누가 남긴 건지는 나도 모르지만.”

“안 열어 보셨습니까?”

“당연한 거 아냐? 진 공자와 약속한 부분인데.”

어깨를 으쓱해 보인 홍진이 웃으며 덧붙였다.

“물론 내 실력으로는 저 철궤를 열 자신도 없었고.”

농담처럼 한 말이었지만, 그렇다고 마냥 농담인 것만은 아니었다는 사실은 철궤를 건네받는 순간 알 수 있었다.

띠링.



- [매우 단단한 철궤]를 습득하셨습니다.

- 새로운 아이템을 습득하셨습니다. 아이템을 감정하여 정보를 확인하시겠습니까?



작게 고개를 끄덕이자, 반투명한 홀로그램 창이 홍진과 나 사이에 펼쳐졌다.



아이템창



[매우 단단한 철궤]

등급 : 절정

제한 : 無

설명 : 소량의 만년한철(萬年寒鐵)을 혼합하여 제작된 철궤. 당연하게도 엄청난 강도를 지녔으며, 방패로 쓰거나 소중한 물건을 보관하기에 더할 나위 없이 적합하다.

다만 다섯 개나 되는 자물쇠가 있어 자주 사용하기에는 다소 번거로울지도.





활자를 빠르게 읽은 나는 헛웃음을 삼켰다.

‘아니, 아무리 소량이라지만 무슨 놈의 철궤에 만년한철을…….’

만년한철은 매우 귀하고, 그만큼 더럽게 비싼 광물이다.

어느 정도 이름난 장인이 무기를 제조할 때 만년한철이 넉 냥만 들어가도 명검(名劍) 소리를 듣고, 그 이상이면 성질 더럽고 침 좀 뱉는다는 고수들이 아귀처럼 달려들 정도다.

한 마디로 돈이 있다고 해서 쉽게 구할 수도 없고, 아무리 돈이 많아도 정상인이라면 무기를 만드는 데 투자하는 물건.

그리고 한낱 보관함에 지나지 않는 철궤에 만년한철을 섞을 만큼의 재력을 지닌 정신 나간 인간은 그리 많지 않다.

물론…….

‘당장 생각나는 사람이 있긴 하지.’

나는 쓴웃음을 지으며 철궤를 어루만졌다.

땅 깊숙이 묻혀 있었다는 사실을 증명하듯, 표면은 축축하고 곳곳에는 미처 털어내지 못한 흙이 진한 향을 뿜어내고 있었다.

‘도대체 뭘까. 당신이 이렇게까지 숨겨 두려고 했던 것이.’

내가 철궤의 옛 주인을, 동천마군을 떠올리며 마음속으로 뇌까린 그때였다.

“이만 가 볼게요. 괜히 더 있어 봤자 방해만 될 것 같으니까.”

눈을 찡긋하며 자리에서 일어난 홍진은 내 대답을 기다리지 않고 방을 떠났다.

문을 닫기 전, 한 마디를 남기는 것도 잊지 않고.

“아, 황태제 전하께서 이 말을 전해 달래.”

“어떤……?”

“하나뿐인 친구가 보고 싶다고. 지금은 사정이 있어 찾아가지 못하지만, 떠나기 전에 꼭 만나자고.”

하나뿐인 친구라.

건청궁에서 만독지환을 건네주며 했던 말이 떠올라, 나는 실소를 금치 못했다.

“저도 마찬가지라고 전해 주세요.”

살짝 웃는 것으로 대답을 대신한 홍진은 곧장 자리를 떠났고, 주위의 모든 인기척이 사라진 것을 확인한 나는 철궤를 바닥에 내려놓은 뒤 불현듯 손을 뻗었다.

‘인벤토리 오픈. 소환.’

띠링.

마음속으로 읊은 짤막한 명령어와 함께, 더없이 익숙하면서도 서늘한 금속의 감촉이 손아귀에 감겼다.

백염(白炎).

내 독문 병기이자 천하제일의 장인이 일 년의 고행 끝에 벼려 낸 신병이기.

그리고 동시에 단단하게 잠겨 있는 저 철궤를, 다섯 개나 되는 자물쇠를 열 수 있는 열쇠(물리).

“어디 한 번 봅시다. 뭘 그렇게 꽁꽁 숨겨 뒀는지.”

작게 중얼거린 나는, 망설임 없이 창날을 내리그었다.

서걱.

한 줄기 섬광과 함께 잘려 나가는 금속.

조금의 흐트러짐도 없이, 깔끔하게 다섯 개나 되는 자물쇠를 한 번에 갈라 낸 나는 철궤 안의 내용물을 확인했다.

‘이건…….’

철궤를 처음 받아들었을 때부터 알고 있었지만, 가벼웠던 무게만큼이나 그 안에 들어 있는 내용물은 단출했다.

낡다 못해 거의 삭아 버린 죽간(竹簡)이 십여 개.

거기에 더하여 비교적 최근에 채워진 듯, 희고 깨끗한 종이 뭉치들과 자그마한 비단 주머니 하나.

‘뭐지?’

어째서인지 그것들을 보자마자 알 수 없는 전율이 등골을 타고 흘러내렸다.

이건 동천마군의, 굳이 말하자면 유품(遺品)이나 다름없다.

분명 단순히 무게나 형태로는 측정할 수 없는 물건일 터였다.

황금보다 더 값지고, 화약보다도 위험한 무언가가.

그리고 내가 그 직감이 사실이었음을 깨닫기까지는 그리 오랜 시간이 걸리지 않았다.

아니, 불과 촌각(寸刻)이었다.

스륵.

가장 맨 위에 놓여진 종이 뭉치, 아직 새하얀 그것을 묶은 끈을 풀자마자 한 줄기 벼락이 정수리를 관통했으니까.

“……!”

나도 모르게 덜컥 굳어 버린 전신.

떨리는 동공으로 종이를 가득 채운 활자들을 읽어 내려가던 그때, 언제 돌아왔는지 모를 혁무진의 목소리가 귓가에 닿았다.

“저기, 조장님. 아무래도 못 데려오겠…….”

마치 먼 곳에서 들려오듯이, 메아리처럼 울려 퍼지는 음성.

나는 격동을 억누르며 입을 열었다.

“……러와.”

“예?”

“다들 불러오라고. 어서!”

“……!”

무언가 잘못되었음을 직감한 혁무진의 얼굴이, 딱딱하게 굳었다.
```

## Final English reading copy

```markdown
# Chapter 937

“I heard it was important, so I took care of it as quickly as I could…… Oh my, why’s the mood so grim?”

The moment Hong Jin entered the room, he sensed the strange tension and asked about it. I answered with a troubled expression.

“It’s nothing.”

“Nothing? It sure looks like something happened.”

Hong Jin glanced between Hyuk Mujin and me, then murmured, his expression suddenly growing serious.

“Oh, that’s what it is? Hmm. But there’s nothing you can do about that.”

“……?”

“It’s all right, so don’t take it too hard. These things happen sometimes. It’s part of life.”

What was he talking about? Could Hong Jin know, too?

Thinking it over, he was now the East Depot eunuch, so it was entirely possible he knew about the Emperor’s illness.

*Maybe he’d heard something about it while enthusiastically torturing rebels for the last three days.*

Having reached a reasonable conclusion, I cautiously asked, “You already knew?”

Hong Jin hesitated for a moment, then nodded.

“Yeah. I happened to hear.”

“It’s supposed to be top secret…… More people know than I expected.”

“Eyes and ears are everywhere. No matter how tightly you try to wrap something up and keep it hidden, it’s bound to leak out eventually.”

Fair enough. The Emperor keeping quiet couldn’t protect every secret.

Every incident had victims and perpetrators, and perpetrators had mouths, too.

The rebels who were already dead—or waiting for death.

Some of those who’d passed through Hong Jin’s and the Embroidered Uniform Guard’s hands must have been close aides to the Eastern Heaven Demon Lord, and known the Emperor had been poisoned with Blood Soul Gu.

“You must’ve found out while interrogating the prisoners. Which ones knew?”

“What?”

“The prisoners who knew about it. They must have been closely connected to the Eastern Heaven Demon Lord.”

“Uh, well……”

Maybe that was a sensitive thing to bring up.

I realized my mistake too late and was about to wave my hands to take it back when Hong Jin, who’d been blinking quietly, continued.

“I heard it from Young Hero Taishan.”

“Ah. I see…… Wait. Who?”

“Young Hero Taishan. That huge guy.”

“……?”

No, something wasn’t right here.

Hyuk Mujin spoke up in my place.

“You mean the Taishan I know?”

“Yeah.”

“Built like a mountain, just like his name?”

“That’s right.”

“Usually an idiot, but smart whenever food comes up?”

“I don’t know about that part.”

“Obsessed with five-spice pork?”

“That part’s definitely true. Actually, some intelligence came in yesterday. According to my men, the imperial cooks tried to poison his food.”

If he was the number one target for assassination among the imperial cooks, then it had to be the Taishan I knew.

I asked, utterly confused, “How would he know that?”

“How would he know? He saw it.”

“That can’t be right. He wouldn’t have seen it.”

“He said he saw it clearly.”

“……What are you even talking about?”

“……That’s what I’d like to ask you. What’s all this about prisoners and interrogations?”

Hong Jin frowned at me, then went on.

“Weren’t you talking about ‘that thing’ that happened right after Young Master Jin woke up?”

“W-what?”

“You look really unsettled. Is that why? I told you it’s fine, so why are you still worrying? You just have a little more energy than other people.”

“……!”

Oh, shit.

My vision went dark in an instant, and my whole body trembled.

“How…… how did you know?”

“It’s all over the palace. Didn’t you know?”

“It’s all over……?”

“I’m one of the last to hear, since I was away for a while. Less than two shichen after you woke up, half the people in the Inner Palace probably knew.”

I couldn’t breathe. My hands and feet shook, and I felt like I was about to cry.

It was like turning on the TV one day out of boredom and finding a national broadcast channel throwing a wet-dream party for me.

Twitching like I was sick, I barely managed to force the words out.

“Taishan. Bring that bastard here right now.”

Hyuk Mujin, who’d frozen with his mouth hanging open, answered.

“I’m really sorry to say this, but Taishan’s stronger than I am.”

“Bring him here, no matter what!”

“Come on, Captain. You know he tears people apart with both hands.”

“I can tear you apart with one.”

“Ah. Aah.”

Hyuk Mujin let out a brief yelp and dashed out. Feeling the air grow heavy, Hong Jin spoke with a troubled expression.

“Young Master Jin. Don’t take it so hard.”

For the moment, even my worries about treating the Blood Soul Gu had been completely driven from my mind.

I replied to Hong Jin’s attempt at comfort with a groan. “Don’t say that so casually when it’s someone else’s business.”

“I told you it’s fine.”

“What’s fine? Have you ever been in a situation like mine?”

At my sharp question, Hong Jin answered with a sad smile.

“Of course not. I had it cut off a long time ago.”

“……”

“Just look on the bright side. I’m actually jealous of you, Young Master Jin. Especially during the rainy season, it aches so much down there that sometimes I can barely walk without poppy……”

“Okay, I get it. I get it, so please stop.”

Using his eunuch trump card—one he pulled out whenever he was bored—to shut me up, Hong Jin held out something he’d been carrying and continued.

“I was going to do that anyway. I’m a busy man, too. I only came to hand over the item I was asked to deliver.”

Realizing how badly my question had backfired snapped me to my senses. Only then did I notice the small iron chest in Hong Jin’s hand and remember why he’d come back.

The mysterious place the Eastern Heaven Demon Lord had told me about in his final moments.

The item he’d said to find there.

“This is……”

“It’s an iron chest, as you can see. I don’t know what’s inside or who left it there, though.”

“You didn’t open it?”

“Obviously not. That’s what I promised you.”

Hong Jin shrugged and added with a smile, “Besides, I wasn’t confident I could open it myself.”

He’d said it as if it were a joke, but the moment I took the chest from him, I realized it wasn’t entirely one.

*Ding.*

> **System**
>
> Very Sturdy Iron Chest acquired.
>
> New Item acquired. Would you like to appraise the Item and view its information?

I gave a slight nod, and a translucent holographic window opened between Hong Jin and me.

> **System**
>
> **Item Window**
>
> **Very Sturdy Iron Chest**
>
> **Grade:** Peak  
> **Restriction:** None  
> **Description:** An iron chest made by mixing in a small amount of Ten-Thousand-Year Cold Iron. As you’d expect, it’s incredibly durable—perfect for use as a shield or for storing precious belongings.
>
> However, it has no fewer than five locks, so using it often may be a bit of a hassle.

After quickly reading through the text, I swallowed a dry laugh.

*Seriously? Even if it’s only a little, why use Ten-Thousand-Year Cold Iron in an iron chest……?*

Ten-Thousand-Year Cold Iron was incredibly rare—and filthy expensive to match.

If a renowned smith used even four nyang of it to forge a weapon, people would call it a fine sword. Use any more than that, and masters with foul tempers and a knack for spitting would descend on it like starving demons.

In short, it wasn’t something you could easily get just because you had money. And no matter how rich you were, any sane person would use it to forge a weapon.

And there weren’t many crazy people rich enough to mix Ten-Thousand-Year Cold Iron into an iron chest that was nothing more than a storage box.

Of course……

*I can think of someone right away.*

I gave a bitter smile and ran my hand over the iron chest.

As if to prove it had been buried deep underground, its surface was damp, and patches of soil that hadn’t been brushed off gave off a strong earthy smell.

*What could it be? What did you want to hide away so badly?*

I was thinking of the chest’s former owner, the Eastern Heaven Demon Lord, when Hong Jin rose to his feet with a wink.

“I’ll get going. There’s no point sticking around and getting in your way.”

He didn’t wait for my answer before leaving the room.

Before closing the door, he remembered to pass along one more message.

“Oh, His Highness the Emperor’s Brother and Heir asked me to tell you this.”

“What is it……?”

“He misses his one and only friend. He can’t come see you right now because of the circumstances, but he wants to make sure he sees you before he leaves.”

His one and only friend.

Remembering what he’d said when he gave me the Myriad-Poison Ring at Qianqing Palace, I couldn’t help letting out a quiet laugh.

“Tell him I feel the same way.”

Hong Jin answered with a slight smile of his own, then left. Once I’d confirmed that all signs of life around me had disappeared, I set the iron chest on the floor and abruptly held out my hand.

*Inventory open. Summon.*

*Ding.*

Along with the brief command I recited in my mind, the familiar, cold feel of metal wrapped around my hand.

White Flame.

My personal weapon, and a divine weapon forged by the world’s greatest smith after a year of hardship.

And, at the same time, the key—of the physical sort—that could open that tightly locked iron chest and its five padlocks.

“Let’s see what you were so determined to keep hidden.”

I murmured, then brought the spearhead down without hesitation.

*Slice.*

A flash of light, and the metal split apart.

With no loss of form at all, I cleanly cut through all five padlocks in a single stroke and looked inside the chest.

*This is…….*

I’d known from the moment I first picked up the iron chest, but its contents were as spare as its weight was light.

A dozen or so bamboo slips, so old they were practically rotting away.

Along with them, a bundle of papers that looked relatively recent, still white and clean, and a small silk pouch.

*What is this?*

For some reason, the moment I saw them, an inexplicable shiver ran down my spine.

These were the Eastern Heaven Demon Lord’s—or, to put it another way, his keepsakes.

They had to be worth more than gold and more dangerous than gunpowder, in ways that couldn’t be measured by their weight or shape alone.

And it didn’t take long for me to realize my instinct was right.

No—it took only moments.

*Rustle.*

The moment I untied the string around the bundle of papers on top, still pristine white, a bolt of lightning shot through the crown of my head.

“……!”

My entire body went rigid before I knew it.

As I read the lines of text filling the page with trembling eyes, Hyuk Mujin’s voice reached my ears. I didn’t know when he’d come back.

“Um, Captain. I don’t think I can bring him……”

His voice rang out like an echo, as if coming from far away.

Suppressing the surge of emotion, I spoke.

“……Go get them.”

“What?”

“Bring everyone here. Now!”

“……!”

Sensing that something was wrong, Hyuk Mujin’s face went stiff.
```
