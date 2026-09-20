<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0532.txt",
      "sha256": "705755291bb49efdc8e03af066f27b291c147daa33eb69feee350e61adfb986a",
      "bytes": 16584
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "edabfdb7b139dd1eb614e2ad57bb22d46acfe1e82e523fdc04d87d3b52c18189",
      "bytes": 3769
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "45b6bf942b171f3de42d49b20dbbb26d00990fab5102d28bea7ef78ef4cd3ae7",
      "bytes": 169746
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "159a4e437b2487ec19a9c801c3ef5ddde3ab55d324ba48d95131d6ab59c31802",
      "bytes": 1070
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d07f4b9d19e720970a1380182e701d41a132d7d32d4af6b14169aea23a0bbbf1",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "d8c95973bd4405d4e7555c45121c04cf19bd6888f548bd17e2cd1ae4c64d8f30",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "3a7c0add06cc86cfbf64d54281fbb3fc2afa56093d2d70d583ddf52ac29d0aca",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a44ac13640150f3a1cbca53ddd3d5af0462c69c44388e8e230c5c8d7f9cef9ab",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "497fb2f4465c60e1037273b1aae754ee159f8c4da9f15cae594c5350fd50cd53",
      "bytes": 2021
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "19a4e807b86dc48c62515adb744187d9bc684119ee1774b8639aa865a03398ea",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "196acce3e9114abed2b8070a5c59a673e0b3efd949b0002bbc9fd284d05dd693",
      "bytes": 930
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "233796857221c696d3b048439fff67bebdf7fbd3b7a82c7633d503251ba39a1d",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "79e8dc47cf872f00f5b5087599e3aaae9f006ff04de1c74ee32f06c6ca7d4a4f",
      "bytes": 889
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "258b4036a6641496f9be4b5d8a428dbebe23ea7ddd67cf558a6266957c8e036c",
      "bytes": 159469
    }
  ],
  "estimated_tokens": 16028
}
-->

# Durable State Update — Chapter 532

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 532. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 532. Profile updates may replace only one
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
  "chapter": 532,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 532,
    "continuity_sources": [532],
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
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Wudang's second report identifies Jang Sam as the Killing Ghost and links his transformation to the Blood Fish.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Ju Hwaran was among the two men and woman accompanying an unidentified giant, remained unharmed, and has just called out to Taekyung after a long separation.",
    "The unidentified giant attacked Hwangbo Ak after Hwangbo insulted him; Taekyung stopped both, forced reconciliation, warned Hwangbo against further provocation, and sent him away."
  ],
  "continuity_sources": [
    531,
    530
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Who is the unidentified giant accompanying Ju Hwaran and the two men, and what is his relationship to her?",
    "How will Taekyung incorporate Mungyeong's martial principles, and what effect will the custom pill have on him?"
  ],
  "safe_through": 531,
  "temporary_decisions": [
    "Render 숭산결의 as Mount Song Resolution, 고월루 as Gowolru, and 취팔선보 as Drunken Eight-Immortals Step; retain footwork technique for 보법.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 홍적 as Hong Jeok, 모용영휘 as Murong Yeonghwi, and 복마전 as demon-slaying battleground.",
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 쌀벌레 as Rice Weevil and 만두 벌레 as dumpling grub; retain the chapter's blunt profanity, monster-comparison humor, and the unidentified giant's clipped childlike speech."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 은비화    | **Dagger Hidden Flower**      | Ju Hwaran      |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 무당파    | **Wudang**                       |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 표국     | **Escort Bureau**                            |
| 표사     | **escort**                                   |
| 소국주    | **Young Bureau Head**                        |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 보상               | **Reward**                     |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 곤륜     | **Kunlun**             |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 형장      | **Brother** / **Brother [Name]**                                |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 은자 | **silver nyang** | Silver currency unit. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 곤륜운룡 | **Kunlun Cloud Dragon** | Epithet of a Kunlun Sect young prodigy. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 광동진가 | **Guangdong Chen Family** | Family whose last child Ju Gongsan carried to Henan during the Great Faction War. |
| 광동 | **Guangdong** | Province under Demonic Cult control during the war. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 황보세가 | **Hwangbo Family** | Hwangbo Ak's established martial family and the long-standing hegemon of Shandong. |
| 황하 | **Yellow River** | River along which civilization began. |
| 고월루 | **Gowolru** | Three-story inn where the meeting was scheduled. |

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
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 528
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, and the creator of the snake-inspired Mimi Step footwork technique.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 526
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 531
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 530
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 529
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 529
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 529
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 531
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal and now investigating at least two escort captains suspected of aiding his scheme.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, and Jin Taekyung’s earlier reassurance remains emotionally vivid to her as she calls out to him after a long separation.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 330
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 330
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau and one of its Dragon-Phoenix Three Escorts who developed his martial ability on battlefields, was known as the Soul-Chasing Guest ten years ago, and plans to remain one more month to help Ju Hwaran purge traitors before seeking an elixir for Ju Hogun in Xianyang.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

## Korean source

```text
＃532화



청년은 곰곰이 생각했다.

어디서부터 잘못된 걸까.

누군가가 사 놓은 만두를 꾸역꾸역 삼켰던 것? 아니면 살살 아려 오는 배를 무시하고 호법을 서다 깜빡 졸았던 것?

정확히 어디서부터 어떻게 잘못된 것인지, 도저히 모르겠다. 다만 한 가지는 확실하다.

콰앙!

측간에 들어서자마자 갑자기 울려 퍼진 굉음이, 그의 모든 것을 끝장냈다는 사실 말이다.

“아아, 따뜻해…….”

언젠가 조장님이 그랬다. 포기하면 편하다고.

그 말이 맞았다. 쾌감은 황홀했고 그의 하반신에서는 어머니의 품과도 같은 따스함이 느껴졌다.

그런데 왜 볼에서는 눈물이 흐르는 걸까.

‘왜긴. 씨바.’

쌌다. 싸 버렸다.

그것도 사람들이 우글거리는 대로변에 위치한 대형 객잔의 측간에서.

돈푼깨나 있는 이들만 출입하는 고급 객잔이기에 칸막이로 분리되어 있다는 사실이 한줄기 위안이었지만, 이 꼴로는 죽어도 나갈 수 없다는 사실은 변하지 않았다.

‘만약 이 모습을 누군가에게 들켰다가는 끝장이다.’

상상만으로도 등골이 오싹해지고 오장육부가 뒤틀린다.

자존심과 무공을 빼면 가죽만 남는 것이 바로 무림인이다.

지금 이 모습이 발각되어 소문이 퍼지느니, 차라리 잔혹한 마두와 목숨을 건 생사결을 펼치는 편이 훨씬 나았다.

‘어떡하지?’

일생일대의 고민.

하의와 속곳은 당연히 버려야 한다. 얼마 전 큰맘 먹고 장만한 가죽신도 이미 회생 불능이다.

그럼 이걸 모조리 벗고, 상의를 얼굴에 뒤집어쓴 채 온 힘을 다해 뛴다면…….

‘죽겠지.’

덜렁거리며 필사적으로 대로변을 가로지르는 놈이 있다면 당장 쳐 죽여도 무림에서는 합법이다.

지나가던 무림인들이 죄다 뛰쳐나와 병장기를 휘둘러 댈 것이 분명했다. 어쩌면 암천의 마두보다 더한 공격을 받을 수 있었다.

‘그럼 다른 사람의 도움을 받는 수밖에 없는데. 점소이라든지.’

이건 그나마 낫다. 점소이를 불러 적당히 은자를 쥐여 주면 몸을 닦을 만한 면포와 옷을 가져다줄 테니까.

혹시 점소이가 그의 정체를 알고 있다면 추가 비용이 들겠지만, 장례식 비용을 치르는 것보다는 나았다.

‘다른 사람들은…… 아니다. 조장님이나 궁기방, 그 인간들한테는 절대 이 모습을 보여서는 안 돼!’

혁무진은 굳게 다짐했다.

안타깝게도 그와 동행한 이들은 집요하기로는 독사보다 더한 종자들이었다. 이런 약점을 잡혔다가는 십 년은 기본이고 이, 삼십 년까지 놀려 댈지도 모른다.

아니, 어쩌면 혁무진이 임종하기 직전에도 멈추지 않을 것이 분명했다.



‘무진아…….’

‘아이고, 혁가 놈아!’

‘허허, 때맞춰 오셨군요. 조장님. 그리고 궁 대협.’

‘흑흑. 당연히 때맞춰 와야지! 넌 그날 늦어서 바지에 똥을 지렸지만 난 늦지 않아!’

‘혁가야, 이제 편히 쉬어라. 이제 병풍 뒤에서 마음껏 똥 냄새를 풍겨도 괜찮아.’

‘……제발 그만해.’



생각하는 것만으로도 비참한 최후다.

잠깐 점소이를 시켜 처소에 남아 있는 청풍을 부를까도 생각해 봤지만, 그건 제 무덤을 파는 격이었다.



‘와아, 저 바지에 똥 지린 사람 처음 봐요! 처음에는 뱀인 줄 알았어요! 미미와 닮은 천년 똥각사예요!’

‘잠깐. 청 소협! 잠깐만요!’

‘기다리고 계세요. 다른 분들을 불러올게요! 저기요! 거기 지나가시는 무당파 도사님! 여기 제가 아는 분이 똥을 지리셨는데…….’

‘야, 이 개새끼야!’



차라리 목에 ‘똥 지린 놈’이라고 푯말을 걸고 다니는 편이 백배 낫다.

뇌리를 가득 채운 끔찍한 상상들로 등골이 서늘해진 혁무진이 몸을 떨고 있던 바로 그때였다.

드르륵.

문이 열리는 소리와 함께 느껴지는 누군가의 인기척.

눈이 번쩍 뜨인 혁무진이 헛기침을 내뱉었다.

“커흠. 큼.”

문밖에서 별다른 반응이 없자, 기침 소리는 더욱 거세졌다.

“커흐흐흠! 거기 누구. 콜록, 없나. 콜록!”

“음?”

드디어 반응이 왔다. 마른침을 꿀꺽 삼킨 혁무진은 억지로 근엄한 목소리를 쥐어 짜냈다.

“점소이인가?”

혁무진의 물음에 문밖의 누군가가 대답했다. 젊고 부드러운 사내의 목소리에는 자연스러운 하대가 배어 있었다.

“점소이를 찾는 모양인데, 안타깝지만 그쪽까지 신경 쓸 겨를이 없다네. 당신도 들었으니 알겠지만 제법 큰 소란이 일어났거든.”

모를 수가 없다. 그 빌어먹을 굉음이 결정적인 원인이었으니까. 그렇다고 건물이 무너진 것도 아니라 다들 수습에 바쁜 모양이었다.

‘그래도 이 와중에 측간에 들르는 사람이 있다는 사실을 위안으로 삼아야지.’

혁무진이 내심 중얼거린 그때였다.

“그럼 욕보게.”

무심하게 건넨 한 마디와 함께 서서히 멀어지는 인기척. 가슴이 덜컥 내려앉은 혁무진이 외쳤다.

“자, 잠깐! 잠깐만!”

“음?”

“미안하지만 나 좀 도와줄 수 있소? 꼭 도움이 필요하오.”

“글쎄. 나도 바쁜 몸이라.”

“그, 아주 사소한 문제가 생겨서 그렇소.”

“사소한 문제라면 알아서 해결해야지.”

“잠깐만! 형님! 아버님! 은인!”

짧은 침묵 후, 재차 목소리가 들려왔다.

“혹시, 지렸나?”

지렸나. 지렸나. 지렸나……

메아리치듯 귓가를 파고드는 한 마디. 혁무진이 울먹거리는 목소리로 대답했다.

“흑. 그렇소.”

“큰 거? 작은 거?”

“…….”

“허어. 둘 다?”

“크흑. 흐으윽.”

문밖의 사내가 작게 중얼거렸다.

“큰일을 처리하면 작은 일도 자연스럽게 해결된다더니.”

“제발, 제발 나 좀 도와주시오.”

“지나가는 길에 점소이를 보면 언질 정도는 해 두지.”

“지, 지금 가져다 주면 안 되겠소? 그때가 되면 말라 버릴 수도 있단 말이오.”

“……더럽군. 그럼 만날 사람이 있어서 이만.”

“자, 잠깐!”

다급해진 혁무진은 눈을 질끈 감고 입을 열었다.

“나, 나는 혁무진이라는 사람이오! 보아하니 형장도 무림인 같은데, 한 번만 도와주고 함구한다면 내 이 은혜는 절대 잊지 않겠소!”

“혁무진이라면. 혹시 열화신룡의 새끼발가락이라는?”

“……그렇소. 그리고 새끼발가락이 아니라 오른팔이오.”

혁무진은 눈앞이 캄캄해졌다. 문밖의 사내가 무림인이라는 사실을 짐작했지만, 이렇게 단박에 자신의 정체를 알아차릴 줄은 몰랐던 탓이었다.

하지만 적어도 떠나려는 상대의 발길을 붙잡고자 하는 의도로는 성공적이었다.

“우연인지, 필연인지 모르겠군. 재미있어.”

“……?”

펄럭.

혁무진이 의아해하던 그때, 의미를 알 수 없는 낮은 웃음소리와 함께 머리 위로 비단 장포가 훨훨 떨어져 내렸다.

엉겹결에 장포를 받아든 혁무진이 더듬거리는 목소리로 감사를 표했다.

“고, 고맙소.”

“적당히 닦고 나오게. 은혜를 갚을 기회를 줄 테니.”

“그. 혹시, 우리 조장님과 아는 사이…….”

“초면일세. 하지만 열화신룡도 딱히 날 박대하진 않을 거야.”

부드러운 목소리가 이어졌다.

“자신의 새끼발가락, 아니 오른팔을 도와준 은인 아니겠나.”

“……!”

혁무진은 깨달았다. 상대의 정체가 무엇인지는 몰라도, 뭔가 단단히 잘못 걸렸다는 것을.

그러나 이미 후회하기에는 늦은 상황. 혁무진이 딱딱하게 굳은 얼굴로 입을 열었다.

“이러려고 장포를 던져 준 거요?”

“왜. 마음이 바뀌었나? 그럼 장포를 도로 던…….”

“기왕 이럴 거면 입을 만한 옷도 좀 구해 주시오. 지금 닦는다고 어떻게 될 수준이 아니오.”

“…….”



* * *



고월루(古月樓).

그것이 호화로운 삼 층 객잔의 이름이었다.

큰 규모만큼이나 말썽도 자주 일어나는지, 우리가 안으로 들어서자 기다렸다는 듯 주인장이 십여 명의 고용 무사들을 거느리고 다가왔다.

그러고는 험악한 얼굴로 입을 열었다.

“뉘신지는 모르겠으나, 제아무리 강호의 소협들이라 하셔도 보상은 치러야…….”

나는 이야기를 끝까지 듣지도 않고 말을 잘랐다.

“우선 심심한 위로를 드리고, 수리비 얼마 나옵니까?”

“뭐요?”

“수리비.”

“……이백 냥쯤 나올 것 같습니다만.”

“그럼 이것저것 피해 보상까지 합쳐서 삼백 냥으로 합시다.”

“예?”

끽해야 삼 층의 난간과 벽 일부가 좀 무너진 정도다.

큰맘 먹고 이백 냥을 불렀는데 삼백 냥으로 응수했으니 주인장 입장에서는 뭐 하는 놈인가 싶을 거다.

하지만 나는 엄청난 금액을 불러 놓고도 거리낌이 없었다. 이유는 간단하다.

어차피 내 돈 아니니까.

“단, 황보세가 이름으로 달아 놔요. 돈 받으러 갔는데 거기 소가주라는 놈이 지랄하면 진태경이 시켰다고 하고.”

“그 말을 제가 어떻게…… 잠깐. 진태경?”

수상쩍은 눈빛으로 나를 훑던 주인장과 고용된 칼잡이들이 눈을 부릅떴다.

“지, 진태경이면. 태원진가의 그 진태경?”

“헉, 열화신룡! 열화신룡이다!”

“나, 강림.”

하남 대로변에서 이 정도 규모의 객잔을 운영하려면 그만한 능력이 있어야 한다.

그리고 고월루의 주인장은 확실히 눈치가 빠른 편이었다.

“진태경 대협께서 방문해 주시다니, 일생의 영광입니다!”

“기왕이면 가문의 영광으로 생각하세요. 그나저나 아까부터 목이 깔깔한데…….”

“상다리가 부러지도록 차려 올리겠습니다! 다들 뭣 하는가!”

역시 화를 가라앉히는 데에는 금융 치료가 최고지.

언제 그랬냐는듯 초롱초롱해진 눈망울로 외친 주인장이 칼잡이들을 이끌고 사라지자, 옆에서 작은 웃음소리가 흘러나온다.

나는 듣는 것만으로도 귀가 간지러워지는 웃음소리의 주인을 향해 고개를 돌렸다.

“왜요?”

은비화(隱匕花) 주화란. 그녀가 물망초 같은 눈빛으로 대답했다.

“그냥, 지난번 일이 생각나서요.”

“지난번이라면. 아.”

“설마 잊으신 건 아니죠?”

“그럴 리가 있습니까.”

용봉표국과 종남파 간의 분쟁.

적천강의 치료를 위해 사천으로 향하던 나는 우연히 그 일에 끼어들었고, 힘으로 내리찍으려는 태을무정검을 꺾은 뒤 협상 과정에까지 참여했었다.

‘그때 종남파 기둥뿌리 두세 개 정도는 뽑았지.’

주화란은 지금 그때의 상황을 떠올린 것이 분명했다. 나를 바라보는 눈동자가 은은하게 빛났다.

“얼마 되지도 않았는데, 참 오랜만인 것 같아요.”

“그러게요. 신기하네.”

정작 신기한 것은 따로 있었다. 대화하는 사람의 눈을 바라보며 이야기하는 것이 이렇게 힘든 일이었다니.

“왜 시선을 피하세요?”

“사시입니다. 지금 똑바로 보고 있는 거예요.”

“풋.”

“왜, 왜 웃어요.”

무슨 말이라도 잘못했나?

당황하는 나를 보며 주화란이 가벼운 미소를 띠었다.

“참 여전하시네요, 진 대협은. 하나도 변하지 않았어요.”

“주 소저도…… 여전하십니다.”

무심코 튀어나오려는 말이 있었지만, 겨우 참았다.

그건 옆에서 가늘어진 눈매로 이쪽을 바라보는 몇 쌍의 눈동자 때문이기도 했다.

나는 기침을 하는 척하며 은밀히 전음을 흘려보냈다.

- 기방아. 뭘 그렇게 뚫어져라 쳐다보냐. 명치 뚫리고 싶니?

- 크흠. 큼.

한 놈 클리어.

하지만 아직도 무려 세 놈이나 남아 있다.

나는 그중에서도 가장 쓸모없어 보이는 놈을 그윽하게 바라보았다.

- 어이.

곤륜운룡 학우, 성라대연 예선 당시 내게 정수리를 밟혀 추락한 곤륜파 최고의 후기지수다.

어째서인지 원형 탈모가 생긴 그가 내 시선에 흠칫 놀라며 전음을 보냈다.

- 무, 무슨 일 때문에 그러시오. 진 도우.

- 별건 아니고. 바쁜 일이 있을 것 같아서.

- 으응?

- 솔직히 말해 봐. 지금 바쁘잖아.

- 무량수불. 안 바쁘오만.

- 아닐걸. 당장 급한 일이 생각나서 가 봐야 할걸.

- 사문에는 이미 오늘 약속에 관하여 허락을 받았소. 급한 일 같은 거 없…….

- 어이, 학 씨.

- 무량수불?

- 가라고. 머리털 죄다 뽑히기 싫으면.

- ……!

탈모인들에게 머리카락이란 목숨만큼이나 소중하다. 이제야 말귀를 알아먹은 학우가 울상이 된 얼굴로 주화란을 향해 입을 열었다.

“저어. 주 소저.”

“응? 왜 그러세요?”

“빈도가 급한 일이 생각나서 가 봐야 할 것 같습니다. 주 소저께는 참으로 죄송한 말씀이지만.”

“아니에요. 전 괜찮으니 어서 가보세요.”

“하지만 그래도 실례인…….”

“멀리 못 나가요. 조심히 들어가세요.”

“잠깐만요. 말이라도 끝까지 들어 주시…….”

“다음에 또 뵐게요!”

지금 보니 주화란은 은근히 성격이 급한 모양이다.

눈물이라도 뚝뚝 떨어질 것 같은 눈으로 나와 주화란을 번갈아 바라보던 곤륜운룡 학우가 사라지자, 아직 처리하지 못한 두 사람에게 자연히 시선이 쏠렸다.

“미리 말해 두는데, 난 안가. 소국주 직속 호위라서.”

검 한 자루를 품에 안고 삐딱한 자세로 앉아 있던 표사. 송일섬의 한마디에 내가 어깨를 으쓱했다.

“가라고도 안 했다. 그럴 생각도 없고.”

“흠. 믿어 주지.”

송일섬의 표면적인 신분은 주화란의 호위지만, 극소수만에게만 알려진 숨겨진 신분은 따로 있다.

바로 정마대전 당시 마교에 의해 멸문당한 철혈의 무가, 광동진가의 마지막 후예이자 과거 추혼객(抽魂客)이라는 별호를 지녔던 불패의 낭인이라는 것이었다.

‘그나저나 이놈은 똑같네.’

그때의 나도 유명했지만, 지금의 명성에 비할 바가 아니다.

그럼에도 송일섬은 변함없이 처음 만났을 때처럼 덤덤하고 까칠한 기색이었다.

어쩌면 그래서 더욱 마음에 드는 것일지도 모른다.

하지만 마지막 남은 한 놈은…….

“배고프다. 밥. 너무 늦다.”

“…….”

저 뻔뻔한 태도 뭔데.

정체불명의 거한. 이 자식은 왜 따라온 걸까.

하지만 이유는 몰랐어도 굳이 막지는 않았다. 녀석의 정확한 정체가 궁금했기 때문이었다.

[기감]으로 확인할 수 있는 건 고작해야 레벨과 이름 정도다. 사문이 어디인지, 누구와 얽혀 있는지는 대화로 파악해야 했다.

“많이 배고픈 모양이네.”

“맞다. 나, 많이 배고프다.”

거한이 심각한 표정으로 말을 이었다.

“오늘. 여섯 끼밖에 못 먹었다. 죽을 것 같다.”

“…….”

여섯 끼 실화냐.

사문이 어디인지는 몰라도 이놈 식비로 기둥 몇 개는 뽑았다는 것에 혁무진 손목을 걸 수도 있다.

‘어, 잠깐만. 혁무진?’

그러고 보니 이 자식은 똥 싸러 간다고 사라지더니 왜 안 나타나?

이제야 혁무진의 빈자리를 눈치챈 내가 주위를 둘러보던 바로 그 순간이었다.

“조, 조장님!”

왠지 모르게 불안한 기색이 잔뜩 서린 외침.

하지만 내 시선은 마침내 나타난 혁무진을 향하고 있지 않았다.

녀석의 등 뒤, 이쪽을 향해 빙긋 웃고 있는 낯선 사내와 눈이 마주친 나는 작게 중얼거렸다.

“저건 또 누구실까…….”
```

## Final English reading copy

```markdown
# Chapter 532

The young man thought long and hard.

*Where did everything go wrong?*

Was it when he had forced down the dumplings someone had bought? Or when he had ignored his mildly aching stomach and accidentally dozed off while standing guard?

He had no idea exactly where or how things had gone wrong. But one thing was certain.

BOOM!

The thunderous roar that had suddenly erupted the moment he entered the privy had ended everything for him.

“Ahhh. So warm…”

His Captain had once told him that giving up made things easier.

He had been right. The pleasure was heavenly, and warmth like a mother’s embrace spread through the young man’s lower body.

So why were tears running down his cheeks?

*Why else? Fuck.*

He had shit himself. He had really shit himself.

And he had done it in the privy of a large inn located on a crowded main street.

The inn was an expensive establishment where only people with money to spare could afford to dine, so the fact that its privies were separated by partitions was a small comfort.

But it didn’t change the fact that he could never leave in this state.

*If anyone finds out what happened, I’m finished.*

His spine prickled and his insides twisted at the mere thought.

A martial artist was nothing but skin once you stripped away his pride and martial arts.

Rather than let anyone discover his current condition and spread the story, he would much rather engage in a life-and-death duel against a cruel fiend.

*What do I do?*

This was the greatest dilemma of his life.

His pants and underwear would obviously have to be thrown away. The leather shoes he had recently bought after working up the nerve to spend the money were already beyond saving.

What if he took everything off, pulled his shirt over his face, and ran across the main street with all his might?

*I’d die.*

In Murim, beating to death a man who was running desperately across the main street with everything dangling freely would practically be legal.

Every passing martial artist would rush out and start swinging their weapons. He might even receive an attack worse than anything a Dark Heaven fiend could unleash.

*Then I have no choice but to ask someone else for help. An inn attendant, maybe.*

That was at least somewhat manageable. If he called over an attendant and slipped him a few silver nyang, the man would bring him a cloth to wipe himself down and some clothes.

If the attendant happened to know his identity, it might cost extra, but that was still better than having to pay for his own funeral.

*What about the others…? No. I absolutely can’t let Captain or Gung Gibang see me like this!*

Hyuk Mujin made a solemn vow.

Unfortunately, his traveling companions were more persistent than poisonous snakes. If they got hold of a weakness like this, they would tease him for at least ten years—possibly even twenty or thirty.

No, they would probably keep going until the very moment Hyuk Mujin was on his deathbed.

*“Mujin…”*

*“Oh, you Hyuk bastard!”*

*“Heh heh. You arrived right on time, Captain. And Great Hero Gung.”*

*“Sob. Of course I had to arrive on time! You were late that day and shit your pants, but I’m not going to be late!”*

*“Hyuk, rest easy now. You can stink up the place behind the folding screen all you want.”*

*“…Please stop.”*

It was a miserable end, even in his imagination.

For a moment, he considered sending an attendant to call Cheongpung, who had remained behind at their lodgings.

But that would be like digging his own grave.

*“Wow! This is the first time I’ve seen someone who shit his pants! At first, I thought you were a snake! You’re a Thousand-Year Dung-Horned Snake that looks just like Mimi!”*

*“Wait. Young Master Cheongpung! Wait!”*

*“Stay here. I’ll go get the others! Excuse me! Daoist from Wudang! Someone I know shit his pants over here…”*

*“You fucking bastard!”*

It would be a hundred times better to hang a sign around his neck that said *The Man Who Shit His Pants* and walk around with it.

Hyuk Mujin was trembling from the chills brought on by the horrifying images filling his mind when it happened.

Rattle.

The door opened, and he sensed someone’s presence.

Hyuk Mujin’s eyes flew open. He cleared his throat.

“Ahem. Cough.”

When there was no response from outside, he coughed even harder.

“Ahem! Ahem! Is anyone there? Cough, cough!”

“Hm?”

At last, he got a response. Hyuk Mujin swallowed dryly and forced out a dignified voice.

“Is that an inn attendant?”

Someone outside answered. The young man’s soft voice naturally carried the casual tone of someone speaking down to him.

“You seem to be looking for an attendant, but unfortunately, I don’t have time to worry about that. You heard it yourself, so you know there’s quite a commotion going on.”

There was no way he could have missed it. That damned roar had been the decisive cause.

It wasn’t as though the building had collapsed, but everyone still seemed busy dealing with the aftermath.

*I should take comfort in the fact that someone is still coming to the privy in the middle of all this.*

That was when Hyuk Mujin heard the man say,

“Then, good luck with that.”

The presence began to recede with those indifferent words.

Hyuk Mujin’s heart plummeted.

“W-Wait! Just a moment!”

“Hm?”

“I’m sorry, but could you help me? I really need help.”

“Well, I’m a busy man myself.”

“A small problem has come up.”

“If it’s a small problem, you should solve it yourself.”

“Wait! Hyung! Father! Benefactor!”

After a brief silence, the voice came again.

“Did you shit yourself?”

Did you shit yourself? Did you shit yourself? Did you shit yourself?

The single question drilled into his ears like an echo. Hyuk Mujin answered in a tear-choked voice.

“Sniff. I did.”

“The big one? The small one?”

“……”

“Good grief. Both?”

“Urgh. Sob…”

The man outside muttered quietly.

“They say taking care of the big job naturally takes care of the small one, too.”

“Please. Please help me.”

“If I see an inn attendant on my way, I’ll let him know.”

“C-Couldn’t you bring me something right now? It might have dried by the time an attendant comes!”

“……That’s disgusting. Anyway, I have someone to meet, so I’ll be going.”

“W-Wait!”

Desperate, Hyuk Mujin squeezed his eyes shut and opened his mouth.

“I-I’m Hyuk Mujin! You appear to be a martial artist as well. If you help me this once and keep quiet about it, I’ll never forget this favor!”

“Hyuk Mujin? As in the Blazing Flame Divine Dragon’s little toe?”

“……That’s right. But I’m his right arm, not his little toe.”

Hyuk Mujin’s vision went dark.

He had guessed that the man outside was a martial artist, but he had never expected the man to identify him so quickly.

At least his attempt to keep the man from leaving had worked.

“I don’t know whether this is coincidence or fate. Interesting.”

“……?”

Flap.

Just as Hyuk Mujin was wondering what he meant, a silk outer robe fluttered down over his head, accompanied by a low chuckle whose meaning he could not understand.

Hyuk Mujin caught the robe by reflex and stammered his thanks.

“T-Thank you.”

“Clean yourself up and come out. I’ll give you a chance to repay the favor.”

“Um. Do you happen to know our Captain…?”

“It’s our first meeting. But the Blazing Flame Divine Dragon isn’t the sort to treat me poorly.”

The soft voice continued.

“Not when I’m the benefactor who helped his little toe—or rather, his right arm.”

“……!”

Hyuk Mujin realized that he had no idea who the man was, but he had clearly gotten tangled up in something serious.

By then, however, it was too late for regret. Hyuk Mujin opened his mouth with a stiff expression.

“Did you throw me this robe for that reason?”

“Why? Have you changed your mind? Then I’ll throw the robe back—”

“If this is how things are going to be, could you find me some clothes to wear, too? I’m far beyond saving with a simple wipe.”

“……”

* * *

Gowolru.

That was the name of the luxurious three-story inn.

Judging by its size, trouble must have broken out there often. The moment we entered, the owner approached us as though he had been waiting, leading more than ten hired martial artists behind him.

He spoke with a fierce expression.

“I don’t know who you are, but no matter how highly regarded you young heroes may be in the martial world, compensation must still be paid—”

I cut him off before he could finish.

“First, my condolences. How much will repairs cost?”

“What?”

“Repairs.”

“……Around two hundred silver nyang, I would say.”

“Then let’s make it three hundred nyang, including compensation for all the other damage.”

“What?”

At worst, part of the third-floor railing and a section of the wall had collapsed.

The owner had gone out on a limb and asked for two hundred nyang, only for me to counter with three hundred. From his perspective, he probably had no idea what kind of person I was.

But I had no hesitation about naming such an enormous sum.

The reason was simple.

*It wasn’t my money anyway.*

“Put it on the Hwangbo Family’s tab. If that Lesser Family Head bastard gives you trouble when you go to collect, tell him Jin Taekyung sent you.”

“How am I supposed to say that…? Wait. Jin Taekyung?”

The owner and the hired blades, who had been studying me suspiciously, opened their eyes wide.

“J-Jin Taekyung? The Jin Taekyung of the Jin Family of Taiyuan?”

“The Blazing Flame Divine Dragon! It’s the Blazing Flame Divine Dragon!”

“I have descended.”

To operate an inn of this size on the main street of Henan, the owner had to be capable.

And the owner of Gowolru was clearly quick-witted.

“It is the honor of a lifetime to receive a visit from Great Hero Jin Taekyung!”

“Better consider it the honor of your entire family. In any case, my throat has been rather scratchy lately…”

“I’ll have a feast laid out so lavishly that it’ll break the table legs! What are you all standing around for?”

As expected, financial therapy was the best way to calm people down.

The owner’s eyes had brightened as though nothing had ever happened. He shouted the order, then led the hired blades away.

A small laugh drifted over from beside me.

I turned toward the owner of that laugh, whose sound made my ears itch just by reaching them.

“What is it?”

Dagger Hidden Flower Ju Hwaran answered with a gaze like forget-me-nots.

“Nothing. I was just reminded of what happened last time.”

“If you mean the last time… Ah.”

“You haven’t forgotten, have you?”

“Of course not.”

The dispute between the Yongbong Escort Bureau and the Zhongnan Sect.

While heading to Sichuan to treat Jeok Cheongang, I had happened to get involved in the matter. After crushing the Taeeul Merciless Sword’s attempt to force the issue through strength, I had even participated in the negotiations.

*I uprooted two or three of Zhongnan Sect’s foundation pillars back then.*

Ju Hwaran was clearly thinking about what had happened. Her eyes glimmered faintly as she looked at me.

“It hasn’t even been that long, but it feels like it’s been ages.”

“It does. Funny, isn’t it?”

The truly strange thing was something else.

Who would have thought that looking into the eyes of the person I was speaking to could be so difficult?

“Why do you keep avoiding my eyes?”

“I’m cross-eyed. I’m looking straight at you right now.”

“Pfft.”

“W-Why are you laughing?”

Had I said something wrong?

Ju Hwaran smiled faintly at my confusion.

“You really haven’t changed at all, Great Hero Jin. Not even a little.”

“You haven’t changed either, Young Lady Ju…”

There was something that almost slipped out, but I barely managed to hold it back.

That was partly because of the several pairs of eyes beside me, watching with narrowed eyes.

Pretending to cough, I secretly sent a Sound Transmission.

*—Gib, why are you staring so hard? Do you want me to punch a hole through your solar plexus?*

*—Ahem. Cough.*

One down.

But there were still three of them left.

Of those three, I looked meaningfully at the one who seemed the least useful.

*—Hey.*

Kunlun Cloud Dragon Hak Woo was the Kunlun Sect’s greatest young prodigy. During the Star-Array Grand Banquet preliminaries, I had stepped on his crown and sent him tumbling down.

For some reason, he had developed a bald spot. He flinched at my gaze and sent a Sound Transmission back.

*—W-What is it, Fellow Daoist Jin?*

*—Nothing much. I was just thinking you probably had somewhere important to be.*

*—Huh?*

*—Tell me honestly. You’re busy right now, aren’t you?*

*—Infinite Life Buddha. I’m not busy.*

*—I don’t think so. I think you’ve just remembered something urgent and need to leave right away.*

*—I have already received permission from my sect regarding today’s appointment. There’s no urgent matter that I need to attend to—*

*—Hey, Hak.*

*—Infinite Life Buddha?*

*—Go. Unless you want me to pluck out every last strand of hair on your head.*

*—……!*

To bald people, hair was as precious as life itself.

Only then did Hak Woo understand what I meant. With a mournful expression, he turned toward Ju Hwaran.

“Um. Young Lady Ju.”

“Yes? What is it?”

“I have just remembered an urgent matter, so I believe I must leave. I’m truly sorry to say this, Young Lady Ju.”

“No, it’s all right. I’m fine, so go ahead.”

“But even so, it’s rude of me to—”

“I can’t walk you out very far. Take care.”

“Wait. At least let me finish what I was saying…”

“I’ll see you next time!”

Come to think of it, Ju Hwaran seemed surprisingly impatient.

Kunlun Cloud Dragon Hak Woo looked back and forth between Ju Hwaran and me with eyes on the verge of tears before disappearing, and my gaze naturally shifted to the two people I had yet to deal with.

“I’ll tell you in advance. I’m not leaving. I’m the Young Bureau Head’s direct escort.”

Song Ilseom, an escort sitting crookedly with a single sword tucked against his chest, spoke flatly.

I shrugged.

“I didn’t ask you to leave. I have no intention of doing so, either.”

“Hm. I’ll take your word for it.”

Song Ilseom’s apparent identity was Ju Hwaran’s escort, but he possessed another hidden identity known only to a very small number of people.

He was the last descendant of the Guangdong Chen Family, an iron-blooded martial family destroyed by the Demonic Cult during the Great Faction War.

He was also an undefeated wandering martial artist who had once gone by the epithet Soul-Chasing Guest.

*Come to think of it, this guy hasn’t changed at all.*

I had been famous back then, too, but my fame was nothing compared to what it was now.

Even so, Song Ilseom was just as calm and prickly as he had been when we first met.

Maybe that was why I liked him even more.

But the last one was…

“Hungry. Food. Too late.”

“……”

What was with that shameless attitude?

Why had this unidentified giant followed us?

I did not know the reason, but I had not stopped him. I was curious about his true identity.

With Qi Sense, I could determine little more than his Level and name. I would have to learn which sect he belonged to and what sort of people he was connected to through conversation.

“You must be very hungry.”

“Correct. I very hungry.”

The giant continued with a serious expression.

“Today. Only ate six meals. Feel like dying.”

“……”

*Six meals? Is that for real?*

I didn’t know which sect he belonged to, but I’d bet Hyuk Mujin’s wrist that this bastard’s food bill had already cost it a few foundation pillars.

*Wait. Hyuk Mujin?*

Come to think of it, he had disappeared saying he was going to shit. Why hadn’t he come back yet?

I had only just noticed Hyuk Mujin’s absence and was looking around when it happened.

“C-Captain!”

The shout was filled with inexplicable anxiety.

But my gaze was not fixed on Hyuk Mujin, who had finally appeared.

Behind him stood an unfamiliar man, smiling faintly in my direction.

Our eyes met.

I muttered quietly,

“Who might that be…?”
```
