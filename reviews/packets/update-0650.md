<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0650.txt",
      "sha256": "ee4ab8c14cb9445b87b20a08a4d812ed28e615f69e0e5380fd4fd311666bbf16",
      "bytes": 13560
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "76aa94005da7a6b41623b6fdeb155c236270bb56b4b7eab4f3b7bf3741935244",
      "bytes": 984
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c60d77664c271582e2323ff18e216f423a3d9b066bfd2d0518707c75257990ed",
      "bytes": 199345
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "6a6416a8424ae0bda9443fe52b8095ac19659290823f56ebd0d7f7060cc7c68e",
      "bytes": 794
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "d51c23e053f0412b4d4ee453f9d68ef7509cd990b23f7118210a457e6d4bb4e0",
      "bytes": 766
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "537b82f8b3cf95fa4ed0772684828b495d4f0ee6b157291fcaa158dee682c1fd",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "7818b2eb3a3749ba46106a43dc7f9066935c0689cb6c06f6372740de859244ad",
      "bytes": 623
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "144d56d4a31c75bc52706eca5deb9d391bb49d52fc19d2bdce215774771e5b98",
      "bytes": 1702
    },
    {
      "path": "characters/Namho.md",
      "sha256": "6386252b467e519765c299a15491ed39646c56a1a67a95e7ebcc3a59f1e944c5",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "8623e422b76cd8034e508ba81223d0190e8ec93d4e164aa9c368a2dbff0f36fd",
      "bytes": 899
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "6a2ce2311ff87905599a6f21774a0c99cb3d30489fbb65af28c89d6ac82c76d7",
      "bytes": 528
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "89468adfe6497a221776a2100068b5af5658d8b1d35a79835dff4ee834652bf7",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9cb7b38a9267df33306a107efe9aed44b4b9c4dd9e73e30b113adbe177e2e439",
      "bytes": 205447
    }
  ],
  "estimated_tokens": 11476
}
-->

# Durable State Update — Chapter 650

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 650. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 650. Profile updates may replace only one
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
  "chapter": 650,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 650,
    "continuity_sources": [650],
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
    "Jin Taekyung is staying in the Nanman Beast Palace’s Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of a Murim Alliance pavilion.",
    "An unidentified assailant fired an arrow through the latrine door at Jin Taekyung.",
    "The arrow carried a rolled leather message reading “Today. Insi. West Gate.”",
    "Jin can store and retrieve physical objects through the System’s Inventory.",
    "The message appears to be an invitation from an unidentified sender."
  ],
  "continuity_sources": [
    649
  ],
  "open_questions": [
    "Who fired the arrow and sent the leather message?",
    "Was the arrow intended as an attack, an invitation, or both?",
    "What awaits Jin at the West Gate during Insi?"
  ],
  "safe_through": 649,
  "temporary_decisions": [
    "Use Insi for 인시.",
    "Use West Gate for 서문.",
    "Use Pavilion Master for 각주.",
    "Use missive for 전서."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 대사      | **Master** for a senior Buddhist monk                           |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 대장군 | **Great General** | Military title used for the official who claimed credit after the Demonic Cult withdrew. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 이족 | **Yi people** | One of Nanman's four great tribes. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 649
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and may resent the orthodox Murim over the loss of his only child or be secretly aligned with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 648
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 648
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 648
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung is foolish, easily flattered, and politically dependent on stronger personalities despite leading a powerful tribe.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Yohi and Baeksang keep Heugung under their control, while Heugung responds to Yohi's manipulation with apparent infatuation.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 647
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 649
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 649
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 649
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 648
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃650화



그날 부족 대회의와 함께 내궁에서 열린 연회는, 축시(丑時) 무렵이 다 되어서야 파장 분위기에 접어들었다.

나로서는 매우 안도할 만한 일이었다.

그렇지 않았다면 사방에서 느껴지는 시선과 수군거림을 밤새 들어야 했을 테니까.

“저 한족 친구 말인데, 아랫도리를 벗은 채로 전각 위에 올라가 있었다면서?”

“예? 그게 무슨 소립니까?”

“내 처조카가 내궁 경비 소속이잖나. 한 시진 전에 잠깐 비상이 걸린 게 저 친구 때문이었다는군.”

“그러고 보니 호각소리를 듣긴 했는데…… 아니, 그보다 한 시진 전이라면 소피 보러 간다고 사라진 것 아니었습니까?”

“소피 보러 간 게 아니라 다른 걸 보여 주고 싶었나 보지. 사람 취향이라는 게 그렇잖나. 뭐 중원의 풍습일 수도 있고.”

“저런. 중원에 그토록 미개한 풍습이 있었다니.”

“미개하기 짝이 없지. 하지만 그것과는 별개로 대단한 것 같긴 해.”

“뭐가 말입니까?”

“그, 왜. 있잖나.”

“아…….”

“처조카 말로는 무기를 들고 있는 줄 알고 공격할 뻔했다더군. 횃불로 비춰 보기 전까지는 그게 창인 줄 알았다던데.”

“예? 아무리 그래도 창과 헷갈리다니. 그게 말이 됩니까?”

“어허. 이 사람. 별호에 괜히 용이 붙었겠나? 역시는 역시인 거지.”

“허어어어어!”

띠링.



- 당신에 관한 소문이 일파만파 퍼져나갑니다!

- 상당수의 유력 인사들이 소문에 반응합니다!

- 명성치가 소량 상승했습니다!

- 명성치가 소량 상승했습니다!



“…….”

제발 그만해. 그리고 명성치는 왜 또 오르는 건데.

‘인생 씨바 거…….’

나는 주위에서 들려오는 수군거림을 애써 무시하며 얼마 남지 않은 술잔을 기울였다. 그런 내 모습에 야수묘왕이 껄껄 웃으며 어깨를 두드렸다.

“너무 개의치 말게. 사내가 살다 보면 그럴 수도 있지 뭘.”

“아니, 그렇게 말씀하시면 진짜 일부러 그런 것 같지 않습니까. 그냥 실수였다니까요. 워낙 급하게 나오느라 바지춤을 고정하는 걸 깜빡…….”

“응? 급하게 나올 일이 뭐가 있다고.”

“아, 그게.”

젠장. 말이 실수로 헛나왔네. 정체불명의 인물이 보낸 전서(傳書)에 관한 사실은 아직 야수묘왕에게도 알리지 않은 상태다.

잠시 침묵하던 나는 자포자기한 마음으로 입을 열었다.

“사실 일부러 한 거 맞습니다.”

“저런.”

“어릴 때부터 그랬어요. 지금도 종종 합니다.”

“어이구.”

“취미고 특기입니다. 제가 창 한 자루만 쓰시는 줄 알죠? 사실 두 자룹니다.”

“허어어.”

만약 내가 남만에서 죽는다면, 어떤 방식으로 죽건 간에 사인은 무조건 수치사다.

하지만 지금은 어쩔 수 없었다. 상대가 이런 방식으로 비밀리에 접선했다는 것은, 다른 이들에게는 알리지 말아야 한다는 뜻도 포함되어 있으니까.

‘최소한 남만야수궁 내의 그 누구도 알아서는 안 된다는 뜻이겠지.’

나는 분명 야수묘왕을 신뢰하고 있지만, 무림만큼 신뢰와 믿음이라는 단어가 싸구려 취급받는 곳도 없다.

무슨 일이 벌어질지는 아무도 모르니까.

그리고 이런 결정을 내린 데에는 야수묘왕이 이 사실을 알게 되면 다른 누군가가 눈치를 챌지도 모른다는 생각도 한몫했다.

예를 들자면…….

‘저 인간이라든지.’

나는 무감정한 눈동자로 이곳을 응시하고 있던 백상과 눈이 마주쳤다. 보면 볼수록 도무지 생각을 읽을 수 없는 눈빛이다.

연회가 진행되는 내내 술과 음식에는 손 하나 까딱하지 않고 앉아 있던 그는, 나와 눈이 마주치자 새하얀 옷자락을 정돈하며 자리에서 일어나 입을 열었다.

“궁주, 이미 밤이 깊었습니다. 이쯤에서 파하시지요.”

“흠. 그러지.”

야수묘왕은 별다른 고민 없이 고개를 끄덕였다.

내일도 대회의가 이어진다는 점을 생각하면 당연한 일이었다.

물론 다들 무공을 익힌 절정 고수인 만큼 숙취는 없겠지만, 과한 분위기 속에서 마시는 술은 정신을 흐트러트리기 마련이다.

툭. 투둑.

손가락 끝으로 주독(酒毒)을 배출해 낸 야수묘왕이 멀쩡해진 얼굴로 연회의 끝을 알리자, 곳곳에서 아쉬움이 섞인 목소리들이 흘러나온다.

‘일단 저 사람들은 아니겠네. 곧 약속했던 시각이 다가오는데 연회가 끝나는 걸 아쉬워하는 걸 보면.’

아쉬워하는 이들의 면면을 빠르게 확인한 나는 야수묘왕을 향해 말을 건넸다.

“야율 대협, 저도 이제 들어가 봐야 할 것 같습니다.”

“물론 그래야지. 한데 이번에는 어느 전각으로 갈 생각이냐?”

“…….”

거, 진짜.

내 표정을 본 야수묘왕은 무릎을 두드리며 웃었고, 한숨을 내쉰 나는 남호를 비롯한 사파 잡졸들과 함께 자리를 떴다.

어느새 밤은 깊었고, 시간은 인시(寅時)에 접어들고 있었다.

이제 전서의 주인을 만날 시간이다.



* * *



“혼자 가도 괜찮겠느냐? 함정일 수도 있다.”

화룡각에게 배정된 처소로 향하는 길. 나는 걱정스러운 눈빛을 보내는 남호를 안심시켰다.

“괜찮습니다. 그리고 어차피 남 노인은 같이 가 봤자 짐만 돼요.”

“…….”

“설마 따라오실 생각이었습니까?”

“이 정도면 제법 오래 살긴 했지만, 개죽음 당하긴 싫다.”

“그럼 처소에 계세요. 다른 짐덩이 둘이랑 같이.”

태산은 언제나처럼 별생각이 없었고, 사마표는 나름 사파 제일의 후기지수인 자신이 짐덩이 취급받는다는 것에 약간의 불만을 표했지만 내 한마디를 듣고 입을 다물었다.

“아. 억울하면 초절정 찍든가.”

“……”

“난 어떻게든 살아남을 수 있지만, 너희는 아니지. 돌아올 때까지 처소 주변이나 잘 경계하고 있어. 그사이에 검이라도 한 번 더 휘두르고.”

우리는 아무 일도 없는 것처럼 함께 처소로 들어갔고, 나는 일각을 기다린 뒤 은밀하게 빠져나와 곧장 어둠 속으로 녹아들었다.

‘인시 무렵. 서문이라고 했지.’

화살에 매달려 있던 전서의 내용이 함정인지, 제보를 위한 접선인지는 잘 모르겠다. 그저 직접 가 보는 수밖에.

쉬쉬쉭!

순찰을 돌고 있는 전사들의 이목을 속이며 이동하길 얼마나 되었을까.

저 멀리에서 메아리처럼 들려오던 환호와 온갖 소음이 가까워졌다.

쉬이이익! 퍼벙!

- 와아아아!

내궁에서 벌어진 연회는 이미 끝났지만, 외궁의 밤은 지금까지도 계속해서 이어지고 있었다. 비단 오늘뿐만이 아니라 내일도, 모레도 마찬가지일 것이다.

대회의에 참석하는 부족장도, 경계를 서는 전사들도 아닌 평범한 부족민들은 축제 분위기에 흠뻑 젖어 있었다.

‘이래서 외궁 쪽으로 장소를 정한 거군. 일 년 중 어느 때보다 사람이 많을 시기니까.’

내심 중얼거린 나는 자연스럽게 사람들 사이로 녹아들었다.

거리는 분위기에 알맞게 동물 가면을 쓴 이들로 인산인해였고, 지난번에도 사용했던 호랑이 가면을 착용한 나를 의심하는 사람은 아무도 없었다.

‘서문이면…… 저쪽인가?’

외궁은 축제 분위기로 한창이었지만, 그렇다고 해서 경계가 흐트러진 것은 아니었다.

곳곳에 배치된 전사들의 눈을 속이며 이동한 나는 얼마 지나지 않아 서문에 도착할 수 있었다.

사실 조금 더 정확히 말하자면, 역시 사람들이 우글거리는 서문 언저리 어딘가다.

‘일단 전서에 적힌 그대로 오긴 왔는데…….’

주위에 사람이 너무 많을뿐더러, 서문 근처라 그런지 배치된 전사들의 머릿수도 적지 않다.

이런 상황에서 천하대장군마냥 우뚝 서 있기만 하면 눈에 띌 것이 뻔했다.

‘이다음에는 어떻게 되는 거지?’

의문을 느낀 내가 주변을 둘러보던 그때였다.

“거기, 호랑이 가면 쓴 형씨. 할 거 없으면 와서 소면이나 한 그릇 하고 가지?”

호랑이 가면이라는 말에 고개를 돌린 나는, 근처 좌판에 앉아 있던 중년인과 눈이 마주쳤다.

눈빛과 인상은 평범하고, 비쩍 마른 체형의 그는 내 시선에 씩 웃으며 자신의 앞에 놓인 그릇을 들어 보였다.

“내가 원래 모르는 사람한테 말 거는 성격은 아닌데, 여기 국물이 기가 막혀.”

“……음.”

글쎄. 기가 막힌 건 국물뿐만이 아닌 것 같은데.

찰나라고 부를 수 있을 만큼 짧은 순간, 말없이 중년인을 응시하던 나는 고개를 끄덕이며 그의 옆자리에 앉았다.

그리고 마침내 마주하게 된 뜻밖의 접선자를 향해 한 줄기의 전음(傳音)을 흘려보냈다.

- 참 희한하게도, 잠깐 사이에 살이 많이 빠지셨네. 연회장에서는 이것저것 많이 드시는 것 같던데.

“……!”

툭!

비쩍 마른 몸이 동요로 움찔. 떨리는 것이 느껴진다.

나는 몰라보게 달라진 그가 떨어트린 젓가락을 주워 주며 전음을 이었다.

- 그래서, 이족의 대족장씩이나 되시는 분께서 어쩐 일로?

귓가를 파고든 전음에, 흑웅(黑熊)의 눈동자가 크게 뜨였다.



* * *



단번에 정체를 알아차린 것이 충격이었는지 흑웅은 놀란 기색이 다분했지만, 나 역시 그에 못지않게 놀랐다.

‘전서를 보낸 게 이 사람이라고?’

만난 시간도, 횟수도 적지만 흑웅이라는 사람에 대해서는 이미 나름대로 판단을 내렸다.

요희의 미모에 홀딱 반해서 간이고 쓸개고 내주는 한심한 인간. 줏대 없이 백상의 뜻에 따라 움직이는 허수아비.

그래서 더욱 놀라웠을지도 모른다.

지금 마주하는 그의 모습과 행동은 지금까지 내가 알고 있던 것과는 완전히 딴판이었고, 성지 순례를 가도 될 것 같던 풍만한 배둘레햄은 눈을 씻고도 찾아볼 수 없었으니까.

‘시스템이 아니었으면 꼼짝없이 속을 뻔했네.’

내심 혀를 내두른 나는 그의 손에 다시 젓가락을 쥐여 주었다. 주위의 이목을 신경 쓴 자연스러운 대사와 함께.

“이 양반 이거, 갑자기 젓가락은 왜 떨어트려? 아무리 몸에 힘이 없어도 그렇지.”

내 말에 정신을 차린 흑웅이 황급히 표정을 수습했다.

“아, 고맙소.”

하지만 그런 대화 속에서, 서로 간에 들리지 않는 전음이 오가고 있다는 것은 나와 흑웅만이 아는 사실이었다.

“어르신. 여기 소면 하나 주십시오.”

나는 주문과 함께 입술을 달싹였다.

- 화살에 묶여 있던 전서, 당신이 보낸 거 맞습니까?

허리 굽은 주인이 꿈쩍도 하지 않자 흑웅이 좌판을 쾅쾅 내리쳤다.

“주인장! 소면 하나!”

그러고는 나를 향해 씩 웃으며 말했다.

“이해하시오. 여기 주인장 연배가 구순이 넘어서 귀가 어둡거든.”

- ……맞네. 그나저나 축골공(縮骨功)으로 모습을 바꾸었는데. 어떻게 한눈에 알아봤지?

아하, 축골공.

흑웅의 깜짝 변신에 대한 의문이 하나 풀린다.

과거 적천강이 말해 준 바에 의하면 축골공은 뼈와 살을 고무줄처럼 늘이고 줄일 수 있는 무공인데, 익히는 과정이 까다롭고 고통스러운 탓에 중원에서는 익히는 이가 거의 없다고 했다.

‘하지만 그렇다고 한들 남만에서도 흔한 무공은 아닐 텐데.’

아직 해결되지 않은 의문이 많다. 나는 소면이 나오는 것을 기다리며 중얼거렸다.

“따끈한 국물이 좀 땡기긴 했는데, 잘됐네.”

- 알아본 건 중요한 게 아니니까 넘어가고. 그런 전서를 보낸 이유는?

흑웅이 젓가락을 챙겨 주며 대답했다.

“다른 건 몰라도 국물 하나는 죽여주지. 나이만큼이나 장사한 지 오래됐거든.”

- 반드시 알려야 하는 정보가 있었네.

“아, 그래요? 그럼 기대해 볼 만하지.”

- 죽이려고 한 겁니까, 아니면 알리려고 한 겁니까? 하마터면 머리통에 화살 구멍 날 뻔했는데.

- 자네라면 피할 거라고 생각했네. 백상 대족장도 자네에게 낭패를 면하지 못했는데, 화살 하나 피하지 못하겠나.

“…….”

그거 때문에 노출신룡이 된 건 아는지 모르겠다.

이참에 흑웅의 머리통을 한 대 때려 줄까 고민하던 나는, 관대한 마음으로 참아내며 물었다.

- 그래서. 그 반드시 알려야 하는 정보가 뭡니까?

김이 모락모락 피어오르는 그릇을 빤히 바라보던 흑웅이 힘겹게 입술을 달싹였다.

- 백상 대족장이…… 암천과 결탁했네.

“……!”

우둑.

순간 나도 모르게 힘이 들어간 손아귀에서, 젓가락이 힘없이 부러졌다.
```

## Final English reading copy

```markdown
# Chapter 650

The banquet held in the Inner Palace alongside the Tribal Grand Council that day didn’t start winding down until around the Ox hour.

For me, that was a great relief.

Otherwise, I would have had to listen to the whispers and feel the stares coming from every direction all night.

“That Han Chinese fellow—wasn’t he up on top of a pavilion with his pants off?”

“What? What are you talking about?”

“My wife’s sibling’s kid is with the Inner Palace guard, you know. Apparently, the brief alert one shichen ago was because of that fellow.”

“Now that you mention it, I did hear a whistle… But if it was one shichen ago, wasn’t that when he disappeared to go take a leak?”

“Maybe he didn’t go take a leak. Maybe he wanted to show everyone something else. People have all kinds of tastes, you know. Could be a Central Plains custom.”

“Good heavens. I had no idea the Central Plains had such a barbaric custom.”

“Barbaric as it gets. But separate from that, he does seem pretty impressive.”

“What does?”

“You know. That thing.”

“Ah…”

“According to the kid, they nearly attacked him because they thought he was holding a weapon. Until they shone a torch on him, they thought it was a spear.”

“What? Even so, how could she mistake it for a spear? Is that even possible?”

“Now, now. Do you think the word ‘dragon’ was added to his sobriquet for no reason? A dragon is a dragon.”

“Whaaaaaaaaaat!”

> **System**
>
> - Rumors about you are spreading far and wide!
>
> - A considerable number of influential figures are reacting to the rumors!
>
> - Fame has increased slightly!
>
> - Fame has increased slightly!

“…”

Please stop. And why does my Fame keep rising?

*My fucking life…*

I did my best to ignore the whispers around me as I tipped back the last of my drink. Seeing me like that, the Beast Miao King laughed heartily and patted me on the shoulder.

“Don’t take it too much to heart. Things like that happen to a man every now and then.”

“No, when you put it that way, it sounds like I did it on purpose. It was really just an accident. I was in such a hurry to get out that I forgot to fasten my trousers…”

“Hm? What was there to hurry out for?”

“Ah, well…”

Damn it. That had slipped out by accident.

I still hadn’t told even the Beast Miao King about the missive sent by the unidentified figure.

After a brief silence, I spoke with the abandon of a man who had given up.

“Actually, I did do it on purpose.”

“Oh my.”

“I’ve been like that since I was young. I still do it from time to time.”

“Good grief.”

“It’s both a hobby and a special talent. You thought I only used one spear, didn’t you? I actually use two.”

“Whaaaaaat…”

If I died in Nanman, no matter how I died, the cause of death would definitely be humiliation.

But there was nothing I could do about it now. The fact that the other party had made secret contact in this manner also meant that I wasn’t supposed to tell anyone else.

*At the very least, it means no one in the Nanman Beast Palace can know.*

I certainly trusted the Beast Miao King, but there was no place where the words *trust* and *faith* were treated more cheaply than the Murim.

No one knew what might happen.

Another reason I had made this decision was that if the Beast Miao King found out, someone else might notice something was wrong.

For example…

*That man.*

My eyes met Baeksang’s as he stared this way with emotionless eyes. The longer I looked at him, the less I could understand what was going on behind those eyes.

He had spent the entire banquet sitting without lifting a finger to touch the food or alcohol. Now, after meeting my gaze, he smoothed his immaculate white robes, rose from his seat, and spoke.

“Palace Lord, it is already late. We should end the banquet here.”

“Hm. Let us do so.”

The Beast Miao King nodded without much hesitation.

Considering that the Tribal Grand Council would continue tomorrow, it was only natural.

Of course, since everyone present was a Peak master who practiced martial arts, none of them would suffer from a hangover. Even so, drinking in an atmosphere like this was bound to dull the mind.

Pop. Pop.

The Beast Miao King expelled the alcohol from his body through his fingertips. His face instantly returned to normal, and when he announced the end of the banquet, disappointed voices rose from every corner.

*It isn’t any of them, at least. If they’re disappointed that the banquet is ending when the promised time is almost here, they can’t be the ones involved.*

After quickly checking the faces of those who looked disappointed, I spoke to the Beast Miao King.

“Sir Yayul, I should probably head in as well.”

“Of course. But which pavilion are you planning to go to this time?”

“…”

Seriously?

Seeing my expression, the Beast Miao King slapped his knee and laughed. I sighed and left with Namho and the other unorthodox faction underlings.

By then, the night had deepened, and the time had entered Insi.[^1]

It was time to meet the owner of the missive.

* * *

“Are you sure you’ll be all right going alone? It could be a trap.”

On the way to the quarters assigned to the Fire Dragon Pavilion, I reassured Namho, who was looking at me with concern.

“I’ll be fine. And Elder Nam, you’d only be a burden if you came along anyway.”

“…”

“Did you actually plan to follow me?”

“I’ve lived a fairly long life, but I have no desire to die like a stray dog.”

“Then stay in the quarters. Along with the other two deadweights.”

Taishan, as usual, didn’t give it much thought. Sama Pyo, who was arguably the greatest young prodigy of the unorthodox faction, showed some displeasure at being treated like a deadweight, but he shut his mouth after hearing my next words.

“Ah. If you’re upset, reach Supreme Peak.”

“…”

“I can somehow survive, but you two can’t. Keep watch around the quarters until I return. And swing your swords at least one more time while you’re at it.”

We entered the quarters together as if nothing had happened. After waiting for fifteen minutes, I slipped out in secret and melted into the darkness.

*Around Insi. It said the West Gate, right?*

I had no idea whether the contents of the missive tied to the arrow were a trap or an attempt to make contact in order to share information.

There was nothing to do but go and find out.

Whoosh—whoosh!

I moved while evading the notice of the warriors on patrol. After some time, the cheers and assorted noises echoing in the distance began to grow closer.

Shiiiiing! Boom!

“Waaaaaaah!”

The banquet in the Inner Palace had already ended, but the night in the Outer Palace was still going strong. And it wouldn’t end tonight. The same would be true tomorrow and the day after.

The ordinary tribespeople—neither the chieftains attending the Tribal Grand Council nor the warriors standing guard—were completely immersed in the festival atmosphere.

*So that’s why he chose the Outer Palace. There will be more people here than at any other time of year.*

I murmured inwardly and naturally melted into the crowd.

The streets were packed with people wearing animal masks to match the festive mood, and no one suspected me as I wore the tiger mask I had used last time.

*If he said the West Gate… would it be over there?*

The Outer Palace was in the middle of a festival, but that didn’t mean the guards had let their vigilance slip.

Evading the eyes of the warriors stationed throughout the area, I reached the West Gate before long.

To be more precise, I reached somewhere around the West Gate, which was just as crowded with people as everywhere else.

*I came here exactly as the missive instructed, but…*

There were too many people around me. And since this was near the West Gate, there were plenty of warriors stationed nearby as well.

If I simply stood there like some Great General, I was bound to attract attention.

*What happens next?*

Just as I began looking around in puzzlement, someone called out to me.

“Hey, tiger-mask fellow. If you’ve got nothing better to do, come have a bowl of somyeon before you go.”

At the mention of the tiger mask, I turned my head and met the eyes of a middle-aged man sitting at a nearby food stall.

His eyes and features were ordinary, and his body was painfully thin. He gave me a crooked grin and lifted the bowl in front of him.

“I’m not usually the type to talk to strangers, but the broth here is incredible.”

“…Hm.”

I wasn’t sure the broth was the only incredible thing here.

For a moment so brief it could hardly be called an instant, I silently stared at the middle-aged man. Then I nodded, sat down beside him, and finally sent a thread of Sound Transmission to the unexpected contact before me.

—Funny, you’ve lost quite a bit of weight in such a short time. You seemed to be eating quite a lot at the banquet.

“…”

Pop!

His scrawny body flinched in agitation. I could feel him trembling.

I picked up the chopsticks he had dropped and continued the Sound Transmission.

—So, what brings a great chieftain of the Yi people here?

The Sound Transmission pierced his ear, and Heugung’s eyes widened.

* * *

Perhaps the shock of having his identity recognized so quickly had left Heugung stunned, but I was just as surprised.

*The person who sent the missive was him?*

Although we had met only a few times and not for very long, I had already formed my own assessment of Heugung.

A pathetic man who had fallen head over heels for Yohi’s beauty and would give her his liver and gallbladder. A spineless puppet who moved according to Baeksang’s will.

That was probably why I was even more surprised.

The Heugung I was seeing now, in both appearance and behavior, was completely different from the man I had known. Not even after scrubbing my eyes could I find the enormous belly that looked fit for a pilgrimage to a holy site.

*If not for the System, I would have been completely fooled.*

I clicked my tongue inwardly and placed the chopsticks back in Heugung’s hand, speaking naturally to keep the attention of those around us away.

“What’s with you dropping your chopsticks all of a sudden? Even if you’re feeling weak, that’s no excuse.”

Heugung came to his senses and hurriedly composed his expression.

“Ah, thank you.”

But only Heugung and I knew that, beneath that ordinary conversation, Sound Transmissions were passing between us without anyone else hearing them.

“Master, one bowl of somyeon, please.”

I placed my order and moved my lips.

—You sent the missive tied to the arrow, didn’t you?

When the hunched old owner didn’t move at all, Heugung slammed his fist against the stall.

“Master! One bowl of somyeon!”

Then he gave me a grin and said,

“You’ll have to understand. The owner here is over ninety, so his hearing isn’t very good.”

—…That’s right. By the way, I changed my appearance using the Bone-Shrinking Technique. How did you recognize me at a glance?

Ah. The Bone-Shrinking Technique.

One of my questions about Heugung’s sudden transformation had been answered.

According to what Jeok Cheongang had told me in the past, the Bone-Shrinking Technique was a martial art that allowed its user to stretch and shrink bone and flesh like rubber bands. But because the process of learning it was difficult and painful, almost no one in the Central Plains practiced it.

*Even so, it can’t be a common martial art in Nanman either.*

There were still many questions left unanswered. As I waited for the somyeon to arrive, I spoke aloud.

“I was craving some hot broth anyway. This worked out nicely.”

—Whether I recognized you isn’t important, so let’s move on. Why did you send that missive?

As Heugung made sure I had chopsticks, he answered.

“The broth really is to die for. The owner has been running this stall almost as long as he’s been alive.”

—I had information I absolutely needed to tell you.

“Oh, really? Then I suppose I have something to look forward to.”

—Was it meant to kill me or tell me something? I nearly ended up with an arrow through my head.

—I thought you’d dodge it. Even Great Chieftain Baeksang suffered a setback at your hands. How could you fail to dodge a single arrow?

“…”

I wondered if he even knew that was how I had become the Naked Divine Dragon.

I considered smacking Heugung over the head, but held back out of sheer generosity and asked,

—So, what is this information you absolutely had to tell me?

Heugung stared at the steaming bowl in front of him and moved his lips with difficulty.

—Great Chieftain Baeksang… has colluded with Dark Heaven.

“…”

Crack.

The chopsticks snapped uselessly in my clenched hand.

[^1]: Insi is the traditional time period from three to five in the morning.
```
