<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0687.txt",
      "sha256": "28da594db039b842fdc5b99555934cec7d243bef3e3853113cdc0c3d32cf9d72",
      "bytes": 13262
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "25d9ba0fcab3ef6ddbf18902a670178ef8e59ecd9e3dd3540943b92a68db0a03",
      "bytes": 1684
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "cf9b125e6cbbf29df3c6313906f57c6008b807cf89d30117838b588e873a3043",
      "bytes": 204081
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "10130d7421dc2fcdf727d9cc9a75e3045358c93650deefd53fb2301f093049ad",
      "bytes": 980
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "8730659d14ceaa20a3b2e0ae222793c6ce267fb9b161820c56c07ee8c82c85ad",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7b810cdccdf23de957697544e1c519d9212bd325b303bdd944a0686317af5afa",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "af4c5f8682e553fbcb8f01bbfe33fe099b2eabb67cb9f5f808524724c26a8150",
      "bytes": 705
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8d372b38312fe9c008ec1b120b00dc2518ff77d65f2a18006ac4940b7057b4d3",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f5c0993827cdaaffa3a8c89f3dcb78f4b9364ea3615b710e00074c203806849c",
      "bytes": 622
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "93bb16b4b2b2f9c2808f7f2fa3b186a5713bd32520096a2f69c3de5f2a92ced1",
      "bytes": 564
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c732c6e0b915fb40ebc0712e4137a1d00d0de261ab8f5e3a98f70aa047ca1d3f",
      "bytes": 211718
    }
  ],
  "estimated_tokens": 11726
}
-->

# Durable State Update — Chapter 687

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 687. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 687. Profile updates may replace only one
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
  "chapter": 687,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 687,
    "continuity_sources": [687],
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
    "Jin is alive but unconscious after defeating two Supreme Peak masters and remains critically injured.",
    "Jin's Water God Dragon's Origin Essence remains associated with the danger of conflict against his Scorching Yang Qi.",
    "The Fire Dragon Armor is shattered around the chest and still requires repair.",
    "Yohi has resolved to expose Baeksang's conspiracy with Dark Heaven and oppose them despite the consequences.",
    "Yohi and Heugung are heading west to Boshan rather than entering the Inner Palace.",
    "Yohi plans to rally the Yao people and notify Nanman of Baeksang's atrocities within seven days.",
    "Heugung has acquired an antidote from the Black Hand Fist Demon's corpse.",
    "Muyaho had accepted Jin but was apparently struck at the chapter's end."
  ],
  "continuity_sources": [
    686
  ],
  "open_questions": [
    "What did Heugung's final attack hit, and what hidden identity or allegiance was he concealing?",
    "Did Muyaho survive the attack, and what is the condition of Jin, Yohi, and Heugung afterward?",
    "Has Baeksang already seized the Inner Palace with Dark Heaven's support?",
    "Will the Water God Dragon's Origin Essence save Jin or kill him because of its incompatibility with his Scorching Yang Qi?",
    "Can Yohi rally enough Nanman warriors to challenge Baeksang before the conspiracy consolidates?"
  ],
  "safe_through": 686,
  "temporary_decisions": [
    "Render 보산 as Boshan.",
    "Render 탈각 as molting.",
    "Render 대계 as the grand plan.",
    "Render 해약 as antidote.",
    "Render 수신룡의 원정 as Water God Dragon's Origin Essence."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 중원     | **Central Plains**                               |                                                       |
| 태원     | **Taiyuan**            |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 적통 | **orthodox lineage** | The legitimate succession of the Fire Gate Clan's tradition. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 이족 | **Yi people** | One of Nanman's four great tribes. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 축골공 | **Bone-Shrinking Technique** | A martial art that stretches and shrinks bone and flesh to alter the user's appearance. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 요서부 | **Western Yao Estate** | Estate inherited by Yohi when she became a Great Chieftain. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 보산 | **Boshan** | Western Yao stronghold where several thousand Yao people are settled. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 686
- **Aliases:** None
- **Role:** Baeksang is the temporary Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the leader of Nanman's general mobilization, with nearly ten thousand troops stationed in the Inner Palace.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 686
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 686
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 686
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; Black Hand captured him and Yohi, and by the end of Chapter 685 he has returned with Yohi on Muyaho to find Jin.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 686
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 686
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 686
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people and now intends to expose Baeksang and Dark Heaven while traveling west with Heugung and Jin Taekyung to rally Nanman from Boshan.

## Korean source

```text
＃687화



서걱, 쿵!

순간, 세상이 정지한 것 같았다.

- 크르륵.

썩은 통나무처럼 쓰러져 숨을 헐떡이는 거대한 백호와 완전히 의식을 잃은 진태경.

그리고 그런 그를 품에 안고 담담하게 말을 이어 가는 한 사람의 모습이 요희의 눈동자에 비쳤다.

“말하지 않았소. 나 자신부터 숨겼어야 했다고.”

“……!”

섬전처럼 뇌리를 스치는 깨달음과 경악.

언제나 그윽한 빛을 띠고 있던 요희의 눈동자가 부릅떠졌다.

“흑웅, 당신!”

“이제는 오라버니라고 부르지 않는구려. 그래도 제법 듣기 좋았는데.”

분명 그랬었다. 불과 몇 시진 전까지는.

하지만 이제 오라버니라는 호칭은 두 번 다시 쓸 수 없을 것이다.

지금 요희가 바라보고 있는 후덕한 체격의 중년인은, 그녀가 알던 흑웅이 아니었으니까.

“어째서?”

의문으로 가득 찬 음성. 흑웅이 어깨를 으쓱하며 대답했다.

“간단한 이야기요. 그대가 나를 이용했던 것처럼, 나도 그대를 이용한 것뿐이지.”

“……결국 백상과 한패였군요. 당신도.”

“말에 어폐가 있군. 우리 모두가 한패 아니었소?”

“……!”

덜컥 굳은 요희의 모습에, 흑웅이 피식 웃었다.

“부정하지는 마시오. 나는 누구보다 가까이에서 그대와 백상을 지켜본 사람이니까.”

“그럼 갑작스럽게 요서부에 찾아온 것도?”

“전부 계획의 일환이었지. 그대도, 진태경도, 야수묘왕도, 심지어 백상도. 물론 내 정체에 대해서는 몰랐겠지만……. 사실 따지고 보면 우리가 한패였다고 말하는 것도 우스운 일이오.”

흑웅의 대답에서 무언가를 깨달은 요희는 침음성을 삼켰다.

자신이 모르는 것은 이해할 수 있었다. 비록 백상의 뜻에 동조했다고는 하나, 어디까지나 묵인을 앞세운 간접적인 동조자에 불과했으니까.

하지만 백상에게조차 정체를 숨겼다는 것은…….

“그동안 감시했던 거군요. 나와 백상을.”

“축하하오. 답을 향해 한 걸음 나아갔군. 앞으로 두 걸음 남았소.”

“마후(魔后)의 명이었나요?”

“좋아. 마지막 한 걸음이오.”

“만일의 상황을 대비해서 마후가 숨겨 둔 소매 속의 칼, 그게 당신이었어요.”

짝. 짝.

느릿하게 두 손뼉을 마주친 흑웅이 빙긋 웃었다.

“과연 영민하군. 정답이오. 다만 나도 일이 이렇게까지 흘러갈 줄은 꿈에도 생각하지 못했지.”

흑웅은 천천히 주위를 돌아보았다.

온통 폐허가 된 공간. 숨이 끊긴 채 쓰러진 두 노괴(老怪)을 스친 그의 시선이 마침내 한 사람에게 닿았다.

“열화신룡 진태경. 태원진가의 삼공자이자, 장차 열화문의 적통(嫡統)을 이을 화왕의 후인.”

나지막이 이어지는 목소리.

품 안에서 기절하듯 잠들어 있는 그를 응시하는 흑웅의 눈동자에 기광이 스쳤다.

“이곳에서 놈을 발견했을 때 일이 틀어졌다는 걸 깨달았지. 모든 것이 계획대로 진행되었다면 뇌옥에 처박혀 있거나, 이미 마후께서 놈을 거두어 가셨을 테니까. 하지만…….”

진태경은 추종향을 쫓아 독혈지에 당도했고, 마후가 안배해 둔 바에 따라 야수묘왕을 기다리던 두 초절정 고수를 죽이고 살아남았다.

“멍청한 놈들. 마후께서 그토록 주의하라 하셨거늘.”

작게 중얼거린 흑웅은 가래를 탁 뱉었다. 그리고 언제 그랬냐는 듯 사람 좋은 웃음과 함께 요희를 바라보았다.

“이 지경까지 와서 과연 놈을 생포하는 것이 옳은 선택인지는 모르겠지만…… 그래도 틀어진 일을 수습할 수 있어서 다행이오. 아, 물론 그전에 우리의 행선지가 바뀌었다는 사실을 알려 줘야겠구려.”

“……내궁. 내궁으로 향할 생각이군요.”

신음과도 같은 요희의 뇌까림에, 흑웅이 고개를 끄덕였다.

“아마 내가 돌아간다면 꽤 재미있는 일이 벌어질 거요. 한족의 간악한 흉계에서 살아남은 대족장의 증언에 남만이 격동할 테고, 이 땅의 모든 전사와 맹수가 내궁에 결집하겠지. 중원과 일전을 치르기 위해서.”

“하지만 사람들은 바보가 아니에요. 고작해야 절정의 경지에 불과한 당신이, 어떻게 홀로 사지(死地)를 빠져나올 수 있었는지에 대해 모두가 의심하겠죠.”

“제법이구려. 하지만 내가 초절정 고수라면 어떻겠소?”

“그게 무슨…….”

“세간의 인식으로 진태경을 제압할 만큼 무위가 뛰어난 초절정 고수. 거기에 더해 인덕과 명망을 갖추었고, 백상에게 동조하지 않을 이들까지 포용할 수 있는 자. 그런 자라면 모두가 믿어 주지 않을까?”

그 순간, 요희의 신형이 덜컥 굳었다.

“당신, 설마……!”

“맞소.”

빙긋 웃은 흑웅이 공력을 일으켰다.

요서부에서부터 지금까지. 단 한 번도 금제 된 적 없던 그의 공력이 뼈와 살을 움직이고 근육을 비틀었다.

뿌득. 뿌드득.

요희의 귓가를 파고드는 섬뜩한 파육음.

어느덧 먹구름 사이로 모습을 비춘 희미한 달빛 아래에서 흑웅의 그림자가 흔들렸다. 더욱 장대하고, 강건하게.

“크윽.”

그리고 고통에 찬 흑웅의 외마디 신음과 함께 모든 변화가 끝났을 때, 얼어붙어 있던 요희의 입술 사이로 짧은 두 글자가 흘러나왔다.

“……궁주?”

믿을 수 없다는 듯이 부릅떠진 요희의 눈동자에, 한 사람이 비쳤다.

흑웅이면서 야수묘왕. 야수묘왕이면서 흑웅임에 틀림없는 그는 거대해진 자신의 그림자를 바라보며 만족스럽게 웃었다.

“사람들은 축골공(縮骨功)의 묘리가 단순히 체격을 줄이는 것에만 있다고 생각하지. 하지만 그 끝에 다다라 대성(大成)하게 된다면, 완전히 다른 사람으로 거듭날 수도 있소.”

“……!”

“자, 이렇게 합시다. 내가, 아니 야수묘왕이 이곳에 찾아와 진태경을 제압했고, 놈의 간악한 흉계로부터 목숨을 건진 그대는 내궁으로 돌아가 사람들에게 이렇게 말하는 거요.”

넋 놓은 얼굴로 자신을 바라보는 요희를 향해, 흑웅은 천천히 말을 이었다.

“근래 일어난 모든 일은 남만을 집어삼키려는 진태경과 무림맹의 음모였다고. 남녀노소 가릴 것 없이, 이 땅의 모든 인간과 짐승을 동원하여 중원으로 쳐들어가야 한다고. 어떻소?”

요희는 대답하지 않았다. 아니, 대답할 수 없었다. 전신을 옥죄이는 두려움과 분노로 숨이 막히고 눈앞이 어지러웠다.

“다, 당신이 어떻게…….”

“아. 한 가지를 말 해주는 걸 깜빡했구려. 만약 그대가 이 제안을 거절한다면 보산(保山)이 피로 물들 거요. 그리고 남만을 주름잡던 사대 부족은 삼대 부족이 되겠지.”

까드득.

분노를 참지 못한 요희의 붉은 입술 사이로, 한 줄기 핏물이 흘러나왔다.

타오르는 눈빛으로 흑웅을 노려보던 요희가 씹어뱉듯 입을 열었다.

“개새끼.”

“마음이 아프구려. 곧 지아비가 될 사람에게 그런 말을 하다니.”

“그 입 닥쳐라. 누가 네놈과 혼례를 치른다더냐?”

“아마 그렇게 될 거요. 오천이 넘는 요족이 눈앞에서 차례차례 목이 달아나는 걸 보게 된다면.”

“……!”

“그대는 고집이 센 여인이고, 나는 인내심이 강한 사내지. 그러니 기다리겠소. 오천 개의 수급이 전부 땅에 떨어질 때까지.”

느긋한 목소리로 대답한 흑웅이 요희를 향해 활짝 웃었다. 마치 아무 일도 없었다는 듯, 지금껏 늘 그래 왔던 것처럼 환하게.

“사랑하오, 요희.”

전신의 털이 곤두서는 듯한 오한과 함께, 요희는 질끈 눈을 감았다.

믿을 수 없었다. 언제부터 진행되었는지 모를 이 계획과 모두가 무시하던 저 한량(閑良)의 진면목이.

그리고 자신의 머리 위로 드리워진 암천의 짙은 그림자가.

하아.

흩어지는 숨과 함께 뇌리를 스치는 수많은 생각들.

다음 순간, 천천히 눈을 뜬 요희가 허리춤의 연검(軟劍)을 뽑으며 입을 열었다.

“더러운 변절자.”

“더러운 변절자라니. 부디 자신을 그리 자책하지는 마시오.”

“부정하지는 않겠어. 결국 나도 변절자였으니까. 하지만 암천이, 남천마후가 널 살려 둘까? 네놈이 이끄는 이족은?”

날카로운 외침처럼 울려 퍼지는 목소리에, 잠시 눈을 깜빡이던 흑웅이 돌연 너털웃음을 터트렸다.

“나와는 관련 없는 문제요.”

“뭐?”

“사십여 년 전. 이족의 전대 부족장이 정마대전에서 목숨을 잃었을 때 남만에 남아 있던 그의 유일한 적자(嫡子)는 여섯 살에 불과했지. 건장한 사내와 여인들은 전장으로 향했고, 어미는 자식의 얼굴을 보기도 전에 죽었으며, 곁에는 눈과 귀가 어두운 늙은 유모 하나뿐이었소.”

“……!”

“요희.”

흑웅은, 아니 어느덧 흑웅이 되어 버린 사내는 희미한 미소와 함께 말을 이었다.

“나는 변절자였던 적이 없소. 단 한 순간도.”

철컹.

요희의 손아귀에서 미끄러진 연검이 요란한 소리와 함께 지면에 떨어졌다.

그녀는 가쁜 숨을 내쉬며 검을 줍고자 했지만, 어째서인지 몸이 말을 듣지 않았다.

‘이건.’

요희의 눈꺼풀이 파르르 떨렸다.

여러 가지 충격적인 사실들이 불러온 마음의 격동 때문에?

아니다. 그녀가 움직이지 못하는 것은, 이미 전신 구석구석 퍼져나간 음습하면서도 끈적한 기운 때문이었다.

“다, 당신…….”

힘없이 흐려지는 목소리와 시야.

그 너머에서 천천히 가까워지는 흑웅의 모습은 아지랑이처럼 일렁였고, 뒤이어 귓가를 파고드는 목소리는 멀게만 느껴졌다.

“이러니 내가 그대를 사랑할 수밖에 없지. 눈이 부시도록 아름다운 데다가 이토록 순진하기까지 하니.”

“해, 해약(解藥)이 아니었…….”

“아쉽게도 난 야수묘왕이 아니라, 당신과 검을 맞대는 것조차 부담스럽거든. 부디 이 못난 지아비를 이해하시오, 부인. 다시 깨어났을 때는 모두를 위한 선택을 하길 바라지.”

요희는 비명을 내지르고 싶었다. 누군가가 와서 이 끔찍한 사내를 죽여 달라고. 이 어두운 구렁텅이에서 자신들을 꺼내고, 남만을 집어삼킬 거대한 흉계를 막아 달라고 외치고 싶었다.

하지만 그녀의 간절한 바람과는 달리 목구멍을 비집고 솟구친 비명은 입 밖으로 새어 나가지 못했고, 수마(睡魔)라는 괴물에 사로잡힌 진태경은 마지막까지 눈을 뜨지 못했다.

그리고 다음 순간.

스륵. 툭.

실 끊어진 인형처럼 무너지는 요희의 신형을, 흑웅은 부드럽게 감싸 안았다.

야수묘왕의 얼굴을 한 그의 입가에는 미소가 떠올라 있었다.

“잠든 모습조차 아름답구려.”

흑웅은 진심으로 요희를 사랑했다. 그녀가 자신을 원하지 않는다는 건 중요하지 않았다.

요희는 결국 옳은 선택을 할 테고, 마침내 자신을 사랑하게 될 테니까.

암천은, 남천마후는 약속을 지킬 것이다.

오랜 세월 정체를 감추고 고생한 대가는 열 배, 스무 배로 돌아올 것이다.

물론 그 전에…….

‘이 일을 끝내야겠지.’

요희의 이마에 입맞춤한 흑웅은 천천히 돌아섰다.

그의 발걸음이 향하는 곳에는 감히 대계(大計)를 그르치려 한 원흉이 있었다.

‘진태경.’

놈은 누구도 예상치 못했던 변수였고, 이는 성공을 코앞에 둔 대계에 큰 타격을 입혔다. 존재 자체만으로도 전황(戰況)을 뒤바꿀 초절정 고수가 둘이나 희생당했으니까.

그러나 바뀌는 것은 없었다.

‘대계는 성공할 것이고, 저들을 대신할 손발도 남아 있다.’

진태경은 적어도 며칠간 정신을 차리지 못할 터.

흑웅이 요희와 진태경을 데리고 내궁으로 돌아간다면, 모든 것이 끝난다.

‘그래. 끝이지.’

만족스럽게 웃은 그는 숨을 헐떡이는 백호를 지나, 진태경의 뒷덜미를 잡고 들어 올렸다.

아니, 들어 올리려던 그때였다.

솨아아아아.

어디선가 불어온 스산한 바람에 흑웅은 문득 고개를 들었다.

희끄무레한 달빛 아래, 무언가의 형체가 그의 눈동자에 비치고 있었다.

“저게 뭐…….”

의문을 표하려던 그 순간.

슈화아악!

칼날로 화한 스산한 바람이 그의 전신을 덮쳤다.
```

## Final English reading copy

```markdown
# Chapter 687

SLICE. THUD!

For a moment, it seemed as though the world had stopped.

“Grrrk.”

A massive White Tiger lay collapsed like a rotten log, panting for breath. Jin Taekyung had lost consciousness completely.

And reflected in Yohi’s eyes was the sight of one man holding him in his arms and calmly continuing to speak.

“I told you. I should have hidden myself first.”

“……!”

Enlightenment and shock flashed through Yohi’s mind like lightning.

Her eyes, which had always held a deep and gentle light, flew wide open.

“Heugung, you!”

“You don’t call me big brother anymore. I rather liked hearing it.”

It had certainly been that way—until only a few shichen ago.

But Yohi would never be able to use that title again.

The middle-aged man with the kindly, heavyset build standing before her was not the Heugung she knew.

“Why?”

Her voice was filled with questions. Heugung shrugged and answered.

“It’s a simple story. Just as you used me, I used you.”

“……So you were on Baeksang’s side after all. You too.”

“That is a strange way to put it. Weren’t we all on the same side?”

“……!”

At the sight of Yohi stiffening, Heugung let out a quiet laugh.

“Don’t deny it. I was the person who watched you and Baeksang from closer than anyone else.”

“Then what about your sudden appearance at the Western Yao Estate?”

“That was all part of the plan. You, Jin Taekyung, the Beast Miao King, and even Baeksang. Of course, none of you knew my true identity… Though, when you think about it, calling us all allies is rather amusing.”

Yohi swallowed a low groan as she realized something from Heugung’s answer.

She could understand why she had not known. Although she had sided with Baeksang, she had only been an indirect accomplice whose involvement amounted to tacit acquiescence.

But the fact that he had hidden his identity even from Baeksang meant…

“You were watching us all this time. Baeksang and me.”

“Congratulations. You’ve taken one step toward the answer. Two more remain.”

“Was it the Demon Empress’s order?”

“Good. One final step.”

“You were the knife hidden up the Demon Empress’s sleeve in case something went wrong.”

Clap. Clap.

Heugung slowly brought his hands together and smiled.

“You’re quite perceptive. Correct. Though even I never dreamed things would go this far.”

Heugung slowly looked around.

The entire area had been reduced to ruins. His gaze passed over the two dead old monsters before finally coming to rest on one person.

“Jin Taekyung, the Blazing Flame Divine Dragon. The Third Young Master of the Jin Family of Taiyuan, and the heir of the Fire King who will one day inherit the orthodox lineage of the Fire Gate Clan.”

His voice continued in a low murmur.

A glint flashed in Heugung’s eyes as he stared at Jin, who was sleeping as though he had fainted in his arms.

“When I found him here, I realized things had gone wrong. If everything had proceeded according to plan, he would have been thrown into the underground prison—or the Demon Empress would already have taken him. But…”

Jin Taekyung had followed the tracking scent to the Poisonblood Grounds, killed the two Supreme Peak masters waiting for the Beast Miao King according to the Demon Empress’s arrangements, and survived.

“Fools. The Demon Empress told them to be so careful.”

Heugung muttered under his breath and spat out a wad of phlegm. Then, as though he had never done such a thing, he looked back at Yohi with a friendly smile.

“I don’t know whether capturing him alive is still the right choice after things have reached this point… But at least it’s fortunate that I can clean up the mess. Ah, before that, I suppose I should tell you that our destination has changed.”

“……The Inner Palace. You intend to head to the Inner Palace.”

At Yohi’s mutter, which sounded almost like a groan, Heugung nodded.

“If I return, something quite interesting will probably happen. Nanman will be thrown into turmoil by the testimony of the Great Chieftain who survived the Han Chinese’s wicked conspiracy, and every warrior and beast in this land will gather at the Inner Palace.”

“To fight the Central Plains.”

“But people aren’t fools. Everyone will wonder how you, a man who is only at the Peak realm, managed to escape from a deadly place all by yourself.”

“You’re quite sharp. But what if I were a Supreme Peak master?”

“What are you talking about…?”

“A Supreme Peak master whose martial prowess is great enough, by the public’s understanding, to subdue Jin Taekyung. Someone who also possesses virtue and prestige, and can embrace even those who would never side with Baeksang. Wouldn’t everyone believe such a person?”

At that moment, Yohi’s body stiffened.

“You… Don’t tell me!”

“That’s right.”

Heugung smiled faintly and released his internal energy.

From the Western Yao Estate until now, his internal energy had never once been sealed. It moved his bones and flesh and twisted his muscles.

CRACK. CRACK.

The eerie sounds of flesh being torn apart pierced Yohi’s ears.

Under the faint moonlight that had appeared between the clouds, Heugung’s shadow began to shift.

It grew taller. Stronger.

“Ghk.”

When every change was complete with a brief, pain-filled groan from Heugung, a short title slipped from Yohi’s frozen lips.

“……Palace Lord?”

In Yohi’s wide, disbelieving eyes, one person was reflected.

He was Heugung and the Beast Miao King. The Beast Miao King and, without a doubt, Heugung.

He gazed at his enlarged shadow and smiled with satisfaction.

“People think the essence of the Bone-Shrinking Technique lies solely in reducing one’s size. But when you reach its pinnacle and attain Great Completion, you can be reborn as an entirely different person.”

“……!”

“Now, let’s put it this way. I—or rather, the Beast Miao King—came here and subdued Jin Taekyung. You survived his wicked conspiracy, then returned to the Inner Palace and told everyone this.”

Heugung slowly continued, speaking to Yohi, who stared at him in a daze.

“That everything that has happened recently was a conspiracy by Jin Taekyung and the Murim Alliance to swallow Nanman whole. That we must mobilize every human and beast in this land, regardless of age or sex, and invade the Central Plains. What do you think?”

Yohi did not answer.

No, she could not answer. Fear and rage constricted her entire body, making it difficult to breathe and causing her vision to swim.

“H-How could you…”

“Ah. I forgot to tell you one thing. If you refuse my proposal, Boshan will run red with blood. And the four great tribes that dominate Nanman will become three.”

CRUNCH.

A thin line of blood trickled between Yohi’s red lips as she struggled to contain her rage.

She glared at Heugung with blazing eyes and spat out the words.

“You son of a bitch.”

“My heart aches. To think you would say such a thing to the man who will soon become your husband.”

“Shut your mouth. Who said I was going to marry you?”

“You probably will if you have to watch more than five thousand Yao people lose their heads one after another before your eyes.”

“……!”

“You’re a stubborn woman, and I’m a patient man. So I’ll wait. Until all five thousand heads have fallen to the ground.”

Heugung answered in a leisurely voice, then beamed at Yohi.

It was the same bright smile he had always worn, as though nothing had happened.

“I love you, Yohi.”

A chill rose over Yohi’s body, making every hair stand on end. She squeezed her eyes shut.

It was unbelievable.

This plan, whose beginning she could not even identify, and the true nature of the wastrel everyone had ignored.

And the dark shadow of Dark Heaven hanging over her head.

Haa.

A great many thoughts flashed through her mind along with her scattering breath.

A moment later, Yohi slowly opened her eyes, drew the flexible sword from her waist, and spoke.

“You filthy traitor.”

“A filthy traitor? Please don’t be so hard on yourself.”

“I won’t deny it. In the end, I was a traitor too. But will Dark Heaven—the Southern Heaven Demon Empress—allow you to live? What about the Yi people you lead?”

Her voice rang out like a sharp cry.

Heugung blinked for a moment, then suddenly burst into hearty laughter.

“That has nothing to do with me.”

“What?”

“More than forty years ago, when the former chieftain of the Yi people lost his life in the Great Faction War, his only legitimate son remaining in Nanman was only six years old. The strong men and women went to the battlefield. His mother died before she could even see her child’s face, and the only person left at his side was an old nurse whose eyes and ears had grown dim.”

“……!”

“Yohi.”

Heugung—or rather, the man who had become Heugung—continued with a faint smile.

“I have never been a traitor. Not for a single moment.”

CLANG.

The flexible sword slipped from Yohi’s grasp and struck the ground with a clatter.

She breathed heavily and tried to pick it up, but for some reason, her body would not obey.

*What is this?*

Yohi’s eyelids trembled.

Was it because of the upheaval in her heart caused by the succession of shocking revelations?

No.

She could not move because of the sinister, sticky energy that had already spread through every corner of her body.

“You…”

Her voice and vision faded weakly.

Heugung’s approaching figure wavered like a heat haze, and the voice that followed felt as though it were coming from far away.

“This is why I can’t help loving you. Not only are you dazzlingly beautiful, you’re this naïve too.”

“That wasn’t an antidote…”

“Unfortunately, I’m not the Beast Miao King, and even crossing swords with you would be too much for me. Please understand this sorry husband of yours, my dear wife. When you wake up again, I hope you’ll make the choice that is best for everyone.”

Yohi wanted to scream.

She wanted someone to come and kill this horrible man. She wanted to shout for someone to pull them out of this dark pit and stop the enormous conspiracy that would swallow Nanman whole.

But contrary to her desperate wishes, the scream that surged up through her throat could not escape her lips.

And Jin Taekyung, seized by the monster known as the sleep demon, did not open his eyes until the very end.

Then, in the next moment—

SWISH. THUD.

Heugung gently caught Yohi’s body as it collapsed like a puppet with its strings cut.

A smile appeared at the corner of his mouth, which now wore the face of the Beast Miao King.

“Even the way you sleep is beautiful.”

Heugung truly loved Yohi. The fact that she did not want him did not matter.

Yohi would eventually make the right choice.

And, in the end, she would come to love him.

Dark Heaven—the Southern Heaven Demon Empress—would keep her promise.

The price for hiding his identity and suffering through all these years would return to him tenfold, twentyfold.

Of course, before that…

*I need to finish this.*

Heugung kissed Yohi on the forehead, then slowly turned around.

He walked toward the culprit who had dared to jeopardize the grand plan.

*Jin Taekyung.*

He had been a variable no one could have predicted, and his existence had dealt a severe blow to the grand plan that stood on the verge of success.

Two Supreme Peak masters whose very presence could turn the tide of battle had been sacrificed.

But nothing had changed.

*The grand plan will succeed, and there are still hands and feet left to replace them.*

Jin Taekyung would not regain consciousness for at least several days.

If Heugung brought Yohi and Jin Taekyung back to the Inner Palace, everything would be over.

*Yes. It will be over.*

He smiled in satisfaction, passed the panting White Tiger, and grabbed Jin Taekyung by the nape to lift him up.

No—he was just about to lift him when it happened.

WHOOSH!

A bleak wind blew in from somewhere, and Heugung suddenly raised his head.

Beneath the pale moonlight, the shape of something appeared in his eyes.

“What is that…?”

At the very moment he began to voice his question—

SHWAAAASH!

The bleak wind turned into a blade and engulfed his entire body.
```
