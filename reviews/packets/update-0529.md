<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0529.txt",
      "sha256": "91ca9fd1c048eb87583c2b438bca182aae2dbf7db1afa8fe23de9b81fd0f51f5",
      "bytes": 13702
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1ef508dc8c82a1cf5bb86b8bd53835bbba3712c1b52174e16a5938b8e62fad69",
      "bytes": 3569
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5b8a3b7691981a2eddad149a60ae832221992dfc29bdeef6f12d008e24a74515",
      "bytes": 168930
    },
    {
      "path": "characters/Baek Woo.md",
      "sha256": "a418f2948214679c8174c28f374dd21187caa29fbce2d28339c9f4a8ceee8409",
      "bytes": 811
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "6eee1f9a1c5422b05038f06cbb9662c5331cc983d8a49465eaba3701371f026b",
      "bytes": 686
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3cc71440d260b1950b558de25c79ee7ef62586115b788f129e1ff32d9d0d19a3",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "94877ee4682c7cd2696193163816a22358c4311b637202c4a72f965c7ed8594d",
      "bytes": 1497
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3f19e17d8dc2398f56cc832a9f1b2ab1d4a341ab85b6997328166b592eee73c6",
      "bytes": 2021
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "150d88f85da55be2c55b08641ebe4ab0f8fbb9629110168a5a2eefc71a804913",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "ef6536015e204e95922203406e18ea1d9bf93e8a1ac2107534d08417686c3ae6",
      "bytes": 921
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5055fd089787aa6ed7851e0569df53546ad0b97272966a57ddd5f2bcd686b8b4",
      "bytes": 158189
    }
  ],
  "estimated_tokens": 12269
}
-->

# Durable State Update — Chapter 529

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 529. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 529. Profile updates may replace only one
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
  "chapter": 529,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 529,
    "continuity_sources": [529],
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
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes.",
    "Cheongpung has recently lost his appetite and is concentrating on refining Mimi Step, marking an apparent change in his behavior.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Wudang's second report identifies Jang Sam as the Killing Ghost and links his transformation to the Blood Fish.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Gung Gibang opposes the war on principle, and Ju Hwaran is eagerly awaiting Taekyung at a gathering of roughly half the Ten Dragons and Phoenixes."
  ],
  "continuity_sources": [
    528,
    527
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Did the Blood Fish cause Jang Sam's transformation, and could similar Blood Fish or Gate-related transformations occur elsewhere?",
    "How will Taekyung incorporate Mungyeong's martial principles, and what effect will the custom pill have on him?"
  ],
  "safe_through": 528,
  "temporary_decisions": [
    "Render 숭산결의 as Mount Song Resolution and 미미보 as Mimi Step; retain footwork technique for 보법.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 홍적 as Hong Jeok, 모용영휘 as Murong Yeonghwi, and 복마전 as demon-slaying battleground.",
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 쌀벌레 as Rice Weevil and 만두 벌레 as dumpling grub; retain the chapter's blunt profanity and monster-comparison humor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 적천강    | **Jeok Cheongang** |
| 주화란    | **Ju Hwaran**      |
| 백우     | **Baek Woo**       |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 은비화    | **Dagger Hidden Flower**      | Ju Hwaran      |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 곤륜파    | **Kunlun Sect**                  |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 천무학관   | **Heaven's Gate Temple**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 신법     | **movement technique**                           |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 표국     | **Escort Bureau**                            |
| 표사     | **escort**                                   |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 곤륜     | **Kunlun**             |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 곤륜운룡 | **Kunlun Cloud Dragon** | Epithet of a Kunlun Sect young prodigy. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 운룡대팔식 | **Cloud-Dragon Eight Forms** | Baek Woo's Kunlun movement technique. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 백우 | 진태경 | rival_finalists | Fellow Daoist Jin Taekyung | formal-polite and admonishing | Baek Woo uses 도우 while criticizing Taekyung's vulgarity. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 백우 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Baek Woo, Gung Gibang, and Zhuge Gyun collectively as 세 얼간이. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |

## Listed compact profiles

### Baek Woo.md

# Baek Woo (백우)

- **Safe through:** Chapter 456
- **Aliases:** Kunlun Cloud Dragon
- **Role:** Kunlun Daoist martial artist and finalist in the Star-Array Grand Banquet; Taekyung sent him plummeting during the third preliminary assessment after stepping on his face.
- **Personality:** Fastidious, easily offended, and self-righteous about propriety.
- **Voice:** Formal, archaic, and admonishing, with repeated complaints about vulgarity.
- **Relationships:** Rival finalist alongside Gung Gibang and Zhuge Gyun; regards Taekyung as an offensively vulgar fellow Daoist, but accepts Taekyung's demand to remain silent and use polite speech after being subdued aboard the carriage; his Master has instructed him to get along with Taekyung.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 528
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 528
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 526
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a twenty-three-year-old cadet at Heaven’s Gate Temple, and a young Peak-level genius swordsman who has remained secluded in the training hall for more than a year after losing to Cheongpung and refuses to emerge until he achieves a great accomplishment.
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 527
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 527
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 528
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal and now investigating at least two escort captains suspected of aiding his scheme.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, and Jin Taekyung’s earlier reassurance remains emotionally vivid to her as she eagerly awaits seeing him again.

## Korean source

```text
＃529화



짤랑.

“어서 옵쇼!”

문이 열리는 종소리와 함께 들려오는 점소이의 힘찬 외침.

하지만 혹시나 하는 기대감으로 벌떡 일어난 주화란의 눈동자에는 금세 실망의 빛이 깃들었다.

“아…….”

그가 아니다. 내려다보이는 각도 때문에 얼굴은 제대로 보이지 않았지만, 그것만으로도 충분히 구분할 수 있었다.

아니, 정말 그였다면 그림자만으로도 알 수 있을지도 몰랐다.

‘아니었구나. 그분이 아니었어.’

후우.

나직한 한숨을 흘린 주화란은 아쉬움이 담긴 눈빛으로 다시 한번 일 층을 내려다보았다.

그렇다고 달라지는 것도 없는데, 어째서인지 자꾸만 미련이 남는다.

그리고 그런 주화란의 모습에, 함께 동석한 사내들은 헛기침을 내뱉었다.

“크흠.”

“크흐흠.”

처음부터 주화란의 일거수일투족에 모든 신경을 기울이고 있던 그들이다.

지금 그녀가 보인 행동이 무엇을 의미하는지 모를 만큼 멍청하지도 않았다.

탁자를 사이에 두고 주화란의 맞은편에 앉아 있는 세 남자. 그중에서도 특히 두 사내의 시선이 허공에서 얽혀들었다.

아니, 그들이 주고받는 것은 시선뿐만이 아니었다. 미약하게 움찔거리는 입술 사이로는 이미 은밀한 전음(傳音)이 오가는 중이었다.

- 이보시게. 황보 도우. 지금 주 소저가 기다리는 사람이 누구일 것 같은가?

먼지 한 톨 묻지 않은 백의에 깨끗한 피부를 지닌 미남자.

자타공인 곤륜파 제일의 후기지수이자 십봉룡의 일원인 곤륜운룡(崑崙雲龍) 백우의 전음에, 날렵한 콧날을 지닌 미공자가 미미하게 눈살을 찌푸렸다.

- 모르겠군.

- 빈도는 아무래도 한 사람밖에 생각나지 않는데. 아마 그 짐작이 맞다면 열화신룡 진태…….

- 그 얘기는 그만하지.

서늘하게 대답한 미공자, 황보세가의 소가주이자 또 다른 십봉룡의 한 사람인 산동권룡(山東拳龍) 황보악은 기분이 영 좋지 않았다.

‘이 황보악이 다른 놈보다 못한 취급을 받다니.’

결코 있을 수 없는 일이다. 특히 자기애가 넘치는 황보악으로서는 납득하기 어려운 현실이기도 했다.

비록 천하 오대세가에 포함되지는 않았지만, 황보세가라는 네 글자는 무림에서 상당한 위세를 누리고 있었다.

오랜 세월 산동 지방을 주름잡은 패자이자 뿌리 깊은 무가(武家)라는 것에는 그 누구도 이견을 제시할 수 없을 정도니까.

황보악은 바로 그 황보세가의 소가주다.

거기에 더해 십봉룡으로 불릴 만큼 뛰어난 무재의 소유자이자 어디에 내놔도 빛나는 미남자이기도 했다.

훌륭한 집안. 막대한 부와 명예. 얼굴까지 잘생겼으니 여인들 사이에서 인기가 천정부지로 솟는 것은 당연했다.

하지만 가장 큰 문제는, 황보악이 이립에 가까운 인생을 살아오면서 누렸던 그 모든 것들이 지금 이 순간만큼은 부질없게 느껴지고 있다는 것이었다.

‘은비화(隱匕華) 주화란.’

그녀를 처음 본 순간, 황보악은 깨달았다. 자신이 지금까지 만났던 숱한 미녀들은 모두 태양 앞의 잔딧불에 불과했다는 것을.

다른 여인들과 달리 화장기 하나 없는 얼굴임에도 뭐라 형용할 수 없을 만한 아름다움이 흘러나왔고, 그녀가 걸친 단조로운 색의 무복은 화려한 궁장보다 기품 있어 보였다.

그야말로 첫눈에 반한 것이다.

‘이런 여인을 왜 일찍 만나지 못했을까.’

황보악은 홀린 듯이 주화란을 응시했다.

그녀의 작은 움직임 하나하나에, 샛별처럼 반짝이는 눈빛에 가슴이 울렁거리고 깊숙한 곳에 숨어 있던 욕망이 꿈틀거렸다.

하지만…….

“후우.”

아쉬움이 담긴 주화란의 한숨에 그의 미간이 찌푸려졌다.

저 한숨에 담긴 감정이 무엇인지, 그리고 그 감정이 누굴 향한 것인지 이미 알고 있는 탓이다.

‘열화신룡 진태경.’

마음속으로 조용히 뇌까리는 한 사람의 별호와 이름.

탁자 아래로 내려가 있던 손에 저절로 힘이 들어갔다.

‘그깟 놈이 뭐길래.’

주화란과 진태경 사이에 무슨 인연이 있었는지는 이미 들어서 알고 있다.

비록 두 달 전 용봉표국과 종남파 사이에 무슨 일이 있었는지는 자세히 알려지지 않았다.

그러나 종남파에서도 세 손가락 안에 드는 고수인 태을무정검이 이제 갓 약관을 넘긴 후기지수에게 무릎을 꿇었다는 충격적인 소식은 이미 무림을 휩쓸었다.

‘있을 수 없는 일이지.’

상식적으로 있을 수도 없고, 있어서도 안 되는 일이다. 황보악은 그저 그것을 헛소문으로 치부하며 혀를 찼다.

허나 그보다 중요한 것은 그 일로 인해 주화란이 진태경에게 어떠한 감정을 품었다는 불쾌한 짐작이었다.

- 확실한가?

돌연 들려온 전음에 곤륜운룡 백우가 귀를 쫑긋 세웠다.

- 응?

- 아까 했던 말이 확실하냐 물었네. 열화신룡 진태경. 지금 주 소저가 기다리는 자가 그놈이 맞는지.

- 그럼 설마 후개를 기다리겠나?

- …….

황보악이 생각해 봐도 그건 아니었다.

주화란이 아무리 특이 취향이어도 그렇지. 옆에 앉아 있기만 해도 개밥 쉰내를 풀풀 풍기는 궁기방을 좋아할 리는 없다.

- 그럼 정말 그놈이라는 소린가? 산서성 촌구석에서 기어 나온 지렁이보다 본 공자가 못하다는 소리야?

- 지렁이가 아니라 신룡이지. 그리고 산서성도 더 이상 촌구석이 아닐세. 진태경이라는 용이 솟아오른 잠저(潛邸)이자 북부고원을 통한 교역로의 중심이야.

황보악의 말을 가볍게 정정한 백우가 전음을 이었다.

- 황보 도우. 자네가 알고 있는 예전의 태원진가가 아닐세. 사실 말이 나왔으니 말인데, 빈도는 일찍이 진천검 그 친구를 봤을 때 진즉 알아차렸지.

- 진천검? 진천검 진무경?

- 우리가 아는 진천검이 그 한 사람 말고 또 있나?

황보악의 눈썹이 파르르 떨렸다.

탁자 너머에서 연신 한숨을 내쉬고 있는 주화란, 그리고 어디서 굴러먹다 온 개뼉다구인지 모를 젊은 표사가 그를 바라보고 있지 않았다면 진즉 인상을 구겼을 것이다.

- 그 이름 꺼내지 말게. 자네는 지금 내가 그놈이 누구인지 몰라서 물어본 것 같나?

- 아, 그러고 보니 진천검과 자네는 천무학관에서…….

- 그만. 그만하게!

- 깜짝이야. 알겠네. 왜 소리를 지르고 그래?

잔뜩 힘이 들어간 황보악의 주먹이 붉게 달아올랐다.

진무경. 아마 황보악이 죽을 때까지 잊을 수 없는 이름 중 하나다.

모든 것을 가졌다고 생각한 그에게 넘을 수 없는 벽을 느끼게 함과 동시에 엄청난 굴욕감을 주었으니까.

‘빌어먹을.’

그런데 이제는 그 형이라는 놈에 이어 아우까지 그의 앞길을 막는다.

은은한 노기를 드러내는 황보악의 모습에 백우가 조심스러운 표정으로 입술을 달싹였다.

- 그, 황보 도우. 한 가지 조언해도 되겠나?

- 또 뭔가?

- 자네가 빈도에게 했던 말 있잖나. 만약 열화신룡이 오면 절대 입 밖으로 꺼내지 말게. 아니, 애초에 입도 벙긋하지 마.

- 흥. 칼부림이라도 날까 염려되나?

- 아니, 그게 아니고. 빈도까지 말려들까 봐 걱정돼서 그래.

- ……뭐?

백우가 연민과 걱정이 담긴 그윽한 시선으로 황보악을 응시했다.

- 죽으려면 혼자 죽게.

- ……!

- 자네는 성라대연 때 가문에서 폐관 중이었으니 잘 모르겠지. 하지만 빈도는 아직도 그자만 생각하면, 어후. 아무튼, 그렇게 알고 있게. 알았지?

아니, 이게 대관절 무슨 소린가. 죽으려면 혼자 죽으라니.

잠시 입을 다문 채 어이없는 눈빛으로 백우를 바라보던 황보악이 전음을 날렸다.

- 지금…… 진심인가?

- 무량수불. 원시천존께 맹세컨대 매우 진심일세.

- 아니, 무인으로서의 자존심도 없나?

- 그건 이미 성라대연 때 사라졌어. 운룡대팔식(雲龍大八式)을 펼치고도 정수리를 짓밟힌 기분을 자네가 알아?

- 아무리 그래도 그렇지!

- 아무리 그래도 안 돼. 그자는 괴물일세.

- 이, 이런. 한 마리의 고고한 학 같던 곤륜운룡은 어디 갔나! 내가 알던 그 백우는 어디 간 거냔 말일세!

백우가 추억에 잠긴 눈빛으로 과거를 응시했다.

- 그러고 보니 그때 당시 후개도 빈도에게 비슷한 말을 했었지. 그런데 바로 다음 시험에서 진태경에게 한 마리의 개처럼 두들겨 맞더군. 궁기방이 경신법에서 밀리니까 눈깔이 뒤집혀서 머리채 잡으려고 했다가 머리통 날아갈 뻔했다는 소식은 들었지?

- ……!

- 무량수불. 딱 까 놓고 얘기하세. 자네는 열화신룡이 보여 준 모습이 모두 헛소문이었다고 생각하나?

- 물론일세!

단호한 황보악의 대답에 백우가 나직한 한숨을 내쉬었다.

- 왜?

- 어찌 사람이 그럴 수 있단 말인가? 스승인 화왕이 모든 것을 해결하고 공을 가져간 것이 분명하지!

- 하긴, 상식적으로 따졌을 때 말이 안 되긴 하지. 약관을 갓 넘은 나이에 초절정의 반열에 오른다는 것이 말이나 되나?

드디어 정상적인 답변이 나오자, 황보악이 확신에 찬 표정으로 고개를 끄덕였다.

- 내가 말하고 싶은 것이 그것일세. 스승인 화왕 적천강이 나서고, 공을 제자에게 돌린 것이 분명해.

- 그, 걱정돼서 다시 하는 말인데, 그 공을 돌렸다는 말은 열화신룡 앞에서 하지 말게. 자네와 전우조로 묶여서 죽탱이 돌아가긴 싫으니까.

- ……지금 뭐 하자는 건가?

- 무량수불. 간단한 이야기일세. 상식으로 따지지 마. 이해하려고 하지도 말고. 그냥 받아들여.

해탈한 듯한 백우의 말에 일순 말을 잃은 황보악은 이번엔 접근하는 방향을 돌렸다.

- 아, 아니. 그러는 자네도 주 소저에게 마음이 있지 않나?

- 주 소저? 물론 좋아하지. 사내라면 어찌 그녀에게 호감을 품지 않을 수 있겠나.

- 바로 그 주 소저가 진태경에게 마음이 있네. 그런데도 연적을 비호할 생각인가?

- 주 소저보다 빈도의 목숨이 더 소중해. 머리카락도 마찬가지고.

- 뭐?

주위의 눈치를 살피던 백우가 자연스럽게 고개를 슬쩍 숙여 보였다.

가지런하게 정리된 머리카락 사이로, 왠지 모르게 휑한 정수리가 눈에 띄었다.

- 무량수불. 봤나?

- 아니, 자네 도대체.

전음을 잇지 못하는 황보악의 모습에, 백우가 서글픈 웃음을 지었다.

- 성라대연 때 정수리 밟힌 이후로 머리카락이 안 자라…….

- ……!

- 포기해. 포기하면 편하네. 그래도 도저히 포기 못 하겠으면 부디 빈도 없을 때 해 주게. 나라도 살고 싶으니까.

뭐 이런 미친 소리가 있나.

황보악은 마른침을 꿀꺽 삼켰다.

여전히 분노가 남아 있긴 매한가지지만, 꽤 오랫동안 알고 지낸 벗이자 자존심 강한 한 사람의 무인인 백우가 이렇게까지 말하니 등골이 서늘해졌다.

‘이거 실화인가?’

열화신룡을 둘러싼 소문들이 전부 사실이라고는 단 한 번도 생각해 본 적 없다.

하지만 정말, 만에 하나, 그 모든 소문이 일말의 거짓도 없는 진실이었다면…….

‘상식을 벗어난 괴물.’

그래. 정말 의심의 여지 없는 괴물이다.

그리고 동시에 참을 수 없는 모멸감이 황보악의 전신을 휘감았다.

‘이, 이런 빌어먹을 일이.’

불끈 쥔 주먹. 열린 잇새 사이로 앓는 소리가 흘러나오자 심상치 않은 분위기를 눈치챈 주화란이 입을 열었다.

“황보 소협. 왜 그러세요?”

“아, 아닙니다. 아무것도.”

애써 대답하는 황보악의 모습에, 하는 일도 없이 자리만 차지하고 앉아 있던 젊은 표사가 피식 웃었다.

“굉장히 아무 일 같아 보이오만.”

“……아무 일 아니라고 했소.”

“아니면 말고. 그나저나 여기 음식 맛있구려.”

황보악의 눈매가 가늘어졌다.

행동부터 말까지. 주화란의 호위라고 하여 특별히 동석을 허락했건만, 도무지 하나하나가 마음에 안 드는 놈이다.

비틀어진 입매 사이로 작은 중얼거림이 흘러나왔다.

“하여간, 이래서 근본 없는 것들이란…….”

주화란은 바보가 아니다. 순간 심란함이 가득하던 아름다운 얼굴 위로 서늘한 한기가 스쳤다.

“황보 소협.”

“아, 혹시 주 소저께서 오해하실까 봐 드리는 말씀인데. 저 친구에게 한 말이 아닙니다.”

꾸며 낸 웃음을 지은 황보악이 저 멀리 떨어진 탁자를 가리키며 말을 이었다.

“저 사마외도(邪魔外道) 종자들에게 한 말이지요.”

그리고 크지도, 작지도 않은 그의 목소리가 울려 퍼진 그 순간.

드르륵.

한 사람이 자리에서 일어났다.
```

## Final English reading copy

```markdown
# Chapter 529

Jingle.

“Welcome!”

The inn attendant’s energetic cry came with the ringing of the bell above the opening door.

Ju Hwaran sprang to her feet in hopeful anticipation, but disappointment quickly filled her eyes.

“Ah……”

It wasn’t him. She couldn’t make out the person’s face properly from the angle above, but that alone was enough to tell.

No, if it had really been him, she might have recognized him from his shadow alone.

*It wasn’t him. That person wasn’t here.*

Hwaran let out a quiet sigh and looked down at the first floor once more, her eyes filled with regret.

Nothing would change just because she kept looking, yet for some reason, she couldn’t let go of her disappointment.

The men seated with her cleared their throats at the sight.

“Ahem.”

“Ahem.”

They had been paying close attention to Hwaran’s every movement from the very beginning.

They weren’t stupid enough not to understand what her actions meant.

Three men sat across the table from Hwaran. Among them, two exchanged glances that tangled in midair.

And it wasn’t only their eyes that communicated. Their lips twitched faintly as discreet Sound Transmission passed between them.

—Fellow Daoist Hwangbo. Who do you think Young Lady Ju is waiting for?

The handsome man in spotless white clothes and with clear skin was Baek Woo, the Kunlun Cloud Dragon—a universally acknowledged number-one young prodigy of the Kunlun Sect and one of the Ten Dragons and Phoenixes.

At his Sound Transmission, the beautiful young man with a sharp nose slightly furrowed his brow.

—No idea.

—I can think of only one person. If my guess is correct, then it must be the Blazing Flame Divine Dragon, Jin Tae—

—Drop it.

Hwangbo Ak, the beautiful young man who had coldly cut him off, was the Lesser Family Head of the Hwangbo Family and another member of the Ten Dragons and Phoenixes.

He was in a terrible mood.

*How dare I, Hwangbo Ak, be treated as though I’m inferior to some other bastard.*

It was impossible. And for someone as self-obsessed as Hwangbo Ak, it was a reality he found especially difficult to accept.

Although the Hwangbo Family was not one of the Five Great Families, the name carried considerable influence throughout the Murim.

No one could dispute that it was a deeply rooted martial family and the long-standing hegemon of the Shandong region.

Hwangbo Ak was the Lesser Family Head of that very family.

On top of that, he possessed exceptional martial talent worthy of the name Ten Dragons and Phoenixes, and he was a handsome man who would shine wherever he went.

An excellent family. Immense wealth and prestige. A handsome face as well.

It was only natural that his popularity among women had soared to the heavens.

But the greatest problem was that all the things Hwangbo Ak had enjoyed throughout his life, now approaching thirty, felt meaningless at this very moment.

*The Dagger Hidden Flower, Ju Hwaran.*

The instant he first saw her, Hwangbo Ak realized that all the countless beautiful women he had met until now had been nothing more than fireflies before the sun.

Unlike other women, her face was entirely free of makeup, yet an indescribable beauty radiated from it. And the plain-colored martial uniform she wore seemed more refined than any ornate court dress.

He had fallen in love at first sight.

*Why couldn’t I have met a woman like her sooner?*

Hwangbo Ak stared at Ju Hwaran as though entranced.

His heart fluttered at each of her small movements. Her eyes sparkled like morning stars, and the desire hidden deep inside him stirred.

But then……

“Phew.”

Hwaran’s sigh, heavy with regret, made his brow crease.

He already knew what emotion that sigh contained—and whom it was directed toward.

*The Blazing Flame Divine Dragon, Jin Taekyung.*

He silently repeated the epithet and name in his mind.

His hand, resting beneath the table, clenched on its own.

*What does that nobody have that I don’t?*

Hwangbo Ak had already heard about the connection between Ju Hwaran and Jin Taekyung.

The details of what had happened between the Yongbong Escort Bureau and the Zhongnan Sect two months earlier had not become widely known.

But the shocking news that the Taeeul Merciless Sword, one of the Zhongnan Sect’s three greatest masters, had knelt before a young prodigy who had only just passed twenty had already swept through the Murim.

*It’s impossible.*

It was something that could not and should not have happened. Hwangbo Ak had dismissed it as a ridiculous rumor and clicked his tongue.

But more important than that was his unpleasant suspicion that the incident had caused Hwaran to develop feelings for Jin Taekyung.

—Are you certain?

Baek Woo’s sudden Sound Transmission made him prick up his ears.

—Hm?

—I asked whether what you said earlier was certain. The Blazing Flame Divine Dragon, Jin Taekyung. Is the person Young Lady Ju is waiting for really that bastard?

—Then do you think she’s waiting for the Successor Beggar?

—……

Even Hwangbo Ak had to admit that was unlikely.

No matter how peculiar her tastes were, Ju Hwaran could not possibly like Gung Gibang, who filled the air with the reek of stale dog food just by sitting nearby.

—So you really mean it’s that bastard? Are you saying this Young Master is inferior to a worm that crawled out of some backwater corner of Shanxi Province?

—Not a worm. A Divine Dragon. And Shanxi Province is no longer a backwater corner. It is the hidden residence from which the dragon named Jin Taekyung rose, as well as the center of the trade routes running through northern Gaoyuan.

Baek Woo lightly corrected Hwangbo Ak before continuing.

—Fellow Daoist Hwangbo. The Jin Family of Taiyuan you knew in the past is no more. In fact, now that we’re talking about it, I knew it long ago, from the moment I saw that fellow, the Heaven Shaking Sword.

—The Heaven Shaking Sword? Heaven Shaking Sword Jin Mukyung?

—Do you know another Heaven Shaking Sword?

Hwangbo Ak’s eyebrows trembled.

If Ju Hwaran, who kept sighing across the table, and that young escort who looked like he had crawled in from who knew where had not been watching him, he would have scowled long ago.

—Don’t bring up that name. Do you think I’m asking because I don’t know who that bastard is?

—Ah, now that you mention it, you and the Heaven Shaking Sword were at Heaven’s Gate Temple together—

—Enough. Stop!

—Good heavens. All right. Why are you shouting?

Hwangbo Ak’s tightly clenched fist had turned red.

Jin Mukyung was one of the names Hwangbo Ak would never be able to forget, even until the day he died.

That man had made Hwangbo Ak, who believed he possessed everything, feel an insurmountable wall—and had given him a tremendous humiliation at the same time.

*Damn it.*

And now, after the older brother, the younger brother was blocking Hwangbo Ak’s path too.

Seeing the faint anger showing on Hwangbo Ak’s face, Baek Woo cautiously moved his lips.

—Fellow Daoist Hwangbo. May I offer you one piece of advice?

—What now?

—You remember what you said to me. If the Blazing Flame Divine Dragon comes, don’t ever mention it out loud. No—don’t even move your lips.

—Hmph. Are you worried there might be a fight?

—No, that’s not it. I’m worried I might get dragged into it too.

—……What?

Baek Woo gazed at Hwangbo Ak with deep concern and sympathy.

—If you want to die, die alone.

—……!

—You were in closed-door training at your family’s estate during the Star-Array Grand Banquet, so you probably don’t know. But even now, whenever I think about that man, I feel—ugh. Anyway, keep that in mind. Understood?

What in the world was he talking about? Die alone?

Hwangbo Ak remained silent for a moment, staring at Baek Woo in disbelief. Then he sent another Sound Transmission.

—Are you…… serious?

—Infinite Life Buddha. I swear before the Primordial Heavenly Venerable that I’m completely serious.

—Don’t you have any pride as a martial artist?

—That disappeared during the Star-Array Grand Banquet. Do you know what it feels like to have the top of your head stepped on even after using the Cloud-Dragon Eight Forms?

—That’s going too far!

—No matter how you look at it, it’s impossible. That man is a monster.

—W-What happened to the Kunlun Cloud Dragon who was like one lofty crane? Where did the Baek Woo I knew go?

Baek Woo gazed into the past with a nostalgic look in his eyes.

—Come to think of it, the Successor Beggar said something similar to me back then. Then, in the very next test, he was beaten like a dog by Jin Taekyung. You heard what happened, didn’t you? Gung Gibang fell behind in movement technique, his eyes rolled back, and he tried to grab Jin Taekyung by the hair. He nearly got his head knocked off.

—……!

—Infinite Life Buddha. Let’s be blunt. Do you really think everything the Blazing Flame Divine Dragon showed us was nothing but a rumor?

—Of course!

At Hwangbo Ak’s firm answer, Baek Woo let out a quiet sigh.

—Why?

—How could a person do such things? It’s obvious that his master, the Fire King, solved everything and gave the credit to his Disciple!

—True. If you look at it with common sense, it doesn’t make sense. How could anyone reach Supreme Peak at barely twenty?

At last, Hwangbo Ak heard a normal answer. He nodded with a look of certainty.

—That is exactly what I’m saying. His master, the Fire King Jeok Cheongang, must have stepped in and given the credit to his Disciple.

—I’m saying this again because I’m worried about you: don’t tell the Blazing Flame Divine Dragon that his master handed him the credit. I don’t want to be paired with you as a battle partner and have my face beaten in.

—……What exactly are you trying to do?

—Infinite Life Buddha. It’s simple. Don’t try to reason it out with common sense. Don’t even try to understand it. Just accept it.

For a moment, Hwangbo Ak was speechless at Baek Woo’s almost enlightened tone. Then he changed his approach.

—W-Wait. You have feelings for Young Lady Ju too, don’t you?

—Young Lady Ju? Of course I like her. How could any man not be attracted to her?

—That very Young Lady Ju has feelings for Jin Taekyung. And you still intend to protect your rival?

—My life is more important than Young Lady Ju. My hair is, too.

—What?

Baek Woo glanced around to see whether anyone was watching, then casually lowered his head.

Between his neatly arranged hair, his strangely bare crown stood out.

—Infinite Life Buddha. Do you see it?

—No, what the hell—

Hwangbo Ak could not finish his Sound Transmission. Baek Woo gave him a sorrowful smile.

—My hair stopped growing after my head was stepped on during the Star-Array Grand Banquet……

—……!

—Give up. Giving up makes life easier. But if you absolutely can’t give up, please do it when I’m not around. I’d like to live, too.

What kind of insane nonsense was this?

Hwangbo Ak swallowed dryly.

He was still just as angry, but the chill running down his spine was impossible to ignore. Baek Woo had been his friend for a long time and was a martial artist with a strong sense of pride. If even he was speaking like this, then—

*Is this for real?*

Hwangbo Ak had never once believed that every rumor surrounding the Blazing Flame Divine Dragon was true.

But if, just for argument’s sake, every one of those rumors really was true without a shred of falsehood……

*An inhuman monster.*

Yes. A monster beyond any doubt.

And at the same time, an unbearable humiliation wrapped itself around Hwangbo Ak’s entire body.

*How the hell could this happen?*

His fist tightened. A pained groan slipped through his parted teeth, and Ju Hwaran, sensing the unusual atmosphere, spoke.

“Young Hero Hwangbo. Is something wrong?”

“Ah, no. It’s nothing.”

At Hwangbo Ak’s forced answer, the young escort who had been sitting there doing nothing but taking up space gave a quiet laugh.

“You look very much like something’s wrong.”

“……I said it was nothing.”

“If you say so. In any case, the food here is delicious.”

Hwangbo Ak’s eyes narrowed.

From his behavior to the way he spoke, there was nothing Hwangbo Ak liked about the man. Hwangbo Ak had allowed him to sit with them only because he was Young Lady Ju’s escort, but every little thing about him irritated Hwangbo Ak.

A mutter slipped through his twisted lips.

“This is the problem with lowborn rabble……”

Ju Hwaran was not a fool. A cold chill passed over her beautiful face, which had been filled with troubled thoughts only a moment earlier.

“Young Hero Hwangbo.”

“Ah, I’m only saying this in case Young Lady Ju misunderstands. I wasn’t talking about that fellow.”

Hwangbo Ak put on a fabricated smile and pointed toward a table some distance away.

“I was talking about those bastards who practice demonic, heterodox arts over there.”

And at the moment his voice, neither loud nor soft, rang through the inn—

Scrape.

Someone rose from their seat.
```
