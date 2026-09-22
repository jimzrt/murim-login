<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0675.txt",
      "sha256": "dd2e1631ca23f583529b5f6df9799945d3158045654d69a01d9a91d684d2dcd2",
      "bytes": 13038
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "08eee2f9cf98c323cd1d2166544e821830def90f7f1c5dcfcc68a6c8a8c89464",
      "bytes": 1863
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6c78ffaa1ea268bd2774e6a91268e4e10199d6311a9d431b27a1aba295079287",
      "bytes": 202892
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "f64086ebf20a267eb2fb4d071d494779bd58869cf28936d2718600ccdcc8398c",
      "bytes": 1011
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "562da525e39cd76adcbced2681282f5ed60d9ac1206b0932c4a898613eff967f",
      "bytes": 830
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "12a33670cb9ef726e75e4263b567a8de2819d76786320a4dc2b0774713e02c3b",
      "bytes": 769
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "3b7fbd1f3272f4fc46b22fb373d91f4afcae3108f389a729969a3274da27f082",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1248e9ec4258bde1df2a1b9f0ae1e7aa4b284da7250854d94de0fc44bb16b030",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a25cfc252e06047636fc18c799dd3383ac0045fc10710ebd2a3fa273fdc09b91",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "a3d5b382f010df287f5a32a7b4ca101dd3b314f47d83d3a631a19350a826e9d3",
      "bytes": 580
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "b10068248ae6490066875fd54ca591b0099ba2c2ce13fb6913fc8ca7211c0b7e",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b7183c308c8b26d01e1f910810cf9c3c9a8753d63d86b134042dfd2568c02e6e",
      "bytes": 209070
    }
  ],
  "estimated_tokens": 12087
}
-->

# Durable State Update — Chapter 675

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 675. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 675. Profile updates may replace only one
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
  "chapter": 675,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 675,
    "continuity_sources": [675],
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
    "Nanman has issued a general mobilization order and placed Baeksang in the temporary position of Palace Lord.",
    "Baeksang's left arm was severed by Force, and he remains under the Southern Heaven Demon Empress's command.",
    "The Southern Heaven Demon Empress has ordered Baeksang to find and eliminate the Beast Miao King within three days while Dark Heaven handles Jin Taekyung.",
    "Dark Heaven's decades-long undertaking is nearing completion and is intended to open a bridgehead from Nanman toward the Central Plains.",
    "Dark Heaven expects the return of the Lord of Heaven at the end of its undertaking.",
    "Jin Taekyung and Muyaho are fleeing south after repelling multiple pursuit squads and have reached a dark mountain beside a black forest.",
    "Baeksang admits that his remaining sworn-brotherly feelings may have helped the Beast Miao King escape, but vows that such leniency will not happen again."
  ],
  "continuity_sources": [
    674
  ],
  "open_questions": [
    "What exactly is Dark Heaven's great undertaking and how will it bring about the Lord of Heaven's return?",
    "Can the Beast Miao King evade Baeksang's three-day pursuit?",
    "How will Jin Taekyung survive Dark Heaven's direct intervention?",
    "What awaits Jin Taekyung and Muyaho in the dark forest?"
  ],
  "safe_through": 674,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Palace Lord for 궁주.",
    "Use temporary Palace Lord for 임시 궁주 and Palace Lord's Hall for 궁주전.",
    "Use Southern Heaven Demon Empress for 남천마후 and Dark Heaven for 암천.",
    "Use Great undertaking for 대사 when it refers to Dark Heaven's plan.",
    "Preserve the Southern Heaven Demon Empress's playful, taunting menace and Jin Taekyung's crude, irreverent narration."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 몬스터     | **monster**           |
| 정마대전   | **Great Faction War**         |
| 도사      | **Daoist**                                                      |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 서요부 | **Western Yao Estate** | Yohi's residence in the western part of the Inner Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
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

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 674
- **Aliases:** None
- **Role:** Baeksang is the temporary Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; despite his bond with Yayul Cheok, he has chosen to oppose the Beast Miao King's escape and has surrounded Wonhu's remaining force with Bai warriors.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 674
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 671
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he disappeared alongside Yohi after the assault on the Fire Dragon Pavilion, and his death remains unconfirmed after a severed wrist believed to be his was found at her estate.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 674
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 674
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 674
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 674
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and currently carries Jin while aiding his escape.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 672
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃675화



처음부터 그 장소를 떠올린 것은 사실이지만, 그래도 설마 했다. 남만의 면적은 실로 광활하고, 나는 아직 중원 지리도 제대로 모르는 한국인이니까.

사실 천하의 모든 무림인을 통틀어도 나만 한 혼종도 없을 거다.

‘중원에서는 사실상 외지인. 남만에서도 빼도 박도 못하는 외지인.’

그런 나였으니 정확히 알 턱이 없었다. 어디로 향하는지, 어디에서 멈출지.

더군다나 무야호는 사람의 말을 이해하는 영물이지, 말할 수 있는 영물은 아니었다.

그렇기에 마침내 백호의 발걸음이 느려졌을 때, 나는 깨달았다.

‘설마가 진짜 사람 잡겠네, 시바 거.’

그저 바라보는 것만으로도 불길함이 느껴지는 산세(山勢).

불과 며칠 만에 다시 돌아온 애뇌산(哀牢山)은 여전했다. 어둡고, 서늘하고, 자욱한 안개 너머로는 피비린내가 풍겨 오는 듯했다.

한마디로 말해서 언제 와도 기분이 좆 같아지는 장소였다.

애뇌산에 한해서만큼은 뫼 산이 아니라, 좆 산. 뭐 그런 글자를 따로 만들어 표기해야 하는 게 맞지 않나 싶을 정도로.

“……진짜 여기냐?”

- 크릉.

“거짓말하면 발모가지 날아가는 건 알고?”

- 크르릉!

“아. 오케이.”

젠장, 진짠가 보네.

나는 살짝 성이 난 백호의 미간을 살살 긁어 주며 주위를 살폈다.

간간이 들려오는 늑대 울음소리와 그럴 때마다 푸드득 날아오르는 산새들. 주위에서 들려오는 소음은 그것이 전부였다.

‘그래, 적어도 소리만큼은 그렇겠지.’

마음속으로 뇌까린 나는 퀘스트 창을 확인했다.

무야호와 함께 일행에서 떨어져 나오며 자동으로 시작된 연계 퀘스트는, 초절정이라는 높은 등급치고는 짧고 간단했다.



퀘스트



[너의 추종향이 보여]



당신은 추종향을 추적하는 것을 선택했습니다.

지금 향하는 그 길의 끝에, 부디 원하는 것이 있기를.



등급 : 초절정

제한 : 진태경

임무 : 요희 발견 (미완료)

보상 : ???

실패 : ???





요희 발견이라. 당연히 성공해야지.

하지만 솔직히 내 입장에서는 요희든, 흑웅이든 상관없다.

이건 굳이 퀘스트가 아니더라도 반드시 해내야 하는 임무다. 그 두 사람이야말로 남천마후와 백상의 계획을 저지시킬 수 있는 가장 확실한 카드 중 하나이기 때문이다.

‘얻은 정보에 따르면 야수묘왕은 행방이 묘연하고, 남만야수궁 내 우호 세력은 사실상 힘을 잃은 상황. 시간이 촉박한 지금 상황에서는 두 대족장을 구해서 내궁으로 가는 것이 최선이야.’

무야호는 죽어라 뛰게 시키면서 나는 등에 앉아 편하게 경치 구경만 했겠나. 이에 관한 생각들은 오는 길에 이미 끝냈다.

서요부의 일로 남만야수궁이 인정한 천하의 개썅놈이 된 이상, 나 혼자 닥치고 돌격해 봤자 기다리고 있는 건 창칼밖에 없다.

하지만 납치된 장본인들인 흑웅과 요희가 나와 함께 생환한다면?

‘판이 뒤집히지. 아주 확실히.’

누가 하느냐에 따라 무게감이 달라지는 것이 바로 ‘말’이다.

그런 의미에서 사대 부족을 이끄는 각 대족장들이 나서서 내 결백을 증명하고, 이번 참극의 진실을 밝힌다면 현재 남만에서 벌어지고 있는 모든 상황은 새로운 국면에 접어들 것이다.

그것이 어떻게든 이 퀘스트를 성공해야 하는 이유였다. 단숨에 전세를 뒤바꿀 수도 있는 묘수(妙手)니까.

물론…….

“바둑돌부터 잡아야 묘수를 놓는 건데. 쉽지 않네, 시작부터.”

한숨처럼 중얼거린 나는, 어느새 사방을 에워싸며 다가오는 인기척들을 느끼며 말을 이었다.

“그래서 바둑돌 대신 우선 몇 놈 잡고 시작할까 하는데…… 누구부터 뒈질래?”

“……!”

예상했던 대로 대답은 없었고. 나는 망설임 없이 신형을 날렸다.

화륵. 콰아아!

염화일로(炎火一路).

걸음을 따라 솟구친 불꽃이, 유성의 꼬리가 되어 어둠을 갈랐다.



* * *



적의 숫자는 추종향을 추적하기 시작한 이래, 그 어느 때보다 많았다.

당장 눈에 보이는 머릿수만 해도 어림잡아 삼백.

아마 저 무성한 풀숲 뒤에도 그와 비슷하거나 이상의 숫자가 도사리고 있을 터였다.

하지만…….

‘겨우 이 정도로?’

무림이라는 이 거대한 먹이사슬 속에서 맹수로 우뚝 선 내게, 지금 이 순간 사방을 에워싼 적들은 힘없는 양 떼에 불과한 존재다.

굳이 목덜미에 이빨을 박아넣지 않아도 제압할 수 있는.

화륵, 콰아아아!

어둠을 살라 먹는 불꽃과 함께 쏘아지는 신형. 반 박자 늦게 그 사실을 알아차린 적들 사이에서 비명이 터져 나왔다.

“바, 발각됐습니다!”

“막아라! 놈이 온……!”

콰아아앙!

누군가의 고함은 곧이어 터져 나온 굉음에 파묻혔다.

뒤집히는 땅거죽과 뿌리째 뽑혀 나간 아름드리나무. 수십에 달하는 적들이 약속이라도 한 것처럼 동시에 사방으로 튕겨 나갔다.

“커헉!”

“크아아악!”

이미 촘촘하던 진형은 무너졌고 그 빈자리를 채운 것은 비명뿐이다.

어깨에 묻은 흙을 털며 걸어 나오는 내 모습에 누군가가 외쳤다.

“모두 맹수를 앞세워라! 후방에서 놈을 공격해!”

“오, 저 동물학대범 새끼.”

하지만 그것과는 별개로 괜찮은 선택이었다.

맹수를 이용하는 남만식 전투법은 나름대로 정평이 나 있었고, 그게 중원의 무림인들에 비해 개개인의 실력이 떨어지는 남만 전사들이 정마대전에서 활약할 수 있었던 이유이기도 했으니까.

물론, 그것도 상황 봐 가면서 했을 때의 이야기다.

그워어어!

평범한 불곰보다도 훨씬 커다란 체격을 지닌 녀석이 포효와 함께 달려들던 그 순간.

쉬쉬쉭!

날카로운 파공성과 함께 내 옆을 스쳐 지나간 희끗한 무언가가 대장 불곰의 아구창을 후려쳤다.

콰직! 콰드득!

허공에 점점이 흩뿌려지는 핏방울과 그대로 고꾸라지는 동체.

어쩌면 이 자리에 있는 맹수 중에서도 세 손가락 안에 들 만큼 강했을 대장 불곰을, 냥냥펀치 한 방으로 제압한 무야호가 눈빛을 번뜩였다.

솨아아악!

보이지는 않지만 느껴진다. 사방으로 퍼져 나가는 서늘한 기운이.

‘이건…….’

피어(Fear).

이미 날 때부터 맹수의 그릇을 벗어난 백호의 위압감이 주위를 짓누르자, 으르렁거리던 맹수들의 울음소리가 씻은 듯 사라지고 바짝 곤두서 있던 꼬리 끝이 땅을 향한다.

동시에 달빛을 머금은 청백색 눈동자에 다시 한번 기광(奇光)이 스친 그때.

- 크아아아아앙!

폭발하듯 터져 나온 포효에 대기가 파르르 떨린다.

바람이 출렁이자 풀과 꽃은 허리를 숙였고, 동공이 팽창한 맹수들은 몸을 잔뜩 움츠린 채 뒷걸음질 쳤다.

그리고 이러한 기현상은, 비단 맹수에게만 해당하는 것이 아니었다.

“흡.”

“모, 몸이…….”

무야호가 발산하는 기세는 수신룡이나 지금껏 내가 만난 몇몇 몬스터에 미치지 못할 뿐, 그리 뛰어난 무공을 지니지 못한 일부 적들을 얼어붙게 하기에는 충분했다.

물론 그 말은, 예외도 있다는 뜻이다.

“이, 이런 멍청한 놈들! 뭘 하는 것이냐!”

당황과 분노로 얼룩진 외침.

비교적 떨어진 후방에서 표범 가죽을 뒤집어쓴 중년인을 발견한 나는, 마치 한 자루의 창처럼 쏘아졌다.

쐐애애액! 콰득!

“크아악!”

“괴, 괴물!”

맞다. 적어도 이 순간, 이 장소에서 나는 하나뿐인 괴물이다.

누구도 막을 수 없는 존재. 지금껏 머릿속에서만 그렸을 뿐, 단 한 번도 적이 되어 맞서 싸우리라 생각지 못했던 강자.

설령 이 자리의 모두가 나를 막아선다 해도, 내게는 나아갈 힘이 있다.

“족장님을 지켜라!”

“무슨 수를 써서라도 놈을 막…… 커헉!”

부드럽게 상대의 가슴을 두드린 일장(一掌).

몸 안으로 스며든 열양지기가 진기의 흐름을 헝클어트리자 왈칵, 분수처럼 터져 나온 토혈과 함께 신형이 무너진다.

“노옴! 감히!”

쉬이익! 툭.

방금 쓰러트린 놈이 동료였나?

기세는 좋았지만, 실력이 부족하다.

두 손가락으로 손쉽게 검신을 붙잡으며 공수납백인(空手納白刃)의 묘리를 선보인 나는, 파르르 떨리는 검신 너머로 보이는 얼굴을 향해 어깨를 으쓱해 보였다.

“안 죽었어. 한 달쯤 누워서 피똥은 지리겠지만.”

“……!”

“그런 김에, 옆자리에서 같이 지려라.”

퍼엉!

맹렬한 기세로 튕겨 나간 신형에 십수 명이 휩쓸린다.

나는 활짝 열린 길을 따라 걸으며 양손을 펼쳤다. 하단전에 똬리를 튼 화룡(火龍)이 몸 안의 혈도를 타고 솟구쳐 올라 손아귀에 깃든다.

화륵. 치이익.

사방으로 퍼져 나가는 끔찍한 열기.

진흙탕에 발을 내딛기도 전에 수분이 증발하고, 나를 향해 달려들려던 정예 전사들의 눈동자에 청백색의 화염이 비쳤다.

“자, 잠깐……!”

그리고 나는 쌍장(雙掌)으로 대답을 대신했다.

한때 오독문을 멸문시켰다는 과거의 열화문주처럼, 화염신장을 사방으로 퍼부었다.

콰아아앙!

구구궁!

허공을 격하고 쏘아진 화염이 수풀을 휩쓸고 빽빽하게 들어선 나무를 불태운다.

어둠을 집어삼킨 그 거대한 불길 아래로, 비명을 지르며 도망치는 수백여 명의 적들이 있었다.

참으로 고맙게도, 한눈에 알아볼 수 있을 만큼 화려한 표범 가죽을 걸친 어느 중년인도.

“비켜라! 썩 비키지 못하겠느냐!”

정신없이 도망치는 걸 보니 살고 싶긴 한 모양이다.

하지만 그를 비롯한 일단의 호위가 이곳을 빠져나가기 위해 아무리 노력한다 해도, 세상에 불가능이라는 단어가 괜히 있는 게 아니다.

“어. 비키지 못하겠는데.”

“지, 진태경!”

“부족장이라고 하길래 긴가민가했는데. 확실히 대회의 때 한 번 본 얼굴이네. 그래, 그동안 잘 지냈고?”

쐐애애액!

이래서 칼 차고 다니는 놈들이 못 배워 먹었다는 소리 듣는 거다. 반가운 마음을 담아 인사를 건넸는데 병장기부터 휘두르다니.

쉭, 콰득!

“크아아악!”

손쉽게 검을 피한 뒤 손목을 부러트리자 고통에 찬 비명이 터져 나온다.

나는 곧장 달려드는 호위 다섯을 향해 지풍(指風)을 쏘았고, 뒤이어 바람처럼 나타난 무야호의 등장에 맹수들은 꽁무니를 뺐다.

화륵. 쿠구궁!

머리 위에서 흩날리는 불꽃과 재. 그리고 도미노처럼 쓰러지는 거목(巨木)들을 바라보는 부족장의 얼굴이 새하얗게 질린다.

“사, 살려…….”

“그래도 부족장씩이나 되시는 분인데, 당연히 살려 드려야지. 물론 묻는 말에 제대로 답했을 경우에.”

“구, 궁금한 게 있다면 뭐든 말하겠다!”

내게 사로잡힌 부족장은 가장 적으로 만나고 싶은 부류였다. 제 목숨은 귀한 줄 알아서 굳이 묻지 않는 부분까지 술술 불어 주니까.

그리고 그중에는 제법 유용한 정보 역시 포함되어 있었다.

“……총동원령?”

부족장이 정신없이 고개를 끄덕였다.

“배, 백상 대족장께서 임시 궁주가 되셨고, 이미 일만에 달하는 대병력이 내궁에 주둔 중이다.”

“계속.”

“묘족은 철저한 감시를 받고 있어 응하지 못했지만, 백상을 필두로 한 삼대 부족을 중심으로 남만 전체가 움직이고 있다.”

빌어먹을.

나는 욕설을 삼켰다.

야수묘왕이 도주한 이상, 백상이 임시 궁주가 되는 것은 예견된 일이었다.

하지만 나를 잡기 위한 천라지망(天羅蜘網)이 아니라 총동원령이라니.

‘설마.’

전신을 사로잡는 불길한 느낌.

어쩌면 암천이 그린 그림은, 나를 포함한 모두가 생각했던 것보다 더욱 거대하고, 완성을 앞에 두고 있을지도 모른다.

‘여기서 한 시라도 지체한다면…….’

화륵. 콰아아아.

빠르게 애뇌산으로 번져 나가는 불길을 바라보며, 나는 황급히 신형을 날렸다. 애뇌산에 웅크린 어둠 속으로, 화염 속으로.
```

## Final English reading copy

```markdown
# Chapter 675

It was true that I had thought of this place from the beginning, but even so, I had hoped I was wrong. Nanman was vast, after all, and I was still a Korean who didn’t even properly know the geography of the Central Plains.

In fact, even among all the martial artists in the world, there probably wasn’t another hybrid as strange as me.

*An outsider in the Central Plains, for all intents and purposes. An outsider in Nanman too, with no way to deny it.*

As someone in that position, there was no way I could have known exactly where we were headed or where we would stop.

Besides, Muyaho was a spiritual creature that understood human speech, not one that could speak it.

That was why, when the White Tiger’s pace finally slowed, I realized it.

*Looks like “no way” really is going to get someone killed. Fuck.*

The mountain’s shape alone gave off an ominous feeling.

Ailao Mountain, which we had returned to after only a few days, was unchanged. It was dark and chilly, and beyond the thick fog, it seemed as though the smell of blood was drifting toward us.

In short, it was the kind of place that felt fucking awful no matter when you came.

As far as Ailao Mountain was concerned, it felt like it deserved a separate name written with the character for “dick” instead of the character for “mountain.”

“…Is it really here?”

- *Grrr.*

“You know your leg’s getting chopped off if you lie, right?”

- *Grrrr!*

“Ah. Okay.”

Damn, I guess it really was.

I gently scratched the White Tiger between the brows, soothing its slight irritation as I surveyed the surroundings.

The occasional howl of a wolf. Mountain birds taking flight with a flutter whenever it sounded. Those were the only noises coming from around us.

*Yeah. At least as far as sound goes.*

Muttering inwardly, I checked the Quest window.

The linked Quest that had begun automatically when Muyaho and I split off from the group was short and simple for something with such a high grade as Supreme Peak.

> **System**
>
> **Quest**
>
> **I Can See Your Tracking Scent**
>
> You chose to track the tracking scent.
>
> At the end of the road you are traveling now, may you find what you seek.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Find Yohi (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

Find Yohi, huh? Of course I had to succeed.

But honestly, from my perspective, it didn’t matter whether it was Yohi or Heugung.

This was a mission I had to accomplish even if it wasn’t a Quest. Those two were among the surest cards I had for thwarting the Southern Heaven Demon Empress and Baeksang’s plans.

*According to the information I gathered, the Beast Miao King’s whereabouts are unknown, and the friendly forces inside the Nanman Beast Palace have effectively lost their power. With time running out, the best option is to rescue the two Great Chieftains and head to the Inner Palace.*

Did you think I’d made Muyaho run like hell while I sat comfortably on the tiger’s back doing nothing but sightseeing? I had already finished thinking things through on the way here.

Now that I had become the greatest fucking bastard under heaven in the eyes of the Nanman Beast Palace because of what happened at the Western Yao Estate, charging in alone would only leave me facing spears and blades.

But what if Heugung and Yohi—the people who had actually been abducted—returned alive with me?

*The whole board would turn over. Completely.*

“Words” carried different weight depending on who spoke them.

If each of the Great Chieftains leading the four tribes came forward to prove my innocence and reveal the truth behind this tragedy, then everything currently happening in Nanman would enter a new phase.

That was why I had to succeed at this Quest somehow. It was a brilliant move that might overturn the entire situation in a single stroke.

Of course…

“You need a Go stone before you can make a brilliant move. Not easy, starting from here.”

I muttered like a sigh, then continued as I sensed presences approaching from every direction, surrounding me.

“So I’m thinking I’ll grab a few of you first instead of Go stones and get started… Who wants to die first?”

“……!”

As expected, there was no answer. Without hesitation, I launched myself forward.

Whoosh. Fwoooosh!

Flamefire Path.

Flames surged up with each step, cleaving through the darkness like the tail of a meteor.

* * *

There were more enemies than at any point since I had begun tracking the tracking scent.

Just the ones visible at a glance numbered roughly three hundred.

There were probably as many, or more, lying in wait behind the dense grass.

But…

*Only this much?*

To me, who stood at the top of the food chain known as the Murim, the enemies surrounding me at this very moment were nothing more than a powerless flock of sheep.

I could subdue them without even sinking my teeth into their necks.

Whoosh, fwoooosh!

My body shot forward amid flames that devoured the darkness. Screams erupted from among the enemies who realized what was happening half a beat too late.

“He’s spotted us!”

“Stop him! He’s com—!”

Kwaaaang!

Someone’s shout was swallowed by the thunderous explosion that followed.

The ground overturned. Massive trees were ripped out by their roots. Dozens of enemies were flung in every direction at the same time, as if they had planned it together.

“Cough!”

“Aaargh!”

The tightly packed formation had already collapsed, leaving nothing in the gaps but screams.

As I walked out, brushing dirt from my shoulder, someone shouted.

“Put the beasts in front! Attack him from the rear!”

“Oh, that animal-abusing bastard.”

That aside, it was a decent choice.

Nanman’s method of fighting with beasts was well respected in its own right. It was also one reason Nanman warriors, whose individual abilities were inferior to those of martial artists from the Central Plains, had been able to distinguish themselves during the Great Faction War.

Of course, that only applied when the situation allowed for it.

Grrrrrrr!

The moment a creature far larger than an ordinary brown bear charged at me with a roar—

Shh-shh-shhik!

A pale blur accompanied by a sharp whistle of displaced air flashed past my side and struck the alpha brown bear in the mouth.

Crack! Crunch!

Blood droplets scattered through the air, and the massive body collapsed forward.

Muyaho had subdued the alpha brown bear—perhaps one of the three strongest beasts present here—with a single kitty-paw punch. Its eyes gleamed.

Whooosh!

I couldn’t see it, but I could feel it. A chilly aura spreading in every direction.

*This is…*

Fear.

The pressure of the White Tiger, which had transcended the vessel of a beast from the moment it was born, weighed down on the surroundings.

The growls of the beasts vanished as though washed away, and their tails, which had been standing straight up, lowered toward the ground.

At that moment, another strange gleam passed through the moonlit blue-white eyes.

- *GRAAAAAAWR!*

The explosive roar made the air tremble.

The wind rippled. Grass and flowers bent at the waist. The beasts’ pupils dilated as they crouched low and backed away.

And this strange phenomenon did not affect only the beasts.

“Gasp.”

“My, my body…”

Muyaho’s aura did not reach the level of the Water God Dragon or some of the monsters I had encountered so far. But it was more than enough to freeze several enemies who did not possess particularly outstanding martial arts.

Of course, that meant there were exceptions.

“You idiots! What are you doing?!”

The shout was stained with panic and fury.

I spotted a middle-aged man wearing a leopard hide relatively far behind the others and shot toward him like a spear.

Shaaak! Crack!

“Argh!”

“M-Monster!”

That was right. At least at this moment, in this place, I was the only monster.

An existence no one could stop. The kind of powerhouse they had only ever imagined, never once thinking they would have to face one as an enemy.

Even if everyone here stood in my way, I had the strength to move forward.

“Protect the Chieftain!”

“Stop him by any means necessary—cough!”

A palm gently tapped the opponent’s chest.

The Scorching Yang Qi that seeped into his body disrupted the flow of his qi. His body crumpled as blood burst from his mouth like a fountain.

“You bastard! How dare—!”

Whoosh! Thud.

Was the guy I’d just taken down a comrade of his?

He had plenty of momentum, but not enough skill.

I caught the blade between two fingers with ease, displaying the essence of Empty-Hand Seizes the Blade. Then I shrugged at the face visible beyond the trembling sword.

“He’s not dead. He’ll just be bedridden for about a month, shitting blood.”

“……!”

“Since you’re at it, you can shit beside him.”

Boom!

More than a dozen people were swept up by the body that shot backward with tremendous force.

I walked along the path that had opened before me and spread both hands.

The fire dragon coiled in my lower dantian surged upward along the acupoints in my body, lodging itself in my palms.

Whoosh. Ssssss.

Terrible heat spread in every direction.

The moisture evaporated before my feet even touched the mud, and blue-white flames reflected in the eyes of the elite warriors who were trying to charge me.

“W-Wait…”

I answered with both palms.

Like the former Sect Leader of the Fire Gate Clan who had once annihilated the Five Poisons Sect, I unleashed Flame Divine Palm in every direction.

Kwaaaang!

Rumble!

Flames fired through the air swept across the undergrowth and set the densely packed trees ablaze.

Beneath the enormous blaze that swallowed the darkness, hundreds of enemies fled screaming.

Including, most thankfully, a middle-aged man wearing a leopard hide so striking that I could recognize him at a glance.

“Move! Get out of my way!”

Judging by the way he was running for his life, he clearly wanted to live.

But no matter how hard he and his guards tried to escape, there was a reason the word “impossible” existed in this world.

“Yeah. I’m afraid I can’t get out of your way.”

“J-Jin Taekyung!”

“They said you were a tribal chieftain, so I wasn’t sure at first. But I definitely saw that face once at the Tribal Grand Council. So, have you been well?”

Shaaak!

This was why people said sword-carrying bastards had no manners. I greeted him warmly, and he started by swinging a weapon.

Whoosh, crack!

“Aaargh!”

I easily dodged the sword and broke the man’s wrist, drawing a scream of pain.

Then I fired Finger Qi at the five guards charging straight at me. Muyaho appeared like the wind right afterward, and the beasts fled with their tails between their legs.

Whoosh. Rumble!

Flames and ash drifted overhead. Massive trees toppled one after another like dominoes.

The tribal chieftain’s face turned deathly pale.

“P-Please, spare me…”

“You’re a tribal chieftain, so of course I’ll spare you. Assuming you answer my questions properly.”

“I-I’ll tell you anything you want to know!”

The chieftain I had captured was the kind of enemy I most wanted to encounter.

People like him knew the value of their own lives, so they willingly confessed even things I had not thought to ask.

And some of the information included in his confession was quite useful.

“…A general mobilization order?”

The chieftain nodded frantically.

“G-Great Chieftain Baeksang has become the temporary Palace Lord, and an army of nearly ten thousand is already stationed in the Inner Palace.”

“Continue.”

“The Miao people are under such strict surveillance that they couldn’t respond, but all of Nanman is moving, centered around the three tribes led by Baeksang.”

Damn it.

I swallowed the curse.

With the Beast Miao King having fled, it had been inevitable that Baeksang would become the temporary Palace Lord.

But this was not a net over heaven and earth meant to capture me. It was a general mobilization order.

*No way.*

An ominous feeling seized my entire body.

Perhaps the picture Dark Heaven had drawn was far larger than any of us—including me—had imagined, and perhaps it was nearing completion.

*If I delay here for even a moment…*

I watched the flames rapidly spreading through Ailao Mountain, then hurriedly launched myself forward.

Into the darkness crouched over Ailao Mountain.

Into the flames.
```
