<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0507.txt",
      "sha256": "ccb0507f0a49ba868a0e679fa6d0f65a6a545bc1b734d59bc3d13dcab59292b0",
      "bytes": 13767
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "64f7e28292bcad319362acb85a5628b849b8fa0f696aa125bcef0d10b2d41d3b",
      "bytes": 5488
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e1741e8d8552f45dee01dca5807c5b163f5d9ad345d4d844914aedbcc955610f",
      "bytes": 161011
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6f71e458f07e8cc671b70af6c3c18567c11c81daa38737322cae3909e407818d",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "fa35a9981a9f1a5101656278fb7341798ea532a7d47ab3d12e1f3af40bc3c91a",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1c2def9aaa680a6b54218e0a32078c06b484ef78a98739ce4dc801b1372d9986",
      "bytes": 1630
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "47f26b8f8428b7926b26b85f2a79aeb425c31c0eebac4bbdd01ff7b5d181410d",
      "bytes": 931
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "b7c8e464b6b831f0c8443530f90cab24fbcc06bce4a3fb083f4f88079991ddae",
      "bytes": 842
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55e1b559aab842913d6859ee4f86aff71a3a23ad89553d949f27b82a0965ae8",
      "bytes": 154523
    }
  ],
  "estimated_tokens": 12393
}
-->

# Durable State Update — Chapter 507

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 507. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 507. Profile updates may replace only one
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
  "chapter": 507,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 507,
    "continuity_sources": [507],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master whose assassin instincts remain formidable despite decades spent living as a medical apprentice.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun and the New Murim Alliance is being formed at Mount Song; Taekyung believes Dark Heaven planned the Gate incident, while Jin Wikyung's Hubei arrangement was designed to create an opening among rival unorthodox factions.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Jin Taekyung's party is traveling by ship along the Yangtze toward Xixia in southwestern Henan and will continue overland after leaving the river.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters.",
    "The Yangtze River Channel League and Green Forest Alliance may become rear threats if they oppose the Murim Alliance or side with Dark Heaven.",
    "The Wudang pursuit party has brought back remains attributed to the Killing Ghost, but their nature is neither beast nor human."
  ],
  "continuity_sources": [
    506,
    505
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Which four did Mungyeong mean when he corrected the count of two, and how will the Yangtze River Channel League and Green Forest Alliance choose?",
    "What is the true nature and identity of the remains attributed to the Killing Ghost?"
  ],
  "safe_through": 506,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher's Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 흑풍단 as Black Wind Corps, 혈어 as Blood Fish, 변이된 송사리 as Mutated Minnow, 왜국 as Wa Kingdom, 인자 as ninja, and 절강 as Zhejiang; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, 천기 as heavenly patterns, and 후천지기 as acquired qi.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, 진룡 as Jin Dragon, 마봉진 as Demon-Sealing Formation, 철기당 as Ironcraft Hall, 철기당주 as Master of Ironcraft Hall, 신룡 as Divine Dragon, 신(新) 무림맹 as New Murim Alliance, 면벽수련 as secluded meditation, 호법 as stand guard, 한나절 as half a day, 일다경 as the time it takes to drink a cup of tea, 촌각 as moments, 진맥 as take one's pulse, 은영술 as concealment techniques, 표창 as throwing blades, 철구 as iron balls, 현천진인 as Perfected Being Hyeoncheon, 장문 사형 as Sect Leader Senior Brother, 서협 as Xixia, and 삼강오륜 as Three Bonds and Five Relationships."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 무신     | **Martial God**               | —              |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 화신귀무   | **Dance of the Fire God and Demon** |
| 시스템              | **System**                     |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 열화동 | **Fire Gate Cavern** | Ancestral cavern where the Fire Gate Clan began and its legacy continues. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 한신 | **Han Xin** | Historical military commander invoked in the same exchange. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 505
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 504
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 506
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 506
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song belongs to the Yangtze River Channel League's moderate faction, answers to his Master and Alliance Leader the Seafaring King on major League decisions, and regards Hwang Chung, his senior and Uncle Hwang, as family.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 506
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, and Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics.

## Korean source

```text
＃507화



문경이 이쪽으로 다가오고 있다는 사실은 알고 있었다. 칠 주야 동안의 피나는, 아니 피똥 싸는 수련으로 평소의 기감이 훨씬 더 날카로워졌으니까.

아직 시스템이 표시하는 기감의 경지는 오르지 않았지만, 그러기 위해서는 적어도 앞을 가로막은 벽을 넘어야 한다는 것도 어렴풋이 느끼고 있었다.

‘그런데 둘이 아니라 넷이라니, 이건 무슨 소리지?’

그러나 의문은 잠시뿐이었다.

장강수로맹과 녹림맹의 힘은 정파 무림으로서도 쉽게 무시할 수 없는 수준이고, 그런 두 세력과 한 세트로 엮일 만한 곳은 정해져 있다.

나는 과거 적천강에게 들었던 이야기를 어렴풋이 떠올리며 나직하게 중얼거렸다.

“새외무림(塞外武林).”

중원을 벗어난, 무림 밖의 무림.

혹자는 고대 황제가 세운 장성(長城) 밖의 오랑캐를 새외라 지칭하기도 하지만, 적천강은 그런 이야기들을 코웃음으로 일축한 바 있었다.



‘장성이 무슨 온 천하를 감싸고 있더냐? 천하는 말 그대로 천하(天下)다. 하늘 아래 펼쳐진 세상은 끝도 없이 드넓고, 저마다의 무림이 있는 것이지.’



타고난 성격 때문인지는 몰라도, 적천강이 바라보는 시선은 틀딱 중화사상과는 거리가 멀었다.

그가 이런 식견을 갖출 수 있었던 이유는, 정마대전 활동 시기를 제외하면 산기슭 여포였던 적천강과 달리 인싸 기질을 마음껏 뽐낸 선대 문주들의 기록도 한몫했다.

사실 후대를 위한 기록이라기보단, 자기만족용으로 쓴 일기에 가깝긴 했지만.

‘충격적이었지.’

나는 열화동에서 읽었던 몇 가지 기록을 떠올렸다.



xx년 x월 x일. 열화문 삼 대 문주 천봉.

중원이 지긋지긋했다. 사방에서 전쟁이 이어지고 무림도 개판이다. 하여 견문을 넓힐 겸 천축에 갔다.

긴 여정 끝에 갠, 뭐라고 부르는 강에 도착했다.

장강보다는 못하지만 넓고…… 아무튼 열화문의 후배들은 천축에 가거든 가장 먼저 갠 뭐 강에서 몸을 씻어라. 묻지도 따지지도 말고.

이곳저곳을 구경하고 있었는데 웬 땡중들이 우르르 몰려와 알 수 없는 말을 하며 칼을 들이밀기에 두들겨 팼다.

우연히 주위를 지나가고 있던 중원의 역관이 질겁하며 저들이 바로 천축의 소뢰음사(小雷音寺)라고 했다.

이름만 듣고 소림사랑 비슷한 줄 알았는데, 이곳의 땡중들은 난폭하기가 이루 말할 데 없었다.

더 많은 패거리를 이끌고 온 중놈들을 모조리 불구로 만들고 요상하게 생긴 절간을 모조리 불태웠다.

그 모습이 보기에 참 좋았다.



xx년 x월 x일. 열화문 오 대 문주 송학.

본 좌는 사조(師祖)이신 삼 대 문주를 마음 깊이 존경해 온바, 그분의 행적을 좇아 천하와 새외무림을 탐방했느니라.

뜨거운 사막 너머에 존재하는 대막의 광풍사(狂風社)와 일전을 겨루고, 서장(西藏)의 포달랍궁으로 찾아가 기둥을 뽑았느니라.

그러자 서장의 모든 인마가 분노하여 본 좌를 쫓았느니라.

허나 본 좌가 누구인가. 대 열화문의 오 대 문주, 귀염권(鬼炎拳) 송학.

털끝 하나 상하지 않고 놈들을…… 피해 무사히 중원으로 돌아왔느니라.

먼 훗날 열화문의 진전을 이어받을 누군가여, 명심하거라.

상대가 일류 고수 일백이라면 맞서 싸우고, 일천이라면 화신귀무를 펼치고, 그 이상이면 후일을 도모하라.

물론 이 글을 보게 될 그대가 본 좌보다 강하다면 그냥 싸워라.

아, 그리고 천축의 갠 무슨 강에 간다면 바로 뛰어들어 몸부터 씻어라. 두 번 씻어라.



xx년 x월 x일. 열화문 구 대 문주 구진천.

남만(南蠻)에 갔다. 오독문을 멸문시켰다.

파사국(波斯國)에 갔다. 영웅건 대신 터번이라 불리는 것을 쓴 이들과 만났다.

그들은 회교도(回敎徒)라 불리는 자들로, 선지자이자 예언자를 믿는다고 했다.

예언자를 만나고 싶다 하니 이미 죽었다고 했다. 참으로 이해가 되지 않아 여러 번 물었더니 칼을 빼 들었다.

어쩔 수 없이 그들을 예언자의 곁으로 보내 주었다.

다음은 북해(北海)에 있다는 빙궁(氷宮)이었는데, 사방이 얼음이요 물이라 그냥 돌아왔다.

후대의 연자여, 그대가 가라.

아, 그리고 갠 무슨 강의 이름을 알아냈다. 갠지스강. 천축에 간다면 반드시 그곳에서 몸부터 씻어라. 꼭 씻어라.



xx년 x월 x일. 열화문 십이 대 문주 한신.

불민한 제자. 여러 선조의 기록을 좇아 천축에 당도하여 갠지스강에 곧장 들어갔나이다.

머리를 감던 도중에 상류에서 떠밀려 오는 시체를 보았나이다.

자리를 옮겨 몸을 씻던 도중에 옆을 지나가는 똥을 보았나이다.

상류로 올라가 보니 수백여 명이 강에 시체를 버리고 똥을 싸고 있었나이다.

아니 시팔 이런 개수작을 부리시면 어떡하나이까.



“…….”

다시 생각해 봐도 기가 막힌 이야기뿐이다.

기록만 대충 훑어봐도 수틀리면 중원, 새외 가리지 않고 닥치는 대로 깨부수고 다녔다.

그 와중에 갠지스강에서 목욕하라는 건 병영 설문 조사에서 유격 훈련 강화하라는 말년 병장의 심술이나 다를 바가 없다.

일명 너도 좆 돼 봐라 마인드.

갠지스강에서 똥물 목욕 후 개빡친 십이대 문주 이후로는 딱히 새외무림에 관한 기록이 많지 않지만, 중원과 새외를 잇는 교역로가 열리자 중원 밖의 무림에 관한 정보가 들어오기 시작했다.

또한 지금 막 적천강의 입에서 흘러나오고 있던 저 두 세력이야말로, 지리적으로 중원과 가장 가까우며 관계적으로도 밀접한 곳이라 할 수 있었다.

“북해빙궁(北海氷宮), 그리고 남만야수궁(南蠻野獸宮).”

다시 들어도 각자의 위치와 색깔을 확실히 드러내는 문파 명이다.

물꼬를 튼 적천강의 말에 문경이 가증스럽게도 해맑게 웃으며 고개를 끄덕였다.

“네, 맞아요. 스승님께서 알려 주셨어요. 오래전 가 본 적이 있는데, 확인해 본 바로는 중원의 명문 대파와 비교해도 결코 밀리지 않는다고 하시더라고요.”

“…….”

“…….”

분명히 사람 죽이러 갔다는 것에 혁무진의 모두를 건다.

순간 나와 적천강이 비슷한 눈빛을 주고받자 문경의 눈이 슬그머니 가늘어졌다.

“왜 그러세요?”

“……어? 어어. 그냥.”

“크흠. 아무것도 아니다. 병자가 있는 곳이라면 어디든지 달려가는 신의답군.”

나야 당연하고, 적천강도 큰 도움을 입었으니 최대한 장단을 맞춰줘야 하는 처지일 수밖에 없다.

그런 우리의 반응에 언제 그랬냐는 듯 소년 의생으로 돌아간 문경이 말을 이었다.

“스승님이 하신 말씀이, 정마대전 때도 마교가 그 두 세력을 가장 먼저 포섭하려고 했다던데…… 그게 정말인가요, 적 대협?”

“응? 으음.”

적천강이 떨떠름한 표정으로 대답했다.

“사실이다. 마교 놈들에게 중원의 사마외도는 한 뿌리에서 나온 곁가지라 할 수 있으니 당연히 합류시켰고, 마교의 포섭에 응한 북해빙궁이 남하하고 남만야수궁이 북상한다면 정마대전은 매우 힘든 양상으로 흘러갔겠지.”

그러나 두 세력 중 어느 쪽도 마교가 내민 손을 잡지 않았다.

북해빙궁은 지금까지 그래 왔듯 외부와의 단절을 선언했고, 그보다 지리적으로 중원과 가까운 남만야수궁은 저울질 끝에 정파 무림의 손을 들어 주었다.

“야수궁 놈들은 처음에 싸우는 시늉만 내려 했지만, 나중 가서는 제법 큰 도움이 됐다. 놈들이 데려온 온갖 맹수들은 하나하나가 능히 일류 고수 몇 사람 몫을 해냈고, 마교가 천하 각지로 날려 보낸 전서응은 야수궁의 비전으로 조련한 천응(天鷹)에게 붙잡혔지.”

남만야수궁은 현대에 존재하는 동물 애호가들의 공적이나 다름없었다.

그들은 아주 오래전부터 남만의 밀림에 서식하는 온갖 생물체들을 붙잡아 조련하고 맹수의 움직임을 본 따 무공을 창시하여 익혀 왔으니까.

“어, 잠깐. 그러고 보니까 그쪽에 계신 분과 친하다고 하시지 않았어요?”

갑자기 떠오른 생각을 묻자 적천강이 눈살을 찌푸렸다.

“누구?”

“궁주요. 궁주.”

“궁주? 아, 야수묘왕(野獸苗王) 말이냐?”

“네, 그분.”

야수묘왕은 십왕(十王) 중에서도 가장 말석이자, 가장 특이하다고 할 수 있는 인물이었다.

애당초 본인부터가 남만의 토착민인 묘족(苗族)의 우두머리일뿐더러, 남만의 패주라 할 수 있는 남만야수궁의 주인이기 때문이었다.

그가 십왕에 들어간 이유는 정마대전에서 세운 공과 출중한 무공 때문이었으나 밖에서 보는 시선은 외국인에게 주는 명예 훈장에 가까웠고, 그 때문인지 중원 무림 내부에서도 언급을 꺼렸다.

같은 정파 식구나 넣어 주지, 뭐 하러 남부 야만인 놈을 그렇게 추켜세우냐는 것이 야수묘왕 거품설의 시작이었다고 했다.

“그저 몇 번 일면식이나 한 정도다.”

“그런데 야수묘왕이 직접 인사하러 찾아온 적도 있다면서요?”

“그건 사실이다. 대낮에 웬 상반신을 헐벗은 시커먼 놈이 거처로 찾아왔길래 화염신장부터 날릴 뻔했지.”

어째서인지 조금 전부터 불안한 눈빛으로 엉거주춤 서 있던 무송이 눈을 크게 떴다.

“정말이십니까?”

“그럼 노부가 이 나이에 거짓부렁이라도 늘어놓으리?”

“그, 그게 아니라 놀라워서 그랬습니다. 제 스승님께서도 야수묘왕에 대해 언급하신 적이 있지만, 그는 성격이 폭급하고 오만방자하여 오직 무신께만 예의를 갖췄다고 들었는데…….”

“해상왕, 이 새파랗게 어린놈이 벌써부터 노망이 났나. 제깟 놈이 병신 같으니 야수묘왕이 예의를 안 차린 걸 가지고. 쯧쯧.”

같잖다는 표정으로 혀를 찬 적천강이 말을 이었다.

“야수묘왕이 겉보기에는 그럴지 몰라도, 필요할 때는 예의를 갖추는 놈이다. 그냥 무식하게 힘만 센 놈이었으면 묘족이 한 깃발 아래 모였겠느냐?”

확실히 고개를 끄덕일 수밖에 없는 부분이다.

문도가 수십 명밖에 없는 중소 문파도 제자가 없어 사라지고 생기길 숱하게 반복하는데, 야수묘왕은 단순히 생각해도 수천이 넘는 묘족을 다스리는 족장이니까.

“그래서요?”

내 물음에 적천강이 윤기가 흐르는 붉은 수염을 쓰다듬었다.

“그래서는 뭔 놈의 그래서. 별거 없다. 찾아와서 사근사근한 말투로 선대의 인연을 들먹이더구나.”

“선대의 인연이요?”

“허, 참. 이런 불민한 놈을 보았나. 다른 놈들은 몰라도 넌 알아야지!”

“깜짝아. 왜 그러세요?”

우리 노야 갑자기 풀 악셀로 급발진하시네.

한차례 불호령을 내린 적천강이 심기 불편한 목소리로 말을 이었다.

“지금으로부터 이백여 년 전, 본문의 오대 문주께서는 남만의 오독문을 멸문시켰다.”

“그게 왜…… 아, 혹시?”

“당시의 남만은 세 발 달린 솥의 형국이었지. 오독문의 세가 가장 강성했고, 그다음이 남만야수궁이었으며 마지막은 독곡이었다.”

“결국, 오독문이 멸문당하자 남만야수궁이 치고 올라왔다?”

“그렇지. 독곡도 흡수하여 남만을 제패했고.”

“와, 미친. 이게 이렇게 되네.”

“그런 이유로 야수묘왕은 본문에 호의를 품고 있었지. 정마대전에 참여한 이유 중 하나이기도 했, 그런데 지금 감히 반말을 지껄인 게냐?”

“……시정 하겠습니다. 저도 모르게 그만.”

오래전 역대 문주가 행했던 깡패짓이 이렇게 돌아왔다고 생각하니 감탄을 금할 수 없다.

그나저나 야수묘왕이 열화문에 호의를 품고 있고, 그 때문에 정마대전에도 정파의 손을 들었다는 건…….

“남만야수궁은 이번 무림맹에도 참여할 가능성이 높겠네요.”

“글쎄, 그 부분은 노부도 쉽게 단언할 수 없다. 하지만 노부가 기억하는 야수묘왕이라면, 충분히 정파를 도울 것이다.”

“그럼 북해빙궁은요?”

“하남에서 보낸 사절이 가는 길에 얼어 죽지만 않았다면 서신 정도는 읽어 보겠지. 하지만 기대는 하지 않는 편이 좋을 게다.”

풍부한 식견과 깊은 연륜을 지닌 노강호의 눈빛이 무송을 향했다.

“다만 당장 급한 것은 이쪽인데…… 해상왕이 어찌하려나?”

무송이 신형을 움찔거린 그때, 문경이 나직히 입을 열었다.

“그런데 아까부터 무송 대협께 여쭈어보고 싶은 것이 있습니다.”

“으, 응?”

파르르 떨리는 무송의 눈동자를 말없이 바라보던 문경이 문득 혀를 찼다.

“너, 내가 누군지 알지?”

“……!”
```

## Final English reading copy

```markdown
# Chapter 507

I knew Mungyeong was approaching. Seven days and nights of grueling—no, blood-shitting—training had sharpened my usual Qi Sense considerably.

The realm stage displayed by the System had not increased yet, but I could vaguely sense that I would have to break through the wall blocking my path before that happened.

*But what does he mean, not two, but four?*

My question lingered only briefly.

The Yangtze River Channel League and the Green Forest Alliance were both powerful enough that even orthodox Murim could not afford to dismiss them easily. And there was only one place that could be grouped together with those two factions.

Vaguely recalling what I had once heard from Jeok Cheongang, I murmured,

“The Outer Murim.”

The Murim beyond the Central Plains. The Murim outside the Murim.

Some people called the barbarians beyond the Great Wall built by an ancient emperor the Outer Lands, but Jeok Cheongang had always dismissed such talk with a snort.

*“Does the Great Wall surround the whole world? The world beneath the heavens is exactly that—the world beneath the heavens. The lands beneath the sky are boundlessly vast, and each has its own Murim.”*

Whether it was because of his innate temperament or not, Jeok Cheongang’s outlook had been far removed from the stale, old-man Zhonghua chauvinism of his era.

Part of the reason he had gained such insight was the records left behind by previous Sect Leaders, who had indulged their social-butterfly tendencies to the fullest. That was in contrast to Jeok Cheongang, who had been a Lü Bu living at the foot of a mountain whenever he was not active during the Great Faction War.

Though, to be honest, those records were less like documents written for future generations and more like diaries written for their own satisfaction.

*They had been shocking.*

I recalled a few of the records I had read in Fire Gate Cavern.

---

Year xx, Month x, Day x. Cheonbong, Third Sect Leader of the Fire Gate Clan.

I had grown sick of the Central Plains. War continues on all sides, and the Murim is a complete mess. So, to broaden my horizons, I went to India.

After a long journey, I arrived at a river called the Gan… something.

It is not as large as the Yangtze, but it is wide… Anyway, to all the younger disciples of the Fire Gate Clan: if you ever go to India, wash yourselves in that Ganges-whatever river first. Do not ask questions. Do not argue.

I was sightseeing here and there when a group of bald monks suddenly rushed over, shouted things I could not understand, and thrust swords at me. So I beat them senseless.

A Central Plains interpreter who happened to be passing by was horrified and told me that they were from the Small Thunderclap Temple of India.

I had assumed it would be similar to Shaolin Temple from the name alone, but the bald monks here were indescribably violent.

I crippled every monk who came with an even larger gang and burned down every strange-looking temple.

It was quite a pleasant sight.

---

Year xx, Month x, Day x. Songhak, Fifth Sect Leader of the Fire Gate Clan.

I have always held my Grandmaster, the Third Sect Leader, in the deepest respect. Following in his footsteps, I have traveled throughout the world and explored the Outer Murim.

I crossed blades with the Mad Wind Society of the great desert beyond the scorching sands, then traveled to the Potala Palace in Tibet and pulled out its pillars.

As a result, every man and beast in Tibet flew into a rage and chased after me.

But who am I? Songhak, the Ghost Flame Fist and Fifth Sect Leader of the great Fire Gate Clan.

Without suffering so much as a scratch, I… avoided them and returned safely to the Central Plains.

To whoever inherits the Fire Gate Clan’s true legacy in the distant future, remember this well.

If your opponent is one hundred First Rate masters, fight them head-on. If there are one thousand, unleash the Dance of the Fire God and Demon. If there are more than that, live to fight another day.

Of course, if you who are reading this are stronger than I am, just fight them.

Ah, and if you go to that Gan-whatever river in India, jump in and wash yourself immediately. Wash yourself twice.

---

Year xx, Month x, Day x. Gu Jincheon, Ninth Sect Leader of the Fire Gate Clan.

I went to Nanman. I destroyed the Five Poisons Sect.

I went to Persia. I met people who wore something called turbans instead of hero headbands.

They were called Muslims, and they said they believed in a messenger and a prophet.

When I said I wanted to meet the prophet, they told me he was already dead. I could not understand this at all, so I asked several times. They drew their swords.

I had no choice but to send them to the prophet’s side.

Next, I went to the Ice Palace in the North Sea. It was surrounded by nothing but ice and water, so I simply returned.

To the future disciple who will read this, you go.

Ah, and I finally learned the name of that Gan-whatever river. The Ganges River. If you go to India, make sure you wash yourself there first. Be sure to wash.

---

Year xx, Month x, Day x. Han Xin, Twelfth Sect Leader of the Fire Gate Clan.

I am an unworthy Disciple. Following the records of several ancestors, I arrived in India and immediately entered the Ganges River.

While washing my hair, I saw a corpse being carried down from upstream.

I moved to another spot and saw a turd floating past while I was washing my body.

When I went upstream, I saw several hundred people throwing corpses into the river and defecating.

For fuck’s sake, how could you pull this kind of bullshit on me?

---

“……”

Even after thinking it over again, all I could find were astonishing stories.

I only had to skim through the records to see that whenever something displeased them, they smashed their way through anything and everything, whether in the Central Plains or the Outer Murim.

And telling their successors to bathe in the Ganges was no different from a sergeant about to be discharged writing “more field training” on a barracks survey out of pure spite.

In other words: *You get fucked too.*

There were not many more records about the Outer Murim after his shit-water bath in the Ganges left the Twelfth Sect Leader royally pissed off. But once trade routes connecting the Central Plains to the outside world opened, information about the Murim beyond the Central Plains began to flow in.

And the two factions currently coming from Jeok Cheongang’s mouth were precisely the ones that were geographically closest to the Central Plains and most closely connected to it.

“The North Sea Ice Palace and the Nanman Beast Palace.”

Even when I heard them again, the names clearly revealed their respective locations and character.

At Jeok Cheongang’s words, which had finally opened the floodgates, Mungyeong nodded with an infuriatingly bright smile.

“Yes, that’s right. My Master told me. He said he had visited them long ago, and from what he had confirmed, they were in no way inferior to the renowned great sects of the Central Plains.”

“……”

“……”

I would stake everything Hyuk Mujin had on the fact that he had gone there to kill people.

The instant Jeok Cheongang and I exchanged similar looks, Mungyeong’s eyes slowly narrowed.

“Why are you looking at me like that?”

“……Huh? Oh, nothing.”

“Ahem. Nothing at all. You truly are a Divine Physician, rushing anywhere there are patients.”

Naturally, I had to play along. Jeok Cheongang had also received considerable help from him, so he had no choice but to do the same.

As if he had never done anything suspicious, Mungyeong returned to his medical-apprentice persona and continued.

“My Master said that during the Great Faction War, the Demonic Cult tried to recruit those two factions before anyone else. Is that true, Great Hero Jeok?”

“Hmm? Ah.”

Jeok Cheongang answered with a sour expression.

“It is true. To the Demonic Cult, the wicked and unorthodox factions of the Central Plains were branches grown from the same root, so they naturally brought them into the fold. If the North Sea Ice Palace had accepted the Demonic Cult’s offer and moved south while the Nanman Beast Palace moved north, the Great Faction War would have taken a very difficult turn.”

But neither of the two factions accepted the hand extended by the Demonic Cult.

The North Sea Ice Palace declared its isolation from the outside world, as it always had. The Nanman Beast Palace, which was geographically closer to the Central Plains, weighed its options and ultimately sided with orthodox Murim.

“The Beast Palace bastards only intended to pretend to fight at first, but they ended up being quite a great help. Every one of the countless ferocious beasts they brought was worth several First Rate masters, and the messenger eagles the Demonic Cult sent flying throughout the land were captured by Heavenly Eagles trained through the Beast Palace’s secret martial arts.”

The Nanman Beast Palace was practically the public enemy of modern-day animal lovers.

For a very long time, its people had captured and trained every kind of creature living in Nanman’s jungles. They had also created and practiced martial arts modeled after the movements of ferocious beasts.

“Oh, wait. Come to think of it, didn’t you say you were close to someone over there?”

When I asked about the thought that had suddenly occurred to me, Jeok Cheongang frowned.

“Who?”

“The Palace Lord. The Palace Lord.”

“The Palace Lord? Ah, you mean the Beast Miao King?”

“Yes, him.”

The Beast Miao King was both the lowest-ranking and the most unusual of the Ten Kings.

For one thing, he was the leader of the Miao people, the indigenous people of Nanman. For another, he was the master of the Nanman Beast Palace, which could be called the overlord of Nanman.

He had entered the Ten Kings because of his accomplishments during the Great Faction War and his outstanding martial arts. But from the outside, it was almost like an honorary medal given to a foreigner, and perhaps because of that, people within Central Plains Murim were reluctant to mention him.

*Why raise up some southern barbarian when we could just add another member of orthodox Murim?*

That was supposedly how the theory that the Beast Miao King was being overhyped had begun.

“I merely met him face-to-face a few times.”

“But I heard the Beast Miao King even came to pay his respects to you in person.”

“That is true. One day, a black-skinned man with his upper body bare came to my residence in broad daylight. I almost sent a Flame Divine Palm at him.”

For some reason, Mu Song, who had been standing awkwardly with an anxious look in his eyes for a while now, opened his eyes wide.

“Is that really true?”

“Would this old man start making up lies at my age?”

“N-no, that’s not what I meant. I was surprised. My Master has mentioned the Beast Miao King before as well, but I heard that he was short-tempered and arrogant, and showed courtesy only to the Martial God……”

“The Seafaring King? Has that young whelp already gone senile? The Beast Miao King only refused to show him respect because he was such a damned fool. Tsk, tsk.”

Jeok Cheongang clicked his tongue with an expression of utter disdain and continued.

“The Beast Miao King may look that way on the surface, but he knows how to show courtesy when necessary. If he were merely an ignorant man with nothing but brute strength, do you think the Miao people would have gathered beneath a single banner?”

That was something I could only nod along with.

Even small- and mid-sized sects with only a few dozen Disciples vanished and reappeared countless times because they could not find enough Disciples. The Beast Miao King, on the other hand, was a tribal chief ruling over several thousand Miao people at the very least.

“So?”

At my question, Jeok Cheongang stroked his gleaming red beard.

“What do you mean, ‘so’? There was nothing special about it. He came to visit and spoke in a soft, ingratiating tone while bringing up a connection with the previous generation.”

“A connection with the previous generation?”

“Good grief. Have you always been this unworthy a fellow? You should know better than anyone else!”

“Whoa. What’s wrong?”

Our Old Master had suddenly floored the accelerator and rocketed off.

After unleashing a tirade, Jeok Cheongang continued in an irritated voice.

“More than two hundred years ago, the Fifth Sect Leader of our sect destroyed the Five Poisons Sect of Nanman.”

“Why would that…… Ah, could it be?”

“At the time, Nanman was like a cauldron balanced on three legs. The Five Poisons Sect was the strongest, followed by the Nanman Beast Palace, with Poison Valley in last place.”

“So after the Five Poisons Sect was destroyed, the Nanman Beast Palace rose to the top?”

“That’s right. It also absorbed Poison Valley and conquered Nanman.”

“Wow, that’s insane. So that’s how it turned out.”

“For that reason, the Beast Miao King held goodwill toward our sect. It was also one of the reasons he participated in the Great Faction War. But how dare you speak to me informally just now?”

“……I’ll correct myself. It slipped out before I realized it.”

It was impossible not to marvel at how the thug-like behavior of a Sect Leader from generations ago had come back around like this.

But more importantly, the Beast Miao King held goodwill toward the Fire Gate Clan, and because of that, he had sided with orthodox Murim during the Great Faction War……

“The Nanman Beast Palace is probably quite likely to participate in this New Murim Alliance.”

“I can’t say for sure. Even this old man cannot make an easy judgment about that. But if the Beast Miao King I remember is still the same, he will help orthodox Murim.”

“Then what about the North Sea Ice Palace?”

“If the envoy sent from Henan hasn’t frozen to death on the way, they will probably read the letter at least. But it would be better not to get your hopes up.”

The eyes of the seasoned old martial-world veteran, rich in knowledge and experience, turned toward Mu Song.

“But this is the urgent matter right now. What will the Seafaring King do?”

At that moment, Mu Song flinched.

Mungyeong quietly opened his mouth.

“There’s something I’ve been wanting to ask Great Hero Mu Song for a while.”

“Uh, yes?”

Mungyeong silently watched Mu Song’s trembling eyes, then suddenly clicked his tongue.

“You know who I am, don’t you?”

“……!”
```
