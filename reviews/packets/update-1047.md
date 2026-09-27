<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1047.txt",
      "sha256": "ac93e3c5dc466851a5df7ebe97222ec304b66fe827ecb447f5d7f7fa087fc9c3",
      "bytes": 12712
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d1a54c0204a770d5c9289a0c586420ca70e3478e71e600f6f35003bdbb424ae7",
      "bytes": 1506
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "12d0a20e001dc1fbc724be8144e4b4fda2c12037b1c80473f7dfc2a2f121a506",
      "bytes": 914
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b399fa814623db4cb08f3cee7c62a622f3b1cf72d2dc374520e95bf1030784aa",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "bf5e49764f1cba576a19438bb2ce3e1eec9c5b2b6eca691b27342fd249b164a4",
      "bytes": 1502
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "864145616532dd5f247599e7fe6f64ba4f339c468263cc56828bed8e666f2528",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2319c817ad8d28a56de42d0dc28fe49edbeb82c185063281e08bb36c56270974",
      "bytes": 281330
    }
  ],
  "estimated_tokens": 10095
}
-->

# Durable State Update — Chapter 1047

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
1 and safe_through 1047. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1047. Profile updates may replace only one
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
  "chapter": 1047,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1047,
    "continuity_sources": [1047],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "The Bow Saint’s Force arrows destroyed the fireballs threatening the battlefield; the Taeeul Merciless Sword and Roaring Fury Swordsman survived, injured.",
    "Fewer than five hundred Zhongnan Sect disciples remain; they continue fighting, and Hyuk Sopyung’s rally helps the Gansu Coalition Army resume its attack.",
    "Taishan, Namho, Song Ilseom, Ju Hwaran, Hyuk Mujin, and Ma Junggeol are fighting toward Jin Taekyung; Mujin and Ma Junggeol are wounded.",
    "A thousand Embroidered Uniform Guards led by Jeong Hogun arrived under the Emperor’s order to protect Jin Taekyung and defeat his enemies."
  ],
  "continuity_sources": [
    1045,
    1046
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "What happened to Jin Taekyung, Jeok Cheongang, Sima Gong, Song Il, and Hwangbo Eom after the blast?"
  ],
  "safe_through": 1046,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 삼성     | **Three Saints**    |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 감숙     | **Gansu**              |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 천주 | servant_to_master | Lord of Heaven | deferential | In his inner monologue, he addresses his absent master as 당신 and refers to himself as 속하. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1045
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1046
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1045
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1045
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1047화



전투의 승패를 결정짓는 가장 큰 요인이 무엇이냐 묻는다면, 백이면 백 모두가 같은 답을 내놓을 것이다.

병력의 질, 혹은 숫자라고.

그러나 질문을 받은 이가 일군(一軍)을 이끄는 장군이라면, 그는 다르게 답할 것이다.

지금 이 순간, 혈검마군의 머릿속에 스쳐 지나가는 두 글자를.

‘기세.’

틀림없다.

적들의 기세가, 흐름이 바뀌었다.

혈검마군은 불현듯 뜨겁게 달아오르는 공기를 느꼈다.

부슬비에 젖은 모닥불처럼 조금씩 꺼져 가던 적들의 투기(鬪氣)가, 그들이 온 힘을 다해 내지르는 함성이 점점 더 강렬해지고 있었다.

처절함에 가까운 그 감정. 죽음을 불사한 의지.

언제 포기하려 했냐는 듯, 마지막 불꽃을 담아 휘둘려지는 병장기들.

그리고.

슈확!

그런 그들보다 한발 앞서, 허공을 가로지르는 휘황한 빛줄기.

콰아아앙!

끔찍한 파괴력이 담긴 섬광이 수십여 명이나 되는 암천의 교도들을 단숨에 집어삼킨다.

이미 크고 작은 화염구의 폭발로 인해 생겨난 공백.

거기에 더해 엄청난 위력을 지닌 빛줄기가 단단하던 전열을 뒤흔드니, 이제 저들에게 필요한 것은 이 틈새를 비집고 적의 심장을 관통할 한 자루의 창뿐이었다.

이를테면…….

금의위(錦衣衛)라 불리는, 황금빛 창이.

콰드드드득!

귓가가 먹먹해질 정도의 함성과 굉음이 뒤섞인다.

격돌과 함께 벼락처럼 휘둘려진 날붙이 사이로 수많은 죽음과 삶이 오가고, 짙은 피 안개가 일대를 뒤덮었다.

대설산의 가파른 산비탈을 휩쓸며 전장으로 돌격한 황금빛 물결이 붉게 물들기까지는, 그야말로 찰나의 순간만이 필요했을 뿐이었다.

서걱! 푸푸푹!

번뜩이는 검신이 단숨에 목을 자르고, 날카로운 창끝이 가슴을 관통한다.

한 사람 한 사람이 최소 초일류에서 절정의 경지에 도달한, 그렇기에 황실을 수호하는 영광스러운 자리에 오를 수 있었던 대국 최강의 무력 집단은 앞길을 막아서는 모든 것을 베고 찔렀다.

자신들이 이 전장에 나타난 이유를 거센 함성으로 토해 내며.

“황제 폐하 만세! 황태제 전하 천세!”

“상산후(上山侯)를 위하여!”

“쳐라!”

쉬쉬쉬쉭!

광신도와도 같은 충성심으로 무장한 그들을 선두로, 살아남은 이만여 명의 연합군이 돌격을 감행했다.

누군가는 동료의 복수를 위해. 누군가는 대의를 위해.

저마다의 이유와 목적은 달랐지만, 그들 모두가 원하는 결과는 같았다.

승리.

그리고 오늘 이 자리에서 찬란한 승리를 원하는 것은, 이 뜻밖의 이변 앞에서 빠르게 기울어지는 승패의 저울추를 느끼고 있던 혈검마군 역시 마찬가지였다.

“이런 개 같은……!”

앙다문 입술 사이를 비집고 흘러나오는 침음성.

현재의 전황은 그만큼 혈검마군이 예상치 못한 방향으로 흘러가고 있었다.

‘궁성에 더해 금의위까지 나타나다니.’

삼성(三星)의 일원인 궁성은 말이 필요 없는 존재고, 황실 직속의 금의위는 대국이 가진 가장 날카로운 검이다.

비록 병력의 숫자는 여전히 우세를 점하고 있으나, 이제는 전력 면에서 앞선다고도 자신할 수 없는 상황.

심지어 이 강력한 지원군의 등장으로 기세를 되살린 이만여 명의 적들까지 미친 듯이 날뛰기 시작하자, 혈검마군의 마음 한구석에서는 불안감이 싹트기 시작했다.

‘설마…… 아니, 아니다. 그럴 리 없어.’

혈검마군은 애써 부정했다.

자신도 모르게 머릿속에 떠올린 패배라는 두 글자를.

그 어느 때보다 강력한 존재로 거듭난 이 순간에도, 조금씩 위축되어 가는 자신의 모습을.

‘아직 술사들이, 대술사가 남아 있다. 그년이 조금 전과 같이만 해 준다면 전력 면에서는 결코 밀리지 않아.’

하지만 어째서일까.

아군인 혈검마군조차도 잠시나마 경악하게 만들었던 그 거대한 불덩어리는 지금도 나타나지 않고 있었다.

또 다른 마법도, 이를 예고하는 기의 파동도 느껴지지 않았다.

‘……도대체 어째서?’

설마 그 짧은 사이에 대술사에게 무슨 일이라도 생긴 것일까.

순간 가슴이 덜컥 내려앉은 혈검마군은 고개를 돌려 언덕 위의 상황을 확인했다.

아니, 정확히는 확인하려 했다.

바로 그때, 담담한 시선으로 그를 응시하던 누군가가 불쑥 입을 열기 전까지는.

“일이 뜻대로 풀리지 않는 모양이구려.”

흑야왕 사마공.

피에 젖은 그의 입술 사이로 흘러나온 한 마디에, 정곡을 찔린 혈검마군의 얼굴이 악귀처럼 일그러졌다.

“뭐?”

“이해하오, 살다 보면 그럴 때가 있는 법이지.”

사마공은 침착하게, 그러나 지친 목소리로 말을 이었다.

이미 혈검마군에 의해 처참하게 뜯겨 나간 자신의 팔, 아니 어깻죽지를 바라보며.

“불과 한 식경 전까지만 하더라도, 나 역시 이런 꼴이 되리라고는 상상하지 못했으니까.”

단지 팔 하나를 잃었기 때문에 이런 말을 하는 것이 아니다.

지금 사마공은 피 웅덩이에 잠겨 있었다. 오직 자신의 피로 이루어진 그 끈적한 핏물 속에.

그러나 감히 자신의 앞을 막아선 배신자를 불과 촌각 만에 쓰러트린 혈검마군은, 단죄에 대한 기쁨이 아닌 분노로 몸을 떨고 있었다.

“네놈만, 네놈만 아니었더라면……!”

일이 한참이나 틀어졌다.

본래대로라면 사마공은 적당한 시점에서 감숙 연합군에 퇴각을 명령해야 했고, 혈검마군은 손쉬운 승리를 얻어냈을 터였다.

그것이 두 사람 간의 거래였다.

만약 사마공이 암천을 도와 감숙에서의 승리를 이끌어 낸다면, 이를 교두보로 삼아 중원을 손에 넣고 감숙과 섬서에 한하여 소유권을 인정해 주겠다는.

아주 은밀하고, 합리적으로 이루어진 거래.

그리고 그 거래의 일부분은 이미 성공적으로 이행되었다.

바로 이곳 대설산이 아닌, 감숙성 서쪽 끝자락에 위치한 돈황(敦煌)에서.

“처음부터 이럴 생각이었느냐? 단지 오늘의 승리를 위해, 네가 여전히 간자라는 사실을 믿게 하기 위해 다른 무엇도 아닌 공동파를 단순한 미끼로 사용했다는 말이냐?”

속사포처럼 터져 나오는 의문.

지체할 시간이 없었다.

현실적으로 보자면 지금 당장이라도 이 찢어 죽여도 시원치 않을 배신자의 숨통을 끊고 수습에 나서는 것이 옳았다.

그러나 혈검마군은 아직까지도 자신의 판단이 틀렸다는 사실을 믿을 수 없었고, 이에 대한 답을 반드시 들어야 했다.

그가 본 흑야왕 사마공은 뼛속까지 사파인이었으니까.

생존을 위해서라면 암천이 아니라 악마와도 손을 잡을 수 있는, 박쥐보다 더한 해충 같은 인간이었으니까.

그렇기에 거래의 대상으로 사마공을 택했으면서도, 감숙 땅에 발을 디딘 그 순간까지 마지막 의심을 끈을 놓지 않았었다.

그에게 전달받은 정보를 토대로, 돈황을 지키던 공동파를 상대로 엄청난 대승을 거두기 전까지는.

“대답해라, 어서!”

비단 혈검마군이 아닌 다른 누구라 할지라도 같은 반응이었을 것이다.

그만큼 돈황에서 공동파가 보인 저항은 격렬했고, 그로 인해 그들이 입은 타격은 극심했으니까.

제아무리 대를 위해 소를 희생한다지만, 구파일방의 일익인 공동파를 일시적인 눈가림을 위한 미끼로 쓸 정신 나간 생각은 그 누구도 할 수 없을 테니까.

그리고 혈검마군이 뿜어내는 그 막강한 기세 앞에서, 마침내 굳게 닫혀 있던 사마공의 입술이 열렸다.

“나는 광인이 아니오. 이제 와서 두 번 배신하는 미친 짓을 벌이기에는 너무 이성적이지. 그렇기에 당신들과 손을 잡은 것이고.”

혈검마군의 짐작이 옳았음을 알려 주는 한 마디.

하지만 그것은 혈검마군이 원했던 답인 동시에, 그의 마음에 더욱 큰 의문을 심어 주는 말이기도 했다.

“그럼 도대체……”

“왜, 어찌하여 이런 짓을 벌였느냐고? 글쎄.”

혈검마군의 말을 끊어 낸 사마공은 힘없이 눈을 깜빡이며 스스로에게 반문했다.

왜 이런 멍청한 선택을 했느냐고.

모든 것이 순조로웠는데, 어째서 돌이킬 수 없는 강을 건넜느냐고.

그리고 문득 이 자리에 없는, 동시에 있어서는 안 되는 한 사람을 떠올리는 자신을 발견하고 씁쓸하게 웃었다.

“어쩌면 아주 잠깐, 미쳐 있었던 모양이지.”

“뭐……라고?”

“하지만 나로서는 천만다행이오. 그 미친 짓이 통했으니. 안 그렇소?”

결과적으로 사마공이 혈검마군을 막아선 촌각의 시간은 전투의 향방을 뒤바꾸지는 못했으나, 그의 도움을 받은 화왕 적천강은 결코 그 사실을 잊지 않을 터.

사마공에게는 그것만으로도 충분했다.

설령 그가 죽더라도 최소한의 면죄부를 쥔 흑룡마문은 존속할 수 있을 테니까.

이 자리에 없는 자신의 후계자가 살아남아, 자신에게 물려받은 모든 것들을 더욱 강성하게 키워 낼 테니까.

“피곤하군. 이제 쉬어야겠어.”

눈을 부릅뜬 채 굳어 버린 혈검마군을 향해, 늙은 사파인은 담담한 음성으로 말을 이었다.

천마를 배신하고 새로운 주인을 섬기게 된, 눈앞의 광신도에게 줄곧 하고 싶었던 한 마디를 마지막으로 덧붙이며.

“이만 죽여라. 이 박쥐 같은 마교 잡놈아.”

“……!”

까드득.

악문 잇새로 흘러나온 섬뜩한 마찰음.

부서질 듯이 어금니를 깨문 혈검마군은 한계에 다다른 분노를 검 끝에 실어 곧추세웠다.

반드시 성공했어야 할 자신의 계획을, 감히 위대한 천주의 앞길에 오물을 뿌린 배신자를 향해.

슈확!

그리고 검붉은 강기에 휩싸인 검신이 벼락처럼 떨어져 내리려던 그 순간.

쉬잉! 콰드드득!

어디선가 날아든 한 줄기의 빛이, 정확히 검의 옆면을 강타했다.

서걱!

마지막 순간 방향이 어긋난 검이 애꿎은 지면을 두부처럼 갈라낸다. 그와 동시에 빛줄기의 정체를 알아차린 혈검마군이 끓어오르는 음성으로 외쳤다.

“궁성……!”

그 부름에 답하듯, 허물어지는 암천의 교도들 사이로 다시 한번 강기의 화살이 날아들었다.

쉬쉬쉬슁!

사방을 밝히는 다섯 줄기의 섬광. 그 휘황한 모습에 이를 악문 혈검마군의 신형이 순간 흐릿해졌다.

쾅! 쾅! 콰아앙!

소리를 뛰어넘은 속도로 움직이는 검을 따라 폭발과 굉음이 일었다.

부르르 떨리는 검신을 통해 적잖은 충격이 전해졌지만 단지 그뿐.

어렵지 않게 궁성이 쏘아 보낸 강기의 화살들을 모조리 베거나 튕겨 낸 혈검마군은 이빨을 드러내며 웃었다.

“그래, 고작 이 정도였느냐?”

혈검마군은 설마하는 마음으로 인해 잠시 잊고 있던 사실을 떠올렸다.

맞다.

술사들의 도움을 받은 지금의 자신의 어느 때보다 강하다.

전설이나 다름없는 삼성의 일원인 궁성이 나타났다고 해도, 이미 한계를 뛰어넘은 자신의 상대는 될 수 없었다.

‘대술사, 그 건방진 년이 왜 아직까지 잠잠한지는 몰라도…….’

츠츠츠.

타오르는 듯한 강기 너머로, 섬뜩한 혈광이 번뜩였다.

“오너라. 이 몸이 모두 상대해 주마.”

그리고 바로 다음 순간. 혈검마군은 깨달았다.

“그거 듣던 중 반가운 소리구먼.”

자신이 잠시 잊고 있던, 또 다른 사실을.

“이 나이 처먹고 합공하기에는 많이 쪽팔렸는데. 덕분에 마음이 한결 편안해졌어.”

화왕(火王) 적천강.

입가에 맺힌 푸근한 미소와는 달리, 끔찍하리만치 강렬한 화염을 두 손에 휘감은 구화산의 노괴를 발견한 혈검마군의 눈동자가 파르르 떨렸다.
```

## Final English reading copy

```markdown
# Chapter 1047

If you asked what mattered most in deciding the outcome of a battle, every single person would give the same answer.

The quality of the troops—or their numbers.

But if the person you asked were a general commanding an army, he would answer differently.

He would name the two words that flashed through the Blood-Sword Demon Lord’s mind at that very moment.

*Momentum.*

There was no doubt about it.

The enemy’s momentum, the tide of battle, had changed.

The Blood-Sword Demon Lord suddenly felt the air grow hot.

The fighting spirit of his enemies, which had been fading little by little like a campfire soaked by drizzle, was rising. Their shouts, wrenched from them with all their strength, were growing more and more intense.

An emotion close to desperation. A resolve to face death without hesitation.

Weapons swung with their final spark of life, as if their wielders had never once considered giving up.

And then—

Shwaaa!

A dazzling streak of light cut across the sky, one step ahead of them.

KWA-BOOOOM!

A flash packed with terrible destructive force swallowed dozens of Dark Heaven cultists in an instant.

The explosions of fireballs, large and small, had already opened gaps in their ranks.

Now the tremendously powerful streak of light shook their once-solid formation. All the enemy needed was a spear to slip through the opening and pierce their heart.

Something like…

A golden spear called the Embroidered Uniform Guard.

KRAK-KOOM!

Deafening shouts and thunderous booms blended together.

As they collided, countless lives were won and lost amid blades swinging like lightning. A thick mist of blood blanketed the area.

It took only an instant for the golden wave that had swept over the steep slopes of the Great Snow Mountain and charged onto the battlefield to turn red.

Slice! Thud-thud!

A flashing blade cut through a neck in one stroke. A sharp spearhead pierced a chest.

Every one of them had reached at least Supreme First Rate, with some attaining the Peak realm. That was how they had earned the honor of protecting the imperial family. The Great Nation’s most powerful force cut and stabbed through everything in their path.

Their fierce shouts proclaimed why they had come to this battlefield.

“Long live His Majesty the Emperor! May His Highness the Imperial Crown Brother live a thousand years!”

“For the Marquis of Shangshan!”

“Charge!”

Shwish-shwish-shwish!

Led by those armed with a fanatic’s loyalty, more than twenty thousand surviving Coalition Army soldiers charged forward.

Some sought revenge for their comrades. Others fought for a greater cause.

Their reasons and aims differed, but they all wanted the same thing.

Victory.

And the Blood-Sword Demon Lord, who felt the scales of battle tipping rapidly in the face of this unexpected turn, wanted a glorious victory here today just as much as they did.

“You’ve got to be fucking kidding me…!”

A groan slipped through his clenched lips.

The battle was unfolding in a way the Blood-Sword Demon Lord hadn’t expected.

*The Bow Saint—and now the Embroidered Uniform Guard?*

One of the Three Saints, the Bow Saint, needed no introduction. The Embroidered Uniform Guard, directly under the imperial family, was the Great Nation’s sharpest sword.

His side still had the advantage in numbers, but he could no longer be sure they were stronger overall.

And now that this powerful reinforcement had restored the momentum of the more than twenty thousand enemy soldiers, they were charging wildly. Unease began to take root in one corner of the Blood-Sword Demon Lord’s mind.

*No… No, that can’t be.*

He desperately rejected it.

The two words that had appeared in his mind without his noticing: *defeat.*

And the sight of himself, growing more and more apprehensive even now, when he had become more powerful than ever.

*The sorcerers are still here. The Grand Mage is, too. If that bitch can do what she did before, we won’t be at a disadvantage.*

But why?

The enormous ball of fire that had even stunned the Blood-Sword Demon Lord, one of its own allies, hadn’t appeared again.

He sensed neither another spell nor a surge of qi heralding one.

*…Why?*

Could something have happened to the Grand Mage in that brief time?

The Blood-Sword Demon Lord’s heart lurched. He turned to check what was happening on the hill.

Or rather, he tried to.

Until someone who had been watching him calmly spoke up.

“Things aren’t going as you planned.”

Black Night King Sima Gong.

At the words that slipped between his bloodied lips, the Blood-Sword Demon Lord’s face twisted like a fiend’s.

“What?”

“I understand. Sometimes things just don’t go your way.”

Sima Gong continued in a calm, weary voice.

He looked at his arm—or rather, the shoulder where the Blood-Sword Demon Lord had brutally torn it away.

“I couldn’t have imagined I’d end up like this, not even half an hour ago.”

He wasn’t saying this merely because he’d lost an arm.

Sima Gong was half-submerged in a pool of blood. Thick blood that belonged to him alone.

Yet the Blood-Sword Demon Lord, who had struck down the traitor in his path in moments, trembled with rage, not the joy of punishment.

“If it weren’t for you—if it weren’t for you…!”

Everything had gone badly wrong.

Under the original plan, Sima Gong was supposed to order the Gansu Coalition Army to retreat at the right moment, and the Blood-Sword Demon Lord would have won easily.

That had been their bargain.

If Sima Gong helped Dark Heaven win in Gansu, they would use it as a foothold to seize the Central Plains and recognize his ownership of Gansu and Shaanxi.

A secret, reasonable deal.

And part of it had already been carried out successfully.

Not here, at the Great Snow Mountain, but in Dunhuang, at the western edge of Gansu Province.

“Was this your plan from the beginning? Are you saying you used the Kongtong Sect—not anyone else—as a simple decoy just to win today and make us believe you were still our spy?”

Questions poured out of him in a rush.

There was no time to waste.

By all rights, he should have cut short the life of this traitor he wanted to tear apart with his bare hands and started to salvage the situation at once.

But the Blood-Sword Demon Lord still couldn’t believe he’d been wrong. He had to hear the answer.

Because the Black Night King Sima Gong he knew was an unorthodox man to the bone.

A pest worse than a bat, ready to join hands with the devil himself—not just Dark Heaven—if it meant surviving.

That was why the Blood-Sword Demon Lord had chosen Sima Gong as a partner, but even when he set foot in Gansu, he still hadn’t let go of his last doubts.

Only after they won a tremendous victory over the Kongtong Sect guarding Dunhuang, using the information Sima Gong had given him, did he finally trust him.

“Answer me! Now!”

Anyone else would have reacted the same way, not just the Blood-Sword Demon Lord.

The Kongtong Sect’s resistance in Dunhuang had been fierce, and the damage they suffered was severe.

No one could come up with the insane idea of using a member of the Nine Sects and One Gang as a decoy in a temporary ruse, no matter how much they believed in sacrificing the small for the greater good.

At last, under the overwhelming pressure radiating from the Blood-Sword Demon Lord, Sima Gong’s tightly closed lips parted.

“I’m no madman. I’m too rational to betray one side only to turn on the other. That’s why I joined hands with you.”

One sentence confirmed the Blood-Sword Demon Lord’s suspicions.

But it was both the answer he wanted and one that planted an even greater question in his mind.

“Then why the hell—”

“Why? Why would I do this? Well…”

Sima Gong cut him off, blinking weakly as he asked himself the question.

Why had he made such a foolish choice?

When everything had been going smoothly, why had he crossed a river he could never return from?

Then he found himself thinking of someone who wasn’t here—and shouldn’t be—and gave a bitter smile.

“Maybe I went crazy for a little while.”

“What… did you say?”

“But I’m incredibly lucky that moment of madness worked. Don’t you think?”

In the end, the moments Sima Gong had spent standing against the Blood-Sword Demon Lord hadn’t changed the course of the battle. But Fire King Jeok Cheongang, whom he had helped, would never forget it.

That was enough for Sima Gong.

Even if he died, the Black Dragon Demon Gate would survive with at least some measure of absolution.

His heir, who wasn’t here, would live and make everything Sima Gong had passed down even stronger.

“I’m tired. I should rest now.”

The old unorthodox sect leader spoke calmly to the Blood-Sword Demon Lord, who stood frozen, eyes wide.

Then he added one last thing he’d wanted to say to the fanatic before him, who had betrayed the Heavenly Demon and taken a new master.

“Go ahead and kill me. You bat-like Demonic Cult bastard.”

“……!”

Grind.

A chilling scrape came from between his clenched teeth.

The Blood-Sword Demon Lord clenched his molars as if to crush them, then raised his sword, pouring his rage into its tip.

He aimed it at the traitor who had ruined a plan that should have succeeded—and dared to throw filth in the path of the mighty Lord of Heaven.

Shwaaa!

But just as the sword, wrapped in dark-red Force, was about to come crashing down like lightning—

Shing! KRAK-KOOM!

A streak of light flew in from somewhere, striking the flat of the blade dead on.

Slice!

The sword veered off at the last moment and carved into the ground instead, as easily as a knife slicing tofu. At the same time, the Blood-Sword Demon Lord recognized the streak of light and shouted, his voice boiling with fury.

“Bow Saint…!”

As if answering his call, another Force arrow came flying through the crumbling ranks of Dark Heaven’s cultists.

Shwish-shwish-shwing!

Five streaks of light illuminated the surroundings. The Blood-Sword Demon Lord’s figure blurred for an instant as he gritted his teeth.

Bang! Bang! KWA-BOOOOM!

Explosions and thunderous booms followed the sword as it moved faster than sound.

The trembling blade sent a powerful shock through him, but that was all.

The Blood-Sword Demon Lord easily cut or deflected every Force arrow the Bow Saint fired. He bared his teeth in a grin.

“So this is all you’ve got?”

The Blood-Sword Demon Lord remembered something he’d briefly forgotten in his disbelief.

That’s right.

With the sorcerers’ help, he was stronger now than he’d ever been.

Even with one of the legendary Three Saints, the Bow Saint, on the battlefield, she couldn’t match him now that he’d surpassed his limits.

*I don’t know why that insolent bitch, the Grand Mage, is still quiet…*

Tzzzz.

Beyond the blazing Force, a sinister red light glinted.

“Come on. I’ll take you all on.”

And in the very next moment, the Blood-Sword Demon Lord realized—

“Now that’s good to hear.”

—another thing he’d briefly forgotten.

“Being this old and ganging up on someone’s pretty embarrassing. You’ve made me feel a lot better.”

Fire King Jeok Cheongang.

The Blood-Sword Demon Lord’s pupils trembled as he spotted the old monster of Mount Jiuhua, a warm smile on his lips, with flames so fiercely bright they were horrifying wrapped around both hands.
```
