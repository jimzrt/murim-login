<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0466.txt",
      "sha256": "c7543a10cca351a3e285bd0967b69b32a95425db406739147d17e011bc3fe180",
      "bytes": 14243
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3ca57369bea314ce5c555ec4a097773c60842d7b976b9eba43e872035b620fe4",
      "bytes": 3399
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "40e16ed958648ca890de876eb17cd1fb2f7d78b3a2efa2a0311eac85444bfaf2",
      "bytes": 151435
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "f37ea950e7d8d2656bc4aa7d00a1ff1d2b3896efbe7972f4018794bd9469246c",
      "bytes": 990
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5abb39e09413dc4eb583c40e3156108f4f0781d26e13b069746cd8f8a9e90843",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "c80ada568c525f87c0601b9408a0b5d38190461f6494f68cc0c669ac1233fa41",
      "bytes": 807
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "127c7b36b263425f07f24c1bf33ee374764ba924bdfb8970d21da2eeefc60d98",
      "bytes": 662
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "0f8d50091ad7dae0652a02a7c6ce2116c210d95e0f4fdd3900ccf0538ed6a112",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "803772152ac2a69603ecca39c8ac1f259c98ae3b72fdc667f0e3c1643c308218",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a5650980c268b0ba8575e7050b93b583a0d0dbbd9ca1bd7eeec781b1a6a530b0",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "184e65bcc5bc18fa87374624023f05bcd4a710550d360b67a965c905dcba7264",
      "bytes": 146297
    }
  ],
  "estimated_tokens": 12349
}
-->

# Durable State Update — Chapter 466

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 466. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 466. Profile updates may replace only one
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
  "chapter": 466,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 466,
    "continuity_sources": [466],
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
    "Taekyung has pierced the Dongting Fisherman’s shoulder with White Flame and pinned him to the cave wall; the confrontation is not yet resolved.",
    "The Dongting Fisherman uses a damaged black-wood fishing rod connected to Heavenly Silkworm Thread, a flexible and extremely tough weapon capable of Force attacks.",
    "The Dongting Fisherman appears eerily emotionless, has blackened eyes during his charge, and was eating a live fish raw inside the refuge.",
    "Taekyung’s opened Middle Dantian has expanded his senses and enabled him to read the Heavenly Silkworm Thread’s attack trajectories.",
    "Taekyung lost part of his bare big toe during the duel but remains combat-capable.",
    "Fresh damage throughout the refuge bears the traces of one person’s deliberate force, but its cause and connection to the Dongting Fisherman remain unknown.",
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued the only two survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung’s investigation.",
    "The shared symbols between the Arch Lich’s magic circle and Dark Heaven’s formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators’ wider plans remain unknown.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings."
  ],
  "continuity_sources": [
    465,
    464
  ],
  "open_questions": [
    "What is the Dongting Fisherman’s exact role in Dark Heaven, why does he appear emotionally hollow with blackened eyes, and what will happen after Taekyung’s attack?",
    "What caused the single person’s deliberate destruction inside the refuge, and is it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich’s magic circle and Dark Heaven’s formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What danger did Mungyeong detect, and are the Wudang killer demon and that danger connected to Taekyung, Jeok Cheongang, or Dark Heaven?"
  ],
  "safe_through": 465,
  "temporary_decisions": [
    "Render 천잠사 as Heavenly Silkworm Thread, 운철 as meteorite iron, 초인 as superhuman, and 극쾌 as extreme swiftness.",
    "Render 노괴 as old monster and 신병이기 as divine weapon.",
    "Preserve Taekyung’s dry contemporary humor and blunt profanity; render 씨부럴 as sibu-leol in direct abuse.",
    "Preserve the Dongting Fisherman’s emotionless, inhuman presentation and violent combat voice.",
    "Continue rendering 오기조원 as Five Qi Returning to Origin, 노화순청 as Furnace Fire Pure Blue, 반로환동 as Returned to Youth, and 복자 as diviner."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 칭호               | **Title**                      |
| 산서     | **Shanxi**             |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 내가중수법 | **Inner-Family Heavy Hand** | Taekyung's joking comparison for his mother's painful palm strike. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 흑목조간 | **black-wood fishing rod** | The Dongting Fisherman's distinctive weapon; the broken rod is his only known trace. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 사공 | **boatman** | Old boatman piloting the ferryboat. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 천잠사 | **Heavenly Silkworm Thread** | Rare treasure used as the Dongting Fisherman’s fishing line and weapon. |

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
| 아이들 | 청년 | children_to_stranger | beggar bastard | childlike-insulting | The children repeat their mother's insulting description of Taekyung's beggar-like appearance. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 사공 | passenger_to_boatman | Boatman | commanding | Taekyung orders the boatman to continue to the final site and asks how long the journey will take. |
| 혁무진 | 사공 | passenger_to_boatman | Boatman | weighty-commanding | Mujin presses the boatman to depart despite the worsening conditions. |
| 진태경 | 동정어옹 | hostile interrogator confronting a suspected perpetrator | you | blunt informal and abusive | Taekyung addresses the Dongting Fisherman without honorifics and calls him a sibu-leol bastard. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 463
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 465
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 465
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he is identified as Dark Heaven's tail and suspected perpetrator of the Dongting Lake attack, with hidden refuges throughout the lake.
- **Personality:** The Dongting Fisherman appears eerily emotionless and savage, eating live fish raw and reacting violently when provoked.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 463
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 463
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 462
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 462
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃466화



공력도 사용하지 않고 적당히 힘 조절을 했다지만, 나는 이미 순수한 근력만으로도 인간의 범주를 훌쩍 뛰어넘은 상태다.

뻐억!

정확히 얼굴 한복판을 강타한 주먹에 동정어옹의 전신이 들썩였다. 아마 놈의 입장에서는 쇠몽둥이에 얻어맞은 듯한 충격이었을 것이다.

시커멓게 물든 동공이 순간 파르르 떨리고 딱 벌어진 입에서는 피에 젖은 누런 이빨이 후두둑 쏟아졌다.

‘한 대 더.’

뻑!

입과 코로 핏물을 폭포수처럼 쏟아낸 동정어옹이 신형을 휘청이며 손을 휘저었다.

작은 움직임이었지만 내 예리한 감각은 주위에서 벌어지는 일들을 일목요연하게 받아들였다.

쉭!

미세하지만 날카롭게 바람을 가르며 등 뒤를 노리는 무언가. 나는 이미 그것의 정체를 알고 있었다.

‘천잠사(天蠶絲).’

나는 피하는 대신 흑목조간을 쥐고 있는 동정어옹의 손목을 꺾었다.

콰득, 뼈가 부러지며 힘을 잃은 손아귀에서 흑목조간이 미끄러진다. 동시에 강기가 실려 있던 천잠사가 나풀나풀 흩날렸다.

“어디서 개수작이야, 개새끼가. 누굴 호구로 보냐?”

그리고 대답 대신 돌아온 것은 묵직한 파공성이었다.

후웅!

동정어옹이 내지른 일장이 무시무시한 기세로 쏘아졌다. 그러나 이미 대비하고 있던 나는 당황하지 않고 마주 손을 뻗었다.

꽈앙!

쾌속하고 간결한 화염신장(火焰神掌)의 일 초.

각기 희고 푸른 두 개의 강기가 허공에서 부딪치자 칼날 같은 바람이 휘몰아쳤다.

거칠게 나부끼는 머리카락 사이, 나는 서늘한 눈동자로 동정어옹을 응시했다.

“뭐 하냐. 머리털도 없는 새끼가.”

“……!”

대답 따위는 필요 없다.

나는 이미 무엇을 해야 할지 알고 있었고, 번개 같은 속도로 내질러진 발끝은 이미 동정어옹의 무릎을 후려치고 있었다.

뻑!

뼈가 으스러지는 소리와 함께 놈의 신형이 휘청이고 입가에서 핏물이 쏟아진다.

상당한 충격으로 순간 공력의 흐름이 끊기자, 맞닿아 있던 동정어옹의 손바닥에 맺힌 수강(手罡)이 흐릿해졌다.

“자, 우리 오늘부터 일 일이다.”

이미 힘의 저울추는 기울어졌다. 나는 놈의 손가락 사이로 단단히 깍지를 낀 뒤, 온 힘을 다해 꺾었다.

우드득!

시부럴. 지금까지 살면서 여자랑 손 한 번 못 잡아 봤는데, 무림에서 나랑 손깍지 낀 사내놈들만 한 트럭이다.

물론 모태솔로의 울분이 실린 다정한 손깍지인 만큼 효과는 언제나 확실했다.

바로 지금처럼.

“끄아아아악!”

잠잠하던 동정어옹의 입에서 고통에 찬 비명이 터져 나왔다.

시커멓게 물든 눈동자를 부릅뜬 놈을 향해, 나는 연달아 주먹을 내질렀다.

뻑, 퍼억! 퍼버버벅!

쉴 새 없이 쏟아지는 일권, 일장의 소나기에 저항하던 동정어옹의 움직임이 천천히 잦아들었다.

아니, 잦아들었다고 생각한 그 순간이었다.

“쿠에에에엑!”

무엇 때문이었을까?

승기를 완전히 굳혔다는 방심? 혹은 죽이지 않고 사로잡을 수 있다는 자신감?

그 이유야 어찌 되었건 나는 철저하지 못했고, 그것이 빈틈을 만들었다.

촤아아악!

온통 붉게 물든 시야. 동정어옹이 토해 낸 끈적한 핏물이 얼굴을 흠뻑 적시고 순간 몸을 굳게 만들었다.

그리고 살고자 하는 초절정 고수의 반격은 생각 이상으로 거셌다.

퍼엉!

압축된 공기가 터져 나가는 소리와 함께, 화룡갑의 표면을 투과하듯 흘러들어온 한 줄기의 공력이 내 상반신을 후려쳤다.

순간 아득해지는 시야. 빠르게 스쳐 지나가는 주위 풍경 속에서 머릿속을 스치는 생각이 있었다.

‘빌어먹을. 내가중수법(內家重手法).’

아직도 이 정도의 힘이 남아 있었나.

나는 목구멍을 타고 울컥 솟구치는 핏물을 삼키며 공력을 끌어올렸다.

비록 예상치 못한 일격을 허용하긴 했지만, 동정어옹의 상태에 비하면 이 정도는 아무것도 아니다.

불시에 내가중수법에 당하고도 지금처럼 작은 내상에 그쳤다는 것이 바로 그 증거였다.

솨아아아악!

나는 순간적으로 끊어졌던 공력을 전신의 사지 백해로 흘려보냈다.

내가중수법의 영향으로 망가진 혈도가 약간의 통증을 호소했지만 딱 그 정도다.

연못에서 한 바가지의 물을 퍼냈다고 해서 연못의 잉어가 죽지 않는 것처럼, 나 역시 마찬가지였다.

‘끝낸다.’

빠르게 쏘아지던 신형을 허공에서 뒤집었다. 어느새 코앞까지 들이닥친 반대편의 동굴 벽면을 부드럽게 밟은 뒤, 발끝으로 흘려보낸 공력을 터트렸다.

꽈앙!

하늘이 쪼개지는 듯한 굉음과 함께, 단단하기 그지없는 벽면의 암석들이 터져 나갔다.

수백, 수천 개의 돌조각이 사방을 찢었지만 나는 이미 그곳에 없었다.

쐐애애애액!

바위보다 무겁고, 바람보다 빨랐다.

튕겨 나왔을 때보다 몇 배는 더 쾌속하게 공간을 격하며 쏘아지는 내 전신에는 만근의 무게가 실려있었다.

“동정어옹-!”

내 입술 사이로 터져 나온 고함이 넓은 동공을 뒤흔들었다. 목소리에 실린 수 갑자의 열양지기가 물을 짓누르고 바위를 밀어 냈다.

그리고, 그 끝에 한 사람이 있었다.

“……!”

어깨와 암벽을 동시에 관통한 백염(白炎)을 막 빼낸 동정어옹이 나를 발견하고 눈을 크게 떴다. 검게 물든 동공이 흔들리고 얼핏 흰자위가 스쳐 지나간다.

덜덜 떨며 벌어지는 주둥이에서 하나 남은 앞니가 애처롭게 떨렸다.

“오, 오, 오, 오지…….”

오지 말라고? 좆 까.

조금 전만 해도 미친놈처럼 굴던 놈이 왜 저렇게 벌벌 떠는지는 모르겠지만, 나는 이미 마음을 굳힌 상태였다.

‘가급적 멀쩡히 데려가려고 했는데…… 안 되겠어.’

이제 와서 후회한들 늦었다. 동정어옹은 훨씬 전에 후회했어야 했다.

암천의 손을 잡기 전, 무고한 양민과 어린아이들을 무참히 살해하기 전에 후회하고 반성해야 했다.

여기까지 온 이상 반성은 필요 없다. 남은 것은 그가 지은 죄에 대한 처벌뿐이다.

‘넌…… 뒈졌다.’

사지를 으스러트려도 상관없다. 머리털과 이빨을 죄다 뽑아 버리고 엉덩이에 종유석을 박아 넣어도 숨만 붙어 있으면 된다.

놈의 목숨을 거두는 것은, 암천에 관한 모든 정보를 토해 낸 다음이 될 것이다.

딱 숨만 붙어 있을 만큼만. 그리고 동정어옹이 한 짓에 대한 분노가 조금이라도 줄어들 정도로만.

그 정도의 힘으로 놈을 향해 쏘아졌고, 느릿해진 세상 속에서 주먹을 뻗었다.

‘멸염신권(滅炎神拳).’

후우우웅!

거세게 타오르는 청백색의 겁화가, 동정어옹이 부러진 손으로나마 내뻗은 일장(一掌)을 집어삼켰다.

어느새 흙탕물처럼 탁한 색을 띤 수강이 열양지기에 의해 부서지고 증발했다. 쉴 새 없이 휘몰아치는 바람과 섬광 너머, 화염에 휩싸인 주먹이 동정어옹을 둘러싼 호신강기를 깨트렸다.

콰직! 콰아아아앙!

실핏줄이 모두 터져 나간 눈동자를 부릅뜬 동정어옹이 피를 토하며 벽면에 틀어박혔다.

단단한 암석으로 이루어진 동공의 벽에 거미줄 같은 실금이 번졌고, 이내 거대한 균열이 되어 천장까지 번졌다.

쿠궁, 쿠구구구궁!

천장이 무너지고 지반이 갈라졌다. 그간 동정호라는 광활한 담수호의 깊은 강물 속에서 엄청난 수압을 버텨 내던 암석들이 하나둘씩 무너져 내리자, 곳곳에서 물줄기가 솟구쳤다.

‘붕괴.’

언제 만들어졌는지 모를 이 공간은 곧 무너져 내릴 것이다. 다시는 자신의 비처로 돌아오지 못할 주인처럼.

‘서둘러야 한다.’

투두두둑!

나는 이미 의식을 잃은 동정어옹의 혈을 짚어 피를 멎게 하고, 만약의 상황을 대비하여 털끝 하나 움직일 수 없도록 점혈했다.

그리고 자그마한 체구의 그를 둘러업고 망설임 없이 주먹을 뻗었다.

꽈앙! 콰과과과과!

싱크홀처럼 뻥 뚫린 바닥의 구멍으로 내려다보이는 급류(急流). 나는 크게 심호흡한 뒤 거센 물살을 향해 뛰어내렸다.

풍덩!

전신을 감싸는 차가운 강물과 함께, 익숙한 메시지가 귓가에 울려 퍼졌다.

띠링. 띠링. 띠링.



- [수상 구조대원]의 칭호 효과가 발동되었습니다!

- 칭호에 내장된 특수 스킬이 적용됩니다!

- [수상 구조대원의 물갈퀴]가 생성되었습니다!

- [수상 구조대원의 아가미]가 생성되었습니다!

- [남은 지속 시간 : 18시간 43분 32초]



시간은 충분하다. 나는 물살을 따라 힘차게 몸을 움직였다.

그리고 얼마 지나지 않아, 입과 코로 쉴 새 없이 거품을 내뿜는 동정어옹의 모습에 잠시 간과하고 있던 사실을 깨달았다.

‘이게 무슨…… 아.’

제아무리 수공의 고수라 해도, 그건 수공을 운용할 만큼의 공력과 의식이 멀쩡할 때의 이야기다.

나처럼 아가미를 이용해 숨을 쉬지는 않을 테니 수중에서의 시간이 길어지면 죽을지도 모른다.

‘잠깐, 그렇다면.’

순간 머릿속을 스치는 한 줄기 깨달음.

동시에 나는 온 힘을 다해 헤엄치기 시작했다. 손깍지는 몰라도 첫 키스까지 헌납할 수는 없다.

그것도 백 살에 가까운 미친 늙은이와는 더더욱!



* * *



쿠구구구궁!

깊은 물 속 어딘가에서 시작된 진동은 지상에 있는 이들에게도 전해질 만큼 거대했다.

난데없이 일어난 이변에 늙은 사공은 두려움 가득한 눈빛으로 몸을 움츠렸고, 다른 세 사람의 얼굴은 딱딱하게 굳었다.

“저기, 아무래도…….”

“드디어 시작된 모양이오. 아니면 이미 끝났거나.”

청풍의 중얼거림을 궁기방이 무거운 목소리로 받았다.

초조하게 흔들리는 절벽과 강물을 바라보던 혁무진이 불쑥 입을 열었다.

“가 봐야겠습니다.”

궁기방이 미간을 좁혔다.

“뭐?”

“조장님께 무슨 일이 생긴 게 확실합니다. 기분이 좋지 않아요.”

“하지만 진태경, 그 녀석이…….”

“꼼짝 말고 기다리라고 하셨죠. 압니다.”

“그럼, 왜?”

“제가 원래 사람 말을 더럽게 안 듣거든요.”

“빌어먹을, 자랑이다.”

“이곳에서 손가락이나 빨고 있는 것보다는 낫지 않겠습니까?”

혁무진의 말에 궁기방이 아랫입술을 잘근잘근 씹었다.

안 그래도 그 역시 아까 전부터 꺼림칙함을 느끼고 있던 차였다.

정확히 언제부터였는지는 모르겠지만, 가슴이 거세게 두방망이질치고 촉각이 날카롭게 곤두섰다.

‘왜 이러지? 정말 그놈에게 무슨 일이라도 생긴 건가?’

한 사람의 얼굴이 눈앞을 스친다.

산서잠룡, 아니 열화신룡 진태경.

당장 저승 밑바닥으로 떨어트린다 해도 살아 돌아올 것 같은 놈. 아귀보다 독하고, 염라대왕도 때려눕힐 것 같은 놈.

‘그놈이 죽는 건 지금까지 단 한 번도 생각해 본 적이 없는데…… 아니, 절대라는 건 없으니까 설마?’

궁기방은 진태경이 강물에 들어가기 전 했던 말을 결코 허투루 듣지 않았다. 이미 지금껏 동행하며 그의 언행에는 항상 이유가 있다는 사실을 알고 있었기 때문이었다.

하지만 지금은 갈등하지 않을 수 없었다.

‘이런 니미럴 거. 날씨도 지랄 같은데. 도대체 어떻게 해야 하지?’

우르르릉, 쾅!

두어 시진 전 늙은 사공이 했던 말대로, 현재 동정호의 기후는 최악이라는 말도 부족할 지경이었다.

휘몰아치는 폭풍우와 내리치는 낙뢰.

복잡한 눈빛으로 주위를 둘러보던 궁기방이 마침내 입을 열었다. 아니, 입을 열려던 바로 그때였다.

“괜찮아요.”

“응?”

“예?”

궁기방과 혁무진은 동시에 고개를 돌렸다.

두 사람의 시선에 어느새 환하게 웃고 있는 한 사람이 들어왔다.

그들이 밟고 서 있는 작은 섬의 귀퉁이. 바닥에 엎드린 채 무언가를 듣고 있던 청풍이 귀에 묻은 모래를 털며 헤헤 웃었다.

“은인이 와요.”

그리고 다음 순간.

촤아아악!

높은 물줄기와 함께 솟구친 한 사람이 거칠게 모래사장 위로 착지했다.

자그마한 체구의 노인을 들쳐업은 근육질의 청년.

바로 진태경이었다.

“조장님!”

“왔구나!”

“은이이인!”

“오지 마. 이 고추 새끼들아. 만약 날 안으려고 한다면 너희 셋은 오늘 피살된다.”

기쁨의 괴성과 함께 달려드는 세 사람을 제지한 진태경이 진중한 어조로 말을 이었다.

“시간 없으니까 단도직입적으로 물어본다. 여기서 내가 입맞춤을 해 봤다, 거수. 혹은 해 보고 싶다는 사람. 거수.”

두 사람은 눈치가 빨랐고, 한 사람은 절망적일 만큼 눈치가 없었다.

궁기방과 혁무진이 슬그머니 뒷걸음질 칠 때, 해맑은 외침과 함께 한 사람의 손이 번쩍 치켜 올라갔다.

“저요, 저! 저 아직 입맞춤 한 번도 안 해 봤어요!”

“시발, 하느님 감사합니다.”

“예?”

어리둥절한 청풍을 향해, 만면에 환한 웃음을 머금은 진태경이 동정어옹을 내밀었다.

“당신의 소원, 지금 이루어졌습니다.”

우르릉, 꽝!

뇌성벽력이 사방 천지를 울렸다.
```

## Final English reading copy

```markdown
# Chapter 466

Even without using internal energy—and though I’d held back—I had already far surpassed human limits through pure physical strength alone.

*Boom!*

The fist struck him squarely in the middle of the face, and the Dongting Fisherman’s entire body jerked. From his perspective, it must have felt like being hit with an iron club.

His pitch-black pupils trembled, and yellow teeth soaked in blood came tumbling from his gaping mouth.

*One more.*

*Thud!*

The Dongting Fisherman, blood pouring from his mouth and nose like a waterfall, staggered and waved his hand.

It was a small movement, but my sharp senses took in everything happening around me with perfect clarity.

*Swish!*

Something sliced through the air with a faint yet sharp sound, aiming for my back.

I already knew what it was.

*The Heavenly Silkworm Thread.*

Instead of dodging, I twisted the wrist of the Dongting Fisherman’s hand gripping the black-wood fishing rod.

*Crack!*

His bones broke, and the hand that had lost its strength let the black-wood fishing rod slip free. At the same time, the Force-infused Heavenly Silkworm Thread fluttered through the air.

“Where do you get off pulling that bullshit, you son of a bitch? Who do you think you’re fooling?”

The answer that came back was a heavy sound splitting the air.

*Whoom!*

The Dongting Fisherman’s palm strike shot toward me with terrifying momentum. But I had already prepared for it, so I reached out to meet it without hesitation.

*Boom!*

A swift, concise move of the Flame Divine Palm.

Two Forces—one white and one blue—collided in midair, and razor-sharp winds whipped around us.

Through my wildly fluttering hair, I stared at the Dongting Fisherman with cold eyes.

“What are you doing, you bald bastard?”

“……!”

I did not need an answer.

I already knew what I had to do, and the tip of my foot was already lashing out at the Dongting Fisherman’s knee with lightning speed.

*Thud!*

His bones crunched. His body staggered, and blood spilled from the corner of his mouth.

The heavy impact momentarily disrupted the flow of his internal energy, and the Palm Force gathered in the palm still pressed against mine began to fade.

“All right. As of today, we’re officially a thing.”

The scales of power had already tipped in my favor. I laced my fingers tightly between his and twisted with all my strength.

*Crack!*

Sibu-leol. I had never even held a woman’s hand in my life, yet here in Murim, I had interlocked fingers with enough men to fill a truck.

Of course, since it was an affectionate finger-lock fueled by the pent-up rage of a lifelong virgin, it was always effective.

Just like now.

“Gyaaaaaaah!”

A scream of pain burst from the Dongting Fisherman’s mouth, which had been silent until now.

I clenched my fist and punched him again and again as he stared at me with his pitch-black eyes wide open.

*Thud! Thud! Thud-thud-thud!*

Under the unceasing rain of fists and palms, the Dongting Fisherman’s movements slowly weakened.

Or so I thought.

“Gueeeeeegh!”

Why?

Carelessness, born from thinking I had completely secured the advantage? Confidence that I could capture him without killing him?

Whatever the reason, I had failed to be thorough, and that created an opening.

*Splaaash!*

My vision turned completely red.

The sticky blood the Dongting Fisherman vomited drenched my face and froze my body for an instant.

And the counterattack of a Supreme Peak master fighting for his life was fiercer than I had expected.

*Boom!*

With a sound like compressed air exploding, a stream of internal energy flowed through the surface of the Fire Dragon Armor as though it had passed straight through it, then battered my upper body.

My vision blurred.

As the scenery flashed past me, one thought crossed my mind.

*Damn it. Inner-Family Heavy Hand.*

He still had this much strength left?

I swallowed the blood surging up my throat and drew on my internal energy.

I had taken an unexpected blow, but compared to the Dongting Fisherman’s condition, this was nothing.

That I had suffered only a minor internal injury despite being caught off guard by the Inner-Family Heavy Hand was proof enough.

*Whoooosh!*

I sent my internal energy, its flow interrupted for only an instant, coursing through every limb and acupoint in my body.

The acupoints damaged by the Inner-Family Heavy Hand complained of a little pain, but that was all.

Just as a carp in a pond does not die because someone scoops out a bowlful of water, I was fine as well.

*I’ll finish this.*

I twisted my body around in midair as I shot forward. The opposite cave wall rushed toward me, so I gently planted my foot against it, then detonated the internal energy that had flowed into my toes.

*Boom!*

With a roar like the sky splitting apart, the unyielding rocks in the wall exploded.

Hundreds—thousands—of fragments tore through every direction, but I was already gone.

*Whoooooosh!*

Heavier than a rock, faster than the wind.

My body tore through the air several times faster than when I had been thrown back, carrying the weight of ten thousand *geun*.

“Dongting Fisherman!”

My shout reverberated through the vast cavern. Several *jiazi* of Scorching Yang Qi infused in my voice crushed the water and pushed the rocks aside.

And at the end of it all, there was one person.

“……!”

The Dongting Fisherman had just pulled White Flame out of his shoulder and the rock wall behind him when he spotted me and opened his eyes wide.

His blackened pupils shook, and a glimpse of white flashed across them.

His trembling mouth opened, and his one remaining front tooth quivered pitifully.

“C-c-c-come…”

Don’t come, you mean?

Fuck off.

I had no idea why the man who had been acting like a madman only moments ago was trembling like that, but my mind was already made up.

*I was planning to take you back in one piece if possible…… but that’s not going to happen.*

Regret would be useless now. The Dongting Fisherman should have regretted his actions long ago.

Before taking Dark Heaven’s hand. Before brutally slaughtering innocent commoners and children. He should have regretted it and repented then.

Now that we had come this far, repentance was unnecessary.

All that remained was punishment for the crimes he had committed.

*You’re fucking dead.*

I did not care if I crushed all four of his limbs. As long as he was still breathing, I could pull out every last strand of his hair and tooth, then drive a stalactite into his ass.

I would take his life only after he had spat out everything he knew about Dark Heaven.

I would keep him alive by the barest margin.

Only until my anger at what he had done had diminished, even slightly.

With exactly that much force, I shot toward him. In the slowed world, I extended my fist.

*Flame-Extinguishing Divine Fist.*

*Whoooooosh!*

The fiercely burning blue-white hellfire swallowed the palm strike the Dongting Fisherman thrust at me, even with his broken hand.

His Palm Force, now murky like muddy water, shattered and evaporated under the power of the Scorching Yang Qi. Beyond the endless whirlwind of wind and flashes of light, my fist wreathed in flame broke through the Body-Protecting Qi surrounding the Dongting Fisherman.

*Crack! Booooom!*

The Dongting Fisherman opened eyes whose blood vessels had all burst, vomited blood, and was driven into the wall.

Fine, spiderweb-like cracks spread across the hard rock of the cavern wall. Soon, they widened into a massive fissure that reached all the way to the ceiling.

*Rumble. Rumble-rumble-rumble!*

The ceiling collapsed, and the ground split apart.

The rocks that had endured tremendous water pressure deep beneath the vast freshwater lake of Dongting Lake began collapsing one after another. Streams of water surged up from every direction.

*Collapse.*

This space, created at some unknown time, would soon come crashing down.

Just like its owner, who would never return to his secret refuge.

*I have to hurry.*

*Rattle-rattle!*

I pressed the Dongting Fisherman’s acupoints to stop the bleeding. Then, in case anything happened, I sealed him with Pressure-Point Strikes so he could not move even a hair.

I hoisted the small old man onto my back, then punched forward without hesitation.

*Boom! Rumble-rumble-rumble!*

A raging current was visible through the hole in the floor, which had opened up like a sinkhole.

I took a deep breath, then leaped toward the violent water.

*Splash!*

As the cold water closed around my body, a familiar message rang in my ears.

> **System**
>
> Title effect activated: Water Rescue Worker
>
> Special Skill embedded in the Title applied.
>
> Water Rescue Worker’s Webbed Feet generated.
>
> Water Rescue Worker’s Gills generated.
>
> **Remaining duration:** 18 hours, 43 minutes, 32 seconds

There was plenty of time.

I moved my body powerfully with the current.

Before long, I saw the Dongting Fisherman constantly blowing bubbles from his mouth and nose. That reminded me of something I had momentarily overlooked.

*What the…… Ah.*

Even if someone was a master of water arts, that only applied when they had enough internal energy and consciousness to operate those techniques.

He did not have gills like I did. If he stayed underwater for too long, he might die.

*Wait. If that’s the case……*

A flash of insight crossed my mind.

At the same time, I began swimming with all my strength.

I might have been willing to donate an interlocked-finger clasp, but I could not give up my first kiss as well.

Especially not to a crazy old man who was nearly a hundred years old!

* * *

*Rumble-rumble-rumble!*

A vibration that began somewhere deep underwater grew so powerful that it reached the people on the surface.

At the sudden anomaly, the old boatman shrank into himself with fear in his eyes, while the other three men’s faces stiffened.

“Um, I think…….”

“It seems it has finally begun. Or perhaps it has already ended.”

Gung Gibang answered Cheongpung’s murmur in a heavy voice.

Hyuk Mujin, who had been anxiously watching the trembling cliff and river, suddenly opened his mouth.

“We have to go.”

Gung Gibang furrowed his brow.

“What?”

“It’s certain that something happened to our Captain. I have a bad feeling.”

“But Jin Taekyung, that bastard…….”

“He told us not to move and wait. I know.”

“Then why?”

“I have a terrible habit of not listening to people.”

“Damn. You sound proud of it.”

“Isn’t it better than sitting here sucking our fingers?”

At Hyuk Mujin’s words, Gung Gibang bit his lower lip.

He had been feeling uneasy for some time as well.

He did not know exactly when it had begun, but his heart was pounding violently, and every one of his senses was on edge.

*Why am I like this? Did something really happen to that bastard?*

A single face flashed before his eyes.

The Sleeping Dragon of Shanxi.

No—the Blazing Flame Divine Dragon, Jin Taekyung.

The kind of bastard who would come back alive even if you dropped him into the deepest pit of the underworld. More vicious than A-Gwi, and strong enough to beat Yama himself into the ground.

*I’ve never once imagined that bastard dying…… No, nothing is absolute, so surely not?*

Gung Gibang had not taken Jin Taekyung’s words before he entered the river lightly. By now, after traveling with him for so long, he knew that there was always a reason behind the man’s words and actions.

But this time, he could not help wavering.

*Goddammit. The weather’s a complete mess, too. What the hell am I supposed to do?*

*Rumble. Crash!*

Just as the old boatman had said a couple of *shichen* earlier, even calling the current weather on Dongting Lake the worst possible would have been an understatement.

A raging storm and lightning crashing down from the sky.

Gung Gibang looked around with a conflicted expression and finally opened his mouth.

Or rather, he was just about to open it when—

“It’s all right.”

“Huh?”

“What?”

Gung Gibang and Hyuk Mujin turned their heads at the same time.

Someone was smiling brightly in their field of view.

At the edge of the small island where they stood, Cheongpung had been lying face-down, listening to something. He brushed the sand from his ear and grinned.

“Benefactor is coming.”

And then—

*Splaaash!*

A person shot up with a towering column of water and landed roughly on the sandy shore.

A muscular young man with a small old man slung over his back.

It was Jin Taekyung.

“Captain!”

“You’re back!”

“Benefactooor!”

“Don’t come near me, you dickheads. If any of you is trying to hug me, all three of you are getting killed today.”

After stopping the three men charging toward him with cries of joy, Jin Taekyung continued in a serious tone.

“We don’t have time, so I’ll ask directly. Raise your hand if you’ve ever kissed someone. Or if you want to try. Hands up.”

Two of them caught on quickly.

One was hopelessly oblivious.

As Gung Gibang and Hyuk Mujin quietly backed away, one hand shot into the air with a bright, innocent shout.

“Me! Me! I haven’t kissed anyone even once!”

“Fuck. Thank God.”

“Huh?”

With a radiant smile on his face, Jin Taekyung held the Dongting Fisherman out toward the bewildered Cheongpung.

“Your wish has just come true.”

*Rumble. Crash!*

Thunder and lightning shook the entire world.
```
