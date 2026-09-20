<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0534.txt",
      "sha256": "b1a257233f614f194d151dd6d88001eaecc32b4308dc47beb98a838c4fee9c77",
      "bytes": 14050
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1652c3e5b541717e5a00461608b95f9766c1e612271a5e3b0a298549f2d58aa8",
      "bytes": 3198
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7b087cd648d0c3c947ecec4e71461d177adf6b761baafa164eda686d57f5a17b",
      "bytes": 170013
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "c7bae3d6df46c98b4d7b6c0445ef43eb7acf996d195904861f92db2267dbdfe1",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "8cab719d1351a777aba8ac1a2b4d85e4adb1faf51b41deab89b1c5a43381b1f8",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ec2e8b1e5ff93bd743ef60d07dc64cb922b3585fa2e38d366f1aab4adfe0ab85",
      "bytes": 2021
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "6f7d34379740d7760a88145737226787c50e123001e4cd3605782fa4188177d3",
      "bytes": 1210
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9c1d0db90f9b0bf5a7a22142981107e515d61060cc124adac896a35792b96c16",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "8f80e040940234492db407d4c01f85b9b52e9c3a2b54c9779ba2f6a11ec4c35a",
      "bytes": 910
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "c4412c858b518075e453d51ff0a0507786d77e9eee630e068483203c58360f3d",
      "bytes": 683
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "a14c10905427ab635fcb1e489164f624383187b7ee0e10477a7c4bcaaa4dffeb",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "dd7630d4729a631dc6c59ab65de10eee399ec9838aa55ddb2f02e9954f824557",
      "bytes": 889
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "8a8db91f535342b3359df7d0f1d9b760934378244e15524fa203402d7229ab5e",
      "bytes": 403
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "313388f14c75dbd3e58a53cfafead300f7d9b321fb3e9756d3f9fc2551525c91",
      "bytes": 160707
    }
  ],
  "estimated_tokens": 13351
}
-->

# Durable State Update — Chapter 534

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 534. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 534. Profile updates may replace only one
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
  "chapter": 534,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 534,
    "continuity_sources": [534],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Jin Taekyung and Cheongpung's prominent role in raising the Murim Alliance flag made them objects of intense attention among Murim factions.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Cheongpung has recently lost his appetite while refining it.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Ju Hwaran is with Taekyung at Gowolru, Song Ilseom remains her direct escort, and she has revealed that Sama Pyo was her former fiancé."
  ],
  "continuity_sources": [
    533,
    532
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "What happened between Ju Hwaran and Sama Pyo, and why did their engagement end?"
  ],
  "safe_through": 533,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, and 학우 as Hak Woo.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, and monster-comparison humor.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 은비화    | **Dagger Hidden Flower**      | Ju Hwaran      |
| 암천     | **Dark Heaven**                  |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 상태               | **Status**                     |
| 감숙     | **Gansu**              |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 혈곤 | **Blood Cudgel** | Sobriquet of Do Sangho. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 황보세가 | **Hwangbo Family** | Hwangbo Ak's established martial family and the long-standing hegemon of Shandong. |
| 고월루 | **Gowolru** | Three-story inn where the meeting was scheduled. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 송일 | Jin Family host to visiting Zhongnan Elder | Senior | formal and guarded | Jin Wikyung respectfully asks Song Il's name before the dispute escalates. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 궁기방 | 진위경 | martial_companion_to_family_head | Great Hero Jin | familiar and polite | Asks Jin Wikyung not to exclude the Beggars' Sect from the defense. |
| 소문주 | 혈곤 | Young Sect Leader addressing a hostile Peak master | Blood Cudgel | Informal and contemptuous | Calls him 혈곤 while offering silver in exchange for his submission. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |

## Listed compact profiles

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 533
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 533
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 532
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 527
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 532
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 533
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal and now investigating at least two escort captains suspected of aiding his scheme.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 533
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate and a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands Taishan, a giant subordinate; Ju Hwaran was his former fiancée; he is the son of a man who previously told him about Jung Ho.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 533
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 533
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau and one of its Dragon-Phoenix Three Escorts who developed his martial ability on battlefields, was known as the Soul-Chasing Guest ten years ago, and plans to remain one more month to help Ju Hwaran purge traitors before seeking an elixir for Ju Hogun in Xianyang.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 533
- **Aliases:** None
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃534화



짤랑. 탁.

종소리를 마지막으로 객잔의 문이 닫히자, 계단을 내려오면서부터 사정없이 뒤통수를 찔러 대던 시선들도 함께 사라진다. 하지만 사마표는 이미 알고 있었다. 이것은 끝이 아니라 또 다른 시작이라는 것을.

“방금 고월루에서 나온 저 두 놈…….”

“맞지?”

“확실해. 흑룡마문의 소문주인 흑룡도 사마표다. 옆에 있는 커다란 놈은 칠 주야 전에 혈곤의 골통을 으깬 그 괴물이고.”

“아까는 황보세가의 소가주와 다툼이 있었다는데, 요즘 같은 시기에 계속해서 소란을 피우다니. 쯧쯧.”

“놔두게. 그러니 사마외도 아닌가. 암천을 몰아내기 위해서는 저런 것들 손이라도 빌려야지.”

“도무지 마음에 안 들어. 언제 뒤통수를 칠 줄 알고?”

“내 말이 그 말……. 쉿. 커다란 놈이 이쪽을 보고 있네.”

이쪽을 주시하는 수많은 시선과 수군거림. 아무리 작게 말한다 해도 마음만 먹는다면 충분히 들리고도 남는 거리였다. 하지만 귓가를 파고드는 사람들의 목소리에도, 걸음을 옮기는 사마표의 표정은 무덤덤했다.

‘이상할 것도 없지.’

이미 너무나도 익숙한 상황이다. 흑룡마문의 본거지이자 막강한 영향력이 미치는 감숙(甘肅)에서조차 그랬다. 태어날 때부터 따라다녔던 사마외도라는 꼬리표는 그에게 있어 벗을 수 없는 굴레와도 같았다.

“후욱.”

옆에서 거친 콧바람이 흘러나왔다. 퉁방울만 한 눈동자를 뒤룩뒤룩 굴리는 태산을 힐끗 본 사마표가 입술을 달싹였다.

- 그만두어라.

순간, 등에 매어 놓은 대초자곤(大梢子棍)을 향해 미끄러지던 태산의 손이 멈칫했다. 사마표가 흘려 보내는 전음에 힘이 실렸다.

- 태산. 네 이 녀석.

- ……알겠다, 주군. 태산이, 참는다.

- 옳지. 착하구나.

- 태산이 말 잘 듣는다. 주군 좋다. 헤헤.

언제 그랬냐는 듯 헤벌쭉 웃어 보이는 태산의 모습에 사마표가 실소를 흘렸다.

- 그래, 나도 네가 참 좋다.

- 태산이. 오늘 칭찬 많이 들었다.

- 오호. 그 고마운 이가 누구더냐?

- 응. 열화신룡이 칭찬해 줬다.

사마표의 걸음이 느려졌다.

- 열화신룡 진태경?

- 맞다. 진태경. 나보고 착한 아이라고 했다.

- 그가 마음에 든 모양이로구나.

- 좋다. 엄청 강하고. 착하다. 태산이 칭찬해 줬다.

사마표는 신이 나서 성큼성큼 걷는 태산의 옆모습을 물끄러미 바라보았다.

뛰어난 무재와 신력(神力)을 타고났지만, 오래전 불의의 사고로 머리를 다쳐 어린아이나 다름없는 녀석이다. 그때의 기억이 있어서일까. 낯을 많이 가리고 경계심이 심하여 사마표를 제외하면 누구에게도 쉽게 마음을 열지 않았다.

‘그런 녀석이 나를 제외한 다른 누군가를 이렇게 좋게 평가하는 건 흔치 않은 일인데.’

열화신룡 진태경.

방만하면서도 능청스럽던 청년의 모습이 눈앞을 스쳤다. 잔잔한 표정과 목소리 안에 숨겨진, 끝을 짐작할 수 없이 강대한 기세도 함께.

‘신룡(神龍)이라 불리는 이유가 있었어.’

천하는 넓고 고수는 많다. 세인들은 십봉룡을 무림 최고의 후기지수들이라 부르며 선망을 시선을 보냈지만, 사마표는 단 한 번도 그들을 인정한 적이 없었다.

‘자신들이 쳐 놓은 울타리 안에서 부르는 허명일 뿐이지.’

울타리 밖의 존재들은 배척당하는 것이 현실이다. 의협(義俠), 정도(正道)와 같은 간질거리는 단어를 앞세워 뻔뻔한 짓을 벌이는 정파 무림인을 한두 명 만나 본 것이 아니다.

하지만…….

‘달랐지. 그는 확실히 달랐어.’

열화신룡 진태경.

비록 짧은 만남이었지만 사마표는 확실히 깨달았다. 진태경은 특별한 존재다. 후기지수를 아득히 벗어난 엄청난 무위도 그렇지만, 그를 더욱 특별하게 느껴지도록 만든 것은 바로 남들과 다른 태도였다.

사마표의 뇌리에 조금 전 진태경과 나누었던 대화가 스쳐 지나갔다.



‘흑룡마문(黑龍魔門)이라고 들어 봤는지 모르겠군.’

‘그래서, 그 흑룡마문의 소문주씩이나 되는 분이 여긴 무슨 일로?’

‘그게 끝인가?’

‘그럼 뭐가 더 필요한데?’

‘……!’



예상치 못한 반문이었고, 그래서 순간 말문이 막혔다. 그것은 그가, 흑룡마문의 소문주 사마표가 지금껏 걸어온 길에는 없던 질문이었으니까.

‘무엇이 더 필요한가. 무엇이 더…….’

마음속으로 뇌까리는 생각은 입 밖으로 흘러나가지 않는다. 소리 없이 입술을 달싹거리던 사마표는 고개를 돌려 태산을 바라보았다.

- 한 가지만 물어보마.

- ……?

- 만약에, 열화신룡 진태경과 싸워야 한다면 넌 어찌하겠느냐?

그야말로 찰나였다. 싱글벙글 웃고 있던 태산의 얼굴이 딱딱하게 굳어 버린 것은. 그리고 이어 한 치의 망설임조차 없는 전음이 흘러나왔다.

- 태산이. 주군에게 큰 은혜 입었다. 주군이 명한다면 누구와도 싸운다.

- 진태경이 좋다고 하지 않았더냐.

- 진태경. 마음에 든다. 하지만 주군만큼은 아니다. 태산이. 주군의 명이라면 목숨을 바쳐 따른다.

- 그래, 그렇구나.

작게 실소를 흘린 사마표가 고개를 내저었다.

- 그거면 충분하다. 착한 녀석 같으니.

- 태산이, 착하다. 그리고 착한 태산이. 배고프다.

울상을 지으며 힐끗거리는 덩치 큰 어린아이의 모습에, 사마표는 소리 내어 웃었다.

“그래. 어디든 가자꾸나. 오늘 밤은 원 없이 배 터지게 먹여 주마.”

“헤헤. 주군이 약속했다. 태산이 믿는다.”

“오냐.”

“그런데 주군.”

“음?”

“아까 그 여자. 예뻤다. 많이 예뻤다. 누구인가?”

순간 사마표의 발걸음이 우뚝 멈췄다. 이상함을 느낀 태산이 고개를 갸웃거렸다.

“주군?”

“아니다. 그래, 그리 예쁘더냐.”

“응. 예쁘고, 착했다.”

“열 길 물속은 알아도 한 길 사람 속은 모른다고 했다. 잠깐 얼굴만 본 것으로 숨겨진 마음을 어찌 알겠느냐.”

태산이 세차게 고개를 내저었다.

“아니다! 예쁜 여자는 착하다!”

“……큰 소리로 얘기하지 말거라. 사람들 쳐다본다.”

“인정해라! 태산이 말이 맞다! 예쁘면 착하다!”

“후우. 빌어먹을 녀석 같으니. 먼저 간다.”

“주군! 주군!”

태산의 애탄 외침을 뒤로하고 걸음을 옮기는 사마표의 얼굴은 모래처럼 건조했다.

‘주화란……. 이런 곳에서 만나게 될 줄은 몰랐는데.’

우연인지, 인연인지 사마표로서는 도무지 알 수 없었다.

하지만 한 가지는 확실하다. 짧은 시간이나마 정혼자였던 여인, 은비화 주화란은 그와 관련된 모든 것을 악연(惡緣)이라 생각하리라는 것.

‘악연이라……. 틀린 말은 아니지.’

사마표의 눈빛이 차갑게 가라앉았다.



* * *



그날의 식사는 순조롭게 마무리되었다. 주인장의 극진한 환대와 쏟아지는 사람들의 관심 아래 객잔을 빠져나온 우리는 서로를 향해 작별 인사를 건넸다. 아니, 정확히는 우리가 아니라 주화란이라고 해야 맞겠지.

“이만 가 봐야 할 것 같아요. 표국 관련해서 처리해야 할 일이 있어서.”

쿡.

은밀하게 옆구리를 찌르는 궁기방의 손길에, 잠시 멍하니 서 있던 나는 반사적으로 입을 열었다.

“아, 네. 안녕히 가세요.”

“네. 진 대협도요.”

쿡.

젠장. 이게 아닌가 본데.

“저기, 주 소저.”

“네?”

“제가 처소까지 바래다 드릴까요?”

“말씀을 감사하지만 괜찮아요. 들리는 말로는 수련할 시간도 부족하시다던데.”

“어. 누구한테 들으셨어요? 사실 요새 좀 바쁘긴 했거든요.”

쿡. 쿡쿡.

고맙다, 이 새끼야.

나는 재차 경로 이탈을 알리는 궁비게이션의 손길에 따라 운전대를 꽉 움켜쥐었다.

“그래도 이상한 놈들이 접근할지도 모르니까 제가 바래다드리는 편이…….”

“아하하. 아니에요. 저도 무인인걸요.”

“아, 그랬죠. 무시하려던 건 아닌데 이게 참.”

“아니에요. 진 대협에 비하면 무공이 부족한 건 사실이니까. 그리고 여기 송 호위도 있고요.”

그러자 송일섬이 무뚝뚝한 목소리로 말했다.

“그런 놈들이 접근하면 단칼에 베어 버릴 테니, 시답잖은 걱정은 하지 마라.”

“들으셨죠?”

“……어, 네. 들었습니다.”

쿡쿡. 쿡쿡쿡쿡!

옆구리에 구멍 뚫리겠다, 이 자식아.

하지만 이번에는 딱히 할 말이 생각나지 않았다. 가뜩이나 복잡한 머릿속에서 온갖 말들이 뒤섞이다가 흩어졌다. 그리고 바로 그 잠깐의 침묵은 타이밍이 지났음을 의미했다.

“그럼 오늘은 이만 들어갈게요. 다음에 또 봬요.”

주화란이 싱긋 웃으며 신형을 돌린다. 섬단 같은 머리카락이 흔들리고 그 사이로 흘러나온 은은한 향기가 공기를 타고 전해졌다. 내가 말없이 서서 멀어지는 두 사람의 뒷모습을 바라보던 그때였다.

“이거 진짜 병신이네.”

“와. 정말 상당하십니다, 조장님.”

“…….”

어떤 놈들인지 확인해 볼 필요도 없다. 나는 처연한 눈빛으로 궁기방과 혁무진을 바라보았다.

“어디서부터 어떻게 잘못된 거냐, 이거.”

두 놈이 기다렸다는 듯 동시에 대답했다.

“주 소저 얼굴에 음식 뱉었을 때부터.”

“애초에 조장님 자체가 잘못된 거 아닐까요.”

각기 다른 대답이지만 확실한 공통점이 두 가지 있다. 첫째는 사람 열받게 만든다는 것. 두 번째는 뭐라 반박하기 힘든 사실이라는 것.

“젠장.”

나는 애꿎은 땅바닥만 걷어찼다. 솔직히 억울한 마음도 든다. 아니, 어떻게 그 상황에서 멀쩡할 수 있냐고.

‘느닷없이 정혼자라니.’

다시 생각해도 정신이 혼미해진다. 이 정도면 그냥 수류탄도 아니고, 탄도 미사일급 아닌가. 그나마 마음에 위안이 되는 건 정혼자라는 단어 앞에 전(前)이라는 한 글자가 붙는다는 것 정도다.

“그러니까 내가 말했잖아. 묻지 말라고.”

궁기방의 말에 나는 한숨처럼 대답했다.

“이런 건 줄 알았으면 나도 안 물어봤지. 그리고 주 소저가 먼저 말했어.”

“계속 궁금해하는 티를 내니까 그런 거 아니냐.”

“궁 소협 말씀이 맞습니다. 그냥 그럴 만한 이유가 있구나, 하고 넘어가시면 되지 왜…….”

“바지에 똥 지린 새끼는 입 다물고 있어라.”

“……옙.”

“나는 안 지렸으니까 계속 말해도 되겠군.”

“아닐걸. 잠시 후면 피똥 지리고 있을걸.”

“……진정해라. 우선 주먹 좀 내려놔.”

사실 때릴 힘도 없다.

고객의 요청사항에 따라 주먹을 내린 나는 허공을 바라보며 중얼거렸다.

“아, 시간을 되돌리고 싶다.”

“못 돌려.”

“못 돌립니다.”

“그래도 그 후에는 별로 티 안 나지 않았냐? 나 되게 태연했는데.”

궁기방과 혁무진이 훈훈하게 웃으며 입을 열었다.

“그럼, 그럼. 티 하나도 안 났다. 물 잔을 여섯 번 엎지른 걸 빼면.”

“젓가락도 일곱 번 떨어트리셨습니다.”

“절정은 그 부분이었지. 점소이가 더 시킬 음식 있으면 주문표에 추가해 달라고 하니까 노려봤던 거.”

“이야, 어떻게 그 상황에서 주문표랑 사마표를 연결시키지? 이해하는 데 한참 걸렸습니다.”

“거진 미친놈이었지.”

“최소 암천이었죠.”

“…….”

알겠으니까 그만해, 이 시벌놈들아.

마음 같아서는 흠씬 두들겨 패 주고 싶은데, 그럴 힘도 없어서 터덜터덜 걸음만 옮기는 것이 고작이다. 삐딱하게 쓴 죽립 아래로 얼굴이 드러나는 것도, 그런 내 얼굴을 사람들이 알아보는 것도 신경 쓸 겨를이 없었다.

“저, 저 사람 혹시…….”

“헉! 맞네, 맞아. 열화신룡 진태경.”

“그런데 왜 저러고 있대?”

“그걸 내가 어찌 아나.”

“꼴을 보아하니 꼭 여인한테 차이기라도 한 모습이군.”

“허허. 이 친구 농담도.”

“…….”

웃지 마. 농담 아냐.

이제는 숨만 쉬고 있어도 사방에서 딜이 들어온다. 한숨을 푹 내쉰 나는 죽립을 고쳐 썼다. 아직도 머릿속은 복잡하기 그지없었다.

‘전 남친. 아니, 전 정혼자라니.’

이미 사정은 대충 들었다. 주화란이 담담하고 솔직하게 과거의 이야기를 털어놓았기 때문이다.



‘정략혼이었어요. 그 전까지는 얼굴 한 번 본 적 없었죠.’



흔한 일이다. 용봉표국은 나날이 기울어지는 상태였고, 흑룡마문은 그런 주화란에게 손을 내밀었다. 거부할 수 없는 제안과 함께.



‘제가 결정한 거였어요. 쓰러진 아버지를 위해서.’



주화란의 담담한 목소리와 표정이 눈앞에 어른거리던 그때였다.

“막내야.”

나는 눈을 깜빡였다. 언제 도착했는지 모를 처소 앞. 태산만큼은 아니어도 커다란 체구를 지닌 사내, 진위경이 나를 향해 말을 이었다.

“매 대협. 아니, 맹주께서 찾으신다.”
```

## Final English reading copy

```markdown
# Chapter 534

Jingle. Clack.

The inn’s door closed with the final ring of the bell, and the stares that had been stabbing relentlessly into the back of Sama Pyo’s head ever since he descended the stairs vanished along with it.

But Sama Pyo already knew.

This wasn’t the end. It was the beginning of something else.

“Those two who just came out of Gowolru…”

“Are you sure?”

“Absolutely. The Black Dragon Saber, Sama Pyo, is the Young Sect Leader of the Black Dragon Demon Gate. And that huge fellow beside him is the monster who crushed Blood Cudgel’s skull seven days ago.”

“I heard he got into a fight with the Hwangbo Family’s Lesser Family Head earlier. Making trouble like that at a time like this… Tsk, tsk.”

“Leave them be. Isn’t that what demonic, heterodox practitioners are like? We’ll have to borrow even their hands to drive out Dark Heaven.”

“I don’t like it one bit. How do we know they won’t stab us in the back?”

“That’s what I’m saying… Shh. The big fellow is looking this way.”

Countless gazes and whispers were focused on them. Even if the people spoke as quietly as possible, they were close enough for him to hear every word if he chose to.

But despite the voices burrowing into his ears, Sama Pyo’s expression remained impassive as he walked.

*There’s nothing strange about it.*

He was already far too familiar with this situation.

Even in Gansu, where the Black Dragon Demon Gate was based and wielded immense influence, things had been the same. The label of demonic, heterodox practitioner that had followed him since birth was an inescapable shackle.

“Whoof.”

A rough snort came from beside him. Sama Pyo glanced at Taishan, who was rolling his enormous eyes around, then moved his lips.

*—Stop.*

Taishan’s hand, which had been sliding toward the two-section staff strapped across his back, halted.

Strength entered the Sound Transmission Sama Pyo sent him.

*—Taishan. You little bastard.*

*—……Understood, Lord. Taishan will endure.*

*—That’s right. Good boy.*

*—Taishan listens well. Taishan likes Lord. Hehehe.*

Taishan flashed a broad grin as though nothing had happened. Sama Pyo let out a quiet laugh.

*—Yes. I like you very much, too.*

*—Taishan got praised a lot today.*

*—Oh? Who was kind enough to praise you?*

*—Mm. Blazing Flame Divine Dragon praised me.*

Sama Pyo’s steps slowed.

*—Blazing Flame Divine Dragon Jin Taekyung?*

*—Correct. Jin Taekyung. He said Taishan was a good boy.*

*—It seems you like him.*

*—Like him. Very strong. Good. Taishan praised him.*

Sama Pyo gazed at Taishan’s profile as the giant strode along excitedly.

Taishan had been born with outstanding martial talent and divine strength, but an unfortunate accident long ago had left him with a head injury. He was no different from a child.

Perhaps it was because of that memory. He was extremely wary around strangers, and aside from Sama Pyo, he rarely opened his heart to anyone.

*It’s rare for someone like him to evaluate anyone besides me so favorably.*

Blazing Flame Divine Dragon Jin Taekyung.

The image of the carefree yet sly young man flashed before Sama Pyo’s eyes. Along with it came the immeasurably powerful aura hidden beneath his calm expression and voice.

*So that’s why they call him the Divine Dragon.*

The world was vast, and there were countless masters. Ordinary people admired the Ten Dragons and Phoenixes, calling them the greatest young prodigies in the Murim.

But Sama Pyo had never acknowledged them.

*They’re nothing more than empty reputations created inside the walls they built for themselves.*

In reality, anyone outside those walls was rejected. Sama Pyo had met more than one or two orthodox martial artists who committed shameless acts while hiding behind irritating words like *justice* and *the orthodox path*.

But…

*He was different. He was definitely different.*

Blazing Flame Divine Dragon Jin Taekyung.

Although their meeting had been brief, Sama Pyo had realized one thing for certain.

Jin Taekyung was special.

His astonishing martial power, which far surpassed that of any young prodigy, was one reason. But what made him feel even more extraordinary was his attitude—the way he differed from everyone else.

The conversation he had shared with Jin Taekyung only moments earlier passed through Sama Pyo’s mind.

*“I don’t know whether you’ve heard of the Black Dragon Demon Gate.”*

*“So what brings someone as important as the Young Sect Leader of the Black Dragon Demon Gate here?”*

*“Is that all?”*

*“What else do you need?”*

*“……!”*

It had been an unexpected question, and Sama Pyo had been rendered speechless for a moment.

That was because it was a question that had never existed anywhere along the path he had walked as Sama Pyo, the Young Sect Leader of the Black Dragon Demon Gate.

*What else do I need? What else…*

The thoughts he muttered inside his heart never escaped his lips.

Sama Pyo silently moved his lips, then turned his head toward Taishan.

*—I have one question.*

*—……?*

*—If you had to fight Blazing Flame Divine Dragon Jin Taekyung, what would you do?*

It happened in the blink of an eye.

Taishan’s smiling face stiffened.

Then a Sound Transmission arrived without the slightest hesitation.

*—Taishan owes Lord a great debt. If Lord commands, Taishan fights anyone.*

*—Didn’t you say you liked Jin Taekyung?*

*—Like Jin Taekyung. But not as much as Lord. Taishan gives life for Lord’s command.*

*—I see.*

Sama Pyo let out a quiet laugh and shook his head.

*—That’s enough. You really are a good fellow.*

*—Taishan good. And good Taishan hungry.*

At the sight of the enormous childlike man glancing at him mournfully, Sama Pyo burst out laughing.

“Come on. Let’s go somewhere. Tonight, I’ll feed you until you’re so full you burst.”

“Hehehe. Lord promised. Taishan believes Lord.”

“Yes, yes.”

“But, Lord.”

“What is it?”

“That woman earlier. Pretty. Very pretty. Who?”

Sama Pyo’s steps abruptly stopped.

Taishan tilted his head when he sensed something strange.

“Lord?”

“No. Was she really that pretty?”

“Yes. Pretty and good.”

“They say you can see ten fathoms into the water, but not one fathom into a person’s heart. How could you know what was hidden inside her after seeing only her face for a moment?”

Taishan vigorously shook his head.

“No! Pretty women are good!”

“……Don’t say it so loudly. People are looking.”

“Admit it! Taishan is right! Pretty means good!”

“Whew. You damned fool. I’m going on ahead.”

“Lord! Lord!”

Sama Pyo walked away, leaving Taishan’s desperate cries behind him. His face was as dry and expressionless as sand.

*Ju Hwaran… I never expected to meet her in a place like this.*

Sama Pyo couldn’t tell whether it was coincidence or fate.

But one thing was certain.

The woman who had been his fiancée, if only for a short time—Dagger Hidden Flower Ju Hwaran—would consider everything connected to him an ill-fated relationship.

*An ill-fated relationship… It wouldn’t be wrong.*

Sama Pyo’s gaze turned cold.

* * *

The meal that day ended without incident.

Under the owner’s lavish hospitality and the flood of attention from the people around us, we left the inn and exchanged farewells.

No. To be precise, it would be more accurate to say that Ju Hwaran said farewell to us.

“I think I should be going. There are some matters related to the Escort Bureau that I need to take care of.”

Jab.

At Gung Gibang’s discreet poke to my side, I stood there blankly for a moment before reflexively opening my mouth.

“Oh, yes. Goodbye.”

“Yes. You too, Great Hero Jin.”

Jab.

Damn it. Apparently, that wasn’t the right thing to say.

“Um, Young Lady Ju.”

“Yes?”

“Would you like me to escort you back to your lodgings?”

“Thank you for the offer, but I’ll be fine. I’ve heard that you barely have enough time to train as it is.”

“Oh. Who told you that? I have been a little busy lately.”

Jab. Jab jab.

*Thanks, you bastard.*

Following the signals from my Gung-vigation system, which was once again informing me that I had veered off course, I gripped the steering wheel tightly.

“Even so, some strange people might approach you, so I think it would be better if I escorted you…”

“Ahaha. No, it’s all right. I’m a martial artist, too.”

“Oh, right. I wasn’t trying to underestimate you, but… well.”

“No, you’re right that I’m lacking compared to Great Hero Jin. Besides, Captain Song is here as well.”

At that, Song Ilseom spoke in his blunt voice.

“If people like that approach, I’ll cut them down in a single stroke. Don’t worry about such trivial matters.”

“You heard him, right?”

“……Yes. I heard him.”

Jab jab. Jabjabjabjab!

*You’re going to put a hole in my side, you bastard.*

But this time, I couldn’t think of anything else to say. My already tangled thoughts twisted together, then scattered.

And that brief silence meant the moment had passed.

“Then I’ll be going now. See you again.”

Ju Hwaran smiled brightly and turned away.

Her silken hair swayed, and a faint fragrance drifted from between the strands and through the air.

I stood there silently, watching the backs of the two people grow more distant.

That was when—

“This guy really is a fucking idiot.”

“Wow. You’re something else, Captain.”

“……”

There was no need to check who they were. I looked at Gung Gibang and Hyuk Mujin with mournful eyes.

“Where did I go wrong, and when?”

The two of them answered simultaneously, as though they had been waiting for the question.

“Since you spat food in Young Lady Ju’s face.”

“Wasn’t the problem Captain himself from the start?”

Their answers were different, but they had two things in common.

First, both of them were infuriating.

Second, both of them were facts I had a hard time arguing against.

“Damn it.”

I kicked the innocent ground.

Honestly, I felt a little aggrieved. How was I supposed to have stayed calm in that situation?

*A fiancé, out of nowhere.*

Even thinking about it again made my head spin.

At this point, it wasn’t a grenade. It was a ballistic missile.

The only thing that comforted me even a little was that the word *former* came before *fiancée*.

“I told you not to ask.”

I answered Gung Gibang with a sigh.

“If I’d known it would be like this, I wouldn’t have asked. Besides, Young Lady Ju brought it up first.”

“You kept making it obvious that you were curious.”

“Great Hero Gung is right. You should have simply assumed there was a reason and left it alone. Why did you…”

“The bastard who shit his pants should shut up.”

“……Yes, sir.”

“I didn’t shit my pants, so I can keep talking.”

“Not for long. In a little while, you’ll be shitting blood.”

“……Calm down. Put your fist down first.”

In truth, I didn’t even have the strength to hit him.

At the customer’s request, I lowered my fist and stared into the empty air.

“I want to turn back time.”

“You can’t.”

“Can’t do that.”

“Still, it wasn’t that obvious afterward, was it? I acted pretty calm.”

Gung Gibang and Hyuk Mujin smiled warmly before answering.

“Of course, of course. It wasn’t obvious at all. Except for the six times you knocked over your water glass.”

“You dropped your chopsticks seven times as well.”

“The best part was when the server told us to add anything else we wanted to the order slip, and you glared at him.”

“Wow. How did you even connect the order slip to Sama Pyo? It took me a long time to understand.”

“You were practically insane.”

“At minimum, you looked like Dark Heaven.”

“……”

*I get it, so stop it, you fucking bastards.*

I wanted nothing more than to beat them half to death, but I didn’t have the strength. All I could do was trudge along.

I didn’t have the energy to care whether my face was visible beneath my crooked bamboo hat, or whether people recognized me.

“Th-That person, could he be…”

“Gasp! It is! It’s Blazing Flame Divine Dragon Jin Taekyung!”

“But why is he walking like that?”

“How would I know?”

“Judging by the way he looks, you’d think some woman had dumped him.”

“Ha ha. What a joke.”

“……”

*Don’t laugh. It isn’t a joke.*

These days, I took damage from all sides even when I did nothing but breathe.

I let out a long sigh and adjusted my bamboo hat.

My mind was still hopelessly complicated.

*An ex-boyfriend. No, an ex-fiancé.*

I had already heard the rough circumstances.

Ju Hwaran had calmly and honestly told me about her past.

*“It was a political marriage. We had never even seen each other’s faces before then.”*

It was a common arrangement.

The Yongbong Escort Bureau had been declining day by day, and the Black Dragon Demon Gate had extended a hand to Ju Hwaran.

Along with an offer she couldn’t refuse.

*“I was the one who made the decision. For my stricken father.”*

That was when Ju Hwaran’s calm voice and expression rose before my eyes.

“My youngest.”

I blinked.

We had arrived at the entrance to our lodgings without my noticing.

The man who spoke to me was large, though not quite as enormous as Taishan.

Jin Wikyung continued.

“Great Hero Mae. No—the Alliance Leader is looking for you.”
```
