<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1064.txt",
      "sha256": "6ac273a7f273cfd5b198769c10b6faf75104a90087965334c32d2a99e7e55ade",
      "bytes": 12120
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8f1c6fa74857f1d9888727ffd0de8488064597f77cefbe90d894f4a061595b6e",
      "bytes": 529
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e6e90c56c4fb5b6e5840445ba07954691ab7080fd172ad4077862271c2c42052",
      "bytes": 241772
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "cf35c4332cf4d7d710b9464b4eed6d3b97c82a1337c97c06f4620387b3062c8b",
      "bytes": 753
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "31d76bf86e664a465f7213e5f548a44042a1930439d027626dd1e7fc9f2c79e3",
      "bytes": 651
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8814983a7574e583d99fbe813584b571cedeff8badec53534dfc98028fbf33c0",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2ad994055a07ae154c9863c2b7e259a89dcd7961f2625d75b51833292ba38f0a",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "637c92c13c026383c86cd753414e5b6830ed35f6b7b2dd5ab85d4f46add72c0b",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3fb747d35d651bb11f40f88b245dcccce3538c58caf24b077427793b7a59a679",
      "bytes": 283398
    }
  ],
  "estimated_tokens": 9789
}
-->

# Durable State Update — Chapter 1064

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
1 and safe_through 1064. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1064. Profile updates may replace only one
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
  "chapter": 1064,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1064,
    "continuity_sources": [1064],
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
    "The victory in Gansu is celebrated across the realm, though reports of enemy casualties are exaggerated.",
    "The Emperor has called for the government and Murim to unite against Dark Heaven.",
    "A falcon arrives from the direction of Qinghai with a bloodied missive; its contents are unknown."
  ],
  "continuity_sources": [
    1063
  ],
  "open_questions": [
    "What does the bloodied missive from Qinghai say?"
  ],
  "safe_through": 1063,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 마교     | **Demonic Cult**                                 |                                                       |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 로그아웃             | **Logout**                     |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 정마대전   | **Great Faction War**         |
| 도사      | **Daoist**                                                      |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 십만마도 | **Hundred Thousand Demonic Disciples** | The earlier force used as a comparison for Dark Heaven’s army. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 대마도사 | 궁성 | Adversaries | Bow Saint | Not established | She identifies him by title when recognizing the archer who struck the Hell Fire sphere. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |

## Listed compact profiles

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1053
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** Fanatically devoted to the Lord of Heaven, she stays composed while coercing her enemies and treats their resistance with contempt.
- **Voice:** Calm and formally polite while taunting, but drops the courtesy for blunt, scornful challenges when addressing an enemy.
- **Relationships:** She commands the white-robed mages, serves a master who has long awaited Jin Taekyung, and acts to keep Jin alive despite being unable to kill him without her master’s permission.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1061
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1063
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1063
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1063
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1064화




만약 조금이라도 발견이 늦었더라면 그 전서응(傳書鷹)은 그대로 모두의 머리 위를 스쳐 지나갔을 것이다.

비록 전서구보다 훨씬 철저한 훈련과 관리 끝에 길러진 전서응이라 할지라도, 결국 정해진 목적지를 오가도록 훈련받았을 따름이니까.

그러나 진태경을 비롯한 극소수의 인물들은 간발의 차로 전서응의 존재를 눈치챌 수 있었고, 그중에는 궁성 역시 포함되어 있었다.

활을 다룸에 있어서만큼은 천하제일, 아니 어쩌면 고금제일이라 칭해도 좋을 신궁(神弓)이.

스르릉, 철컥.

순식간이었다.

강철로 이루어진 이음새가 맞물리는 소음과 함께, 기형적으로 휘어져 있던 두 자루의 곡도(曲刀)를 활로 변모시킨 궁성이 망설임 없이 시위를 당긴 것은.

“지금!”

진태경의 외침이 들린 순간, 궁성은 팽팽하게 당겨진 활시위를 놓았다.

펑!

갈가리 찢겨 나가는 공기.

소리조차 앞질러 쏘아진 빛줄기가 마침내 아득한 하늘 위의 점처럼 보이던 전서응에 닿은 것은, 그야말로 눈 깜짝할 사이에 벌어진 일이었다.

이미 이 모든 상황을 예측한 진태경이 신형을 날린 것 역시도.

쐐애애액!

한 줄기의 바람이 되어 나아가는 신형.

그리고 단숨에 수십여 장의 거리를 주파한 진태경이 내뻗은 손끝에는, 날개를 관통당한 채 추락한 전서응이 있었다.

삣. 삐잇.

“침 바르면 금방 나아. 인마.”

퉁명스러운 말과는 달리, 구슬프게 우는 전서응의 부리를 쓰다듬어 준 진태경은 서둘러 녀석의 발목을 확인했다.

‘이건.’

작게 돌돌 말린 채, 전서응의 발목에 단단히 묶여 있는 전서(傳書)를 본 진태경은 침음성을 삼켰다.

내용을 보기도 전에 엄습해 오는 불길함.

틀림없다.

전서 곳곳에 묻어 있는 저 붉은 무언가는, 필시 누군가의 몸속에서 흘러나왔을 피의 흔적이었다.

그리고 지난 시간을 되짚어 보았을 때, 이런 불길한 예상은 언제나 빗나가는 법이 없었다.

곤륜(崑崙), 함락(陷落).

거친 필체로 휘갈겨 쓴 전서의 첫 줄을 읽는 순간, 진태경은 자신도 모르게 입술을 깨물었다.



* * *



곤륜산맥(崑崙山脈).

청해(靑海)의 서쪽 끝자락에 위치한 이 거대한 산맥은 실로 아득한 역사와 수많은 전설을 간직하고 있다.

고원과 사막까지 이어지는 산줄기는 그 길이만 수천 장에 달하며, 그에 못지않은 해발고도 역시 최고봉(最高峰)이라는 표현에 조금의 모자람도 없을 정도.

그러나 곤륜산맥이 천하 무림인들에게 있어 유독 상징적으로 여겨지는 이유는 따로 있었다.

도가(道家) 무학의 발상지이자, 뿌리 깊은 역사를 지닌 곤륜파의 존재만큼이나 결정적인 이유가.

“결국, 반드시 지켜야 할 관문이 뚫렸군.”

적천강은 씹어뱉는 듯한 말투로 뇌까렸다.

꽉 쥐어진 그의 손아귀 안에는 이미 여러 사람의 손을 거친 전서가 구겨져 있었다.

“여기에 적힌 내용대로 놈들이 곤륜을 점령했다면, 사실상 이미 청해 땅의 절반을 빼앗긴 것이나 다름없다는 뜻.”

나직하게 이어지는 음성에, 사람들이 딱딱하게 굳은 얼굴로 고개를 끄덕였다.

적천강의 말은 틀림없는 사실이었으니까.

곤륜산맥 일대는 대부분 분지로 이루어져 있고, 이는 청해성 면적의 절반에 달할 만큼 광활했으니 이는 곧 아군에게 있어 지배권 상실로 이어졌다.

“옛날 기억이 새록새록 나겠군. 안 그런가, 할망구?”

적천강이 대뜸 던진 물음에 궁성이 미간을 좁혔다.

“당신에게 들을 말은 아니죠. 그게 나이든, 정마대전 당시의 불쾌한 기억이든 간에.”

“그래서, 정마대전 초기 때는 어땠나? 마교 놈들이 곤륜을 넘었을 때 말이야.”

“예기치 못한 기습이었어요. 정마대전 이전까지 마교의 마지막 침공은 이미 수백 년이나 지난 일이었고, 그마저도 곤륜산맥을 넘지 못하고 참패했었으니 더욱 그럴 수밖에 없었죠.”

하지만 인간이란 늘 가지지 못하는 것에 집착하는 동물이다.

지금으로부터 약 오십여 년 전, 그 어느 때보다 강성한 마교를 일구어 냈던 천마(天魔) 역시 예외는 아니었다.

“당시 곤륜파가 며칠을 버텼다고 했지?”

“사흘. 정확히 사흘 밤낮을 싸운 끝에 더는 버티지 못하고 퇴각했죠. 궤멸에 가까운 피해를 입고.”

“십만 명이나 되는 마교 잡놈들을 상대로 사흘이라. 오래도 버텼군.”

저건 결코 비아냥이 아니다.

곤륜파는 어쩔 수 없는 지리적 한계와 까다로운 문규(門規)로 언제나 소수의 제자만을 받아들였고, 그 때문에 구파일방 중에서도 제자들의 숫자가 가장 적었다.

다만 개개인의 뛰어난 실력과 대설산조차 비교할 수 없는 곤륜산맥의 험난함으로 수차례에 걸쳐 마교의 침공을 막아 낼 수 있었을 뿐.

하지만 그런 곤륜파에게도 명확한 한계가 있었다.

반세기 전의 정마대전 때도.

이번에도.

다만 차이가 있다면, 지난 정마대전 당시 개전과 동시에 마교를 상대로 엄청난 타격을 입었던 곤륜파가 이번에는 조금 더 현명한 선택을 했다는 점이었다.

“그나마 다행이지. 망설임 없이 곧장 퇴각을 결정했으니. 그렇지 않으냐?”

적천강이 불현듯 던진 물음에, 말없이 생각에 잠겨 있던 나는 고개를 끄덕였다.

“제가 생각해도 그게 최선이었습니다. 놈들과 정면으로 맞서는 건 미친 짓이에요.”

마교와 암천은 질적으로 다르다.

이는 병력의 질이나 숫자를 논하려는 것이 아니라, 암천이 지닌 어둠은 모두가 예상하는 것보다 훨씬 더 깊고 아득했다.

심지어 나조차도 그 정확한 크기와 깊이를 짐작하지 못할 만큼.

그러나 한 가지는 확실하다.

“만약 정마대전 때처럼 결사 항전을 각오했다면, 곤륜파는 이미 세상에서 지워졌겠죠.”

어쩌면 곤륜파로서도 이것이 가망 없는 전투라는 사실을 짐작하고 있었는지 모른다.

그렇기에 물경 이만에 달하는 청해 무림인들과 관군들까지 합류한 상황에서, 그토록 신속한 퇴각을 결정할 수 있었을 것이다.

물론 전서에는 퇴각하는 과정에서 일천여 명이 죽거나 다쳤다고 적혀 있었지만, 이것이 그들에게 있어 최선의 선택이었다는 사실은 변하지 않았다.

“다행히 대부분의 병력을 보존한 상태로 청해호(靑海湖)까지 물러났다고 하니, 아직 청해 땅을 완전히 빼앗긴 것은 아닐세.”

공동파 장문인, 현천진인이 불쑥 꺼낸 말에 나는 곧장 고개를 저었다.

“틀린 말씀은 아니지만, 이대로라면 시간문제입니다. 지금 청해성에 남아 있는 전력으로는 막아 낼 수 없어요.”

“그건.”

“놈들에게는 마, 아니 믿기 힘든 위력을 지닌 사술(詐術)이 있습니다. 당장 곤륜산맥을 점령한 암천의 병력도 헤아릴 수 없을 정도고요.”

이건 단순한 비유나 표현이 아니다.

나는 조금 전 사로잡은 전서응이 지녔던 전서에 적힌 그대로를 말했을 뿐이었다.

신속한 퇴각을 결정하며 날려 보낸 전서에, 곤륜파의 장로는 이렇게 써놓았다.

헤아릴 수조차 없을 만큼 수많은 적들이, 산맥을 메우며 이곳으로 오고 있다고.

그리고 그 압도적이면서도 무시무시한 광경을 본 순간, 자신도 모르게 수십여 년 전의 어느 날을 떠올렸노라고.

“……십만마도(十萬魔道).”

누군가의 입술 사이로 흘러나온 침음성에 일순간 공기가 무거워졌고, 그것은 너무나도 당연한 일이었다.

이미 두 눈으로 똑똑히 보았으니까.

피부로, 온몸으로 생생하게 느꼈으니까.

지금 이 자리에 있는 이들 중 대부분은 암천이 괴력난신(怪力亂神)의 힘을 부리는 것을 보고 겪었다.

지금까지의 모든 상식을 송두리째 허물어트리는 그 광경을 보며, 절망과 패배감에 휩싸이기도 했을 것이다.

한데, 이번에는 무려 십만이다.

설령 전서를 작성한 곤륜파의 장로가 두려움에 사로잡혀 있었다 하더라도, 과거의 십만마도를 떠올릴 정도의 병력이라면 그리 큰 차이는 없을 것이 분명했다.

‘그리고…… 그중에는 내가 아는 누군가도 포함되어 있겠지.’

짧은 만남에도 불구하고, 잊을 수 없는 한 사람의 얼굴이 불현듯 눈앞을 스쳐 지나간다.

대마도사.

아니, 대술사(大術士).

비록 확신할 수는 없지만, 나는 이미 본능적으로 직감하고 있었다.

그녀는 끈질기게 살아남았으며, 그렇다면 분명 지금쯤 청해에 있으리라는 것을.

‘청해가 무너지면, 그때는 걷잡을 수 없다.’

단지 청해라서가 아니다.

이번에 가까스로 지켜낸 감숙 역시 청해와 크게 다를 것 없는 상황이었다.

천하는 하나의 거대한 댐이고, 댐을 무너트리는 것은 작은 균열과 그로 인한 틈새니까.

‘시간이 필요해. 더 나은 방법을 고민하고, 더 큰 피해 없이 놈들을 저지할 수 있는 시간이.’

엄습해 오는 두통.

하지만 이번에도 시간은 내 편을 들어 주지 않았다.

정확히는, 시간이 아닌 시스템이.

‘로그아웃.’

혹시나 하는 기대를 담아 조심스럽게 마음속으로 되뇌어 보지만, 곧이어 돌아온 시스템의 반응은 담담하면서도 냉정했다.

삐빅.



- [로그아웃]이 불가능한 상태입니다.



“……빌어먹을.”

본능적으로 튀어나온 욕설에 일순간 시선이 집중되었지만, 나는 신경 쓰지 않았다.

아니, 신경을 쓰지 못할 정도로 개 같은 상황이었다.

‘도대체 어째서?’

이미 무림에서만 꼬박 몇 달의 시간을 보내고, 수차례씩이나 생사의 고비를 넘었던 나다.

그런데 시스템은 어느샌가부터 굳게 문을 걸어 잠근 채 열어 주지 않았다.

그저 현대로 되돌아가는 유일한 문을 가로막고, 새로운 퀘스트와 가혹한 현실만을 강요할 뿐이었다.

지금으로부터 며칠 전, 길고도 잔혹했던 대설산에서의 전투를 마무리 지었을 때와 같이.

바로 지금 이 순간에도.



- 진행 중인 연계 퀘스트, [청해성으로]가 아직 완료되지 않았습니다!



으득.

허공에 떠오른 홀로그램 창을 바라보며, 나는 반사적으로 튀어나오려는 욕설을 삼켰다.

그리고 불행 중 다행으로, 새로운 퀘스트의 제목으로 단서를 적선하듯 던져준 시스템을 저주하며 입을 열었다.

이 심각한 상황 속에서도 홀로 병든 닭처럼 꾸벅꾸벅 졸고 있던, 어느 정신 나간 인간에게.

“길잡이 해 준다고 했죠?”

“으, 응?”

그제야 부스스 눈을 뜬 대인이, 입가에 묻은 침을 닦으며 졸린 목소리로 입을 열었다.

“뭐, 그랬던 것 같긴 한데…… 그래서 어디로 갈지는 정했나?”

“네.”

나는 허리를 곧게 펴고 주위를 둘러보았다. 

지금 이 순간 나를 포함한 모든 이가 잠시 멈춰 서 있던 이곳은 기련산맥이라 불리는 장소였고, 며칠 간의 이동 끝에 다다른 산맥의 끝자락에는 새로운 땅이 기다리고 있었다.

청해(靑海)라 불리는, 낯설면서도 위험한 땅이.

“갑시다.”

내 나직한 한 마디에, 사람들이 눈을 빛내며 자리에서 일어났다.
```

## Final English reading copy

```markdown
# Chapter 1064

If they’d spotted it even a little later, that messenger eagle would have flown right over everyone’s heads.

Even messenger eagles, bred with far more rigorous training and care than messenger pigeons, were still only trained to fly between set destinations.

But a handful of people, Jin Taekyung among them, noticed the eagle just in time. The Bow Saint was among them.

The Bow Saint was the greatest archer under heaven—perhaps even the greatest in all history.

*Shing. Clack.*

It happened in an instant.

With the metallic sound of steel joints locking together, the two oddly curved swords transformed into a bow. The Bow Saint drew its string without hesitation.

“Now!”

At Jin Taekyung’s shout, the Bow Saint released the taut bowstring.

*Boom!*

The air tore apart.

A streak of light, faster than sound itself, reached the messenger eagle—a distant speck in the sky—in the blink of an eye.

Jin Taekyung had already anticipated all of this, and he shot forward, too.

*Whoooosh!*

His body surged like a gust of wind.

In a single bound, he crossed dozens of *jang*. At his fingertips was the messenger eagle, falling with an arrow through its wing.

*Screee. Screee!*

“Spit on it and it’ll heal in no time, you idiot.”

His words were gruff, but Jin Taekyung gently stroked the beak of the eagle as it cried mournfully. Then he hurriedly checked its leg.

*This is…*

He swallowed a groan as he saw the missive, rolled into a small bundle and fastened tightly around the eagle’s leg.

A sense of foreboding hit him before he’d even read it.

There was no doubt. That reddish substance smeared across the missive was blood—blood that had flowed from someone’s body.

And looking back at everything that had happened, these ominous suspicions never turned out to be wrong.

Kunlun fallen.

The moment Jin Taekyung read the first line of the missive, scrawled in a rough hand, he bit down on his lip without realizing it.

* * *

The Kunlun Mountains.

This immense range, at the western edge of Qinghai, held a distant history and countless legends.

Its ridges stretched for thousands of *jang*, reaching all the way to plateaus and deserts. And its peaks rose so high that calling them the highest summits was no exaggeration.

But the Kunlun Mountains held a particular significance for the martial artists of the realm for another reason.

A reason every bit as decisive as the existence of the Kunlun Sect, birthplace of Daoist martial arts and heir to a long history.

“So the pass we absolutely had to hold has been breached.”

Jeok Cheongang muttered, as if spitting out the words.

The missive, already passed through several hands, was crumpled in his clenched fist.

“If what’s written here is true and they’ve occupied Kunlun, then we’ve effectively lost half of Qinghai.”

At his low words, everyone nodded with grim faces.

Jeok Cheongang was stating a simple fact.

Most of the area around the Kunlun Mountains was made up of basins, vast enough to cover nearly half of Qinghai Province. Losing them meant losing control of the region.

“Must bring back some old memories. Doesn’t it, you old hag?”

At Jeok Cheongang’s sudden question, the Bow Saint frowned.

“That’s not something I want to hear from you. Whether you mean my age or the unpleasant memories of the Great Faction War.”

“So how was it, back at the start of the Great Faction War? When those Demonic Cult bastards crossed Kunlun.”

“It was an unexpected attack. The Demonic Cult’s last invasion before the Great Faction War had been hundreds of years earlier, and even then they’d been soundly defeated before they could cross the Kunlun Mountains. So of course we never expected it.”

But people always fixated on what they couldn’t have.

The Heavenly Demon, who had built the Demonic Cult into a force stronger than ever some fifty years ago, was no exception.

“How many days did the Kunlun Sect hold out back then?”

“Three. They fought for exactly three days and nights before they could hold out no longer and retreated. They suffered losses that came close to annihilation.”

“Three days against a hundred thousand Demonic Cult bastards. They held out a long time.”

He wasn’t mocking them.

The Kunlun Sect had always accepted only a small number of Disciples due to the harsh limits of their terrain and their strict rules. As a result, they had the fewest Disciples among the Nine Sects and One Gang.

But their Disciples were individually formidable, and the Kunlun Mountains were more treacherous than even the Great Snow Mountain. That was how they’d managed to repel the Demonic Cult’s invasions time and again.

Even so, the Kunlun Sect had its limits.

Back during the Great Faction War half a century ago.

And now.

The difference was that this time, unlike in the last Great Faction War, when the Kunlun Sect was dealt a devastating blow by the Demonic Cult at the very start of hostilities, they’d made a wiser choice.

“At least they made the decision to retreat right away, without hesitation. Isn’t that right?”

At Jeok Cheongang’s sudden question, I nodded, having been lost in thought.

“Even I think that was the best choice. Facing them head-on would’ve been insane.”

The Demonic Cult and Dark Heaven were different in kind.

I wasn’t talking about the quality or number of their troops. The darkness within Dark Heaven was far deeper and more boundless than anyone could imagine.

Even I couldn’t begin to guess its true size or depth.

But one thing was certain.

“If they’d decided to fight to the death like they did during the Great Faction War, the Kunlun Sect would already have been erased from the world.”

Maybe the Kunlun Sect had realized this battle was hopeless, too.

That might be why they’d decided to retreat so quickly, despite being joined by Qinghai’s martial artists and government troops—twenty thousand of them.

The missive said that around a thousand had been killed or wounded during the retreat, but that didn’t change the fact that it had been their best choice.

“Fortunately, they retreated as far as Qinghai Lake with most of their forces intact. Qinghai hasn’t been completely taken from us yet.”

Perfected Being Hyeoncheon, the Sect Leader of the Kongtong Sect, had abruptly spoken up. I immediately shook my head.

“You’re not wrong, but at this rate, it’s only a matter of time. The forces still in Qinghai can’t hold them back.”

“That’s…”

“They have magic—or, no, dark arts with a power that’s hard to believe. And the Dark Heaven forces that occupied the Kunlun Mountains are too numerous to count.”

That wasn’t a figure of speech or an exaggeration.

I was only repeating what was written in the missive carried by the messenger eagle I’d just caught.

As the Kunlun Sect decided to retreat swiftly, one of its Elders had sent a missive with these words:

Countless enemies, too many to even number, were filling the mountains and advancing toward them.

And seeing that overwhelming, terrifying sight had made him think of a certain day from decades ago.

“…The Hundred Thousand Demonic Disciples.”

The groan slipped from someone’s lips, and the air grew heavy. It was only natural.

Most of those present had already seen it with their own eyes.

They’d felt it on their skin, in every part of their bodies.

Most of the people here had seen and experienced Dark Heaven wield supernatural powers.

They must have felt despair and defeat as they watched a sight that tore down every assumption they’d ever held.

And now there were a hundred thousand of them.

Even if the Kunlun Sect Elder who’d written the missive had been overcome with fear, an army large enough to bring the Hundred Thousand Demonic Disciples to mind couldn’t have been far off in size.

*And someone I know is probably among them.*

Despite the brief time we’d spent together, the face of one unforgettable person suddenly crossed my mind.

The Grand Mage.

No—the Grand Mage.

I couldn’t be certain, but I already knew it in my gut.

She’d survived, tenacious as ever. If so, she had to be in Qinghai by now.

*If Qinghai falls, things will get out of hand.*

And not just because it was Qinghai.

Gansu, which we’d barely managed to protect, was in much the same situation.

The realm was one enormous dam. All it took to bring it down was a small crack—and the gap that followed.

*We need time. Time to think of something better, to stop them without taking even greater losses.*

A headache pressed in.

But this time, too, time wasn’t on my side.

Or rather, not time. The System.

*Logout.*

I carefully repeated the word in my mind, with a glimmer of hope.

The System’s response came back calm and cold.

*Beep.*

> **System**
>
> **Logout** is unavailable.

“…Damn it.”

Everyone’s attention snapped to me at the curse that escaped on instinct, but I didn’t care.

No, the situation was so fucked that I couldn’t care.

*Why?*

I’d already spent months in Murim and faced death several times over.

But at some point, the System had slammed the door shut and refused to open it.

It had done nothing but block the only way back to the modern world and force new Quests and a brutal reality on me.

Just like a few days ago, when we’d finally finished the long, brutal battle at the Great Snow Mountain.

Even now.

> **System**
>
> The ongoing linked Quest, **To Qinghai**, has not yet been completed!

*Crack.*

I stared at the holographic window floating in the air and swallowed back the curse that was about to slip out.

And, in a stroke of good luck amid all this misfortune, I cursed the System for tossing me a clue like alms in the form of a new Quest title. Then I spoke to a certain lunatic, who was the only one there nodding off like a sick chicken in the middle of this dire situation.

“You said you’d guide us, right?”

“Huh? Yeah?”

Only then did the Great Sir blink blearily awake. Wiping the drool from his mouth, he spoke in a sleepy voice.

“I think I did say that… So, have you decided where you’re going?”

“Yes.”

I straightened up and looked around.

Everyone, myself included, had paused here for a moment. This place was called the Qilian Mountains. At the range’s far end, after several days of travel, a new land awaited us.

A strange and dangerous land called Qinghai.

“Let’s go.”

At my quiet words, everyone’s eyes lit up as they rose to their feet.
```
