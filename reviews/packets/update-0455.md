<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0455.txt",
      "sha256": "860a91c091023f5749b3c61e4718a8bb81ea0522be9c69e87e0c2b95eda48772",
      "bytes": 13158
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "88745fe7e2a03c8e0f414d6108c3b916cba08d9c03d8b7e3b6636e585f4cf7d7",
      "bytes": 2968
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "71c096f173283804132896bb203b8bbcc1ddb81d6ad3daf9ca9d3e570c348f32",
      "bytes": 149218
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "556cc72733994d39438c47a9c91657e509f92a1cd78ce7a91ba7057031ca7c0b",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f6b79f56a00f59b3dd82646dec183c102ca3f6f44d29dae546c3e801f465a555",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "4e2ab5275d5bd01d043e29b7e274be8eec0527380a62fee35c5564d3baf3a15a",
      "bytes": 559
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "12e27c790205d8e36657af5c43ec346b3b683072ebb82d15efedfb750203fc92",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "bb08a4b2039d737c9daa341400d98590fb1f6cf9131567760a3a9c6703c7ea2e",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "493d85a7486165e3b6fcb14a7aae8c5047e05f77a614c4b598f3e54e29901c4b",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f559a7066578cc5cfea2246a5c30dd947b5a4cbed5dec3ddec327dea4deb04e2",
      "bytes": 622
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "293b6c4822c0b9684fcd4e0af8bb5d904fcb8592634f834b5089843208033558",
      "bytes": 626
    },
    {
      "path": "characters/Zhuge Gonghu.md",
      "sha256": "6f2469213496c9c6dec8d711bcb811fdb4f934ed2aa70f91347e2b058b5860ab",
      "bytes": 561
    },
    {
      "path": "characters/Zhuge Gyun.md",
      "sha256": "dd0d38d97a37ac07975f130fa182bb4ac945750de6d83de91a615ce8efb43578",
      "bytes": 676
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1efb9ebd3c3fe4e414f3e34636d94b404b7121bbceb12037d34bc69c527a868c",
      "bytes": 143675
    }
  ],
  "estimated_tokens": 12272
}
-->

# Durable State Update — Chapter 455

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 455. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 455. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 455,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 455,
    "continuity_sources": [455],
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
    "Taekyung accepted Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and the Yangtze River Channel League's Hubei strongholds were destroyed, while the Dongting Fisherman disappeared.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's party has escaped Tianling Falls, reached Zaoyang, and is traveling by land toward the Zhuge Clan.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children.",
    "Ju Wongong is an exiled Qingxia Hall young master and distant imperial relative who has been forced to defer to Prince Shangshan's authority.",
    "Honglan is Ju Wongong's Lower District Sect singing courtesan and is concealing her real name."
  ],
  "continuity_sources": [
    454,
    453
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left behind?",
    "Is the Dongting Fisherman a member of Dark Heaven, and who are the other Supreme Peak attackers?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 454,
  "temporary_decisions": [
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon and 일급 낭인 as First Rate wandering martial artist.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, and 구족 as the nine branches of kin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 제갈균    | **Zhuge Gyun**     |
| 하오문    | **Lower District Sect**          |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 제갈공후 | **Zhuge Gonghu** | Former Murim Alliance Chief Strategist and deceased member of the Ten Kings. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 신기묘룡 | **Divine Marvel Dragon** | Epithet of the Zhuge Clan's Lesser Family Head. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 파선지왕 | **Fan-Wisdom King** | Epithet of Zhuge Gonghu. |
| 해사방 | **Sea Serpent Society** | Hubei association formed by fishermen and boatmen; it was annihilated at Red Cliffs. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 제갈균 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Zhuge Gyun as part of the trio and threatens them before a duel. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 제갈균 | 제갈풍 | son_to_father_and_lesser_family_head_to_family_head | Family Head | formal-deferential | Gyun calls out to Zhuge Feng as Family Head when the library appears empty. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 454
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 454
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 451
- **Aliases:** None
- **Role:** The Dongting Fisherman is a Supreme Peak master and public critic of the Yangtze River Channel League who is now the leading suspect in the Donghu Stronghold massacre and a possible Dark Heaven member.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League; his current whereabouts are unknown.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 454
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 454
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 449
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 449
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 452
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

### Zhuge Gonghu.md

# Zhuge Gonghu (제갈공후)

- **Safe through:** Chapter 444
- **Aliases:** None
- **Role:** Former Chief Strategist of the Murim Alliance; a Supreme Peak martial artist known for immortal arts and outstanding formation techniques, one of the Ten Kings and a member of the Three Saints; deceased for more than ten years
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Former Murim Alliance Chief Strategist and member of the Three Saints and Ten Kings.

### Zhuge Gyun.md

# Zhuge Gyun (제갈균)

- **Safe through:** Chapter 445
- **Aliases:** Divine Marvel Dragon
- **Role:** Zhuge Gyun is the current Lesser Family Head of the Zhuge Clan, son of its Family Head Zhuge Feng, and a scholar-styled martial artist who was a finalist in the Star-Array Grand Banquet.
- **Personality:** Analytical, pedantic, and unusually preoccupied with theoretical correctness.
- **Voice:** Polished, formal, and interrogative, treating insults as subjects for precise analysis.
- **Relationships:** Rival finalist alongside Baek Woo and Gung Gibang; exchanges restrained arguments with Taekyung.

## Korean source

```text
＃455화



“쿨럭, 쿨럭.”

새우처럼 허리를 굽힌 노인은 힘겹게 기침을 내뱉었다.

그가 몸을 움직일 때마다, 뇌옥의 차가운 돌바닥으로부터 올라온 한기가 뼛속까지 스며들었다.

그러나 노인의 몸에는 그 어떤 병마(病魔)도 깃들지 못할 것이다.

오랜 세월을 거쳐 단전에 축적된 수 갑자의 공력은 더 이상 주인의 통제를 따르지 않았으나, 연로한 몸뚱어리를 보호하기에는 충분했으니까.

그리고 그러한 사실이 노인을 더욱 분노케 했다.

‘빌어먹을……!’

안 그래도 추한 노인의 이목구비가 악귀처럼 일그러졌다.

한때 대륙을 가로지르며 숱한 피바람을 일으켰던 자신이, 현재는 언제든지 도축할 수 있는 가축과도 같은 취급을 받고 있는 것이다.

“차라리 죽여라! 이런 수모를 줄 바에야 차라리 죽이란 말이다!”

노인이 찢어지는 외침과 함께 몸부림치자 몸을 꽁꽁 옭아맨 쇠사슬이 거슬리는 마찰음을 토해 냈다.

그러나 노인의 단전에 봉해진 공력처럼, 쇠사슬에 연결된 십여 개의 철구 역시 꿈쩍도 하지 않았다.

“이놈드으으을!”

비록 무공이 금제 된 탓에 전과 같은 무위(武威)는 보여 줄 수 없지만 타고난 흉성만큼은 여전했다.

노인은 핏빛 눈동자로 굵은 창살 너머를 노려보았다. 어딘가에서 자신을 비웃고 있을 얼굴들이 환각처럼 눈앞을 스쳤다.

“네놈들이……!”

뼈와 영혼에 아로새겨진 원한.

한날한시에 태어나 일평생을 함께하던 두 형제를 놈들의 손에 잃었고 노인 역시 붙잡혀 온갖 수모를 겪어야 했다.

심지어 가축을 거세하는 것처럼 불알을 으스러트리기까지 했으니, 불구대천의 원수라는 말조차 부족할 지경이다.

“오냐, 그렇다면 어떻게든 살아남아 주마.”

노인의 눈동자에서 화염이 줄기줄기 쏟아졌다.

“반드시 이곳을 빠져나가, 네놈들을 산 채로 갈기갈기 찢어 죽이리라!”

살기 가득한 외침이 지하 뇌옥에 울려 퍼지던 바로 그 순간이었다.

“탈출 공약 잘 들었다. 상당히 감명 깊네.”

“……!”

도대체 언제?

노인은 눈을 깜빡였다. 조금 전 눈앞을 스쳤던 얼굴 중 하나가 어느새 뇌옥의 창살 너머로 그를 빤히 바라보고 있었다.

청년의 입가에 걸린 웃음에 가슴 한구석이 서늘해진다.

“네, 네놈은…….”

“터진 곳은 괜찮냐. 오줌 쌀 때마다 아플 것 같은데.”

노인은 하마터면 자신도 모르게 고개를 끄덕일 뻔했다.

하지만 상대는 그의 살생부 맨 윗줄에 나란히 적힌 이름 중 하나. 무슨 수를 써서라도 반드시 죽여야 할 놈이다.

노인은 번들거리는 눈으로 창살 너머의 청년을 노려보았다.

“궁금하면 당장 금제를 풀어라. 노부가 친히 알려 줄 테니.”

“글쎄, 그건 별로 궁금하지는 않고…….”

청년, 진태경의 입가에 맺혀 있던 웃음이 씻은 듯이 사라졌다.

“네가 알고 있는 다른 모든 것들을 알려줘야 할 거다, 삼괴(三怪).”



* * *



현대에서 포로 고문은 위법 행위로 분류되며, 이에 관한 사실이 알려진다면 강대국이라 하더라도 국제 사회에서 지탄의 대상이 된다.

하지만 이곳은 무림이다. 법의 권위는 흐릿하고, 사람과 짐승의 경계는 희미하다.

그리고 내 시선으로 본 삼괴는 사람의 모습을 한 짐승에 가까웠다.

‘망설일 이유가 없지.’

놈은 오랜 세월 동안 수없이 많은 인명을 해쳤다.

단순히 자신의 살심(殺心)을 충족시키기 위해 수백, 수천이 넘는 목숨을 거둔 악귀인 것이다.

지금껏 놈이 걸어온 피의 길과 이 축축하고 어두운 지하 뇌옥에 얄팍한 도덕심 따위는 존재하지 않는다.

나는 차가운 눈빛으로 삼괴를 응시했다.

“꺼흑, 흐으으…….”

철제 의자에 묶인 채 축 늘어진 몸뚱어리.

벌어진 입가에서는 피가 섞인 타액이 흐르고, 온통 찢기고 꺾여 나간 사지는 고통으로 경련을 일으킨다.

“어떻습니까?”

내 물음에, 삼괴를 옆에서 유심히 살피던 노인이 피 묻은 쇠꼬챙이로 머리를 긁적였다.

“이미 한계입니다. 이 정도면 놈이 아는 사실은 전부 토설했다고 봐야 합니다.”

고문 실력을 경지로 나누자면 나는 고작해야 일류, 눈앞의 노인은 초절정 고수다.

어찌나 포로들을 효과적으로 잔혹하게 다루었는지, 정마대전 당시 그의 고문 기술을 눈여겨본 파선지왕(芭扇知王) 제갈공후가 종전 후 제갈세가로 초빙했을 정도라고 했다.

“만약 여기서 더 고문을 진행한다면…….”

“백이면 백, 죽겠지요. 그리고 이놈을 더 족쳐 봤자 나올 것이 없다는 게 이 늙은이의 소견입니다.”

노인의 목소리에는 확신으로 가득 차 있었다.

그리고 반쯤 시체가 된 삼괴의 모습과 금방이라도 꺼질 것 같은 놈의 기운이 노인의 말에 한층 힘을 실어 주었다.

하지만 이것으로는 부족하다. 나는 반쯤 넋이 나간 채 몸을 떠는 삼괴를 응시했다.

‘이게 전부라고?’

사실 삼괴가 아는 정보가 아주 없는 것은 아니었다.

처음 몇 시진은 악으로 버티더니, 고문이 막바지에 다다르자 죽간 다섯 개를 글자로 빼곡하게 채울 만큼 말이 많아졌으니까.

그러나 그중 대부분은 쓸모없거나 지나간 일에 불과했고, 가장 필요한 정보는 마지막까지 나오지 않았다.

‘지금 호북성에서 일어나고 있는 일련의 사건들.’

해사방이 몰락하고 동정채가 몰살당했다.

인명 피해로는 이미 천 명이 훌쩍 넘어가며 그중에는 무공이라고는 일초 반식도 모르는 무고한 양민들도 포함되어 있었다.

이런 미친 짓을 벌일 만한 잔인무도함과 힘을 갖춘 집단은…… 내가 알기로 단 한 곳뿐이다.

‘암천.’

문제는 놈들의 꼬리를 잡을 수 없다는 것이다. 어디서, 어떤 식으로 해사방과 동정채를 공격했는지. 이동진을 감춰 둔 위치는 어디인지.

그리고 마지막, 이와 같은 만행을 저지른 놈들은 지금 어디에서 무슨 짓을 벌이고 있는지.

“이대로는 곤란하지.”

작은 중얼거림과 함께 혼절한 삼괴의 완맥을 틀어쥐었다. 무료한 표정으로 서 있던 노인이 황급히 만류했다.

“대협. 그랬다가는!”

“괜찮습니다. 죽이려는 게 아니니까.”

나는 삼괴의 완맥으로 공력을 흘려보냈다. 열양지기의 따스한 온기가 혈도를 타고 스며들자, 창백하던 놈의 뺨에 붉은 핏기가 돌고 눈꺼풀이 들어 올려졌다.

중심을 잡지 못하고 떨리던 회색 눈동자에 내 얼굴이 비친다.

“너, 너는…….”

“정신 차려야지. 아직은 너무 이르니까.”

“차, 차라리 죽여라.”

“알고 있는 걸 전부 말한다면 당신이 원하는 대로 될 거야. 하지만 끝까지 충신 흉내를 낸다면…….”

미약하게 흘려보내던 공력에 힘을 실었다. 흡, 하는 신음과 함께 삼괴가 눈을 부릅뜬다.

이미 안팎으로 만신창이가 된 놈은 열양지기의 열기를 감당하지 못했다.

“끄윽, 꺽.”

고통으로 헐떡이는 숨소리에 고기 익는 듯한 냄새가 섞여 나왔다. 하지만 나는 흔들림 없는 눈빛으로 삼괴를 응시했다.

“내가 원하는 대답이 아니야.”

“노부는, 나는 이미 모든 걸 말했다.”

“그것도 아니고.”

“크헙. 제, 제발.”

“버티는 걸 보니 죽으려면 아직 한참 남았네. 내가 듣지 못한 정보처럼.”

“도대체 더 이상 무엇을 말한단 말이냐……!”

“이미 몇 번이나 말했잖아. 암천에 관한 모든 것. 호북성에서 벌어지는 일과 동정어옹.”

“모른다 하지 않았, 쿠웨에엑!”

한 마디, 한 마디를 주고받을수록 열양지기의 힘도 강해졌다.

눈을 하얗게 뒤집어 깐 채 파르르 떨던 삼괴의 입술 사이로, 비명 같은 외침이 터져 나왔다.

“죽여! 어서 죽여라! 내 원혼이 되어서도 네놈들의 뼈와 살을 씹어……!”

젠장. 여기까지다.

나는 거칠게 흘려보내던 공력을 회수했다. 동시에 경련을 일으키던 삼괴가 실 끊어진 인형처럼 축 늘어진다.

기세를 바꿔 부드럽게 놈의 신체 내부를 안정시키자, 미리 준비하고 있던 노인이 빠르게 맥을 짚고 상태를 확인했다.

“명줄이 긴 놈이군요. 저승길 문턱에서 멈췄습니다.”

알고 있다. 놈을 죽이지 않기 위해 최대한 힘 조절을 했으니까.

‘이대로 죽여서는 안 되는 놈이지.’

삼괴는 전대의 대마두이자 암천에 속한 초절정 고수.

그런 놈을 살려서 하남으로 호송한다면, 더욱 많은 정보를 알아낼 방법이 있을지도 모른다.

물론 저 죽간에 적힌 것이 삼괴가 아는 전부일 가능성도 무시하지 못한다.

아니, 아마 그럴 가능성이 크다.

‘이 정도까지 했는데도 말하지 않았다는 건…… 이게 전부라는 놈의 말이 사실일 수도 있다.’

초절정 고수의 심력과 인내심은 상상을 초월한다.

그런 삼괴가 원수나 다름없는 내게 멈춰 달라 애원하고, 차라리 죽여 달라며 울부짖는 지경까지 왔음에도 끝까지 자신의 주장을 고수한 것이다.



‘나, 나는. 우리 형제는 마군의 휘하에서 명령에 따랐을 뿐이다! 암천의 총단과 다른 곳에서의 일에 관해서는 아무것도 모른단 말이다!’



고문 도중 몇 번에 걸쳐 나왔던 삼괴의 외침을 떠올리며, 나는 한 사람의 이름을 불렀다.

“궁기방. 새로운 소식은?”

쇠창살에 몸을 기대고 있던 궁기방이 고개를 저었다.

“없다. 본 방의 호북 분타에서도 아직 놈들을 찾지 못하고 있어.”

“초절정 고수 셋. 혹은 수백이 넘는 사람과 선박이 동원되었을 거야. 아무래도 눈에 띌 수밖에 없을 테니 외지인들을 위주로 찾는다면 가능성이…….”

“이미 그러는 중이지만 쉽지 않아. 호북성의 장강은 하루에도 수백 척이 넘는 대형 선박이 오가고, 육로를 통해 이동하는 자들은 셀 수도 없다. 하물며 족히 열흘 전의 일이라면…… 오히려 어떤 방식으로든 호북성을 빠져나갔을 가능성도 커.”

“빌어먹을.”

변방 취급받는 산서성과 달리 호북성은 중원이라 부르는 지역 중 하나이며 여러 방면의 산업이 잘 발달한 곳이다.

안 그래도 넓은 땅에 장사치며 여행객들이 쉴새 없이 드나들면 개방이라 해도 난항을 겪을 수밖에 없었다.

내 눈치를 살피던 궁기방이 조심스럽게 입을 열었다.

“청풍 소협과 혁무진이 하오문에 갔으니 그쪽을 기대해 보는 수밖에. 본 방의 호북 분타와 크게 다를 것 같지는 않지만…… 희망을 품어 봐야지.”

궁기방의 말이 맞았다. 반 시진 후, 제갈세가로 돌아온 청풍과 혁무진의 손에는 커다란 죽간이 들려 있었다.

그리고 죽간을 묶은 끈에 적힌 한 사람의 별호.

동정어옹(洞庭漁翁).

“이건…….”

마른침을 꿀꺽 삼킨 혁무진이 입을 열었다.

“하오문에서 동정어옹과 모종의 마찰이 있었던 모양입니다. 문주의 지시로 수년 전부터 예의주시하고 있었다는데…… 우선 직접 보시는 게 나을 것 같습니다.”

나는 빠르게 죽간에 담긴 내용을 훑었다.

동정어옹에 대한 기록은 자그마치 삼 년 전부터 시작되었고, 내 손에 들린 이 죽간은 그 기록 중의 일부였다.

그리고 한 달 전부터 바로 오늘까지 적혀 있는 죽간의 기록은 단 하나의 사실을 알려 주었다.

‘동정어옹은 아직 호북성 안에 있다.’

그렇다는 건…….

촤르륵!

죽간을 품에 쑤셔 넣은 나는 망설임 없이 한 사람을 찾아갔다.

가주인 제갈풍을 대신하여 지시를 내리던 제갈세가의 소가주. 신기묘룡 제갈균이 내 요란한 방문에 눈을 크게 떴다.

“갑자기 무슨 일이십니까? 제 선조이신 제갈무후께서는 군자란 늘 몸가짐이 바르며 고요해야 한다고 하셨는데…….”

“닥치고. 사람들 준비됐지?”

“아버, 아니 가주님께서 말씀하셨던 이들이라면 이미 떠날 채비를 마쳤습니다. 지금 당장 출발하시게요?”

“어. 그런데 나는 다른 곳에 먼저 들러야 할 것 같다.”

“예? 어디를…….”

“동정호.”
```

## Final English reading copy

```markdown
# Chapter 455

“Cough, cough.”

Hunched over like a shrimp, the old man coughed with difficulty.

Whenever he moved, the cold rising from the prison’s stone floor seeped into his bones.

Yet no illness could ever take root in the old man’s body.

The several jiazi[^1] of internal energy accumulated in his dantian over the years no longer obeyed their master’s control, but they were more than enough to protect his aged body.

And that fact only made the old man angrier.

*Damn it…!*

The ugly old man’s features twisted like those of an evil spirit.

He had once crossed the continent and unleashed countless storms of blood. Now, he was being treated like livestock that could be slaughtered at any moment.

“Then kill me! If you’re going to subject me to this humiliation, just kill me already!”

As the old man writhed and let out a tearing scream, the chains binding his body tightly grated against one another.

Yet just like the internal energy sealed within his dantian, the dozen or so iron balls connected to the chains did not move an inch.

“You bastaaaardsss!”

Although his martial arts had been sealed and he could no longer display the same martial might as before, his innate viciousness remained unchanged.

The old man glared through the thick iron bars with bloodshot eyes. Faces that must have been laughing at him somewhere flashed before his eyes like hallucinations.

“You bastards…!”

A grudge etched into his bones and soul.

They had taken the lives of his two brothers, who had been born on the same day and hour and spent their entire lives together. The old man himself had been captured and forced to endure every kind of humiliation.

They had even crushed his testicles as though castrating livestock. Calling them enemies who could never coexist was not enough to describe it.

“Fine, then. I’ll survive somehow.”

Flames poured from the old man’s eyes.

“I’ll escape this place no matter what, then tear you bastards to pieces and kill you while you’re still alive!”

It was at that exact moment that his shout, brimming with killing intent, rang through the underground prison.

“I heard your escape pledge. Quite moving.”

“……!”

When had he—

The old man blinked. One of the faces that had flashed before his eyes moments ago was now staring at him from beyond the prison bars.

A chill ran through one corner of his chest at the smile hanging from the young man’s lips.

“You—you’re…”

“How’s the busted part? Must hurt every time you take a piss.”

The old man almost nodded without realizing it.

But the young man was one of the names written side by side at the very top of his kill list. He was someone the old man had to kill by any means necessary.

The old man glared at the young man through the bars with gleaming eyes.

“If you’re curious, lift the seal on my martial arts right now. I’ll show you myself.”

“I’m not particularly curious about that…”

The smile on the young man’s lips—Jin Taekyung’s lips—vanished as if wiped away.

“You’ll have to tell me everything else you know, Three Fiends.”

* * *

In the modern world, torturing prisoners was classified as an illegal act. If such a fact became known, even a Great Nation would be condemned by the international community.

But this was the Murim. The authority of the law was vague, and the boundary between people and beasts was blurred.

And in my eyes, the Three Fiends were closer to beasts wearing human faces.

*There’s no reason to hesitate.*

He had harmed countless people over the course of many years.

He was a fiend who had taken hundreds, even thousands, of lives simply to satisfy his own killing urge.

There was no room for shallow morality in the bloody path he had walked or in this damp, dark underground prison.

I stared at the Three Fiends with cold eyes.

“Guhk, hnggg…”

His body hung limply, bound to an iron chair.

Bloodstained saliva dripped from his open mouth, and his limbs, torn and broken all over, spasmed with pain.

“How is he?”

At my question, the old man who had been closely examining the Three Fiends beside him scratched his head with a bloodstained iron skewer.

“He’s already reached his limit. At this point, we must assume he has confessed everything he knows.”

If torture skill were divided into realm stages, I was barely First Rate. The old man before me was a Supreme Peak master.

He had handled prisoners so effectively and cruelly that Zhuge Gonghu, the Fan-Wisdom King, had taken notice of his torture techniques during the Great Faction War and invited him to the Zhuge Clan after the war ended.

“If we continue torturing him…”

“He will certainly die. And this old man’s opinion is that beating him any further will not produce anything else.”

The old man’s voice was full of certainty.

The appearance of the Three Fiends, who had become half a corpse, and his aura, which seemed ready to go out at any moment, lent even greater weight to those words.

But it was not enough. I stared at the Three Fiends, who was trembling as though half his soul had already left his body.

*Is this really everything?*

It was not as though the Three Fiends had known nothing.

He had held out through sheer spite for the first few shichen,[^2] but once the torture reached its final stages, he had talked enough to fill five bamboo slips with closely packed writing.

Yet most of it was useless or concerned events from the past, and the information I needed most had never come out.

*The series of incidents happening in Hubei Province right now.*

The Sea Serpent Society had fallen, and Donghu Stronghold had been massacred.

The casualties had already far exceeded a thousand, including innocent commoners who did not know even a single martial move or half a stance.

As far as I knew, there was only one group with the ruthlessness and power to commit such madness.

*Dark Heaven.*

The problem was that I could not get hold of their trail.

Where and how had they attacked the Sea Serpent Society and Donghu Stronghold? Where had they hidden the Moving Formation?

And finally, where were the people who had committed this atrocity now, and what were they doing?

“This won’t do.”

With a quiet mutter, I seized the unconscious Three Fiends by the wrist. The old man, who had been standing there with a bored expression, hurriedly tried to stop me.

“Great Hero. If you do that—!”

“It’s fine. I’m not trying to kill him.”

I sent internal energy through the Three Fiends’ wrist. As the warm heat of Scorching Yang Qi seeped along his acupoints, color returned to the man’s pale cheeks and his eyelids lifted.

My face was reflected in his gray eyes, which trembled without being able to focus.

“You—you’re…”

“You need to wake up. It’s still too soon.”

“J-just kill me.”

“If you tell me everything you know, you can have what you want. But if you keep pretending to be a loyal subject…”

I increased the strength of the internal energy I had been sending through him. The Three Fiends’ eyes flew open with a sharp gasp.

His body was already ruined inside and out. It could not withstand the heat of Scorching Yang Qi.

“Ghk, gack.”

His painful, gasping breaths carried the smell of meat being cooked. But I continued staring at the Three Fiends without wavering.

“That’s not the answer I want.”

“This old man—I’ve already told you everything.”

“Not that, either.”

“Ghk. P-please.”

“Judging by how well you’re holding out, you’re still a long way from dying. Just like the information I haven’t heard yet.”

“What else in the world are you asking me to say…?”

“I’ve already told you several times. Everything about Dark Heaven. The events happening in Hubei Province, and the Dongting Fisherman.”

“I told you I don’t know—kuweeegh!”

The more we exchanged words, the stronger the Scorching Yang Qi became.

The Three Fiends trembled violently with his eyes rolled white, then a scream burst through his lips.

“Kill me! Kill me already! Even as a vengeful ghost, I’ll chew through your bones and flesh…!”

Damn it. This was as far as I could go.

I roughly withdrew the internal energy I had been sending through him. At the same time, the Three Fiends, who had been convulsing, went limp like a puppet with its strings cut.

I changed the flow of energy and gently stabilized his insides. The old man, who had been waiting nearby, quickly checked his pulse and examined his condition.

“He’s a hard one to kill. He stopped right at death’s door.”

I knew. I had controlled my strength as much as possible to avoid killing him.

*This man can’t die here.*

The Three Fiends was a great fiend from the previous generation and a Supreme Peak master belonging to Dark Heaven.

If we kept him alive and escorted him to Henan, there might be a way to learn even more information.

Of course, I could not rule out the possibility that the writing on those bamboo slips contained everything the Three Fiends knew.

No. That possibility was probably quite high.

*Even after all this, he still refused to talk… That could mean his claim that this is everything was true.*

The mental strength and endurance of a Supreme Peak master were beyond imagination.

Even after the Three Fiends had reached the point of begging someone practically no different from his mortal enemy to stop and screaming for death, he had clung to his story until the very end.

*I—I and my brothers only followed orders under the Demon Lord! I don’t know anything about Dark Heaven’s headquarters or what happened elsewhere, I tell you!*

Remembering the Three Fiends’ cries during the torture, I called out one man’s name.

“Gung Gibang. Any news?”

Gung Gibang, who had been leaning against the iron bars, shook his head.

“Nothing. Our Hubei branch still hasn’t found them.”

“Three Supreme Peak masters. Or hundreds of people and ships must have been mobilized. They couldn’t have avoided attracting attention, so if we focus on outsiders, there should be a chance…”

“We’re already doing that, but it isn’t easy. More than several hundred large ships travel along the Yangtze in Hubei every day, and there are too many people moving by land to count. If it happened a good ten days ago… there’s an even greater chance they escaped Hubei by some means.”

“Damn it.”

Unlike Shanxi Province, which was treated as a borderland, Hubei Province was one of the regions called the Central Plains, and various industries were well developed there.

With merchants and travelers constantly passing through such a vast land, even the Beggars’ Sect could not help but struggle.

Gung Gibang, who had been watching my expression, cautiously opened his mouth.

“Cheongpung and Hyuk Mujin went to the Lower District Sect, so we have no choice but to hope they found something. It probably won’t be much different from our Hubei branch’s findings, but we should hold on to hope.”

Gung Gibang was right. Half a shichen later, Cheongpung and Hyuk Mujin returned to the Zhuge Clan with a large bamboo slip in their hands.

And written on the cord binding the slip was one man’s sobriquet.

Dongting Fisherman.

“This…”

Hyuk Mujin swallowed dryly before speaking.

“It seems the Lower District Sect had some kind of friction with the Dongting Fisherman. They said they had been keeping a close eye on him for several years on the Sect Leader’s orders… It would probably be best if you looked through it yourself.”

I quickly skimmed the contents of the bamboo slip.

The records on the Dongting Fisherman began no fewer than three years ago, and the slip in my hands contained only a portion of them.

And the records from one month ago until today revealed a single fact.

*The Dongting Fisherman is still in Hubei Province.*

That meant…

Rattle!

I shoved the bamboo slip into my robe and went without hesitation to find one man.

Zhuge Gyun, the Divine Marvel Dragon—the Zhuge Clan’s Lesser Family Head, who had been issuing orders in place of the Family Head, Zhuge Feng—opened his eyes wide at my noisy arrival.

“What happened all of a sudden? My ancestor Zhuge Wuhou said that a junzi[^3] should always maintain proper bearing and remain tranquil…”

“Shut up. Are the people ready?”

“The people my fath—no, the Family Head mentioned are already prepared to leave. Do you intend to depart immediately?”

“Yeah. But I think I need to stop somewhere else first.”

“Pardon? Where…?”

“Dongting Lake.”

[^1]: A **jiazi** is a traditional sixty-year cycle.

[^2]: A **shichen** is a traditional time unit of roughly two hours.

[^3]: A **junzi** is the Confucian ideal of a morally upright gentleman.
```
