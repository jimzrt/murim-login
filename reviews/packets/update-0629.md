<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0629.txt",
      "sha256": "20c1805415bd53b577cc5fac044755b7b47cd1341e9e38bf80683adddbb100cd",
      "bytes": 13369
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6c994e2ac65a1520069cf9dd8d2ff5f3395dc6cd8ec6b538392b900271449d4a",
      "bytes": 2534
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "527fe15f8aa215b5254b70898f96e6339f8ec8fba9191e68decb2a6d0fc445b6",
      "bytes": 193641
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "4f94ab7c78d91423a866870747b52f40a4d0c0ec0b11f58e3da3953ef7e85e69",
      "bytes": 695
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "99bd06cb15eaae5c4a28f09d8b932bc754b3f3a4f4c2461107f1d992a00482c3",
      "bytes": 553
    },
    {
      "path": "characters/Lee Sam.md",
      "sha256": "d91f39d8886dcbf75f0eacebcfd0b60b320bce05704ae75c76c067a9d03c9beb",
      "bytes": 623
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "dae26b6b019ea0e5eb6a88f27d5ea9c6d32bddd6b8354840c31d95475548f53c",
      "bytes": 1252
    },
    {
      "path": "characters/Namho.md",
      "sha256": "25691b53599b28d205f4f37468f3f902728e5b51301a5da815ea2e87e038aac1",
      "bytes": 843
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "377c3193ef976671e9bc85d76753d2a800641d3aea06fe2129115b085a8bb889",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "125f5eb0209cf9b4c3184ed15eda2fcee1dd1b93d46e304ec7f1a7ac2915ff71",
      "bytes": 199327
    }
  ],
  "estimated_tokens": 10211
}
-->

# Durable State Update — Chapter 629

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 629. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 629. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 629,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 629,
    "continuity_sources": [629],
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
    "The Fire Dragon Pavilion is staying in temporary lodging within the Nanman Beast Palace after being welcomed by Yayul Cheok.",
    "Nanman sent approximately ten thousand warriors to the Great Faction War, and fewer than a quarter returned alive.",
    "Yayul Cheok lost two sons and a daughter in the Great Faction War.",
    "Yayul Mok's three older siblings died in the Great Faction War, leaving him Yayul Cheok's only surviving son and Young Palace Lord.",
    "Baeksang is the great chieftain of the Bai people, one of Nanman's four most powerful great tribes.",
    "Baeksang is Yayul Cheok's sworn younger brother and childhood companion, but they are now estranged over the Murim Alliance issue.",
    "Baeksang watches Jin Taekyung with cold scrutiny, but the reason for his interest remains unknown.",
    "A massacre killed more than two hundred Miao people, mostly elders, women, and children, deepening Nanman's opposition to helping the Han Chinese.",
    "Nanman's first tribal council opposed joining the Murim Alliance; all thirty-two tribes will meet in three days for a second council.",
    "Baeksang and two other great chieftains oppose joining the Murim Alliance, while Yayul Cheok remains the only great chieftain not committed to that position.",
    "Jin Taekyung came to Nanman to contain a spreading crisis rather than as a diplomat, but he will attempt to persuade Nanman if possible."
  ],
  "continuity_sources": [
    628,
    627
  ],
  "open_questions": [
    "Why does Baeksang oppose joining the Murim Alliance despite his lifelong bond with Yayul Cheok and their shared service in the Great Faction War?",
    "What is the meaning of Baeksang's cold scrutiny of Jin Taekyung?",
    "Will Yayul Cheok overcome the other great chieftains' opposition and bring the Nanman Beast Palace into the Murim Alliance?",
    "Will the remaining tribes follow Baeksang and the other opposing great chieftains at the council in three days?",
    "Was the timing of the Heavenly Demon Escort Bureau massacre connected to Dark Heaven's scheme?"
  ],
  "safe_through": 628,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Use Jiang Taigong for 강태공 and Jindro for 진드로.",
    "Render 황개 as Hwang Gae and 똥개 as Ddong Gae.",
    "Render 입맹 as joining the alliance."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 상호 | **Sangho** | Go Se-won's young son. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 628
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War and opposes the Nanman Beast Palace joining the Murim Alliance.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 628
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Lee Sam.md

# Lee Sam (이삼)

- **Safe through:** Chapter 108
- **Aliases:** None
- **Role:** Leader of a ten-man human-trafficking group and a member of the Red Wind Band; formerly a Level 25 martial artist who had approached First Rate
- **Personality:** Violent, extortionate, lecherous, and cruel toward captives; becomes terrified and submissive when confronted by overwhelming force
- **Voice:** Coarse, threatening, mocking, and vulgar
- **Relationships:** Commands the armed traffickers encountered at the abandoned shrine; associated with the Red Wind Band

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 557
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung is accompanying him while learning his martial arts through observation, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 627
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 628
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃629화



야율목과 헤어진 나는 화룡각 대원들이 기다리고 있을 임시 숙소로 발걸음을 돌렸다.

내 무위 덕분에 누구한테 해코지를 당할 위험은 없더라도, 이런 분위기 속에서 홀로 돌아다녀 봤자 좋을 게 없으니까.

그리고 그렇게 걷다 보니, 어느새 남만야수궁의 외당(外堂)이었다.

“어이쿠, 언제 여기로 왔대.”

나는 혼잣말을 중얼거리며 주위를 둘러봤다.

빽빽하게 우거진 풀숲 사이에 숨어 있어서 그런지, 주위에는 쥐새끼 한 마리 보이지 않……는 것은 아니고.

국방부의 굳건이처럼 남만의 마스코트 격인 원숭이 두세 마리가 얼쩡거리는 중이었다.

- 끼긱?

아니, 한족 새끼가 조용히 숙소에나 처박혀 있지, 왜 여기까지 기어 나왔대?

원숭이의 호기심 어린 눈망울이 그렇게 묻는 듯했지만, 나는 하늘을 우러러 한 점 부끄러움이 없다.

‘길을 잃었는데 어쩌라고.’

물론 신의라는 탈을 쓴 고금제일의 살수에게 받은 가르침대로 호흡을 감추고, 다른 누군가의 눈에 띄지 않기 위해 은밀하게 움직이긴 했다.

하지만 한 가지 확실한 건 내가 길을 잃었다는 거다.

비록 임시 숙소까지는 불과 일각도 걸리지 않는 거리였고 길도 두 개밖에 없었지만, 아무튼 그렇다. 내가 길을 잃었다면 그런 거다.

‘그래도 무림맹을 대표해서 왔는데, 이 정도는 혼자서 파악해 봐야지.’

헌터 훈련소 시절 어떤 동기가 그런 말을 했다.

완벽한 구라는 실화라고.

결국 안 걸리면 그만이란 이야기다. 물론 분위기상 안 걸리도록 노력은 해야겠지만.

스으윽.

호흡을 가다듬은 나는 풀숲을 빠져나와, 가까이 모여 있는 사람들 사이로 스며들었다.

기척을 죽이고 기세를 갈무리하는 한편, 비스듬히 허리를 굽혀 키를 낮춘 채 그들에게 녹아들었다. 언젠가 문경이 가르쳐 준 방식 그대로.



‘이 세상에서 가장 무서운 살수가 누구인지 아느냐?’

‘알죠. 지금 제 앞에 있는 사람이요.’

‘…….’

‘죄송합니다. 죄송합니다. 정말 죽을죄를 지었습니다. 소매에 넣어 둔 비수는 고이 집어넣으시고 이 우매한 놈에게 가르침을 주십시오.’



죽일까 말까 하는 표정으로 나를 노려보던 문경은, 이렇게 대답했었다.



‘평범한 자다.’

‘평범?’

‘누구보다 평범하고, 어떤 곳에서도 자연스럽게 녹아드는 자. 그것이 가장 무서운 살수다.’



그때 문경이 내게 가르친 것은 비단 살수에게만 해당되는 것이 아니었다.

그 스스로는 무공이라 부를 수도 없는 단순한 잡기(雜技)에 불과하다며 지나가듯 알려 주었지만, 나는 그의 가르침을 잊지 않았고 때때로 쏠쏠하게 써먹고 있었다.

바로 지금처럼.

‘확실히 중원이랑은 다르네. 달라.’

나는 티 나지 않을 만큼 자연스럽게 고개를 돌리며 외당 곳곳을 살폈다.

다시 봐도 남만야수궁은 참으로 특색 있는 곳이었다.

하나의 문파라기보다는 작은 도시에 가까웠고, 그 도시에는 각양각색의 이민족들이 어울려 살아가고 있었으니까.

한족들이 대다수인 중원에 비하면 남만은 인종의 용광로나 다름없었다.

화려한 장신구를 걸친 묘족 여인은 사람들의 시선을 즐기며 저자를 활보했고, 흰색의 전통 복식을 갖춘 백족 상인은 어깨에 원숭이를 올려놓고 거래를 시도한다.

그리고 바로 내 정면에서 절룩거리며 걸어오는 어느 노인은…….

아니, 어르신. 왜 이쪽으로 오세요.

“이보게. 시전(市廛)에서 포목을 좀 사려고 하는데, 어느 가게가 좋겠나? 십 년만 젊었다면 눈 감고도 찾아갔을 텐데, 나이가 들어서 그런지 요새는 통 기억이 안 나네. 그려.”

“어…….”

내가 너무 자연스러웠나. 이건 예상 못 했는데.

지팡이를 짚으며 앞을 막아선 어느 이민족 노인의 물음에, 순간 주춤한 나는 이내 천연덕스럽게 대답했다.

“쭉 가서 오른쪽 골목으로 들어가시면 됩니다.”

“오른쪽 골목? 거기에도 포목점이 있었나?”

그건 저도 모르죠. 어르신.

하지만 나는 속마음과 달리 고개를 끄덕였다.

“예. 많습니다. 어르신 머리카락보다 많아요. 아주 우후죽순이에요.”

“그래? 거기 상호명이 어떻게 되나?”

아니, 무슨 상호명까지 가르쳐 달래.

하지만 여기서 우물쭈물했다가는 의심을 산다. 나는 당장 머릿속에 떠오르는 상호명을 그대로 내뱉었다.

“혁가 포목점이라고, 거기 품질이 괜찮습니다.”

“혁가 포목점? 처음 듣는 것 같은데…….”

내가 현지인 짬을 우습게 봤구나.

분명한 무리수였지만 원래 이런 건 뻔뻔한 놈이 이기는 거다. 나는 하늘을 우러러 한 점 부끄러움이 없는 표정으로 단호하게 말했다.

“거기 생긴 지 십 년도 넘었는데요.”

“그래? 희한한 일이군. 내 기억으로는 분명히…….”

“그 기억이 흐릿해서 저한테 물어보신 거 아닙니까?”

“그건 맞네만.”

“어르신. 실례지만 올해 연세가?”

“나? 여든둘일세.”

“전 스물둘입니다. 아버지 쪽에서 어머니 쪽으로 옮겨 갈 때의 기억도 아직 생생해요.”

“그게 기억난다고……?”

“전 스물둘밖에 안 돼서 다 기억납니다. 그러니까 절 믿으세요.”

“아, 알겠네. 아무튼 고마우이.”

박력싸움에서 밀린 노인이 떠나려 하던 그때, 문득 뭔가를 떠올린 내가 서둘러 입을 열었다.

“저기. 어르신?”

“응? 뭔가?”

“지금 인파가 가장 많이 몰려 있는 곳이 어딥니까? 누구랑 만나기로 약속을 했는데, 이 새끼가 통 안 보여서 직접 찾아보려고요.”

“그렇다면 저쪽으로 가 보게. 오는 길에 얼핏 봤는데, 당최 무슨 일인인지는 몰라도 아주 시끄럽더군. 아마 며칠 후에 열릴 축제 때문일 게야.”

바로 그때. 지팡이로 방향을 알려준 노인이 순간 멈칫하는가 싶더니 이내 흐릿한 눈동자로 내 얼굴을 빤히 바라보았다.

“그런데 자네, 어느 부족 사람인가?”

“예?”

“생김새를 보아하니 나와 같은 요족(瑤族)은 아닌 것 같은데. 우리 쪽 말에 능통한 것이 참으로 희한…….”

“어, 저기 보이네요. 조심히 가십시오.”

“이봐. 이보게.”

나는 이민족 노인을 뒤로하고 빠른 걸음으로 자리를 벗어났다.

확실히 아무리 자연스럽게 녹아든다 하더라도, 일정 시간 동안 얼굴을 관찰할 시간을 주면 상대가 눈치를 챌 수밖에 없었다.

비록 확연히 눈에 띌 만큼의 큰 차이가 있는 것은 아니지만, 남만의 이민족과 한족의 생김새는 어느 정도 구별되는 편이니까.

하지만 방법이 없는 것은 아니었다.

다행히도 나는 손이 매우 빨랐고, 때마침 시전은 이민족들로 인산인해였으며, 동물을 본 따 만든 전통 가면을 파는 상인은 사방에서 밀려드는 손님으로 정신이 없었다.

좀 더 간단하게 말하자면, 가면 하나 슬쩍하는 데에는 아무런 문제도 없었다는 얘기다.

‘인벤토리 오픈. 수납.’

띠링.



- [대충 만든 호랑이 가면]을 획득하셨습니다!



눈보다 빠른 건 손이 아니다. 바로 시스템이지.

가면을 인벤토리에 집어넣은 내가 자연스럽게 두어 사람을 지나쳤을 때, 내 얼굴에는 조잡한 염료로 그려진 호랑이 가면이 덧씌워져 있었다.

‘이 정도면 충분하지. 이쪽 동네에서는 크게 눈에 띄지도 않고.’

아까 이민족 노인이 언급했던 축제 때문인가? 당장 눈에 보이는 사람이 열 명이라고 치면, 그중 두세 사람은 나와 비슷한 가면을 쓰고 있었다.

나는 노인이 알려 준 방향으로 걸으며 곳곳에서 들려오는 목소리들을 귀에 담았다.

“그 소식 들었나? 이족(彝族)과 요족(瑤族)의 대족장이 돌아왔다는군.”

“그래? 보름 전쯤에 식인 맹수들을 토벌하러 간다고 들었던 것 같은데.”

“자그마치 오백여 명의 전사를 동원했으니 금방 끝냈겠지. 요족과는 달리 이족의 대족장은 별다른 성과를 얻지 못한 모양이지만.”

“예상했던 결과 그대로군. 뭐, 딱히 기대도 안 했어.”

대화 속에서 오가는 익숙한 대화를, 나는 놓치지 않았다.

‘이족. 그리고 요족이라.’

남만야수궁주인 야수묘왕과 앞서 스치듯이 만났던 백상이 각각 대족장으로 있는 묘족, 백족과 더불어 남만에서 가장 큰 세력을 지녔다는 사대 부족 중 하나다.

나는 남만야수궁으로 오는 길에 남호에게 들었던 정보를 떠올렸다.



‘남만의 사대부족은 묘족과 백족. 그리고 이족과 요족으로 이루어져 있네. 그중에서 묘족의 세가 가장 강하며 백족이 그다음이지.’

‘그럼 이족이랑 요족은요?’

‘한 이삼십 년 전이었다면 이족이 앞섰겠지.’

‘지금은 아니라는 뜻으로 들리네요.’

‘그만큼 세월이 흘렀으니까. 선친에게 자리를 물려받은 이족의 대족장은 그리 심지가 단단하지 못하다는 평이 많네. 반면 요족은 크게 성장했지. 뛰어난 우두머리를 얻었거든. 여느 사내를 앉혀 놔도 그만큼은 못했을 거야.’

‘혹시?’

‘지금 자네가 떠올린 짐작이 맞네. 요족의 대족장은 여인일세. 매우 총명하면서, 극히 아름다운.’



그 순간, 머릿속에서 이어지던 상념이 뚝 끊겼다.

자의가 아닌 타의에 의해서. 그리고 내 상념을 끊어 낸 것은 저 멀리서 아련하게 들려오는 맑은 악기 소리였다.

솨아아아.

후텁지근한 남만의 바람에 섞여든 잔잔한 선율(旋律)이, 너른 공간을 가로질러 귓가에 닿는다.

소란스럽던 시전이 삽시간에 조용해지고 누군가의 입술 사이로 짧은 탄성이 흘러나왔다.

“아…….”

그건 막을 수 없는, 실로 불가항력과 같았다.

그만큼 귓가로 전해지는 선율은 깨끗했고, 분분히 뒷걸음질 치는 사람들 사이로 모습을 드러낸 행렬은 화려하면서도 아름다웠다.

둥. 둥. 둥.

나직한 북소리와 함께 행렬을 이어가는 것은 수백에 달하는 남녀였다.

꽃천으로 테를 두른 검은색 상의와 폭이 넓은 주름 바지를 입은 이족 사내들.

그리고 고깔 형태의 모자를 쓴 요족의 여인들은 두 갈래로 나뉘어 천천히 걸음을 옮겼다.

“와아.”

“이족과 요족이 도착했다!”

곳곳에서 터져 나오는 환호성.

하지만 주위의 모두가 저들의 아름다움과 멋스러움에 감탄할 때, 나는 그들의 허리와 어깨에 매여진 무기를 바라보고 있었다.

‘한 사람, 한 사람이 전사들이군.’

남만의 전사는 중원으로 따지자면 무림인이다. 저들은 각 부족에 속했으니, 한 문파의 문도라고 해야 맞을 것이다.

‘그리고 조금 전 들은 바에 의하면 이족과 요족의 대족장이 토벌을 끝내고 돌아왔다고 했으니까…….’

이건 단순한 행렬이 아니라 일종의 개선식(凱旋式)인 셈이고, 이와 같은 개선식에는 전투를 승리로 이끈 장군이 빠지지 않는다.

그리고 이곳에서 말하는 장군이란, 앞서 들었던 두 거대 부족의 대족장들이다.

“엇!”

“저, 저기……!”

생각하기가 무섭게 들려오는 짧은 경호성.

곧이어 수많은 시선과 목소리가 한 방향을 향해 쏠리고, 다음 순간 누가 먼저랄 것도 없이 거대한 환호성이 터져 나왔다.

“와아아아아아!”

외당을 넘어 남만 전체를 뒤흔들 것 같은 함성 속, 행렬의 중심에서 비로소 모습을 드러낸 두 사람이 손을 흔들었다.

이족의 대족장으로 짐작되는, 커다란 흑곰을 탄 남자. 그리고…….

“요희(妖姬)! 요희 대족장님!”

그와는 비교도 안 되는 사람들의 관심과 사랑 속에서 환하게 웃는 한 여인.

하지만 사람들의 외침을 듣지 못했더라도, 나는 그녀의 정체가 요족의 대족장이라는 것을 금세 깨달았을 것이다.



‘요족의 대족장은 여인일세. 매우 총명하면서, 극히 아름다운.’



남호의 말은 사실이었다. 요희의 용모는 아름다웠다. 한편으로는 요사스럽게 느껴질 만큼.

그녀의 그윽한 눈빛이 주위를 스칠 때마다 사람들은 탄성을 토해 냈다.

아마 그래서였을 것이다.

그녀를 둘러싼 환호와 경탄 속에서, 목석처럼 서 있는 내가 유난히도 눈에 띈 이유는.

“……!”

나를 발견한 요희의 눈동자가 반짝 빛났다.
```

## Final English reading copy

```markdown
# Chapter 629

After parting ways with Yayul Mok, I turned my steps toward the temporary lodging where the Fire Dragon Pavilion members were waiting.

Even if my martial prowess meant there was no danger of anyone trying to harm me, there was nothing to be gained from wandering around alone in an atmosphere like this.

And as I walked, I somehow found myself in the Outer Hall of the Nanman Beast Palace.

“Good grief. When did I get here?”

Muttering to myself, I looked around.

Perhaps because it was hidden among the thick, overgrown grass, I couldn’t see a single rat anywhere…

Well, that wasn’t quite true.

Two or three monkeys—mascots of Nanman much like Gukkeoni is for the Ministry of National Defense—were milling around.

—Screech?

*Why has that Han Chinese bastard crawled all the way out here instead of quietly hiding in his lodging?*

The monkey’s curious eyes seemed to be asking that, but I had nothing to be ashamed of before the heavens.

*What do you want me to do? I got lost.*

Of course, following the teachings I had received from the greatest assassin of all time, who wore the guise of the Divine Physician, I had concealed my breathing and moved stealthily so that no one else would notice me.

But one thing was certain.

I had gotten lost.

The temporary lodging was less than fifteen minutes away, and there were only two possible roads, but that was beside the point. If I had gotten lost, then I had gotten lost.

*Still, I came here representing the Murim Alliance. I should at least be able to figure this out on my own.*

A fellow recruit had said something like that back when we were at the Hunter training center.

*A perfect lie is a true story.*

In the end, all that mattered was not getting caught. Of course, given the circumstances, I still had to make an effort not to get caught.

*Rustle.*

After steadying my breathing, I slipped out of the grass and blended into the people gathered nearby.

I erased my presence and reined in my aura. At the same time, I bent forward slightly to lower my height and melted into the crowd.

Exactly as Mungyeong had once taught me.

*Do you know who the most frightening assassin in this world is?*

*I do. The person standing right in front of me.*

*……*

*I’m sorry. I’m sorry. I’ve committed a crime worthy of death. Please put away the dagger in your sleeve and teach this foolish disciple.*

Mungyeong had glared at me with an expression that seemed to ask whether he should kill me or not, then answered.

*An ordinary person.*

*Ordinary?*

*Someone more ordinary than anyone else, someone who blends naturally into any place. That is the most frightening assassin.*

What Mungyeong had taught me back then didn’t apply only to assassins.

He had mentioned it in passing, saying it was nothing more than a simple miscellaneous skill that couldn’t even be called martial arts. But I hadn’t forgotten his teaching, and I had found plenty of opportunities to put it to good use.

Just like now.

*This really is different from the Central Plains. Completely different.*

I turned my head as naturally as possible and surveyed the various parts of the Outer Hall.

The Nanman Beast Palace was a truly distinctive place, even after seeing it again.

It was less like a sect than a small city, and all kinds of different peoples lived together within that city.

Compared to the Central Plains, where the Han Chinese made up the majority, Nanman was practically a melting pot of races.

A Miao woman draped in colorful jewelry strode through the market, enjoying the attention of the people around her, while a Bai merchant in white traditional clothing tried to conduct a trade with a monkey perched on his shoulder.

And then there was an old man limping straight toward me.

*No, sir. Why are you coming this way?*

“Excuse me. I’m trying to buy some cloth at the market. Which shop would you recommend? If I were ten years younger, I could have found it with my eyes closed, but perhaps it’s because I’m old that I can’t remember anything these days.”

“Uh…”

Had I blended in too naturally? I hadn’t expected this.

The non-Han old man had blocked my path with his cane and asked me the question. I hesitated for a moment, then answered as shamelessly as possible.

“Go straight ahead, then turn into the alley on the right.”

“The alley on the right? Was there a cloth shop there?”

*I have no idea either, sir.*

But contrary to my thoughts, I nodded.

“Yes. There are plenty. More than the hairs on your head. They’re springing up everywhere.”

“Really? What’s the name of the shop?”

*Why do you need me to tell you the name, too?*

But if I hesitated now, he would become suspicious. I blurted out the first shop name that came to mind.

“Hyuk Family Cloth Shop. Their quality is pretty good.”

“Hyuk Family Cloth Shop? I don’t think I’ve heard of it before…”

I had underestimated the old man’s local experience.

It was clearly an unreasonable answer, but in situations like this, the shameless person won. With an expression utterly free of shame, I spoke firmly.

“It’s been around for more than ten years.”

“Really? How strange. As far as I remember, it was definitely…”

“Isn’t that why you asked me? Because your memory is getting hazy?”

“That’s true, but…”

“Sir, if you don’t mind my asking, how old are you this year?”

“Me? I’m eighty-two.”

“I’m twenty-two. I still vividly remember moving from my father’s side to my mother’s side.”

“You remember that…?”

“I’m only twenty-two, so I remember everything. So please trust me.”

“Ah, all right. In any case, thank you.”

The old man, defeated in the battle of sheer confidence, was about to leave when I suddenly remembered something and hurriedly opened my mouth.

“Excuse me. Sir?”

“Yes? What is it?”

“Where is the place with the biggest crowd right now? I was supposed to meet someone, but that bastard isn’t showing up anywhere, so I’m going to look for him myself.”

“If that’s the case, go over there. I caught a glimpse of it on my way here, and I don’t know what exactly was happening, but it was terribly noisy. Perhaps it’s because of the festival that will be held in a few days.”

Just then, the old man, who had pointed in a direction with his cane, seemed to pause. Then he stared closely at my face with his cloudy eyes.

“By the way, which tribe are you from?”

“What?”

“Judging by your appearance, you don’t seem to be from the Yao people like me. It’s quite strange that you speak our language so fluently…”

“Oh, I can see it over there. Please be careful on your way.”

“Hey. Wait.”

I left the non-Han old man behind and hurried away.

No matter how naturally I blended in, if I gave someone enough time to study my face, they were bound to notice something.

The difference wasn’t large enough to make me stand out immediately, but there were still certain distinctions between the appearances of Nanman’s non-Han peoples and the Han Chinese.

But that didn’t mean there was no solution.

Fortunately, my hands were very fast. And as luck would have it, the market was packed with non-Han people, while the merchant selling traditional animal masks was too busy dealing with customers pouring in from every direction to pay attention to anything else.

To put it simply, there was no problem with slipping a mask into my possession.

*Open Inventory. Store.*

*Ding.*

> **System**
>
> You have acquired **Crudely Made Tiger Mask**!

What was faster than the eye wasn’t the hand.

It was the System.

After putting the mask into my inventory and naturally passing two or three people, a tiger mask painted with crude dye had been placed over my face.

*This should be enough. I won’t stand out much in this neighborhood.*

Was it because of the festival the old man had mentioned? If there were ten people in sight, two or three of them were wearing masks similar to mine.

I walked in the direction the old man had shown me, listening to the voices drifting over from various places.

“Have you heard the news? The great chieftains of the Yi and Yao peoples have returned.”

“Really? I thought they left about fifteen days ago to subdue the man-eating beasts.”

“They mobilized around five hundred warriors, so they must have finished quickly. Unlike the Yao people, it seems the great chieftain of the Yi people didn’t achieve any noteworthy results, though.”

“It’s exactly what I expected. Not that I was expecting much.”

I didn’t miss the familiar information exchanged in their conversation.

*The Yi people. And the Yao people.*

Together with the Miao and Bai peoples—led respectively by the Beast Miao King, lord of the Nanman Beast Palace, and Baeksang, whom I had briefly encountered earlier—the Yi and Yao peoples made up Nanman’s four most powerful tribes.

I recalled the information Namho had told me on the way to the Nanman Beast Palace.

*The four great tribes of Nanman are the Miao, Bai, Yi, and Yao peoples. The Miao people are the strongest, followed by the Bai people.*

*Then what about the Yi and Yao peoples?*

*If you were talking about twenty or thirty years ago, the Yi people would have been ahead.*

*That sounds like you’re saying they aren’t anymore.*

*That much time has passed. People say the great chieftain of the Yi people, who inherited his position from his late father, isn’t very strong-willed. The Yao people, on the other hand, have grown considerably. They gained an outstanding leader. No man could have accomplished as much, no matter whom they put in that position.*

*Could it be…?*

*Your guess is correct. The great chieftain of the Yao people is a woman. Extremely intelligent, and extraordinarily beautiful.*

At that moment, the thoughts continuing in my head abruptly came to a stop.

Not by my own choice, but because of an outside force.

The thing that interrupted my thoughts was the clear sound of a musical instrument reaching me faintly from far away.

*Fwoooosh.*

A gentle melody carried on Nanman’s hot, humid wind crossed the wide space and reached my ears.

The noisy market fell silent in an instant, and a short exclamation escaped someone’s lips.

“Ah…”

That exclamation was impossible to suppress—truly involuntary.

The melody reaching my ears was that pure, and the procession that emerged as people retreated in a flurry was both splendid and beautiful.

*Thump. Thump. Thump.*

Hundreds of men and women continued forward in the procession to the accompaniment of low drums.

The Yi men wore black tops edged with floral cloth and wide, pleated trousers.

The Yao women wore conical hats and moved slowly forward in two separate groups.

“Wow.”

“The Yi and Yao people have arrived!”

Cheers burst out from every direction.

But while everyone around me marveled at their beauty and striking appearance, I was looking at the weapons strapped around their waists and shoulders.

*Every single one of them is a warrior.*

A warrior of Nanman was equivalent to a Murim practitioner in the Central Plains. Since these people belonged to their respective tribes, it would be more accurate to call them members of a martial sect.

*And from what I just heard, the great chieftains of the Yi and Yao peoples returned after finishing their campaign…*

This wasn’t merely a procession. It was a kind of victory parade, and a victory parade like this was never complete without the general who had led the battle to victory.

And the generals in question were the great chieftains of those two great tribes I had just heard about.

“Oh!”

“Th-there…!”

A short cry of alarm reached me just as I was thinking that.

In the next moment, countless gazes and voices focused in one direction. Then, without anyone taking precedence over anyone else, a tremendous cheer erupted.

“Waaaaaaaaah!”

Amid the roar that seemed capable of shaking all of Nanman beyond the Outer Hall, two people finally appeared at the center of the procession and waved their hands.

One was a man riding a huge black bear, presumably the great chieftain of the Yi people.

And the other was…

“Yohi! Great Chieftain Yohi!”

A woman who smiled brightly amid an outpouring of attention and affection that surpassed the man’s by comparison.

Even if I hadn’t heard the people shouting her name, I would have quickly realized that she was the great chieftain of the Yao people.

*The great chieftain of the Yao people is a woman. Extremely intelligent, and extraordinarily beautiful.*

Namho’s words had been true.

Yohi was beautiful. Almost bewitchingly so.

Whenever her deep gaze swept across the surroundings, people let out exclamations of admiration.

That was probably why.

Amid the cheers and wonder surrounding her, I stood there like a block of wood, making me unusually conspicuous.

“……!”

Yohi’s eyes lit up when they found me.
```
