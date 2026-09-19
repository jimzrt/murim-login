<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0501.txt",
      "sha256": "dfeb13623041b0e125ea2eef0452d1dfd13914c8e5b35385fef98bc54da9c7f0",
      "bytes": 15782
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "43614dead7e309d2c742f8e41f4a2f74901c79ff7cff8157940d9b655c56859d",
      "bytes": 4932
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b9dbd3f49a511f089287fcf96245709f6461d7df7638822a23dd84b7489cfa48",
      "bytes": 159349
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f8c4dc2a0892acf6c178c2ffdeaa1f1cfc4c175dfe174ad77226d45347d7dab9",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d10088fa67a83a08df8a8290166c7aecbf02ff2241d6a42e288b66f4d8978148",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "24f1bff6fa29507113bedf92553a4492549d32d5bebe8e21652570ba4b977a2e",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "60294b79d4053d386dec0575e99e01bb8f048b6a786e78e293f7c508cf02bae9",
      "bytes": 1239
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "066c0be1ec9b35fa60f8da27a0906126a62ad9930cddab4ba9b9fc0bc02a5169",
      "bytes": 914
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "015cdfa8b02492a475dbf979a1182111b77f191793f33377a3be4e9a23f116e2",
      "bytes": 954
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "0db081ced3df299bf28e48b349d916e55c7f58594ba0e5399af104119c2b0b41",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "eebb6a55d417a0bf58918cb43c8dd3bd0a4d194812edee7631ef94a7e3eedbb2",
      "bytes": 153941
    }
  ],
  "estimated_tokens": 14041
}
-->

# Durable State Update — Chapter 501

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 501. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 501. Profile updates may replace only one
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
  "chapter": 501,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 501,
    "continuity_sources": [501],
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
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun, and weapons and armor orders have sharply increased across Murim.",
    "Taekyung believes Dark Heaven deliberately planned and executed the Gate-related incident and that similar incidents will continue.",
    "Jin Wikyung identifies Henan and the New Murim Alliance as the next matter under discussion.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jeok's innate qi is damaged and steadily diminishing despite treatment, and Taekyung remains uncertain whether he recovered without lasting aftereffects.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Taekyung completed Mungyeong's tests and retained the Water God Dragon's dismantled materials and Origin Essence after permanently losing 5 Strength and 5 Agility from Sinews and Meridians damage.",
    "The Mount Heng Sword Sect has completed its reconstruction and is growing under Lee Seowol, while Cheol Mubaek helps manage the sect's affairs.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment."
  ],
  "continuity_sources": [
    500,
    499
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "Has Jeok fully recovered from the Formless Ultimate Poison, and will Taekyung use the Water God Dragon's Origin Essence to aid him?"
  ],
  "safe_through": 500,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher’s Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, 진룡 as Jin Dragon, 마봉진 as Demon-Sealing Formation, 철기당 as Ironcraft Hall, 철기당주 as Master of Ironcraft Hall, 신룡 as Divine Dragon, and 신(新) 무림맹 as New Murim Alliance."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 진룡대    | **Jin Dragon Squad**             |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 삼류     | **Third Rate**    |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 평화 | **Peace Guild** | Guild name. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 하남성 | **Henan Province** | Province containing Luoyang. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 교주 | **Cult Leader** | Leader of the Divine Cult. |
| 홍천 | **Hongcheon** | Given name of the newly appointed Hubei Provincial Administration Commissioner. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 진룡 | **Jin Dragon** | The two characters embroidered on the Jin Dragon Squad's uniforms. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 위팽 | 혁무진 | mentor_to_junior_martial_artist | Hyuk Mujin | blunt and testing | Wipeng addresses Mujin by name when beginning to assess and train him. |
| 혁무진 | 위팽 | junior_martial_artist_to_mentor | Great Hero Wipeng | formal-deferential | Mujin uses 위팽 대협 when reacting to Wipeng's recognition and instruction. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 관리 | 진위경 | government official to influential martial artist | you | formal, then deferential | The official asks Jin Wikyung's identity before bowing and apologizing after learning of his connection to Yi Hongcheon. |
| 진위경 | 관리 | influential martial artist to government official | you | formal, controlled, and quietly authoritative | Jin Wikyung identifies the official's rank, demands that he withdraw his troops, and directs him to apologize. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 제갈풍 | 진위경 | Zhuge Clan Family Head to Jin Family Lesser Family Head | Lesser Family Head | formal and conciliatory | Uses 소가주 while trying to secure Jin Wikyung's support during the settlement. |
| 진위경 | 제갈풍 | Jin Family Lesser Family Head to Zhuge Clan Family Head | Sir Zhuge | formal with deliberate comic deference | Uses 제갈 대협 while theatrically scolding Taekyung to force Zhuge Feng to concede. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 499
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 498
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 499
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 500
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 459
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor's only younger full brother, and his token commands immediate deference from distant imperial relatives such as Ju Wongong; he admires Jin Taekyung and seeks to emulate him.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 500
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 500
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃501화



“언젭니까?”

제갈풍과 헤어진 후 돌아가는 길, 내가 불현듯 던진 물음에 진위경이 나직하게 대답했다.

“달포 후. 하남성 숭산(嵩山).”

“숭산…….”

무림의 태산북두인 소림사가 위치한 바로 그곳이다.

불과 석 달 전. 천하 무림의 대연회라 할 수 있는 성라대연(星羅大宴)이 시작되고 암천에 의해 피바람이 불어닥친 그 자리에, 신(新) 무림맹이 탄생하는 것이다.

숭산이라는 장소. 그리고 소림사가 지닌 상징성을 생각해 본다면, 장장 오십여 년 만에 부활하는 무림맹의 출발선으로는 적격인 셈이다.

그나저나 겨우 달포밖에 남지 않았다는 건…….

“이미 정해져 있었군요. 사천에 오셨을 때부터.”

그러나 내 예상과는 반대로, 진위경은 작게 고개를 내저어 보였다.

“아닙니까?”

“위팽이 왜 때마침 하남에 있었다고 생각하느냐?”

“그럼 위 대협이 온 이유가…….”

“진룡대는 본가 제일의 정예다. 그중 절반이나 되는 인원을 고작 짐꾼으로 쓰기 위해 불러오는 것은 소가주로서 허락하지 않는다. 설령 옮기고자 하는 것이 천자의 옥새(玉璽)라 해도.”

“예상보다 앞당겨진 거군요.”

“암천의 행보가 생각했던 것 이상으로 거칠고 빨랐다. 사천혈사가 결정적이었지.”

앞서가는 적을 따라잡기 위해서는 뛰어야 한다.

소림사에 휘몰아친 피바람은 사천으로 나아갔고, 이제는 호북에까지 이르렀다. 하남의 수뇌부는 선택해야 했다.

“천하 무림을 한 울타리에 묶는 것은 결코 쉬운 일이 아니다. 하지만 그분들께서도 마침내 결심을 내린 듯싶구나.”

조용한 목소리로 뇌까린 진위경이 품에서 봉첩(封牒)을 꺼내 내밀었다.

“이건.”

“위팽이 하남에서 가져온 서신이다.”

“하남이라면, 역시 무림맹에서 보낸 겁니까?”

“짐작하고 있었구나.”

“그럴 것 같더라고요. 아까 제갈 대협한테 주는 거 보고 알았어요.”

척 봐도 보통의 서신과는 외관부터가 다르다.

하지만 이 서신을 더욱 특별하게 만드는 것은, 겉면에 용사비등한 필체로 적힌 무림맹(武林盟)이라는 세 글자였다.

“막내 너도 직접 읽어 보거라.”

“이미 읽고 있으니까 말 시키지 마세요. 집중 안 돼요.”

“……아앗, 으응.”

나는 시무룩해하는 진위경을 뒤로하고 펼친 서신을 빠르게 훑어내렸다.

천하 무림에 고하노라, 라는 문장으로 시작된 서신의 내용은 짧고 강렬했다. 그래서인지 세 줄 요약도 쉬웠다.



1. 야야, 암천 썰 푼다. 이거 진짜 미친놈들이니까 잘 들어 봐.

2. 정마대전 PTSD 알지? 이거 무슨 수를 써서라도 막자.

3. 숭산 어딘지 모르는 호구 없재? 몇 월 며칠까지 모여라. 안 오는 새끼 암천.



“…….”

세 줄 요약해 놓고 보니까 되게 없어 보이네.

당연하지만, 서신에 이렇게 쓰여 있지는 않았다.

누군지 모르는 서예가가 거침없이 써 내려간 필체는 구름 같았고, 문장 하나하나와 그에 담긴 감정은 장엄하며 심금을 울렸다.

개인적으로 암천의 천주라는 놈에게 보여 주고 싶을 정도다.

‘이거 보면 천주도 무림맹 가입하겠다.’

천주가 무림맹에 가입하면 모두가 행복한 해피 엔딩을 맞이할 수 있을 텐데, 그럴 가능성이 혁무진 귓밥만큼도 존재하지 않는다는 게 안타까울 뿐이다.

“어쨌건, 이제 곧 무림맹이 탄생하겠군요.”

“달포 뒤. 천하 무림이 무림맹의 깃발 아래 모일 것이다.”

잠시 생각하던 진위경이 한마디를 덧붙였다.

“천하 무림이 아니라, 중원의 정파 무림이라고 해야겠군.”

진위경이 덧붙인 저 말의 의미를, 나는 이미 알고 있다.

‘확실히…… 정파가 천하 무림 그 자체라고 하기에는 무리가 있지.’

작금 천하 무림의 패자는 두말할 것 없이 구파일방과 오대세가를 위시한 정파다.

그러나 과거 정마대전에서 살아남아 승자가 된 것은 정파뿐만이 아니었다.

“사파(邪派).”

내 입술 사이로 흘러나온 중얼거림에 진위경이 고개를 끄덕였다.

“그래, 그들을 배제해서는 안 된다.”

천하라는 어항에는 한 색깔의 물고기만 살아가는 것이 아니다.

정파에 비하면 미력하나 자신들만의 영역을 구축한 사파가 있고, 밤거리를 지배하는 흑도가 포함되어 있다.

‘처음에는 그렇게 사마외도 척결을 부르짖으면서 왜 저런 놈들을 남겨 뒀나 했는데.’

모든 일에는 이유가 있는 법.

지금까지 명맥을 이어 가고 있는 사파 세력은 정마대전 당시 정파의 편에 섰기 때문에 살아남을 수 있었다.

문제는 그들의 선택이 단순한 선의가 아니었다는 점이다.

“현존하는 중원의 사파 세력이 왜 정파 무림의 편에 섰는지, 혹 알고 있느냐?”

“제가 지난 일 년 사이 누구와 함께 있었는지 잊으신 건 아니죠?”

“적 대협께서 말씀해 주셨구나.”

“이것저것 많이 주워들었죠.”

옛말에 초록은 동색이고, 가재는 게 편이라고 했다.

정마대전 당시 마교가 청해를 넘어 중원을 향해 들이닥치자, 사파는 교주님 만세를 부르짖으며 재빨리 합류했다.

그만큼 마교의 기세가 엄청난 것도 있었지만 나름대로 동류라 할 수 있는 마교가 천하 무림의 주인이 되길 원했던 것이다.

그러나 천하의 중심부라 할 수 있는 중원(中元)에 자리 잡고 있던 사파 무림인들은 사정이 달랐다.



‘정파에 안 붙으면 당장 중원을 빠져나가기도 전에 척살 당할 텐데, 제깟 놈들이 이쪽에 안 붙고 배겨?’



언젠가 적천강이 코웃음 치며 했던 그 말은 당시 중원의 사파인들에게 정확히 해당되는 현실이었다.

“거의 울며 만두 먹기 식이었다고 하던데요.”

“나 역시 그 시대에 살았던 건 아니지만, 확인해 본 바에 의하면 사실이다.”

“확인?”

“네가 사천에 떠난 뒤 하남에 남아 옛 자료를 찾아보는 과정에서 수많은 기록을 발견할 수 있었다. 사파에 관련된 기록도 그중 하나였고.”

평화가 찾아오자 무림맹은 해산되었지만, 정마대전을 겪은 사람들의 기억과 당시의 상황을 고스란히 담은 기록은 남아 있었다.

생각해 보면 당연한 일이다. 장구한 무림의 역사에서 오십여 년이라는 시간은 ‘고작’ 반세기에 불과하니까.

“기록에 뭐라고 적혀 있었는데요?”

“어떨 것 같으냐?”

“어느 정도 예상이 되긴 하네요. 들은 이야기들이 있어서.”

“적 대협께서 네게 정확히 어떤 이야기를 해 주셨는지는 모르나, 아마 대부분 사실일 것이다.”

“……그게 사실이면 좀 골 때리는데.”

정마대전의 시작과 동시에 중후반에 접어들기까지, 정파에 합류한 사파 무림인들은 끊임없는 배신을 반복했다.

당시 무림맹 수뇌부가 정파 내부의 사파를 모조리 뽑아내는 삭초제근(削草除根)까지 논의했다는 적천강의 말을 생각하면 심각한 수준이었던 건 확실해 보인다.

“그래도 나중에는 열심히 싸웠다면서요?”

“처음과 달리 승패를 알 수 없게 되었으니까. 천면호리 송 대협이 이끄는 은영각(隱影閣)의 철통같은 감시도 있었고, 수뇌부의 분위기가 심상치 않음을 감지한 사파 무림 내부에서 자체적으로 꼬리를 잘라 냈다는 기록이 있다.”

정파라고 무조건 정의로운 것은 아니고, 사파라고 아주 악질들만 모여 있는 것도 아니다.

하지만 정파와 달리 사파는 스스럼없이 꼬리를 잘라 낼 수 있는 행동력과 잔혹함이 있었다.

마교의 간자라고 의심이 가는 순간 가차 없이 멱부터 따고 본 것이다.

“결국 꼬리를 잘라 낸 몸통은 살아남았고, 정파에 협조하여 승자가 되었지.”

사파의 잔존 세력은 그렇게 정파라는 거목의 그늘서 명맥을 이어 갈 수 있었지만, 당연하게도 전과 같은 위세를 과시할 수는 없었다.

가뜩이나 이미지가 지저분한데 마교에 붙어먹은 전력이 셀 수 없이 많았기 때문이었다.

그나마 무림맹 수뇌부 측에서 어느 정도 공로와 권리를 인정해 줬기에 망정이지, 아니었다면 사마외도를 부르짖는 골수 의협들에게 끌려나가 오체분시 당했을 것이라는 게 중론이었다.

종전 후에 사파를 향했던 혐오의 시선은 유구한 전통처럼 아직도 계속되고 있었다.

여기까지는 그다지 크게 문제 될 게 없었지만, 지금부터는 얘기가 다르다.

“걔들도 함께 데리고 싸워야 하잖아요.”

“그래. 무림맹이 아니라면 암천의 편에 설 테니까.”

“품에 안자니 찝찝한데요.”

“전장에서 등을 맡기기에는 싫은 상대지. 전례도 있거니와 종전 후 논공행상에 대한 불만이 수십 년간 쌓여 있을 테니까.”

“차라리 중립을 지키라고 한다면…….”

“만약 무림맹이 패색이 짙다고 치자. 막내 네가 사파의 무림인이라면 어쩌겠느냐?”

“……음.”

저렇게 대놓고 물어보니까 뭐라 할 말이 없네. 입맛을 다신 내가 입을 열었다.

“여기서 이런 말 하긴 뭐한데, 암천에 붙어야죠.”

“이유는?”

“무림맹이 이기면 본전이지만, 말하신 대로면 이미 승부의 저울은 기울었고 암천이 중원 무림의 주인이 될 상황이잖아요.”

“그렇지.”

“암천이 어떤 놈들인데 사파를 가만히 두겠습니까. 중립 지켰다고 칭찬하는 것보다 중요할 때 안 도왔으니 괘씸하다며 싸그리 죽여 버릴 놈들이죠.”

“정확히 맞췄다. 그래서 사파가 계륵(鷄肋)인 것이다.”

계륵. 상당히 적절한 표현이다.

별로 득이 되진 않지만, 버리기에는 아깝다. 함께 싸우자니 찝찝하고 버리면 암천이 고스란히 주워 이쪽을 향해 던질 것이다.

닭 뼈가 아무리 말랑해도 결국 뼈. 맞게 되면 제법 아프겠지.

그렇다면 결국…….

“하남에서도 이미 그쪽으로 서신을 보냈겠군요.”

진위경이 작게 고개를 끄덕였다.

“틀림없다. 굳이 둘 중 하나를 택해야 한다면, 사파 무림은 반드시 우리 쪽으로 끌어들여야 해.”

사파는 계륵치고는 살점이 많이 붙어 있는 편이다.

당장 해 떨어지면 뒷골목에 어슬렁거리는 흑도 칼잡이들도 사파에 속하는데, 지금은 삼류 칼잡이 하나가 아쉬울 때 아닌가.

무엇보다 가까이 두고 목줄을 잡아채는 게 낫지, 아예 암천에 붙는 건 너무 큰 손해…….

‘그런데 잠깐. 흑도?’

나는 문득 떠오른 기억에 눈살을 찌푸렸다.

“왜 그러느냐?”

“아니, 얼마 전에 들은 게 기억나서요. 이번 수신룡에 관한 일로 호북성의 흑도를 흉수로 몰아서 싹 날려 보내지 않았습니까?”

“그랬지.”

“……그럼 사파 애들이 기분 나빠할 것 같은데요. 결국 우리가 관부의 제안을 받아들여서 자기네 식구 족친 거잖아요.”

그림이 좋지 않다. 어쩌면 이번 일로 사파가 무림맹에서 보낸 입맹(入盟) 제안을 거부할 수도 있을 만큼.

그러나 진위경의 안색은 평온하기 그지없었다.

“두 가지가 틀렸다.”

“예?”

“첫째. 종전 이후 사파 무림은 사분오열된 상태다. 식구가 아니라, 오히려 경쟁자라고 봐야 옳겠지. 우리는 이번 일을 기회 삼아 유난히도 숫자가 많던 호북의 흑도를 뿌리 뽑았고, 빈자리는 또 다른 사파가 채울 것이다. 새로운 기회지.”

“……!”

“충분한 먹이를 주었으니 그들은 만족할 게다. 또한 호북의 일을 전해 들으며 깨닫겠지. 이건 경고라는 것을.”

먹이를 던져 주고, 두려움이라는 이름의 목줄을 채웠다.

그것이 무림맹이 사파 무림이라는 사냥개를 길들이는 방식이다.

“그리고 둘째. 관부가 제안하고, 우리가 받아들인 것이 아니다.”

진위경이 메마른 목소리로 말을 이었다.

“우리가. 아니, 내가 먼저 제안했다.”

“아.”

“관부는 받아들였을 뿐이다. 이 차이는 아주 크지.”

“……관부가 그렇게 쉽게 말입니까?”

“호북성의 승선포정사사(承宣布政使司)는 한 성을 좌우할 수 있는 요직이다. 하지만 사람들은 새로운 포정사사가 산서성 육조참정을 지냈다는 사실만 알 뿐, 상산왕의 숨겨진 충복이라는 것까진 알지 못하더구나.”

문득 처음 호북성에 도착했을 때의 기억이 뇌리를 스쳤다.

사람들의 적의 어린 시선. 그리고 관병을 이끌고 나루터를 포위한 관리를 향해 묻던 진위경의 모습.



‘아, 그건 그렇고 이 가에 홍천이라는 함자를 쓰시는 분을 알고 계시오?’

‘그, 그분은 얼마 전에 새로 부임하신 포정사사신데. 혹시 포정사사님과 어떤 관계이신……?’

‘몇 번 만나 뵙고 술 한두 잔 했지. 필요할 때 도움도 드렸고.’



나를 똑바로 응시하는 진위경의 눈빛은 부드러웠지만, 그 안에는 서늘한 칼날이 도사리고 있었다.

그건 책사이자 정객(政客)의 눈빛이었고, 알아채기 무섭게 스르륵 녹아 사라졌다.

“걱정 말거라. 모든 것이 잘될 테니.”

툭툭.

어깨를 두드리는 손에서 힘이 느껴진다. 그런 진위경을 물끄러미 바라보던 나는 불쑥 입을 열었다.

“가주…… 아니, 아버지는 어떤 사람이었습니까?”

진위경의 입가에 맺혀 있던 희미한 미소가 씻은 듯이 사라졌다.

“아니, 분위기 좋았는데 그 인간 이야기는 왜?”

“아시다시피 제가 그때 머리를 다치는 바람에. 기억이 잘 안 나길래.”

“기억할 필요 없다! 그냥 머릿속에서 지워! 내가 네 애비다!”

“…….”

익히 알고 있긴 했지만, 지금까지 쌓인 게 한두 가지가 아닌 모양이다.

진위경은 지난날의 서류 지옥을 떠올렸는지 주먹까지 부르르 떨었다.

“그런데 그건 왜 묻느냐?”

“그냥. 아버지가 사라지고 형님이 가문을 맡은 게 참 다행이라는 생각이 들어서요.”

“……막내야. 부디 선 넘지 말거라.”

나는 어깨를 으쓱해 보이고 돌아섰다.

형이 말하는데 어딜 가냐고, 애정이 식었냐고 묻는 진위경의 물음에 고개도 돌리지 않고 대답했다.

“달포 뒤라면서요. 떠날 준비 하러 갑니다.”

이제는 호북에서의 일을 뒤로하고 떠나야 할 때였다.

나와 함께하는, 그리고 앞으로도 함께하고 싶은 이들과 함께.

“이 정도면 시간은 충분히 드린 것 같은데…… 안 그렇습니까.”

입술 사이로 흘러나온 중얼거림은 주위의 소음에 파묻혀 흔적도 없이 사라진다.

나는 까마득한 높이의 절벽을 바라보며 턱을 긁적였다.
```

## Final English reading copy

```markdown
# Chapter 501

“When is it?”

On the way back after parting with Zhuge Feng, I suddenly tossed out the question. Jin Wikyung answered in a quiet voice.

“In a month. Mount Song, Henan Province.”

“Mount Song…”

The very place where Shaolin Temple—the Mount Tai and Northern Dipper of the Murim—was located.

Only three months ago, the Star-Array Grand Banquet, the greatest gathering of the Murim under Heaven, had begun there. Dark Heaven had unleashed a storm of blood, and now the New Murim Alliance would be born in that same place.

Considering the location of Mount Song and Shaolin Temple’s symbolism, it was the perfect starting line for the Murim Alliance’s resurrection after more than fifty years.

But the fact that only a month remained meant…

“It had already been decided when you came to Sichuan, hadn’t it?”

Contrary to my expectations, Jin Wikyung slowly shook his head.

“It hadn’t?”

“Why do you think Wipeng happened to be in Henan at exactly the right time?”

“Then the reason Great Hero Wipeng came was…”

“The Jin Dragon Squad is our family’s finest elite force. As the Lesser Family Head, I would never allow half of its members to be summoned merely to serve as porters. Even if what they were transporting had been the Son of Heaven’s jade seal.”

“So it was moved forward.”

“Dark Heaven’s movements were harsher and faster than we had expected. The Sichuan Blood Tragedy was decisive.”

To catch an enemy who was ahead, you had to run.

The storm of blood that had swept through Shaolin Temple had spread to Sichuan and now reached Hubei. The leaders of Henan had to make a choice.

“Binding the Murim under Heaven beneath one fence is never easy. But it seems those people have finally made up their minds.”

Muttering quietly, Jin Wikyung pulled a sealed dispatch from inside his robes and held it out to me.

“What’s this?”

“A letter Wipeng brought from Henan.”

“If it came from Henan, is it from the Murim Alliance?”

“You had already guessed.”

“I figured it out when I saw you give one to Sir Zhuge earlier.”

The letter was clearly different from an ordinary one, even in appearance.

But what made it truly special were the three characters written across its surface in a bold, soaring hand:

**Murim Alliance.**

“Read it yourself, youngest.”

“I’m already reading it, so stop talking to me. I can’t concentrate.”

“…Oh. Right.”

Ignoring Jin Wikyung’s downcast expression, I unfolded the letter and quickly skimmed through it.

The letter began with the words, *To the Murim under Heaven,* and its contents were short and powerful. That made it easy to boil down to three lines.



1. Hey, let me tell you about Dark Heaven. These guys are seriously fucking crazy, so listen up.

2. You know the Great Faction War PTSD? Let’s stop this by any means necessary.

3. Any dumbasses who don’t know where Mount Song is? Gather by the specified date. Anyone who doesn’t show is Dark Heaven.

“…”

When I put it into three lines, it sounded pretty pathetic.

Of course, the letter had not actually been written that way.

The calligraphy, written boldly by some unknown master, flowed like clouds. Every sentence and the emotions contained within were solemn and deeply moving.

Personally, I almost wanted to show it to that bastard, the Lord of Heaven.

*If he saw this, even the Lord of Heaven might join the Murim Alliance.*

Everyone could have enjoyed a happy ending if the Lord of Heaven joined the Murim Alliance. It was simply unfortunate that the possibility of that happening was less than the amount of earwax in Hyuk Mujin’s ear.

“In any case, the Murim Alliance will be born soon.”

“In a month, the Murim under Heaven will gather beneath the Murim Alliance’s banner.”

After a moment’s thought, Jin Wikyung added one more thing.

“Not the Murim under Heaven. We should say the orthodox Murim of the Central Plains.”

I already understood what Jin Wikyung meant.

*He’s right. Calling the orthodox faction the Murim under Heaven would be a bit much.*

The dominant force in the Murim under Heaven was unquestionably the orthodox faction, led by the Nine Sects and One Gang and the Five Great Families.

But the orthodox faction had not been the only side to survive and emerge victorious from the Great Faction War.

“The unorthodox faction.”

At my muttered words, Jin Wikyung nodded.

“That’s right. We cannot exclude them.”

The fishbowl called the world did not contain only one color of fish.

Compared to the orthodox faction, the unorthodox faction was weak, but it had built domains of its own. The dark-path figures who ruled the streets at night were part of it as well.

*At first, I wondered why they had left those people alive while shouting about eliminating every demonic and heterodox element.*

Everything happened for a reason.

The unorthodox forces still around today owed their survival to siding with the orthodox faction during the Great Faction War.

The problem was that their choice had not been made out of simple goodwill.

“Do you know why the unorthodox forces currently active in the Central Plains sided with the orthodox Murim?”

“You haven’t forgotten who I’ve spent the past year with, have you?”

“Great Hero Jeok told you.”

“I picked up quite a lot here and there.”

There was an old saying: green goes with green, and crayfish take the crab’s side.

When the Demonic Cult crossed Qinghai and surged toward the Central Plains during the Great Faction War, the unorthodox faction quickly joined them while shouting, “Long live the Cult Leader!”

The Demonic Cult’s momentum had certainly been overwhelming, but the unorthodox faction had also wanted people like themselves—the Demonic Cult—to become the masters of the Murim under Heaven.

However, the unorthodox martial artists living in the Central Plains, the heart of the world, had faced a different situation.



*If they don’t side with the orthodox faction, they’ll be hunted down before they can even leave the Central Plains. Those bastards wouldn’t dare refuse to join this side.*



The words Jeok Cheongang had once spoken with a snort had been an exact description of reality for the unorthodox martial artists of the Central Plains at the time.

“I heard they were basically eating dumplings through their tears.”

“I did not live through that era either, but according to what I have confirmed, that is true.”

“Confirmed?”

“After you left for Sichuan, I remained in Henan and searched through old records. I found countless accounts. The records concerning the unorthodox faction were among them.”

When peace arrived, the Murim Alliance was disbanded, but records preserving the memories of those who had experienced the Great Faction War and the circumstances of that time remained.

It made sense when I thought about it. In the long history of the Murim, fifty years was only half a century.

“What did the records say?”

“What do you think they said?”

“I can make a rough guess. I’ve heard some stories.”

“I do not know exactly what Great Hero Jeok told you, but most of it was probably true.”

“…If that’s true, it’s pretty damn ridiculous.”

From the beginning of the Great Faction War until it had entered its middle and latter stages, the unorthodox martial artists who had joined the orthodox faction betrayed them again and again.

Considering what Jeok Cheongang had said about the Murim Alliance’s leadership even discussing root-and-branch eradication to remove every unorthodox member from within the orthodox faction, the situation must have been serious.

“But I heard they fought hard later on.”

“Because the outcome was no longer certain, unlike at the beginning. There was also the ironclad surveillance of the Hidden Shadow Pavilion, led by Sir Song, the Thousand-Faced Fox. According to the records, once the unorthodox martial artists sensed that the atmosphere among the leadership had become ominous, they cut off their own tails.”

The orthodox faction was not automatically righteous, and the unorthodox faction was not composed solely of the worst kind of villains.

But unlike the orthodox faction, the unorthodox faction possessed the decisiveness and cruelty to cut off its own tail without hesitation.

The instant someone was suspected of being a spy for the Demonic Cult, they slit his throat first and asked questions later.

“In the end, the body whose tail had been cut off survived and became one of the victors by cooperating with the orthodox faction.”

The surviving unorthodox forces were able to maintain their lineage beneath the shade of the great tree known as the orthodox faction. Naturally, however, they could no longer display the same influence as before.

Their reputation had already been filthy, and they had sided with the Demonic Cult countless times.

They were fortunate that the Murim Alliance’s leadership had recognized a certain amount of their contributions and rights. Otherwise, the general consensus was that they would have been dragged out and dismembered by the hardline heroes who screamed for the elimination of every demonic and heterodox element.

The hatred directed toward the unorthodox faction after the war had continued like some ancient tradition.

None of that had been a particularly serious problem.

But from this point onward, things were different.

“We have to take them with us and fight alongside them.”

“Yes. If not with the Murim Alliance, they will side with Dark Heaven.”

“It leaves a bad taste in my mouth to bring them into the fold.”

“They are not people I would want watching my back on a battlefield. There is precedent, and decades of resentment over the postwar allocation of honors and rewards must have accumulated.”

“Then what if we tell them to remain neutral?”

“Let us say the Murim Alliance appears certain to lose. If you were an unorthodox martial artist, youngest, what would you do?”

“…Hmm.”

When he put it that bluntly, I had nothing to say. I smacked my lips, then answered.

“I hate to say it, but I’d side with Dark Heaven.”

“Why?”

“If the Murim Alliance wins, they break even. But as you said, the scales are already tilted, and Dark Heaven is on the verge of becoming the master of the Central Plains Murim.”

“Correct.”

“What kind of people are Dark Heaven? Do you think they’d leave the unorthodox faction alone? Rather than praising them for remaining neutral, they’d be furious that they hadn’t helped when it mattered and kill every last one of them.”

“You are exactly right. That is why the unorthodox faction is a chicken rib.”

A chicken rib. It was a remarkably fitting expression.

It offered little benefit, but it was too wasteful to throw away. Fighting alongside them felt unpleasant, but if we discarded them, Dark Heaven would pick them up and throw them back at us.

No matter how soft a chicken bone was, it was still a bone. Getting hit by one would hurt quite a bit.

If that was the case…

“Henan has already sent them a letter, hasn’t it?”

Jin Wikyung nodded slightly.

“Without a doubt. If we must choose between the two, we need to draw the unorthodox Murim to our side.”

The unorthodox faction had a surprising amount of meat on it for a chicken rib.

Even the dark-path knife-men who wandered the back alleys after sunset belonged to the unorthodox faction. Weren’t we at a point where we would be grateful for a single Third Rate knife-man?

More importantly, it was better to keep them close and hold their leash than let them side with Dark Heaven. That would be far too great a loss…

*Wait a second. The dark path?*

A memory suddenly surfaced, and I frowned.

“What is it?”

“No, I just remembered something I heard recently. Regarding the Water God Dragon incident, didn’t we accuse the dark-path figures of Hubei Province of being the culprits and wipe them all out?”

“We did.”

“…Then the unorthodox faction might be upset. In the end, we accepted the government’s proposal and wiped out their own people.”

It did not look good. This incident might even be enough for the unorthodox faction to reject the Murim Alliance’s offer of membership.

Jin Wikyung, however, looked perfectly calm.

“Two things are wrong with that.”

“What?”

“First. Since the end of the war, the unorthodox Murim has been fractured into countless pieces. They should be considered rivals, not family. We took this opportunity to uproot the dark-path figures in Hubei, whose numbers had become unusually large. Another unorthodox faction will fill the vacant space. It is a new opportunity.”

“…!”

“We gave them enough food, so they will be satisfied. They will also hear what happened in Hubei and realize that it was a warning.”

We had thrown them food, then fastened a leash named fear around their necks.

That was how the Murim Alliance tamed the hunting dog known as the unorthodox Murim.

“And second. The government did not make the proposal and receive our acceptance.”

Jin Wikyung continued in a dry voice.

“We did. No—I made the proposal first.”

“Oh.”

“The government merely accepted it. That distinction is very important.”

“…Would the government really agree that easily?”

“The Provincial Administration Commissioner of Hubei is an important post capable of controlling an entire province. But people know only that the new commissioner previously served as an Assistant Provincial Administrator in Shanxi Province. They do not know that he is Prince Shangshan’s hidden loyal retainer.”

A memory of when we had first arrived in Hubei suddenly flashed through my mind.

The hostile gazes of the people.

And Jin Wikyung questioning the official who had surrounded the ferry landing with government soldiers.



*“By the way, do you happen to know a man surnamed Yi whose given name is Hongcheon?”*

*“H-he was recently appointed as the Provincial Administration Commissioner. May I ask what your relationship with the commissioner is…?”*

*“I have met him a few times and shared a drink or two. I helped him when he needed it.”*



Jin Wikyung’s eyes, fixed directly on me, were gentle. But a cold blade lurked within them.

They were the eyes of a strategist and a politician. Before I could fully register them, they melted away and vanished.

“Do not worry. Everything will work out.”

Tap, tap.

I could feel the strength in the hand patting my shoulder. I gazed silently at Jin Wikyung, then suddenly spoke.

“Family Head… No, what kind of person was Father?”

The faint smile around Jin Wikyung’s mouth vanished as though it had been wiped away.

“No, the mood was so nice. Why bring up that bastard?”

“As you know, I injured my head back then. I don’t remember him very well.”

“You don’t need to remember him! Just erase him from your mind! I’m your father!”

“…”

I already knew he had accumulated quite a bit of resentment, but apparently there was more than one or two things piled up.

Jin Wikyung even trembled his fist, apparently remembering the paperwork hell of those days.

“But why did you ask?”

“Just because. I was thinking how fortunate it was that, after Father disappeared, hyung took charge of the family.”

“…Youngest. Please do not cross the line.”

I shrugged and turned away.

Jin Wikyung asked where I thought I was going when hyung was talking to me, and whether my affection for him had cooled. Without turning around, I answered,

“You said it’s in a month. I’m going to prepare to leave.”

The time had come to leave Hubei behind.

Together with those who were by my side—and whom I wanted by my side in the future.

“I think I’ve given it enough time by now… don’t you?”

The mutter that slipped between my lips vanished without a trace beneath the noise around us.

I scratched my chin as I looked up at the cliff rising into the distant sky.
```
