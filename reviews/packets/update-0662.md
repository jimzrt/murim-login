<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0662.txt",
      "sha256": "a72ef45f51d40ee44ba799d046639d3cb9681211d3a845fd3ce8b5e97fc60085",
      "bytes": 13630
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3216d3f9ecab447c9242d70bc1bfa1535ca399016af3be890c43721dc0a8c10f",
      "bytes": 2285
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6a2a21de185f54d15e930209aa3c179d4b14955192cd9b5a37a916b41cc6cad7",
      "bytes": 201357
    },
    {
      "path": "characters/Baekhwi.md",
      "sha256": "b6f54c680b5a67330e5a572b35295c2c2cfa9b0a404a3b0adc6b2c62f7dd43a8",
      "bytes": 433
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "d7989e9226306416afb92b1aa3b0dc9ec70f6fef28d8aa1df7496b7449552ad2",
      "bytes": 1006
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "68e777c5fe5fa72339189f07806c3f6e6f64038978d940f699251b0970505760",
      "bytes": 814
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fb3bdbfc8f1417d0143a7cecb0596cca1db667897b408f95c52333d3e4cd450e",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Sopyung.md",
      "sha256": "6ad497c3c574d22a15612fc068d669f70f87ec9cb5e78778e1b0c69b0ccd42c1",
      "bytes": 618
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "02e81ca9e995b24989393ffa618b94015b7cf689b3becad6a86e7e8de5893ebd",
      "bytes": 1702
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "8aafa36a73ab539c362cfb99b3585a0dec25a88764d410493fedc9eb3408af80",
      "bytes": 1061
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4b87566b04466cdedd5a25cae0dece9f1c7e71396058292555cc479cd398e2e7",
      "bytes": 206682
    }
  ],
  "estimated_tokens": 11386
}
-->

# Durable State Update — Chapter 662

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 662. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 662. Profile updates may replace only one
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
  "chapter": 662,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 662,
    "continuity_sources": [662],
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
    "Jin Taekyung remains imprisoned in the Nanman Beast Palace's underground prison, bound by iron balls and unable to use internal energy because of the Force-Sealing Pill; his execution is scheduled for noon in two days.",
    "Baeksang has secured the support of twenty tribal chieftains and is using Jin's execution as the final-day agenda of the Tribal Grand Council.",
    "Baeksang's only child was named Baekhwi; Baekhwi is deceased and would have become the Beast Miao King's son-in-law if he had lived.",
    "Baeksang and the Beast Miao King once led ten thousand Nanman warriors alongside the Zhongnan Sect in the Southern Army; fewer than one-tenth survived the war against the Demonic Cult.",
    "The Fire Dragon Pavilion was attacked after Jin left, Dark Heaven is suspected of involvement, and Heugung and Yohi remain missing after the destruction of Yohi's Western Yao Estate.",
    "Chief Jang and Chief Go are keeping the three Han Chinese reconnaissance-squad captives away from the Inner Palace.",
    "Song Ilseom and Hyuk Mujin remain bound and unconscious, while Ju Hwaran remains among the captives.",
    "The reconnaissance squad is traveling through Nanman while guarding against the Blood Monk.",
    "Jin remains committed to protecting his people despite Baeksang's coalition and execution order."
  ],
  "continuity_sources": [
    661,
    660
  ],
  "open_questions": [
    "What happened to Baekhwi at Great Snow Mountain, and who or what turned Baeksang into the man he is now?",
    "Why did the Southern Heaven Demon Empress order or permit Jin's execution to be delayed for two days?",
    "Can Jin survive the scheduled public execution?",
    "What role did Baeksang play in the attacks and the alleged collusion with Dark Heaven?",
    "Where are Heugung, Yohi, and Ju Hwaran being held, and what happened inside the Inner Palace?"
  ],
  "safe_through": 661,
  "temporary_decisions": [
    "Retain Force-Sealing Pill for 금력단 and iron balls for 철구.",
    "Use Chief Jang for 장 족장 and Chief Go for 고 족장.",
    "Use Baekhwi for 백휘.",
    "Use Great Snow Mountain for 대설산 and Southern Army for 남군.",
    "Retain practitioners of the Demonic Path for 마도."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 혁소평    | **Hyuk Sopyung**   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 백휘 | **Baekhwi** | Baeksang's deceased only child. |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 종남일룡 | **Zhongnan One Dragon** | Epithet of Hyuk Sopyung. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 섬서성 | **Shaanxi Province** | Source form specifying Shaanxi as a province. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 골골 | **Golgoli** | Jin's nickname for the Skeleton King. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 남군 | **Southern Army** | Army led by Baeksang and the Beast Miao King alongside the Zhongnan Sect. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 백휘 | father_to_deceased_child | Hwi | emotionally charged and possessive | Baeksang directly invokes his deceased child's name while confronting Jin. |

## Listed compact profiles

### Baekhwi.md

# Baekhwi (백휘)

- **Safe through:** Chapter 661
- **Aliases:** None
- **Role:** Baekhwi was Baeksang's only child and would have become the Beast Miao King's son-in-law if he had lived.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Baeksang's only child; would have been the Beast Miao King's son-in-law if he had lived.

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 661
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman; he has imprisoned Jin Taekyung and joined forces with twenty tribal chieftains to arrange Jin's execution at noon in two days.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi; he opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 661
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 661
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Sopyung.md

# Hyuk Sopyung (혁소평)

- **Safe through:** Chapter 326
- **Aliases:** Zhongnan One Dragon
- **Role:** Peak master of the Zhongnan Sect known as the Zhongnan One Dragon and a senior disciple who can command the Taeeul Sword Unit in Hwangbo Eom's presence.
- **Personality:** Proud, volatile, entitled, and quick to anger, especially when drunk.
- **Voice:** Loud, confrontational, insulting, and imperious.
- **Relationships:** Baek Museong knows him from several prior encounters; Baek says their elders' connection has been passed down to them.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 660
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 647
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

## Korean source

```text
＃662화



한 십 년쯤 됐나? 열심히 무협 소설을 보던 시절, 나는 어쩌다가 한 번씩 그런 생각을 했다.

아니, 어쩌면 꽤 자주.

‘내가 이 소설 속 주인공이라면 어떻게 할까.’

지금 생각해 보면 약간 쪽팔리긴 한데, 어쩔 수 없다. 이건 웹소설 좀 본 독자라면 기본으로 장착하고 있는 옵션 같은 거니까.

예를 들자면 어떤 멍청한 주인공이 시스템창을 쓰면서도 지력을 안 올린다던가. 혹은 여자 캐릭터만 나오면 못 볼 꼴을 보여 줄 때마다 그랬다.

만약에 나였으면, 으로 시작하는 상상.

그러나 막상 무림인이 되고 나니 상상은 상상이고, 현실은 현실이라는 걸 알게 됐다.

지금까지 읽었던 숱한 무협 명작들은 그저 끝내주게 나열된 활자들에 불과했고, 멋있다고 느꼈던 주인공들은 이 세상에 존재하지 않았다.



‘노야.’

‘왜.’

‘그, 천마(天魔)에 관해서 궁금한 게 있는데요. 혹시 성이 묵씨 아닙니까?’

‘……갑자기 뭔 개소리냐? 안 그래도 얼마 전에는 무당마검이니, 화산질풍검이니 하는 듣도 보도 못한 별호를 씨부리더니.’



처음에는 소설 속 주인공을 만나지 못한다는 사실에 아쉬웠지만, 그렇다고 실망스럽지는 않았다. 이 세상의 무림인들도 그들 못지않게 제법 멋있었거든.

하지만 내 환상을 철저하게 박살 낸 무언가가 있다면, 그건 바로…….

“그때의 우리는, 종남파와 함께 남군(南軍)을 이끌고 있었다.”

그래, 지금 막 백상의 입에서 흘러나온 저 세 글자다.

‘종남파(終南派).’

구파일방의 한 자리를 차지한 정파 무림의 거목. 장장 수백여 년간 명맥을 이어 오며, 영혼의 라이벌인 화산파와 함께 섬서성을 양분하는 명문대파.

아니, 이제는 ‘양분했던’이라고 해야겠다.

오랜 세월 모습을 드러내지 않았던 검성 매종학은 이제 무림 맹주가 되었고, 그가 늘그막에 들인 제자는 엄청난 명성을 얻었으며, 그에 따라 두 사람의 사문인 화산파의 영향력은 전과 비교할 수 없이 막대해졌으니까.

반면에 종남파는?

‘초절정 고수 셋 중 두 명이 드러누워서 골골거리는 중이지.’

노호검객(怒號劍客)은 적천강에게, 태을무정검(太乙無情劍)은 나한테 박살 났다.

그나마 나와 비슷한 연배의 후기지수인 종남일룡(綜南一龍) 혁소평은 그럭저럭 괜찮은 놈이었지만, 지금까지 종남파에 대한 이미지는 그리 좋지 못하다.

아니, 최소한 정파에 한해서만큼은 최악이다.

‘윗물이 저 지경이면 군림천하는 꿈도 못 꾸지.’

이쯤되면 좆남파. 혹은 종간나파라고 불러도 무방한 수준.

뭐, 현 장문인인 풍운검군은 다를 수도 있겠지만, 지금까지 무림에서 보고 들은 바에 의하면 종남파에 대한 내 개인적인 생각과 세간의 평가는 그리 큰 차이가 있는 것 같지는 않다.

‘그런데 이 시점에서 종남파라는 단어가 나왔다는 건…….’

감이 온다. 감이 와.

나도 모르게 눈살을 찌푸린 그때, 백상이 목소리가 이어졌다.

“종남파의 당대 장문인이었던 무상진인(無上眞人)은 의로우면서도 현명한 사람이었다. 어떤 상황에서도 침착하게 대처했고, 출신 성분에 상관없이 공정했지. 그렇기에 나와 궁주 역시 그가 남군(南軍)의 총대장이 되는 것에 찬성했다.”

“무상진인이라면…….”

“그래. 현 종남파 장문인인 풍운검군의 스승이다.”

적천강을 통해 몇 번 들었던 별호다.

물론 적천강이 종남파를 칭할 때 주로 쓰는 단어는 ‘버르장머리 없는 호로 새끼들’이었지만, 무상진인만큼은 ‘물렁하지만 훌륭한 사람’이라고 평가했을 정도다.

“문제는 감숙(甘肅) 땅에 접어든 직후에 벌어졌다. 정신없이 퇴각만을 거듭하던 인근의 패잔병들이 대설산(大雪山)에 결집한 것이지. 그 숫자가 물경 이천에 이르렀다.”

“……무슨 인근에 있던 패잔병이 이천 명이나 튀어나와?”

“십만마도(十萬魔徒)라는 말이 괜히 있었겠느냐? 비록 천마라는 구심점을 잃었으나 그들의 숫자는 무시할 수 있는 수준이 아니었다.”

“그래서. 대설산에서 전투가 벌어졌나?”

백상이 천천히 고개를 끄덕였다.

“충분히 승산 있는 싸움이었다. 당시 우리가 속해 있던 서군에는 초절정 고수인 무상진인과 이제 막 야수묘왕이라는 별호로 불리기 시작한 궁주가 있었고, 병력의 숫자와 질에서도 밀릴 것이 없었으니까. 아니, 오히려 훨씬 우세하다고 할 수 있었지.”

“그렇게 말하는 걸 보니 서군의 규모도 컸나 본데?”

“도합 사천여 명. 적들에게는 이렇다 할 초절정 고수도 없었으니, 우리로서는 피할 이유가 없는 전투였지.”

“음.”

적들에게는 없는 초절정 고수 둘. 게다가 두 배나 많은 병력. 반면 싸워야 하는 상대는 이미 피로와 절망감에 지쳐 있는 패잔병들.

누가 생각해도 이미 답이 나온 싸움이다.

하지만 그렇게 쉬운 싸움이었다면, 백상은 하나뿐인 아들을 잃지 않았을 거다.

“함정이 있었나?”

불쑥 던진 내 물음에, 백상이 모래알처럼 건조한 목소리로 대답했다.

“그래. 세 갈래로 나누어 대설산으로 쳐들어간 우리를 기다리고 있던 것은, 패잔병들이 아닌 마교의 정예 타격대였다.”

“……!”

“모든 것이 혼란의 연속이었지. 협곡 위에서는 화살이 비처럼 쏟아져 내렸고, 수백, 수천 근의 바위가 사람을 짓누르며 좁은 길을 가로막았다.”

“…….”

“그제야 함정이라는 걸 알았지만 모든 것이 늦어 버렸어. 정신없이 적들과 맞서 싸우다 문득 고개를 들어 보니, 언제나 곁에 머물러 있어야 할 사람이 없더군.”

이름은 말하지 않았지만 나는 직감적으로 알아차렸다.

지금 백상이 말하는 이가 야수묘왕이 아님을.

‘백휘.’

백상에게는 단 하나뿐인 자식이었고, 그의 모든 것을 물려줄 후계자였다.

대족장으로서의 모범을 보이기 위하여 어린 자식을 이끌고 함께 전장으로 향했지만, 아마 그는 자신의 목숨보다 더 아들을 아꼈을 것이다.

그런데 시체와 핏물로 점칠된 전장에서 훌륭하게 장성한 아들이, 마지막 전투에서 감쪽같이 사라진 것이다.

“나는 처음으로 두려워졌다. 휘, 그 아이는 내 전부였으니까. 아니, 그 이상이었으니까.”

이어지는 백상의 목소리는 공허했다.

“하지만 휘하 전사들을 위해서라도 평정심을 되찾아야 했다. 우선 얼마 떨어지지 않은 곳으로 진입했을 종남파와 또 다른 정파 무림인들에게 지원을 요청하고, 궁주를 도와 놈들과 맞서 싸웠지.”

예상치 못했던 기습. 치열했던 전투였으나 야수묘왕과 백상, 그리고 남만 전사들은 물러서지 않았다.

그들은 어느 때보다 격렬히 싸웠고, 마침내 숱한 희생을 남긴 채 승리할 수 있었다.

“협곡에서의 전투가 끝난 직후에야 알게 되었다. 그 아이가 수십의 전사들과 함께 적들 중 일부를 쫓아 샛길로 향했음을. 그리고 안심했지.”

말없이 이야기를 듣고 있던 내가 물었다.

“어째서?”

“샛길이 이어진 길은 분명 아군의 영역이었으니까. 앞서 내 지원 요청을 받은 이들이 휘, 그 아이를 구했을 것이라 믿었다.”

“…….”

나는 입을 다물었다. 사람을 무너트리는 것은 분노와 슬픔이 아니라 믿음이다.

그리고 그 믿음이 배신당했을 때, 사람은 비로소 절망하게 된다. 지금의 백상처럼.

“어떻게 되었을 것 같으냐?”

나는 대답하지 않았고, 아마 백상 역시 대답을 기대하지 않았을 것이다. 잠시 침묵하던 그는 천천히 말을 이었다.

“그 아이는…… 시신조차 남기지 못했다. 정체를 알 수 없는 적에 의해 난자당한 전사들의 시신만이 곳곳에 가득했지. 나중에야 그 흉수가 대설산을 주름잡던 마두인 대설귀(大雪鬼)라는 것을 알았다.”

“……!”

“지원군? 그런 것 따위는 없었다. 지원을 요청하기 위해 떠났던 전령은 다른 아군들에게 향하던 중 적들에 의해 목숨을 잃었다고 했고, 나는 슬픔과 절망에 빠져 아무것도 할 수 없었다. 그리고 나중에야 알게 되었지.”

그 순간. 백상의 전신이 파르르 떨렸다.

그리고 나는 볼 수 있었다. 언제나 차갑게 가라앉아 있던 그의 눈동자에 덧씌워진 어떤 감정을.

“전령을 죽인 것이 적이 아니라, 아군이었다는 것을.”

그건 분노였고, 증오였다.

“그들은 지원하지 못한 것이 아니라, 하지 않았다는 것을.”

또한 믿음을 배신당한 어느 한 사람의, 조용하고도 처절한 절규였다.

“그들이 왔다면 살 수 있었을 것이다. 하지만 그들은 오지 않았다. 전령을 죽여 내 간절한 요청을 묵살하고, 패퇴하는 적을 뒤쫓는 것을 택했다. 그 이유를 아느냐?”

고인 것은 때가 되면 흘러넘친다. 하지만 수십 년간 그렇게 비워 냈음에도, 백상의 마음에는 증오와 배신감이 끊임없이 차올랐고, 다시 한번 터져 나왔다.

지금 이 순간처럼.

“단지 새외(塞外)의 야만인에 불과한 자들이니까!”

“……!”

“자신들과 같은 한족이 아니고, 한족이 될 수도 없으며, 그런 야만인들을 위해 자신들을 희생할 수는 없으니까!”

쾅! 콰앙!

강대하면서도 거친 기파가 휘몰아친다.

단단하기 그지없는 암석으로 이루어진 바닥과 벽면이 바스라지고, 그의 주먹 끝에서 줄기줄기 흘러나온 유형화된 공력이 내 얼굴을 스쳤다.

피핏!

아릿하게 느껴지는 고통. 뜨거운 핏줄기가 이마를 타고 흐르는 것이 느껴졌다.

하지만 나는 미동도 하지 않은 채 그저 바라만 보았다.

살기로 번뜩이는 백상의 눈동자가 나를 향할 때까지.

“중원은, 한족은 우리를 배반했다. 우리는 놈들이 가장 절박할 때 기꺼이 손을 내밀었지만, 놈들은 십 년간 목숨 걸고 싸운 우리를 배신했어!”

수십여 년 전의 증오가 오롯이 나를 향한다.

나는 그제야 굳게 다물고 있던 입술을 뗐다.

“왜 무상진인에게 말하지 않았지? 그였다면 모든 것을 명백하게 밝혀 주었을 텐데.”

“무상진인?”

백상이 소리 내어 웃었다. 처음 보는 그의 웃음은 허탈했고, 웃음이라 부를 수도 없을 만큼 공허한 것이었다.

“그래, 그랬겠지. 만약 그가 살아 있었다면.”

“그 말은…….”

“그는 내상이 도진 상태에서 전투에 임하다 끝내 대설귀에게 죽었다. 분노한 종남파는 우리가 보낸 전령을 죽여 지원 요청을 묵살한 뒤 놈들을 추격했고, 이는 함께 서군에 배속되어 있던 수십여 개의 크고 작은 문파 역시 다르지 않았다.”

“뭐?”

“믿어지지 않느냐? 나도 그러했다. 유일하게 한 사람. 궁주만이 이 모든 일의 전위를 밝히고자 했지만, 모든 허울과 흠집은 정마대전의 종전과 함께 파묻혔다.”

“……!”

“그리고 우리를 제외한 모두가 승리와 평화에 젖어 있는 사이, 보관되어 있던 전령의 시신도 사라졌다. 종남파 무공의 흔적이 남아 있는 마지막 증거마저 없어진 거지.”

이런 미친 새끼들.

나는 침음성을 삼켰다.

나는 숨이 막혔다. 만약 백상의 말이 사실이라면…… 나를 비롯한 그 누구도 그의 분노를 비난할 수 없다.

‘목숨을 걸고 싸웠는데, 돌아온 것은 배신이었으니까.’

이 와중에도 가장 개 같은 사실은, 증거조차 남지 않은 이 과거의 일이 정말 사실이었을 것 같다는 직감 때문이었다.

‘빌어먹을.’

무림에 온 직후, 나도 한족이라는 울타리에 포함되어 있었기에 잘 안다.

중원인들이 이들을 어떤 시선으로 바라보는지.

또 사람의 감정과 탐욕이 얼마나 얄팍한 것인지.

백상은 아들이 사라졌음에도 승리를 위해 적들과 싸웠지만, 그가 믿고 있던 아군은 아니었다.

무상진인의 죽음에 분노한 종남파는 남만야수궁의 요청을 무시한 채 놈들을 추격했고, 서군에 속한 다른 문파는 병력 손실에 대한 두려움과 공적에 대한 욕심으로 눈이 멀었다.

그리고 그들이 행한 모든 것의 결과가, 바로 지금 내 눈앞에 서 있다.

“네놈이 앞서 말했었지. 이 땅이, 남만은 썩었다고.”

툭둑, 주르륵.

방금 전 있었던 일들의 여파로 갈라진 천장에서, 악취를 풍기는 물들이 쏟아져 내린다.

그 너머에서 백상의 눈동자가 차갑게 빛나고 있었다.

“그날, 너희가 알려 주었다. 내가 어떻게 해야 하는지.”
```

## Final English reading copy

```markdown
# Chapter 662

Was it about ten years ago? Back when I was still devouring martial-arts novels, I would occasionally find myself thinking about something.

No—maybe I thought about it fairly often.

*What would I do if I were the protagonist of this novel?*

Looking back, it was a little embarrassing, but I couldn’t help it. For anyone who had read web novels, that was practically a standard feature.

It happened whenever some idiot protagonist used a System window without raising his Intelligence. Or whenever a female character appeared and he made a complete fool of himself.

*If it were me…*

That was how the fantasies always began.

But after actually becoming a martial artist in the Murim, I learned that fantasies were fantasies, and reality was reality.

The many masterpieces of martial fiction I had read were nothing more than brilliantly arranged letters on a page, and the protagonists I had thought were so cool did not exist in this world.



*Old Master.*

*What.*

*There’s something I’m curious about regarding the Heavenly Demon. By any chance, isn’t his surname Muk?*

*…What the hell are you talking about all of a sudden? Not long ago, you were spouting off about things like the Wudang Demon Sword and the Huashan Gale Sword—titles I’ve never heard of in my life.*



At first, I was sorry I’d never get to meet the protagonists from those novels, but I wasn’t disappointed. The martial artists of this world were every bit as cool as those characters.

However, if there was one thing that had thoroughly shattered my fantasies, it was…

“We were leading the Southern Army alongside the Zhongnan Sect at the time.”

That was right. Those three words that had just slipped from Baeksang’s mouth.

*The Zhongnan Sect.*

A towering pillar of the orthodox Murim, one of the Nine Sects and One Gang. A prestigious great sect that had carried on its legacy for hundreds of years and divided Shaanxi Province between itself and its eternal rival, Huashan.

No—by now, I should probably say they *had* divided it.

The Sword Saint, Mae Jonghak, who had remained hidden from the world for so many years, was now the Alliance Leader. The Disciple he had taken in during his later years had gained tremendous fame, and as a result, the influence of their sect, Huashan, had grown to an extent that could not be compared to the past.

What about the Zhongnan Sect?

*Two of its three Supreme Peak masters are laid up and wheezing.*

The Roaring Fury Swordsman had been crushed by Jeok Cheongang, while the Taeeul Merciless Sword had been crushed by me.

At least Hyuk Sopyung, the young prodigy around my age known as the Zhongnan One Dragon, was a fairly decent guy. But so far, my impression of the Zhongnan Sect had been anything but good.

No. At least among the orthodox factions, it was the worst.

*If the upper reaches are that rotten, they can forget about ruling the world.*

At this point, calling it the *Fucknam Sect*—or the *Zhong-fucking-na Sect*—would hardly be an exaggeration.

Well, the current Sect Leader, the Wind-and-Cloud Sword Lord, might be different. But from everything I had seen and heard in the Murim so far, my personal opinion of the Zhongnan Sect did not seem to be all that different from the general public’s.

*But if the word Zhongnan came up at this point…*

I could feel it. I could feel something coming.

Just as I unconsciously furrowed my brow, Baeksang continued speaking.

“The Sect Leader of the Zhongnan Sect at the time, Venerable Wusang, was a righteous and wise man. He remained calm in every situation and treated people fairly regardless of their background. That was why the Palace Lord and I agreed that he should become the commander-in-chief of the Southern Army.”

“Venerable Wusang…”

“That’s right. He was the master of the current Sect Leader of the Zhongnan Sect, the Wind-and-Cloud Sword Lord.”

It was a title I had heard several times from Jeok Cheongang.

Of course, when Jeok Cheongang referred to the Zhongnan Sect, he usually called them “a bunch of rude, worthless bastards.” But even he had described Venerable Wusang as “soft, but a fine man.”

“The problem occurred right after we entered Gansu. The defeated soldiers from the surrounding areas, who had been retreating in a daze, gathered at Great Snow Mountain. There were no fewer than two thousand of them.”

“…How did two thousand defeated soldiers from the surrounding area suddenly appear?”

“Do you think the phrase ‘a hundred thousand practitioners of the Demonic Path’ existed for no reason? Even though they had lost their central figure, the Heavenly Demon, their numbers were not something that could be ignored.”

“So what happened? Was there a battle at Great Snow Mountain?”

Baeksang slowly nodded.

“It was a battle we had every reason to win. At the time, the Western Army we belonged to had Venerable Wusang, a Supreme Peak master, as well as the Palace Lord, who had only just begun to be called the Beast Miao King. We were not inferior in either the number or the quality of our troops. If anything, we had a considerable advantage.”

“From the way you’re talking, the Western Army must have been pretty large.”

“More than four thousand in total. The enemy did not have any notable Supreme Peak masters, either, so there was no reason for us to avoid the battle.”

“Hmm.”

Two Supreme Peak masters the enemy did not possess. Twice as many soldiers. And the enemy they had to fight consisted of defeated soldiers already worn down by exhaustion and despair.

Anyone could see that the outcome of the battle had already been decided.

But if it had been such an easy fight, Baeksang would not have lost his only son.

“There was a trap?”

At my sudden question, Baeksang answered in a voice as dry as sand.

“Yes. We divided our forces into three groups and advanced into Great Snow Mountain. What awaited us there was not a group of defeated soldiers, but an elite strike force of the Demonic Cult.”

“…”

“It was chaos from beginning to end. Arrows poured down like rain from above the gorge, while rocks weighing hundreds or thousands of geun crushed people and blocked the narrow paths.”

“…”

“By the time we realized it was a trap, everything was already too late. We fought the enemy in a frenzy, and then, at some point, I looked up and realized that the person who should always have been beside me was gone.”

He did not say the name, but I immediately understood.

The person Baeksang was talking about was not the Beast Miao King.

*Baekhwi.*

Baeksang’s only child, and the heir who was meant to inherit everything from him.

To set an example as a great chieftain, he had taken his young child with him to the battlefield. But he had probably cherished his son more than his own life.

And then, on a battlefield painted with corpses and blood, the fine young man he had raised had vanished without a trace during the final battle.

“I was afraid for the first time. Hwi. That child was my entire world. No—he was more than that.”

Baeksang’s voice was hollow as he continued.

“But I had to regain my composure, if only for the warriors under my command. First, I requested support from the Zhongnan Sect and the other orthodox martial artists who had entered the area not far away. Then I helped the Palace Lord fight the enemy.”

It had been an unexpected ambush. The battle had been fierce, but the Beast Miao King, Baeksang, and the Nanman warriors had not retreated.

They fought more violently than ever, and at last, after suffering countless casualties, they achieved victory.

“It was only after the battle in the gorge ended that I learned what had happened. That child had gone down a side path with dozens of warriors, pursuing some of the enemy. And I felt relieved.”

I had been listening in silence when I asked,

“Why?”

“The path connected to territory that definitely belonged to our allies. I believed that the people who had received my request for support would have saved Hwi—that child.”

“…”

I closed my mouth.

It was not anger or sorrow that destroyed a person. It was belief.

And when that belief was betrayed, a person finally fell into despair.

Just like Baeksang now.

“What do you think happened?”

I did not answer, and Baeksang probably had not expected me to. After a brief silence, he slowly continued.

“That child… did not even leave a corpse behind. The bodies of the warriors who had been hacked apart by an unidentified enemy were scattered everywhere. Only later did I learn that the culprit was the fiend who ruled Great Snow Mountain—the Great Snow Fiend.”

“…”

“Reinforcements? There were no such things. They said the messenger who had set out to request support had been killed by the enemy while on his way to the other allied forces. I was overwhelmed by grief and despair, unable to do anything. And it was only later that I learned the truth.”

At that moment, Baeksang’s entire body trembled.

And I saw it.

An emotion had been layered over his eyes, which were always cold and subdued.

“The ones who killed the messenger were not the enemy. They were our allies.”

It was anger.

Hatred.

“They had not been unable to provide support. They had simply chosen not to.”

It was also the quiet, desperate scream of a man whose faith had been betrayed.

“If they had come, he could have lived. But they did not come. They killed the messenger, ignored my desperate request, and chose to pursue the retreating enemy instead. Do you know why?”

Anything that pools will overflow when the time comes.

Though Baeksang had spent decades emptying it out, hatred and a sense of betrayal had kept welling up in his heart until they burst forth once again.

Just as they did now.

“Because we were nothing more than savages from the Outer Lands!”

“…”

“Because we weren’t Han Chinese like them, could never become Han Chinese, and they couldn’t sacrifice themselves for savages like us!”

Boom! Crash!

A powerful, violent wave of energy whipped through the underground prison.

The floor and walls, made from solid rock, crumbled. Streams of tangible internal energy poured from his fist and grazed my face.

Sssht!

A sharp, stinging pain.

I felt hot blood run down my forehead.

But I did not move. I merely stared at him.

Until Baeksang’s eyes, flashing with killing intent, turned toward me.

“The Central Plains—the Han Chinese—betrayed us. We willingly reached out our hands when they were at their most desperate, but they betrayed us after we fought with our lives on the line for ten years!”

The hatred of decades ago was directed entirely at me.

Only then did I part my tightly closed lips.

“Why didn’t you tell Venerable Wusang? If it had been him, he would have brought everything to light.”

“Venerable Wusang?”

Baeksang laughed aloud.

The first laugh I had ever heard from him was hollow. It was so empty that it could hardly be called laughter.

“Yes. He would have. If he had been alive.”

“That means…”

“He entered the battle while suffering from a recurrence of his Internal Injury, and the Great Snow Fiend eventually killed him. The Zhongnan Sect, enraged by his death, pursued the enemy after killing the messenger we had sent and ignoring our request for support. The dozens of large and small sects that had been assigned to the Western Army alongside us were no different.”

“What?”

“You don’t believe it? Neither did I. There was only one person—the Palace Lord—who tried to uncover the truth behind everything that had happened. But every false front and every stain was buried when the Great Faction War ended.”

“…”

“And while everyone except us was basking in victory and peace, the messenger’s corpse, which had been kept in storage, also disappeared. Even the last evidence bearing traces of the Zhongnan Sect’s martial arts was gone.”

*These fucking lunatics.*

I swallowed a groan.

I felt suffocated.

If Baeksang’s words were true, then no one—not even me—could condemn his anger.

*He had fought with his life on the line, and all he received in return was betrayal.*

The most fucked-up part of all this was the instinctive certainty that this long-ago incident, which had left behind not even a shred of evidence, had probably really happened.

*Damn it.*

After coming to the Murim, I had been included within the boundaries of the Han Chinese myself, so I knew.

I knew how the people of the Central Plains looked at them.

And I knew how shallow human emotions and greed could be.

Baeksang had fought the enemy for the sake of victory even after his son disappeared.

But the allies he trusted had not.

The Zhongnan Sect, enraged by Venerable Wusang’s death, had ignored the Nanman Beast Palace’s request and pursued the enemy. The other sects belonging to the Western Army had been blinded by their fear of losing troops and their greed for military credit.

And the result of everything they had done was standing before my eyes right now.

“You said earlier that this land—Nanman—was rotten.”

Drip. Trickle.

In the aftermath of what had just happened, foul-smelling water poured from the cracked ceiling.

Beyond it, Baeksang’s eyes gleamed coldly.

“That day, you people showed me what I had to do.”
```
