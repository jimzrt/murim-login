<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0488.txt",
      "sha256": "326922d53c3c4bd96836c4db7a2ecd1680222a7de2facd0a5390fa992dbc8cf6",
      "bytes": 13007
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "503d546d04c7eb55bdc9c06a63180184c1ccaf78e4182628bf9866c862bc6498",
      "bytes": 3247
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ba49a5ca9800b988d1f6046bf28ca099fb5513fdcf3a2986d7ad4c6cb004116d",
      "bytes": 155608
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "a89e7deb991b80c81df303057b646eeb360c295c6aec6b51223d8e265fdb89c2",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8e4b88757695d62f0fc811f2a2dbcdbf064f5dc8820b2a03703a88fa24127462",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "40a09953d7429c3ff1bf49ed9e868e2abc570d975581b73320c7f51b89b191a8",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "19adb4a3125f4d3ff33eafb0f5e8552bbf06b2caf69931f393770b02b0788bf6",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "fb020b30a21eae160490c0ec61c92e1363ff4772b8fd524387268fe609204b85",
      "bytes": 844
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4f9a2b6f44f23a401944cbb3ff87467abd5f25164948ba8ba22aebcefbbab70a",
      "bytes": 151253
    }
  ],
  "estimated_tokens": 11518
}
-->

# Durable State Update — Chapter 488

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 488. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 488. Profile updates may replace only one
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
  "chapter": 488,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 488,
    "continuity_sources": [488],
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
    "The functionally crippled Gate continues leaking faint mana; it opened at least a month ago, and its residual mana is mutating local life.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Zhuge Feng ordered the entrance waterways completely sealed, and few Blood Fish appear to have escaped so far.",
    "Mimi can swallow Mutated Minnows several times larger than herself and appears to enjoy eating them.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Jeok trusts Taekyung more deeply than anyone else, despite interpreting Taekyung's attempted explanation of his origin as a drawn-out declaration that he wanted to die.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment.",
    "Jeok asked Mungyeong to look after Taekyung and teach him useful secret martial arts and the mindset needed for the future."
  ],
  "continuity_sources": [
    486,
    487
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and how do they relate to the Gate?"
  ],
  "safe_through": 487,
  "temporary_decisions": [
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter.",
    "Render 선천지기 as innate qi and 진원진기 as true-origin qi.",
    "Render 심마 as Heart Demon and 천기 as heavenly patterns.",
    "Render 독문 무공 as secret martial arts and 비급 as martial arts manual."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 무당파    | **Wudang**                       |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 게이트     | **Gate**              |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 송문고검 | **Pine-Pattern Ancient Sword** | Willow-Cloud Divine Dragon’s sword. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 좌장 | **presiding chair** | Authority overseeing the Star-Array Grand Banquet. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 487
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 487
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 486
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 486
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 487
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a former assassin who passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who has asked him to look after and instruct Jin Taekyung, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃488화



수신룡은 확실히 신령스러운 존재가 맞았다.

큰 틀 안에서 보면 영물이라 할 수 있겠지만, 일반적인 영물 이상의 힘을 지녔기에 게이트의 마력을 모조리 흡수할 수 있었을 것이다.

‘날씨만 봐도 알 수 있지.’

역시 오백 년을 살아온 이무기라 그런지 달라도 뭐가 달랐다.

변이된 상태에서의 수신룡이 날뛰었을 때는 뇌성벽력과 파도로 동정호가 뒤집힐 지경이었는데, 지금은 언제 그랬냐는 듯이 잔잔하다.

하지만 평화로워 보이는 동정호와 달리 내 마음속에서는 격랑이 휘몰아치는 중이었다.

‘……이게 그 폭풍전야인가 하는 그거냐.’

나는 앞서 걸어가는 문경의 뒷모습을 힐끔 바라보았다.

나보다 머리 하나는 작고 호리호리한 몸. 그러나 그 실체는 초식동물의 거죽을 뒤집어쓴 맹수다.

‘아니, 갑자기 나를 왜 불러. 무슨 할 말이 있다고.’

갑자기 억울하네.

설마 전투 때 반말한 것 때문에 아직도 열 받아 있는 건가?

할 말이 있다고 불러내 놓고 몸의 대화를 나눠 보자고 하는 건 아니겠지.

자꾸만 으슥한 곳으로 향하는 문경의 모습에 불안감이 점점 더 커져만 가던 그때였다.

“멈추시게.”

파팟!

목소리는 하나인데, 주위를 둘러싼 신형은 일곱이다.

하나같이 상당한 공력을 쌓은 절정 고수들로 이루어진 그들의 허리춤에는 소나무 무늬가 새겨진 검이 매여 있었다.

‘송문고검(松紋古劍).’

아니나 다를까, 무당파의 복색을 한 중년 도사가 짙은 어둠 너머에서 걸어 나오고 있었다.

연배만 봐도 좌장(座長)격인 중년 도사는 우리를 향해 입을 열었다.

“이곳은 술시(戌時) 이후로 출입을 통제하고 있네. 이만 돌아가…… 아니, 잠깐만. 혹시 열화신룡?”

“예?”

문경의 어깨너머로 나를 발견한 중년 도사가 눈을 크게 뜨며 물었다.

“진태경 소협, 아니지. 진태경 대협 아니오?”

“대협은 아닌데, 제 이름이 진태경이긴 합니다.”

“오오. 역시 내 짐작이 맞았구려. 어쩐지 낯익은 얼굴이다 싶더니.”

그쪽은 낯익을지 몰라도, 이쪽은 생판 남이다.

이제 막 군대에서 전역한 아들 대하듯 나를 반가워하던 중년 도사가 문득 생각났다는 듯이 물었다.

“한데 이 늦은 시각에 여기에는 무슨 일이오? 임시 거처도 이미 배정되었을 터인데.”

“……어. 그게.”

살성한테 끌려가고 있었는데요.

솟구치는 말을 꿀꺽 삼키고 대충 둘러대려던 찰나, 내 머릿속에 한 줄기 깨달음이 스쳤다.

다시 생각해 보니 이건 신이 내려 주신 마지막 탈출 기회다.

“여기부터는 출입 통제 구역입니까?”

“그렇소. 만일을 대비하여 돌아가며 번을 서고 있지. 한데 함께 있는 이 어려 보이는 청년은 누구요?”

“살…….”

“음?”

- 즉참(卽斬).

“살살 부네요. 바람이.”

“아, 허허. 그렇구려.”

살성! 아저씨! 저 새끼 살성!

임금님 귀 당나귀 귀를 외쳤던 이발사의 마음을 알 것 같다.

하지만 깊게 가라앉은 맹수의 시선을 마주한 나는 억지웃음을 지으며 대답했다.

“그냥 이래저래 알게 된 사이입니다.”

“아는 사이라면, 정확히 어떤……?”

“사천에서 알게 되어 그 후로 쭉 동행했죠. 무림인은 아니고, 의생입니다.”

“아아. 기억나는구려. 나이는 어려도 솜씨가 뛰어난 명의(名醫)가 한 명 있다더니, 바로 이 친구였군.”

“네. 이 친구가 그 친구입니다.”

“한데 이런 야심한 시각에 여기까지 온 이유가 무엇이오?”

“어, 긴히 나눌 이야기가 있어서요.”

“꽤 친밀한 사이인가 보오?”

다른 건 넘겨도 이건 인정 못 하겠다.

나는 정색하며 대답했다.

“아뇨. 안 친한데요.”

“흠, 그렇다면 아무래도 좀 곤란하오. 진 대협께는 미안한 말이지만 규정상 확실한 보증 없이는…….”

“아아, 그러시구나. 고생 많으십니다. 문경아, 가자!”

- 즉참.

“…….”

- 원위치.

싸늘하다. 전음이 날아와 꽂힌다.

반쯤 신형을 돌렸던 나는 힘없이 돌아섰다.

- 친하다고 해라.

“농담이고, 사실 매우 친합니다.”

나와 문경을 번갈아 보던 중년 도사가 중얼거렸다.

“그런 것치고는 말 한마디 없이 떨어져서 걷고 있던데…….”

- 잘 대답해라.

“눈빛만 봐도 통하는 사이라서 그렇습니다.”

“고개를 돌렸는데 어떻게 눈빛을…….”

“전에는 눈빛만 봐도 통했는데, 요즘은 뒤통수만 봐도 무슨 생각을 하는지 알겠더라고요.”

“…….”

- 이건 진심으로 궁금해서 묻는 건데, 열화문의 문규(門規)에는 병신들만 뽑으라는 내용이 있나?

아니, 시벌. 나보고 어쩌라고.

뜨뜻미지근한 눈빛으로 나를 바라보는 중년 도사의 시선에, 문경의 전음이 이어졌다.

- 가까이 와라.

“……?”

- 어깨동무.

“……!”

아니, 이게 무슨 아바타도 아니고.

하지만 어쩌겠나, 무림에서는 강한 놈이 법이고 신이다.

털레털레 걸어간 나는 문경의 어깨에 팔을 걸치고 죽을상을 썼다.

“후, 진짜 친해요.”

- 웃어.

“하하하! 진짜 친해요!”

- 더 크게.

“으하하하하하!”

- 곁눈질로 신호 주는 것 다 보인다. 한 번만 더 그랬다가는 눈이 아니라 마음으로 세상을 보게 해 주마.

눈깔을 파 버리겠다는 말을 상당히 우아하게도 한다. 나는 필사적으로 하고 있던 곁눈질을 포기하고 중얼거렸다.

“어쨌건 친합니다.”

그리고 이 모든 상황 속, 중년 도사를 포함한 무당파의 무인들은 올여름 최고의 호러 무비를 본 것 같은 표정으로 바라보고 있었다.

죽을상을 썼다가 미친 듯이 웃고, 그러는 와중에도 미친 듯이 문경을 향해 곁눈질해 대니, 이상한 눈치를 채지 못하면 송문고검 내려놓고 무당파 떠야 한다.

이내 뭔가를 결심한 듯한 얼굴의 중년 도사가 입술을 달싹였다.

- 이건 노파심에 하는 말이오만, 혹 본인이 짐작하지 못하고 있는 어떤 일이 있다면 눈을 세 번, 아무 일도 아니라면 두 번 깜빡이시오.

- 다 들었다. 세 번 깜빡이면 몸뚱어리가 세 조각이 날 줄 알아라.

아저씨! 이 새끼! 이 새끼 살성! 이 새끼 귀에 도청 장치!

하지만 외침은 새어 나오지 못했고, 나는 조용히 눈을 두 번 깜빡였다.

사실 저쪽에서 아무리 의심을 해 봤자 눈앞의 어린 의생이 반로환동으로 젊어진 초절정 고수라고는 짐작하지 못할 거다.

그리고 냉정하게 따지고 보면 살성은 명백한 아군이다.

- 확실하오?

그렇게 물어 봤자 내가 할 대답은 정해져 있었다.

같은 초절정 고수여도 깨달음의 깊이가 다른 적천강과 살성은 다른 이의 전음까지 훔쳐 들을 수 있는 생체 도청 장치니까.

- 예. 제가 왜 이런 걸 속이겠습니까. 그냥 동행하면서 우정을 쌓은 친구예요.

누군가는 우정이 대신 살심을 쌓은 것 같긴 하지만. 그래도 뭔가를 쌓긴 쌓았지.

내 전음을 들은 중년 도사가 피식 실소를 흘렸다.

- 하긴, 천하의 열화신룡에게 무슨 일이 생길 리 있겠소. 진 대협이 넓은 아량으로 이해해 주시구려. 근래 벌어지는 일들 때문에 나도 모르게 예민해졌나 보오.

아냐, 둔감해. 제발 조금만 더 예민해져 줘.

하지만 그런 내 바람과 달리, 중년 도사는 훈훈한 미소와 함께 입을 열었다.

“그렇다면 좋소. 다른 사람도 아니고 진 대협이라면 믿을 수 있지. 통과!”

“자, 잠깐만요.”

“허허, 무슨 연유로 이곳까지 오셨나 했더니 정말 중요한 대화인가 보군. 알겠소, 규정상 그러면 안 되지만…… 잠시 자리를 비켜 드리리다.”

“예?”

“한 식경(食頃). 그 정도면 되겠소?”

당연히 안 되지, 이 양반아. 되긴 뭐가 돼.

하지만 내가 뭐라 대답하기도 전에, 문경이 맑은 미소를 지으며 공손히 고개를 숙였다.

“충분합니다.”

“……!”

저 짧은 대답이 내 귀에는 왜 살인 예고로 들릴까.

눈꺼풀을 파르르 떠는 나를 보지 못한 중년 도인은 수염을 쓰다듬으며 흐뭇하게 웃었다.

“예의가 바른 젊은이로군. 다음에 내 몸도 한 번 봐 주시게.”

“물론입니다, 도사님.”

“허허. 그럼 한 식경 뒤에 돌아오겠소.”

파팟!

중년 도인을 포함한 절정 고수 일곱 명, 아니 목격자 일곱 명은 신형을 날렸다.

순식간에 멀어지는 그들의 뒷모습을 멍하니 바라보던 나는, 주위를 겹겹이 에워싸는 기의 장막을 느끼며 천천히 돌아섰다.

소리와 충격.

어느새 그 모든 것이 기막(氣幕)에 외부로부터 차단된 공간.

그리고 그곳에, 어둠 속에서도 시린 빛을 뿜어내는 한 쌍의 눈동자가 있었다.

“스승이나 제자나, 사람 피곤하게 만드는 건 쏙 빼닮았군.”

“……!”

듣는 것만으로도 가슴이 서늘해지는 목소리.

천진난만해 보이는 어린 의생에서 고금제일의 살수로 변모한 어린 청년이 커다란 바위에 등을 기댄다.

그는 어떠한 기파(氣波)도 흘리지 않았지만 나는 느낄 수 있었다. 그의 전신에 감춰진 무수한 칼날들을.

‘살성.’

이것이 문경의 숨겨진 이름이자, 진면목이다.

나는 과거의 그가 어떤 모습이었는지 모른다. 그러나 혁무진의 불알을 걸고 장담컨대, 사십여 년간 무림을 떠나 있었음에도 문경이 지닌 칼날은 조금도 무뎌지지 않았을 것이다.

아니, 오히려 더욱 날카롭고 예리해졌을 것이 분명했다.

‘아, 엄마 보고 싶다.’

사실 나도 안다. 문경이 정말 내게 해를 끼치지는 않으리라는 것을.

하지만 머리와 마음은 생각하는 것이 다른 법.

눈앞의 맹수가 당장 내 목에 이빨을 박아 넣지 않을 거라는 사실을 알아도, 가까이 가고 싶지는 않은 것이 사람 마음이다.

꿀꺽.

마른침을 삼킨 내가 조심스럽게 입을 열었다.

“갑자기 왜…….”

문경이 서늘한 눈동자로 나를 바라보았다.

“불러내서 싫다는 말투로군.”

“헉, 아닌데요.”

“매우 그래 보이는데.”

“그럴 리가요. 제가 감정 표현이 서툴러서 그렇지, 지금 사실 좋아 죽을 지경입니다.”

“죽어?”

“……그 두 글자는 조심스럽게 빼겠습니다. 제가 입이 방정이었네요. 관짝을 봐야 정신을 차리지.”

“관짝을 봐?”

“……살려 주십쇼.”

“살려 줘?”

아니 시발.

인터넷에서는 마지막 말을 되묻는 게 여자들이 설레는 대화법이라던데, 이건 저승사자가 설렐 만한 대화법이다.

업무 마치고 칼퇴근하던 염라대왕이 생사부(生死簿)를 들고 신나게 돌아오는 환영이 눈앞을 스치는 것 같았다.

‘아니, 진짜 뭔데. 대체 왜 불러낸 거냐고.’

정말 지난번에 반말했던 것 때문에 다시 부른 건가?

무슨 일인지 알면 마음이라도 편할 텐데, 저것 말고는 짐작도 가지 않으니 답답해서 미칠 지경이다.

그런 나를 못마땅하게 바라보던 문경이 문득 눈살을 찌푸렸다.

“뭐지?”

“예?”

“혹시 아직 듣지 못했나?”

“뭘요?”

“화왕 적천강. 네 스승 말이다.”

“……?”

“화왕 적천강.”

아니, 그래서 뭐 어쩌라고. 이해가 되지 않으니 무슨 말을 해야 할지도 모르겠다.

잠시 머뭇거리던 나는 혹시나 하는 마음에 조심스레 입을 열었다.

“강강수월래?”

“적천강이 아무 말…… 뭐?”

“아, 끝말잇기 아닙니까?”

“……이런 미친놈을 보았나.”

“아니면 혹시 글자 수 제한 있나요? 근데 화왕 적천강도 다섯 글자라 문제없을 텐데…….”

심상치 않은 공기.

분노와 회한이 가득 찬 눈빛으로 나를 바라보던 문경이 하늘을 우러러보며 탄식했다.

“내가 이런 빡대가리 새끼에게 독문 무공을 전수해야 한다니.”

“…….”

거 시발, 아무리 그래도 사람 면전에다 대고 빡대가리라니. 아무리 그래도 말이 너무 심한…….

‘어?’

내가 방금 뭘 들은 거야.

독문 무공?
```

## Final English reading copy

```markdown
# Chapter 488

The Water God Dragon was definitely a sacred creature.

In the broadest sense, it could be called a spirit beast. But it possessed power far beyond that of ordinary spirit beasts, which was probably why it had been able to absorb all the mana from the Gate.

*You could tell just by looking at the weather.*

As expected of an imugi that had lived for five hundred years, there was something different about it.

When the Water God Dragon had rampaged in its mutated state, thunder and waves had nearly overturned Dongting Lake. Now, however, the lake was calm, as though nothing had ever happened.

But unlike the peaceful-looking Dongting Lake, my heart was being swept by raging waves.

*...Is this what they mean by the calm before the storm?*

I glanced at Mungyeong’s back as he walked ahead of me.

He was a head shorter than me and had a slender frame. But in reality, he was a beast wearing the hide of a harmless herbivore.

*Why did he suddenly call me out? What could he possibly want to say?*

This was so unfair.

Could he still be angry because I had spoken casually to him during the battle?

He hadn’t called me out here just to have a little “physical conversation,” had he?

My unease continued to grow as Mungyeong kept leading me toward increasingly secluded places.

That was when—

“Stop.”

*Whoosh!*

There was only one voice, but seven figures surrounded us.

They were all Peak masters with considerable internal energy, and each had a sword hanging from his waist. The blades were engraved with pine patterns.

*Pine-Pattern Ancient Swords.*

As expected, a middle-aged Daoist dressed in Wudang robes emerged from beyond the deep darkness.

Judging by his age, the middle-aged Daoist was clearly their presiding chair. He opened his mouth toward us.

“This area is closed to visitors after the hour of the Dog. Please turn back—No, wait a moment. Could that be the Blazing Flame Divine Dragon?”

“What?”

The middle-aged Daoist spotted me over Mungyeong’s shoulder and asked with wide eyes,

“Young Hero Jin Taekyung? No, Great Hero Jin Taekyung?”

“I’m no Great Hero, but my name is Jin Taekyung.”

“Oh! My guess was correct after all. I knew your face looked familiar.”

*You may recognize me, but you’re a complete stranger to me.*

The middle-aged Daoist seemed delighted to see me, as though I were his son who had just been discharged from the army. Then he suddenly remembered something and asked,

“But what brings you here at this late hour? You must have already been assigned temporary lodgings.”

“...Uh. Well.”

*I was being dragged away by the Slaughter Saint.*

I swallowed the words rising to my throat and was about to make up some vague excuse when a flash of insight passed through my mind.

Thinking about it again, this was the final escape opportunity God had granted me.

“Is this where access is restricted?”

“That’s right. We’re taking turns standing watch in case of an emergency. But who is this young-looking man accompanying you?”

“Slaugh—”

“Hm?”

“—The breeze is blowing softly.”

“Oh, ha ha. I see.”

*Slaughter Saint! Mister! That bastard is the Slaughter Saint!*

I could finally understand how the barber who shouted that the emperor had donkey ears must have felt.

But when I met the deep, predatory gaze of the beast standing before me, I forced a smile and answered,

“We simply got to know each other somehow.”

“If you know each other, then precisely what kind of—”

“We met in Sichuan and have traveled together ever since. He isn’t a martial artist. He’s a medical apprentice.”

“Ah. I remember now. I heard there was a young medical apprentice with the skills of a renowned physician. So this is him.”

“Yes. This is that fellow.”

“But why did you come all the way here at such a late hour?”

“Uh, we have something important to discuss.”

“You must be quite close.”

I could let the other things pass, but I couldn’t accept that.

I answered with a straight face.

“No. We aren’t close.”

“Hm. In that case, I’m afraid there’s a problem. I apologize, Great Hero Jin, but regulations require a reliable guarantee before we can allow anyone through—”

“Ah, I see. Thank you for your hard work. Mungyeong, let’s go!”

—Instant execution.

“...”

—Back in position.

The Sound Transmission stabbed into me with icy force.

I had already turned halfway around, but I helplessly turned back.

—Say we’re close.

“I was joking. We’re actually very close.”

The middle-aged Daoist looked back and forth between Mungyeong and me before muttering,

“You don’t seem very close. You were walking apart without saying a word to each other...”

—Answer properly.

“We’re the kind of people who understand each other just by looking into one another’s eyes.”

“But you turned your head away. How could you see each other’s eyes...?”

“We used to understand each other just by looking into each other’s eyes. These days, I can tell what he’s thinking just by looking at the back of his head.”

“...”

—I’m asking this out of genuine curiosity. Does the Fire Gate Clan’s sect rule say to recruit only fucking idiots?

*For fuck’s sake. What am I supposed to do?*

As the middle-aged Daoist stared at me with lukewarm eyes, Mungyeong’s Sound Transmission continued.

—Come closer.

“...?”

—Put your arm around my shoulder.

“...!”

*What am I, some kind of avatar?*

But what could I do? In the Murim, the strong were the law—and the gods.

I trudged over, draped an arm over Mungyeong’s shoulder, and put on a dying expression.

“Whew. We’re really close.”

—Smile.

“Ha ha ha! We’re really close!”

—Make it louder.

“Wahahahahaha!”

—I can see you signaling with the corner of your eye. Do that one more time, and I’ll make you see the world with your heart instead of your eyes.

He had found a remarkably elegant way to say he would dig out my eyes.

I gave up my desperate attempts to look sideways and muttered,

“Anyway, we’re close.”

And throughout this entire situation, the Wudang martial artists—including the middle-aged Daoist—stared at us with expressions suggesting they were watching the greatest horror movie of the summer.

I had put on a dying expression, then laughed like a madman, all while constantly sneaking glances at Mungyeong. Anyone who failed to notice something strange would have to put down their Pine-Pattern Ancient Sword and leave Wudang.

The middle-aged Daoist soon moved his lips, his face suggesting he had made some kind of decision.

—Perhaps I’m worrying over nothing, but if something is happening to you without your realizing it, blink three times. If nothing is wrong, blink twice.

—I heard everything. Blink three times, and your body will be cut into three pieces.

*Mister! You bastard! This bastard is the Slaughter Saint! This bastard has a wiretap in his ear!*

But my shout never escaped, and I quietly blinked twice.

No matter how suspicious they became, there was no way they would guess that the young medical apprentice before them was a Supreme Peak master who had Returned to Youth.

And if I looked at things objectively, the Slaughter Saint was clearly an ally.

—Are you sure?

Even if he asked, my answer had already been decided.

Even among Supreme Peak masters, Jeok Cheongang and the Slaughter Saint were on a different level of enlightenment, making them biological wiretaps capable of eavesdropping on other people’s Sound Transmissions.

—Yes. Why would I lie about something like this? We’re simply friends who built a friendship while traveling together.

Though someone seemed to have built up murderous intent instead of friendship.

Still, something had been built.

The middle-aged Daoist let out a quiet snort of laughter after hearing my Sound Transmission.

—Indeed. How could anything happen to the Blazing Flame Divine Dragon of all people? Great Hero Jin, please forgive me for being so suspicious. I suppose the recent events have made me more sensitive than usual.

*No, you’re insensitive. Please get just a little more sensitive.*

But contrary to my hopes, the middle-aged Daoist spoke with a warm smile.

“In that case, very well. If it’s Great Hero Jin and no one else, I can trust you. You may pass!”

“W-Wait a moment.”

“Ha ha. I wondered why you had come all the way here, and it seems you truly have something important to discuss. I understand. Regulations prohibit it, but... I’ll give you some privacy for a little while.”

“What?”

“About half an hour. Will that be enough?”

*Of course it won’t, you idiot. Enough for what?*

But before I could answer, Mungyeong bowed politely with a clear smile.

“That will be sufficient.”

“...!”

Why did that brief answer sound like a death threat to me?

The middle-aged Daoist did not notice my trembling eyelids. He stroked his beard and smiled warmly.

“What a polite young man. You should examine me sometime as well.”

“Of course, Daoist.”

“Ha ha. Then I’ll return in half an hour.”

*Whoosh!*

The seven Peak masters—including the middle-aged Daoist—or rather, the seven witnesses, shot away.

I stared blankly at their backs as they rapidly disappeared into the distance. Then I slowly turned around, feeling layers of qi barriers enclose the area around us.

Sound and impact.

All of it was cut off from the outside by the qi curtain that now surrounded the space.

And within that space was a pair of eyes emitting a sharp, icy light even through the darkness.

“Master and Disciple are exactly alike in the one thing that makes people tired.”

“...!”

The voice alone made my chest turn cold.

The young man who had looked like an innocent medical apprentice had transformed into the greatest assassin in history. He leaned his back against a large rock.

He released no aura of qi, but I could still feel them—the countless blades concealed throughout his body.

*The Slaughter Saint.*

This was Mungyeong’s hidden name and his true nature.

I didn’t know what he had been like in the past. But I would stake Hyuk Mujin’s balls on this: even after spending more than forty years away from the Murim, the blades Mungyeong possessed had not grown dull in the slightest.

No. They had almost certainly grown sharper and more keen.

*Ah. I miss Mom.*

I knew the truth. Mungyeong truly would not harm me.

But the head and the heart thought differently.

Even if you knew the beast before you would not sink its teeth into your throat right away, human nature still made you reluctant to approach it.

*Gulp.*

After swallowing dryly, I carefully opened my mouth.

“Why did you suddenly...?”

Mungyeong stared at me with icy eyes.

“You sound like you disliked being called out.”

“Gasp. No, I don’t.”

“It really seems that way.”

“How could it? I’m just bad at expressing my emotions. In fact, I’m so happy I could die.”

“Die?”

“…I’ll carefully take that part back. I should’ve watched my mouth. I guess I won’t come to my senses until I see a coffin.”

“See a coffin?”

“...Please spare me.”

“Spare you?”

*Goddamn it.*

They said on the internet that repeating a woman’s last words was the kind of conversational technique that made her heart flutter.

This was the kind of conversation that would make the Grim Reaper’s heart flutter.

I could almost see Yama returning excitedly with the Book of Life and Death after clocking out of work right on time.

*What the hell is this, seriously? Why did he call me out?*

Had he really called me here again because I had spoken casually to him last time?

If I knew what this was about, I could at least feel at ease. But I couldn’t guess at anything beyond that, and the frustration was driving me crazy.

Mungyeong looked at me with displeasure, then suddenly furrowed his brow.

“What is this?”

“What?”

“Have you perhaps not heard yet?”

“Heard what?”

“The Fire King, Jeok Cheongang. Your Master.”

“...?”

“The Fire King, Jeok Cheongang.”

*So what am I supposed to do with that?* I didn’t understand what he meant, so I didn’t even know how to respond.

After hesitating for a moment, I carefully opened my mouth, just in case.

“Ganggangsullae?”[^1]

“Jeok Cheongang said something... What?”

“Oh, isn’t this a word-chain game?”

“...What kind of lunatic are you?”

“If there’s a character limit, is there one? But Fire King Jeok Cheongang is five characters in Korean too, so it should be fine...”

The atmosphere turned ominous.

Mungyeong stared at me with eyes filled with anger and regret, then looked up at the heavens and sighed.

“I can’t believe I have to pass down secret martial arts to a fucking blockhead like this.”

“...”

*For fuck’s sake. Even so, calling someone a blockhead right to his face was too much. That was going too far...*

*Huh?*

*What did I just hear?*

*Secret martial arts?*

[^1]: *Ganggangsullae* is a traditional Korean circle dance and folk song. Taekyung treats the last syllable of Jeok Cheongang’s name as the start of a word-chain answer.
```
