<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0783.txt",
      "sha256": "bf751cacf7b0ee67db3168ca6556a976630a82d04064f337ca2548b0becc67fa",
      "bytes": 12612
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "19bebbae3ce5c86bbc89beb788962ab3cb0371dcf3daedc7e1dfe84a1fa73fad",
      "bytes": 927
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "47349c578ce3a378dc53173dec4002c0828b8095d08eadab83cdfaafdabfc433",
      "bytes": 223666
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "34350707fef53f197c0fec3d71468e5277674966afb60c165c6fb09e3ee26e9e",
      "bytes": 1848
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e903ad227cd649aff3eaf6e9ae080304ee3709c79f7415d063e48338e1fab12d",
      "bytes": 2112
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1f4a2b0a0336f546bba1ea2616f91a3430c4d7630184577f2a6ec3efcfc4347e",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "5afb183d0ece3403e85dd1a09a0a96433de4c1b3e81a68c04bbc004c8beae3d9",
      "bytes": 889
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8db9e79ef5ea3bb4279d4c11d5c9e6e23a49de5f2010abaf0bfb116c09d99a97",
      "bytes": 243344
    }
  ],
  "estimated_tokens": 9820
}
-->

# Durable State Update — Chapter 783

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 783. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 783. Profile updates may replace only one
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
  "chapter": 783,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 783,
    "continuity_sources": [783],
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
    "Jin Taekyung and Michael Silbert are still fighting at the National Assembly; Taekyung has resolved to kill Michael.",
    "Michael’s absorbed magical power has repeatedly fallen out of balance with his mana; he has considered becoming a new Demon King.",
    "Some National Assembly cameras remain operational, but the fight is not being broadcast.",
    "Taekyung can combine the Flame-Extinguishing Divine Fist and Flame Divine Palm to disrupt and redirect Michael’s aura."
  ],
  "continuity_sources": [
    782
  ],
  "open_questions": [
    "Who will prevail in the fight at the National Assembly?",
    "Where is Michael’s pet crow, and why is the outside world silent despite the fighting?",
    "What truth does Michael intend to keep from becoming public?"
  ],
  "safe_through": 782,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마정석     | **Magic Gem**         |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 천근추 | **Thousand-Catty Drop** | Technique Cheongpung identifies when Taekyung lifts the spear shaft beneath his foot. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 사량발천근 | **Four Ounces Deflecting a Thousand Catties** | Principle Jongni Chu cites for redirecting force rather than opposing it directly. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 황하 | **Yellow River** | River along which civilization began. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 727
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 780
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the Hunter who exposed Michael Silbert's ability to absorb monsters' magical power.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 780
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 782
- **Aliases:** None
- **Role:** Michael Silbert is Odin Guild Master and a public hero who absorbs monsters’ magical power, which has repeatedly fallen out of balance with his mana, and has contemplated becoming a new Demon King.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃783화



쉬이이잉!

쇄도와 동시에 섬광처럼 내뻗은 창날이 공간을 가른다. 공기를 태우고, 바람을 지우며 솟구친 화염이 짙은 어둠을 관통했다.

퍼어엉!

보이지 않는 흐름을 정확히 꿰뚫는 일점(一點).

파도처럼 덮쳐 오던 마력 중 일부가 힘없이 흩어진다. 쏘아지던 속도 그대로 마력의 틈새를 파고든 내 시야에 익숙한 얼굴이 들어왔다.

아니, 익숙하면서도 낯선 얼굴이라고 하는 것이 맞는 표현일지도 모른다.

지금의 미카엘 실베르트는, 더 이상 미카엘 실베르트가 아니게 되었으니까.

- 제법이구나.

스산한 그 목소리가 귓가에 닿은 그 순간.

쉭.

놈의 신형이 지워지듯 사라졌다.

순식간에 목표가 사라진 시야 속, 나는 당황하는 대신 본능에 가까운 움직임으로 몸을 틀었다.

슈확!

등 뒤에서 불쑥 솟아오른 검이 옆구리를 스쳐 허공을 꿰뚫는다.

만약 피하지 않았다면 심장이 관통되었을 일격. 나는 돌아서며 일장(一掌)을 뻗었다.

꽈아앙!

분명 살과 뼈로 이루어진 육신일진대. 두 손바닥이 부딪침과 동시에 폭발과도 같은 굉음이 터져 나왔다.

폭발 이상의 충격파와 함께.

드드드득!

밀려나는 발끝을 따라 땅거죽이 뒤집힌다. 수 미터를 물러선 나와 달리 제 자리에 우뚝 서 있는 미카엘 실베르트가 입꼬리를 말아 올렸다.

- 이제야 알겠느냐, 내게 맞선 것이 얼마나 멍청한 짓이었는지?

퉤.

나는 대답 대신 입 안에 고인 핏물을 뱉어 냈다. 그리고 그것이 지면에 닿기도 전에, 힘주어 걸음을 내디뎠다.

콰앙!

발끝에 닿은 지면이 폭발하듯 부서진다.

전신을 스치는 바람과 함께 십여 미터의 거리가 단번에 사라지고, 빛살처럼 휘두른 창과 검이 서로를 향해 달려들었다.

카아앙!

날카로운 소음과 함께 주위의 공기가 터져 나간다. 넘쳐나는 마력을 증명이라도 하듯, 검이라고 볼 수 없을 만큼 길고 거대해진 그것은 창날을 크게 밀어 냈다.

우득.

손목으로 고스란히 전해지는 통증.

이건 신체 능력을 떠나, 품고 있는 기운의 크기에서 나오는 차이다.

마정석을 흡수한 미카엘 실베르트의 신체 능력이 훨씬 향상된 것도 있겠지만, 끊임없이 샘솟는 마력으로 더욱더 강화되니 내가 밀리는 것은 당연했다.

물론, 내가 이대로 정면 승부를 고집한다는 전제하에서만.

카드드득!

돌연 부드럽게 회전시킨 창날을 따라 검신이 미끄러진다.

분명 실린 힘에는 큰 격차가 있음에도 불구하고 미카엘 실베르트의 검은 주인의 의지를 벗어났고, 나는 짐작이 맞았음을 확신하며 놈을 향해 일권(一拳)을 뻗었다.

화륵, 후웅!

섬광처럼 터져 나온 화염.

마치 살아 있는 생물처럼 움직인 짙은 어둠이 황급히 주인의 몸을 감쌌으나, 전력이 실린 멸염신권(滅炎神拳)은 마력을 불태우며 놈의 가슴을 후려쳤다.

콰아아앙!

귀가 먹먹해지는 굉음과 함께 포탄처럼 튕겨 나가는 신형.

황급히 양팔을 떨쳐 쏟아낸 마력으로 나를 견제한 미카엘 실베르트가 울컥 핏물을 토해 냈다.

쿨럭.

화살처럼 날아드는 마력을 모조리 베어 낸 나는 비틀거리는 놈의 모습을 보며 묘한 감흥을 느꼈다.

비로소 확실한 타격을 입혔기 때문이 아니라, 놈의 입가에서 흘러나오는 핏물의 색이 붉다는 점에서.

“그래, 너 같은 괴물도 아직까지는 인간이라 이거지.”

혼잣말과도 같은 내 뇌까림에 미카엘 실베르트가 이를 악물었다.

그러나 생각지도 못한 일격을 허용한 놈의 눈동자는 잘게 흔들리고 있었다.

- 도대체, 무슨 수를 쓴 것이냐.

나는 선선히 대답했다.

“사량발천근(四兩撥千斤).”

- 뭐?

“이해할 필요 없다. 어차피 이 세상에는 네가 모르는 뭔가가 존나게 많으니까.”

- ……!

“그래서 나도 굳이 이해하려고 안 해. 너나, 그간 너랑 붙어먹으면서 뭔 개짓거리를 저질렀길래 저기서 싸우고 있는 건지 모를 미친놈들이나…… 죄다 이해할 수 없는 것투성이거든.”

나는 미카엘 실베르트를 빤히 응시하며 말을 이었다.

“아니, 그걸 이해하는 순간 나도 똑같은 병신이 되어 있겠지.”

그 한 마디에 고통의 흔적이 남아 있던 얼굴 위로, 새로운 감정이 덧씌워진다.

분노. 혹은 치욕.

한껏 일그러진 놈의 얼굴을 바라보는 것은, 내가 생각했던 것 이상으로 기분이 유쾌해지는 일이었다.

“내가 아까 말했었지. 거머리는 결국 거머리일 뿐이라고. 죽었다 깨어나도 용이 될 수 없다고.”

- ……네놈.

“그래, 모든 걸 떠나서 하나만큼은 인정한다.”

열기를 머금은 숨결이 화룡(火龍)의 그것처럼 뜨겁다. 나는 놈을 향해 걸음을 내디디며 덧붙였다.

“넌, 내가 지금껏 만난 놈 중에서 가장 강한 거머리라는 거.”

그 한마디와 함께, 나는 역수(逆手)로 말아쥔 백염을 망설임 없이 쏘아 보냈다.

파앙-!

소닉 붐이 일어난 것처럼 겹겹이 터져 나가는 공기.

그리고 그 끝에, 미카엘 실베르트가 있었다.

콰앙! 구구구궁!

화염과 마력이 뒤섞인, 거대한 폭발.

수십 겹의 방어 마법 덕분에 간신히 형태를 유지하고 있던 스테인드 글라스(Stained glass)가 충격파를 이기지 못하고 산산이 부서졌고, 나는 머리 위로 쏟아지는 무수한 파편의 소나기를 섬광처럼 가로지르며 쌍장(雙掌)을 내질렀다.

퍼어엉!

화염을 머금은 광풍이 휘몰아쳤다.

폭발과 함께 온통 뿌옇게 물든 주위 풍경 속에서, 비틀거리는 누군가의 그림자가 두 눈에 선명히 각인된다.

‘놈이다.’

의심의 여지조차 없는 확신.

동시에 땅을 박차며 쇄도한 나는 허공을 움켜쥐었다.

아니, 마음속에서 외친 명령어와 함께 그려지듯 나타난 두 자루의 창을 잡고 다시 한번 쏘아 보냈다.

쐐애애액!

공간을 가로지르는 두 줄기의 섬광.

그리고 미카엘 실베르트가 신형을 비틀며 투창을 피해 냈을 때, 나는 다시 한번 주위를 감싼 어둠을 찢으며 코앞까지 들이닥쳤다.

- 진태경!

후우웅!

분노 어린 외침 너머로 전해지는 묵직한 파공성.

무식하리만치 엄청난 마력을 공급받아 거대해진 검이 일도양단(一刀兩斷)의 기세로 내리그어졌다.

쏴아아악! 서걱!

공간이 갈라지며 목표를 잃은 검이 지면을 쪼갰다.

그와 동시에 가슴으로부터 아릿한 통증이 전해졌다. 분명 마지막 순간 옆으로 피했음에도 불구하고, 검에 실린 압력은 상상 이상으로 강했고 날카로웠다.

모골이 송연해지는 힘과 속도.

하지만 놈이 내가 가질 수 없는 막대한 기운을 가졌듯이, 나 역시 놈에게 없는 무언가를 갖고 있었다.

생과 사가 오가는 전투에서 공력의 크기보다 중요한 것,

바로 무공(武功)을.

쿵! 콰드드득!

재차 검이 들어 올려지던 그 순간, 공력을 끌어올려 짓밟았다.

천근추(千斤錘)를 응용한 움직임과 함께 검을 짓누르는 엄청난 무게에, 미카엘 실베르트의 눈이 크게 뜨였다.

- ……!

처음 무공을 접했다면 당연한 반응이다. 나도 적천강에게 제대로 된 무공을 사사하며 매일같이 놀라움을 겪었으니까.

하지만 내게 있어 놈은 스승이나 제자가 아니라, 반드시 죽여야 할 괴물이었다.

친절한 설명 따위는 해 줄 없는, 순수한 의미의 적.

화륵.

팔 성에 이른 화염신장(火焰神掌)이 끔찍한 열기를 토해 낸다.

이미 검 자루를 쥐고 있던 손을 빼기에는 늦은 상황. 놈이 황급히 다른 한 손을 내뻗었을 때, 나는 마음속으로 명령어를 읊었다.

‘인벤토리 오픈. 소환.’

푸푹!

굉음 대신 터져 나온 것은 핏물이었다. 마력에 이어 손바닥을 관통한 단검을 확인한 미카엘 실베르트가 이를 악물었다.

툭 튀어나올 것처럼 부릅뜬 두 눈동자에는 알 수 없는 깨달음과 고통이 뒤섞여 있었다.

- 이건……!

철두철미한 미카엘 실베르트의 성격이라면, 이미 내가 지닌 인벤토리의 존재를 얼핏 눈치채고 있었을지도 모른다.

하지만 놈이 생각하는 것 이상으로 나는 강하고, 그 이상으로 임기응변에 능숙하다.

설령 놈이 짐작하고 있었다 하더라도, 결과는 크게 달라지지 않았을 것이다.

‘공력의 크기는, 생사(生死)를 결정짓는 한 요소에 불과하니까.’

지금껏 내 손에 쓰러진 강자들이 증인이고 검사이며 동시에 판사다.

누군가는 나를 최고의 후기지수이자 열화신룡(烈火火龍)이라 부르고, 또 다른 누군가는 어느 날 갑작스럽게 찾아온 재각성으로 엄청난 힘을 얻은 행운아라 부르지만.

모두 틀렸다.

F급 헌터였던 나는 흙탕물에서 태어나 숱한 죽음의 위기에서 몸부림치며 성장했다.

혼신을 다한 몸부림으로 주위를 가득 메운 이 구덩이 속의 흙이 모두 빠져나갈 때까지. 마침내 맑은 연못으로 변할 때까지.

그런데…… 사마귀도, 두꺼비도 아닌 거머리 따위에게 연못을 넘겨줄 수는 없다.

이 연못을 흙탕물이 아니라, 핏물로 가득 채울 거머리라면 더더욱.

푹, 푸푸푹!

나는 빛살처럼 손을 휘둘렀다.

단검에 관통당한 미카엘 실베르트의 손을 꽉 움켜쥔 채, 인벤토리에서 불러온 또 다른 무기로 놈의 전신 곳곳을 닥치는 대로 베고, 찌르고, 비틀며 쑤셨다.

- 크아아악!

한껏 벌어진 입가에서 핏물이 뿜어져 나왔다. 동시에 뒤늦게 검 자루에서 떨어져 나온 손이 마치 공성추처럼 내 옆구리를 파고들었다.

후웅!

섬뜩하리만치 묵직한 파공성.

상대는 어지간한 S급 몬스터 두셋을 합친 것 같은 마력과 대형 몬스터도 맨손으로 찢어발기는 근력을 가진 괴물이다.

아무리 내가 시스템으로 강철 같은 육체를 지니게 되었다 해도, 이대로 저 공격을 허용한다면 무사하지 못한다.

그러니까, 지금 이대로라면.

‘인벤토리 오픈. 소환.’

우득!

강렬한 충격에 상반신이 들썩였다. 뼈가 어긋나는 소리와 함께 울컥 솟구친 약간의 핏물이 입안에 고인다.

하지만, 그것이 전부였다.

미카엘 실베르트가 죽을힘을 다해 휘둘렀을 일권은 살을 터트리고 뼈를 부수지 못했다.

갑작스럽게 나타나 내 상반신을 감싼, 붉은빛이 감도는 갑옷의 일부를 파손시켰을 뿐이다.

삐빅.



- [화룡갑(火龍鉀)]의 일부가 파괴되었습니다!

- 현재 파손율 : 44%

- 90% 이상 파손되었을 시. 인벤토리로 회수되며 자동 수복 모드에 들어갑니다.



귓가를 파고드는 알림을 들으며, 나는 멍하니 굳어 버린 미카엘 실베르트를 향해 환하게 웃었다.

“응~ 수리하면 그만이야~”

- ……!

그리고 그 순간.

푸우웃!

입 안에 고여 있던 핏물을 놈의 얼굴에 뱉었다.

동시에 면상에 피를 흠뻑 뒤집어쓴 채 본능적으로 발버둥 치는 몸뚱어리에 일권을 꽂아 넣었다.

마치, 지면에 박힌 못을 망치로 때려 박듯이.

콰앙! 콰드드득!

묵직한 굉음과 진동이 사방을 휩쓸었다. 주위의 지반이 움푹 가라앉으며 생겨난 커다란 크레이터 속, 멸염신권에 가슴을 직격당한 미카엘 실베르트가 쓰러진 채 핏물을 토해 냈다.

- 컥, 커헉……!

울컥거리며 솟구치는 핏물이 구덩이 안으로 고였다.

놈이 걸치고 있던 갑옷은 이미 박살 난 지 오래. 새하얗던 피부는 핏물과 그을림으로 검붉게 물들어 있었다.

“……병신 새끼.”

나는 씁쓸하게 웃었다. 손을 뻗자 쏘아지듯 날아온 백염의 창자루가 손아귀에 감긴다.

그리고 망설임 없이, 창날을 들어 올렸다.

슈확!
```

## Final English reading copy

```markdown
# Chapter 783

*Whoooosh!*

As I charged, the spearhead shot forward like a flash of light, cleaving through space. Flames surged up, burning the air and erasing the wind as they pierced the thick darkness.

*Boom!*

A single point, piercing the invisible flow with perfect precision.

Some of the magical power sweeping toward me like a wave dispersed helplessly. My vision plunged through the gap in the magical power at the same speed as my thrust—and a familiar face came into view.

No, perhaps it was more accurate to call it a face that was both familiar and strange.

Because the Michael Silbert standing there now was no longer Michael Silbert.

“You’re not bad.”

The moment that chilling voice reached my ears—

*Shhk.*

His figure vanished as if it had been erased.

Instead of panicking when my target disappeared from sight in an instant, I twisted around in a movement closer to instinct.

*Whoosh!*

A sword suddenly rose behind me, skimming my side and cutting through empty air.

If I hadn’t dodged, that strike would have pierced my heart. I spun around and thrust out a palm.

*Kwaang!*

He was supposed to have a body made of flesh and bone. Yet the instant our palms collided, a blast like an explosion rang out.

Along with a shock wave greater than an explosion—

*Grrrrk!*

The ground flipped over beneath my sliding toes. Unlike Michael Silbert, who stood rooted to the spot, I was pushed back several meters. He curled up the corner of his mouth.

“Do you understand now how foolish it was to stand against me?”

*Ptoo.*

Instead of answering, I spat the blood pooled in my mouth onto the ground. Before it even hit the earth, I stepped forward with all my strength.

*Kwaang!*

The ground beneath my toes shattered like an explosion.

The wind swept past my body, and the distance of more than ten meters disappeared in an instant. My spear and his sword flashed toward each other.

*Kaaang!*

The sharp clash burst the air around us. The sword had grown so long and massive that it could hardly be called a sword anymore, as if to prove the magical power overflowing from it. It drove my spearhead far aside.

*Crack.*

Pain shot through my wrist.

This wasn’t just a difference in physical ability. It came down to the sheer amount of power we held.

Michael Silbert’s body had undoubtedly grown much stronger after absorbing the Magic Gem. And with the magical power welling up without end, he could reinforce it even further. Of course I was being pushed back.

At least, as long as I insisted on a head-on fight.

*Grrrrk!*

Suddenly, I smoothly rotated the spearhead, and the sword blade slid along it.

Despite the enormous difference in force, Michael Silbert’s sword slipped free of its owner’s control. Certain that my hunch had been right, I thrust a fist at him.

*Fwoosh, whoom!*

Flames burst forth in a flash.

The thick darkness moved like a living creature and hurried to envelop its master, but my Flame-Extinguishing Divine Fist, thrown with all my strength, burned through the magical power and slammed into his chest.

*Kwaaaang!*

A deafening crash rang out, and his body shot away like a cannonball.

Michael Silbert hurriedly flung out both arms, pouring magical power at me to keep me in check. Then he coughed up blood.

*Kh-erk.*

I cut down every bolt of magical power flying toward me and watched him stagger. A strange feeling stirred in me.

Not because I’d finally landed a solid hit, but because the blood spilling from the corner of his mouth was red.

“So even a monster like you is still human—for now, anyway.”

At my mutter, Michael Silbert clenched his teeth.

But his eyes wavered. He hadn’t expected that blow.

“What the hell did you do?”

I answered readily.

“Four Ounces Deflecting a Thousand Catties.”

“What?”

“You don’t need to understand. There’s a shitload of things in this world you don’t know about anyway.”

“……!”

“So I don’t bother trying to understand, either. You, or those lunatics fighting over there—who knows what kind of fucked-up shit they got up to while working with you to end up in that fight? None of it makes any sense to me.”

I stared straight at Michael Silbert and continued.

“No. The moment I understood it, I’d become the same kind of idiot.”

A new emotion covered the traces of pain on his face.

Anger. Or humiliation.

Watching his face twist was far more satisfying than I’d expected.

“I told you earlier. A leech is still just a leech. Even if it died and came back to life, it could never become a dragon.”

“……You bastard.”

“Yeah. Whatever else, I’ll admit one thing.”

My breath was hot with heat, like that of a fire dragon. I stepped toward him and added,

“You’re the strongest leech I’ve ever met.”

With that, I launched White Flame, gripped in reverse, without hesitation.

*Bang!*

The air burst in layers, as if a sonic boom had just gone off.

And at the end of it stood Michael Silbert.

*Kwaang! Grrrrrung!*

An enormous explosion of flame and magical power.

The stained glass, which had barely held its shape thanks to dozens of layers of defensive magic, couldn’t withstand the shock wave and shattered. I flashed through the rain of countless shards falling overhead and thrust out both palms.

*Boom!*

A gale filled with flame swept through.

Amid the surroundings blurred by the explosion, the shadow of someone staggering was etched clearly into my eyes.

*That’s him.*

There was no room for doubt.

At the same time, I kicked off the ground and charged, reaching out to grab empty air.

No—two spears appeared as if drawn into existence by the command I shouted in my mind. I caught them and launched them once more.

*Shweeeek!*

Two streaks of light tore across the space between us.

When Michael Silbert twisted aside and dodged the spears, I tore through the darkness surrounding us again and closed in right in front of him.

“Jin Taekyung!”

*Whooom!*

Beyond his furious shout came the heavy whistle of a weapon cutting through the air.

Supplied with an absurd amount of magical power, the now-enormous sword swung down with the force to cleave me in two.

*Shwaaaak! Shhk!*

Space split open, and the sword, having missed its target, cleaved the ground.

At the same time, a dull pain spread from my chest. I’d dodged to the side at the last moment, but the pressure carried by the sword was far greater and sharper than I’d imagined.

A strength and speed that made my hair stand on end.

But just as he possessed an immense amount of power I could never have, I possessed something he did not.

In a fight where life and death hung in the balance, what mattered more than the size of one’s internal energy—

Was martial arts.

*Thump! Grrrrk!*

Just as he raised his sword again, I drew up my internal energy and stamped down.

I used the Thousand-Catty Drop to bear down on his sword with tremendous weight. Michael Silbert’s eyes widened.

“……!”

It was only natural, if this was his first encounter with martial arts. Even I’d been astonished day after day when I first learned true martial arts from Jeok Cheongang.

But to me, he wasn’t a Master or a Disciple. He was a monster I had to kill.

An enemy in the purest sense of the word, to whom I had no reason to offer a friendly explanation.

*Fwoosh.*

The Flame Divine Palm, brought to eight-tenths of its full power, poured out a dreadful heat.

It was already too late to pull away the hand gripping the sword hilt. When he hurriedly thrust out his other hand, I recited a command in my mind.

*Inventory open. Summon.*

*Thwack!*

What burst out wasn’t a deafening crash, but blood. Michael Silbert clenched his teeth as he saw the dagger that had pierced through his palm, magical power and all.

His eyes were so wide they seemed about to pop out. Some unknowable realization was mixed with the pain in them.

“This is……!”

Given Michael Silbert’s meticulous nature, he might already have vaguely guessed that I had an Inventory.

But I was stronger than he thought—and even better at improvising.

Even if he’d guessed, the result wouldn’t have changed much.

*The size of your internal energy is only one factor in deciding life or death.*

The powerful opponents who had fallen at my hands were my witnesses, jury, and judge all at once.

Some called me the greatest young prodigy and the Blazing Flame Divine Dragon. Others called me a lucky man who’d gained tremendous power through a sudden reawakening one day.

They were all wrong.

I’d been an F-rank Hunter, born in muddy water. I’d struggled and grown through countless brushes with death.

I would keep struggling with all my might until every bit of dirt filling this pit around me was gone. Until it finally became a clear pond.

And yet…… I couldn’t hand my pond over to some leech. Not a mantis, not a toad—a leech.

Especially not a leech that would fill that pond with blood instead of muddy water.

*Thrust, thrust-thrust!*

I swung my hand like a streak of light.

Still clutching Michael Silbert’s hand, pierced by the dagger, I summoned another weapon from my Inventory and slashed, stabbed, twisted, and drove it into him wherever I could.

“Graaah!”

Blood sprayed from his wide-open mouth. At the same time, the hand that had belatedly let go of the sword hilt drove into my side like a battering ram.

*Whoom!*

The air whistled with a weight that made my skin crawl.

My opponent was a monster with magical power equivalent to two or three S-rank monsters combined, and enough strength to tear apart a large monster with his bare hands.

Even with the System having given me a body like steel, I wouldn’t come out of it unscathed if I let that attack land.

At least, if I did nothing.

*Inventory open. Summon.*

*Crack!*

The tremendous impact jolted my upper body. The sound of bones shifting rang out, and a little blood welled into my mouth.

But that was all.

Michael Silbert’s punch, thrown with all his might, had neither split my skin nor broken my bones.

It had only damaged part of the red-tinged armor that had suddenly appeared and wrapped around my upper body.

*Beep.*

> **System**
> A part of the **Fire Dragon Armor** has been destroyed!
>
> Current damage: 44%
>
> At 90% damage or higher, it will be recalled to the Inventory and enter automatic repair mode.

As I heard the alert pierce my ears, I gave a bright smile to Michael Silbert, who had frozen in a daze.

“Mm-hmm. I can just repair it~”

“……!”

And at that very moment—

*Ptoo!*

I spat the blood pooled in my mouth into his face.

At the same time, I drove a punch into his body as he instinctively flailed, his face drenched in blood.

Like hammering a nail driven into the ground.

*Kwaang! Grrrrk!*

A heavy crash and tremor swept in all directions. The surrounding ground sank into a vast crater. Inside it, Michael Silbert lay flat on his back, blood pouring from his mouth after my Flame-Extinguishing Divine Fist struck him squarely in the chest.

“Khk, k-kergh……!”

The blood he kept coughing up pooled inside the crater.

The armor he’d been wearing had long since been smashed to pieces. His once-pale skin was stained a dark red with blood and soot.

“……You fucking idiot.”

I smiled bitterly. When I reached out, the shaft of White Flame shot toward me and wrapped itself in my hand.

And without hesitation, I raised the spearhead.

*Whoosh!*
```
