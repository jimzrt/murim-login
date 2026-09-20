<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0565.txt",
      "sha256": "d1300cb9976b0ecdffc4b0f739277e3493be10e031302ff2488d943828c13875",
      "bytes": 14518
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c31017dfaf6eb68d95e8aa8ece9d2357d39be8650df156ceb9f9947228da979b",
      "bytes": 5151
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "18b4513e2e37892789a771bf292e51ac67713436ec4a5feb678475876ac01348",
      "bytes": 179011
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "75a2012e488d4dbf32fbf8e8385cb25237f46afac78c76c653aced80a8adfe37",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "d407495d5065910d35600bab571b793b345cb02cb71eb93861b1c50b7a4d7225",
      "bytes": 898
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4e76041b5a17e52c054b2990af007cddc21994c1d43d062d7fd1525108edae38",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3c4f18c0ba29f9afa8240147682b119bc301931e7a9f279102a3880a80b521c1",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "6cc2f7b1e014ffec8ac5bab0faf98f6c12560297f8c3a708866d358b648e40a0",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3175a14151a938fcf7afb3084d112240ca72b732a8fec068f4d50cff9158a286",
      "bytes": 173325
    }
  ],
  "estimated_tokens": 11756
}
-->

# Durable State Update — Chapter 565

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 565. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 565. Profile updates may replace only one
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
  "chapter": 565,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 565,
    "continuity_sources": [565],
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
    "Magic Johnson's information records at least thirty-two Mutated Gates in the United States during one week, and the true number is likely higher.",
    "The Peace Guild has risen as the only apparent counterweight to Ares Guild; Team Leader Choi is gathering political, business, and Guild allies to strengthen Peace and weaken Ares, with Magic Johnson and the Wizard Guild supporting him.",
    "Team Leader Choi has confirmed that his blood descends from Cheon Taemin, whose legacy gives him exceptional political and social leverage.",
    "The Fire Dragon Pavilion's six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, leadership of the Fire Dragon Pavilion's first mission to Nanman, and the Peace Guild's modern-world patronage.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "Taekyung is in the modern world in early 2047, has entered the Yeokgok Mutated Gate, and has just killed its Orc Lord to rescue an Ares raid team.",
    "Go Jun is Ares Guild's Vice Guild Master and Lee Jungryong's disciple; Jin Taekyung's public exposure of a major Guild's Gate negligence and the Blue House press conference have intensified the threat to Ares, while Go Jun remains determined to kill Jin.",
    "Ares Guild's authority is visibly cracking: about ten members have transferred to Peace Guild, and Go Jun's legitimacy as Lee Jungryong's successor has been publicly undermined.",
    "The secured Peace Guild training room is restricted to Jin Taekyung and selected founding members training in the Jin Family's Cultivation Technique; Magic Johnson has delivered a chip for Team Leader Choi and reported a seven-percent year-over-year rise in worldwide mana levels."
  ],
  "continuity_sources": [
    564,
    563
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What information is stored on Magic Johnson's chip, and what is causing worldwide mana levels to rise?"
  ],
  "safe_through": 564,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 모하비 사막 as Mojave Desert, 애리조나주 as Arizona, 대의 as greater cause, 순수혈통 as pureblood, 국부 as Founding Father, 위저드(Wizard) 길드 as Wizard Guild, 조셉 바이든 as Joseph Biden, 펠릭스 왕자 as Prince Felix, 곽한구 as Gwak Hangu, 역곡 as Yeokgok, 오크의 황무지 as Orc Wasteland, 오크 로드 as Orc Lord, 국회의사당 as National Assembly, 고세원 as Go Se-won, 경호팀장 as Head of Security, A구역 as Section A, 신성불가침 as sacrosanct, 바티칸 as Vatican, 영구 임대 as permanent lease, 혈안 as bloodshot, 매직 존슨 as Magic Johnson, 썩코춘 as Sseokkochoon, and 길드 하우스 as Guild House."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 스위스 | **Switzerland** | Country associated with the watchmaker. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리자몽 | **Charizard** | Joking alternative sobriquet Taekyung imagines for Jeok Cheongang. |
| 화기 | **fire qi** | The fire nature imparted to internal energy by the Fire Gate Divine Technique. |
| 치코리타 | **Chikorita** | Pop-culture reference used in Taekyung’s taunt to the Ent Elder. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 564
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 564
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death and regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 563
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 563
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 564
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃565화



매직 존슨이 떠난 뒤, 연락을 받지 않는 최 팀장에게 문자를 남긴 나는 곧장 길드 하우스 최상층에 마련된 개인 사무실로 향했다.

쾅.

등 뒤로 거칠게 문이 닫히는 소리를 들으며 바닥에 털썩 주저앉았다.

자그마한 책상과 의자 하나가 전부인 백여 평의 공간.

사무실이라 쓰고 연무장(鍊武場)이라 읽는 그곳에서 나는 즉시 스마트폰을 꺼내 칩을 밀어 넣었다.

달칵.

얼마 전에 바꾼 최신형 스마트폰에는 없는 기능이 없었다.

십여 년 전부터 보편화되기 시작한 홀로그램 영상 재생 기능도 그중 하나였다.

지이잉.

미세한 소음과 함께 스마트폰에 장착된 재생기에서 빛이 흘러나온다.

한발 빠르게 허공섭물(虛空攝物)의 수법으로 폐쇄형 커튼을 친 나는 어두운 사무실 내부를 가득 채우기 시작한 홀로그램 영상에 집중했다.

- 치직. 치지직.

노이즈.

- 퍼벙, 콰아아앙!

굉음.

- 취리리리릭!

몬스터의 울음소리와.

- 으아아악!

인간의 비명.

그 모든 것들이 눈앞에서 뒤섞이고, 흩어진다. 크고 작은 텐트와 건물이 늘어선 그곳은 어느덧 참혹한 전쟁터로 돌변해 있었다.

‘변이 게이트.’

자연스럽게 그 다섯 글자가 머릿속을 스친 그때.

- 알라의 이름으로!

- 와아아아!

군용 모자와 터번을 뒤집어쓴 일단의 무리가 악에 받힌 고함과 함께 나아간다.

아랍계로 짐작되는 그들의 전신은 누군가의 붉은 피로 흠뻑 젖었다.

그중에는 기껏해야 초등학생쯤으로 보이는 어린아이까지 포함되어 있었다.

‘어린아이라니…….’

이런 자들이 정규군일 리가 없다.

통일되지 않고 뒤죽박죽인 복장을 봤을 때부터 짐작했던 사실이지만, 그들은 대격변이 시작되기 전부터 중동을 피로 물들인 아랍 반군이 분명했다.

그리고 다음 순간.

- 으아아! 시, 신은 위대하시다!

공포에 질린 꼬마의 외침과 함께, 저마다의 손에 들린 수많은 화기가 불을 뿜었다.

타탕! 투다다다다!

슈우욱, 퍼엉!

평범한 인간이었다면 벌집이 되었을 화력이 단숨에 퍼부어진다. 하지만 그들이 상대하는 적들은 평범하지도 않았고, 인간도 아니었다.

콰아아아!

폭발과 동시에 거대한 화염이 솟구친다.

사방을 가득 채운 검은 연기를 보며 반군들이 거친 숨을 몰아쉬던 그때, 연기가 좌우로 갈라지며 섬광이 번뜩였다.

쉭, 서걱!

단 일격이면 족했다. 반월의 형태로 뻗어나간 검붉은 마력은 막아서는 모든 것을 절단했다.

목, 허리, 가슴. 저마다의 차이는 있었지만, 그 결과는 같았다.

죽음.

촤아아악!

한 박자 늦게 뿜어져 나온 피분수가 모래를 붉게 물들인다.

스물에 달하는 동료들의 처참한 최후를 눈앞에서 목격한 반군들이 눈을 부릅떴다.

- 마, 마수드!

- 신이시여…….

그러나 그들의 신은 모습을 드러내지도, 신도들의 목소리에 응답하지도 않았다.

신을 대신하여 나타난 것은 녹색 피갑을 전신에 두른 괴물이었다.

- 치륵. 치리리릭.

세모꼴의 머리와 파르르 진동하는 두 개의 더듬이. 낫처럼 구부러진 앞다리를 지닌 괴물의 정체는 사마귀였다.

놈은 성인 남성을 내려다볼 만큼 거대했고, 강한 마력을 띤 몸뚱어리에는 앞서 반군들이 퍼부은 화력에도 흠집 하나 없었다.

- 자, 자이언트 맨티스(Giant Mantis)…….

누군가가 신음처럼 중얼거린 그 순간, 거대한 앞다리가 다시 한번 허공을 내리그었다.

후웅, 서걱!

멍하니 얼어붙어 있던 반군의 몸뚱어리가 좌우로 쪼개진다. 앞다리에 실린 마력이 화살처럼 날아가 사방을 찢어발겼다.

서걱! 서걱! 콰아아앙!

인간. 무기. 심지어는 황급히 출동시킨 전차마저 마력을 막아서지 못했다.

사방을 베고 가르는 공격에 폭발음과 비명이 연이어 울려 퍼지고, 어느새 다섯 마리로 늘어난 자이언트 맨티스는 인간들을 향해 뛰어들었다.

- 치치치칫!

- 치리이잇!

퍼석! 촤아악!

기묘한 울음소리가 흘러나올 때마다 백여 명에 달하는 반군들의 사지가 날아가고 피가 튀었다.

신을 부르짖으며 발악하던 자도, 공포에 질려 도망치던 자도 사막에 쓰러져 두 번 다시 일어나지 못했다.

- 으아, 으아아아!

푸욱!

낫 같은 앞다리가 등을 가르고 가슴뼈를 부수었다.

마지막으로 저항하던 반군의 등에 일격을 꽂아 넣은 자이언트 맨티스가 문득 돌아섰다.

얼굴 옆으로 툭 튀어나온 붉은 눈동자가 정확히 화면을 응시한다.

‘카메라를 발견했어.’

놈은 카메라를 봤고, 나는 놈을 봤다.

그리고 이상함을 느낀 자이언트 맨티스가 조심스럽게 카메라를 향해 다가오던 그 순간.

- 신의 불꽃이 이곳에 임할지니. 파이어 레인(Fire Rain)!

화악!

누군가의 창노한 외침. 동시에 마나로 형성된 불덩이 수십여 개가 자이언트 맨티스의 어깨너머로 유성처럼 쏟아졌다.

- 치리리리릿!

기성(奇聲)을 토한 자이언트 맨티스가 불덩이를 향해 자신의 앞발을 휘둘렀다.

꽈앙!

격돌과 함께 화면이, 아니 온 사방이 붉게 물들고. 저 멀리에서 나타난 수십여 명의 헌터가 터져 나가는 불덩이를 뚫고 전장을 질주했다.

- 알라후 아크바르으!

- 신은 위대하시다! 저 악마들을 모조리 죽여라!

- 크륵, 취잇!

인간과 몬스터. 몬스터와 인간.

두 종족은 또 다시 죽고 죽이는 싸움을 시작했다. 그러나 나는 극으로 치닫는 이 전투의 결과를 끝까지 지켜볼 수 없었다.

치직. 치지지직. 팟!

그야말로 찰나의 순간이었다.

극심한 노이즈와 함께 방안을 가득 채우고 있던 홀로그램 영상이 씻은 듯이 사라진 것은.

“……후.”

참았던 숨을 뱉어낸 나는 잠시 내려놓았던 스마트폰을 집어 들었다.

칩 안에 내장된 목록을 확인해 보니 남은 영상이 스무 개가 넘는다.

‘시벌, 지난번에 영상 받은 지 얼마나 됐다고 또.’

전년도 대비 마력 수치 7% 상승.

어느 멍청한 놈들은 ‘고작’이라고 생각할 만한 수치일지도 모르겠다.

하지만 산소 농도가 몇 퍼센트라도 하락하면 난리가 나듯이, 이건 상황이 개판으로 돌아가고 있다는 증거였다.

아니, 어쩌면…….

‘두 번째 대격변의 시작일지도 모르지.’

그리고 남은 영상들을 차례차례 확인할수록, 마음에 품고 있는 불안감은 점차 실체를 지니기 시작했다.

‘유럽. 중동, 서아프리카. 동남아시아…… 무슨 세계 대축제도 아니고.’

이미 전 세계 곳곳에서 동시다발적으로 변화가 일어나고 있었다.

파트라슈가 개껌 물고 뛰어다닐 것 같은 스위스의 푸른 언덕에 신규 게이트가 생성되고, 반군과 정규군이 서로를 향해 포탄을 퍼붓는 동안 방치된 하급 게이트에서는 몬스터들이 쏟아져 나온다.

몇몇 영상에서는 방비가 철저했는지 조기 진압에 성공하기도 했지만, 과반수 이상의 경우에는 상당한 피해를 입은 뒤에야 몬스터를 물리칠 수 있었다.

‘이건.’

영상을 계속해서 돌려보던 나는 문득 미간을 좁혔다.

이와 같은 피해가 단순히 게이트의 방비가 부족했기 때문만이 아니라는 것을 알아차렸기 때문이었다.

그리고 그 순간 찾아온 것은 깨달음뿐만이 아니었다.

띵.

귓가를 파고드는 엘리베이터의 미세한 소음과 함께, 서서히 가까워지는 두 사람의 인기척.

초대하지 않은 불청객들의 정체를 알아차린 나는 손을 뻗었다.

화악.

따스한 바람이 불었다.

손바닥을 타고 흘러나온 기운이 부드럽게 문을 밀어젖히자, 익숙한 얼굴들이 시야에 들어왔다.

“이제 오면 어떡합니까. 문자 보낸 지가 언젠데.”

“죄송합니다. 잠시 연락이 불가능한 상황이었던 터라.”

지각생을 갈구려던 나는 고개를 갸웃거렸다.

“연락이 불가능한 상황? 게이트라도 다녀왔어요?”

“음, 비슷합니다.”

“……맞으면 맞고, 아니면 아닌 거지 비슷한 건 또 뭐야.”

“김 집사님과 잠깐 들를 곳이 있었습니다. 중요한 볼일이라 어쩔 수 없었죠.”

매끄럽게 대답한 최 팀장이 안으로 걸음을 내디뎠다. 자연스럽게 뒤를 따라 들어온 김 집사가 문을 닫으며 가벼운 눈인사를 건넨다.

‘저 양반도 오랜만이네.’

길드에도 통 얼굴을 안 비추던 김 집사와 중요한 볼일이라. 뭘까?

약 일주일 만에 보는 얼굴과 함께 일말의 의문이 남았지만, 지금은 그보다 더 급한 일이 기다리고 있다.

그 사실을 모를 리 없는 최 팀장이 먼저 입을 열었다.

“이 이야기는 뒤로 미루고, 우선 미스터 존슨이 줬다는 정보부터 확인해 봐야겠군요.”

“아, 여기요.”

다시 한번 홀로그램 영상이 흘러나오고 얼마나 시간이 흘렀을까.

모든 영상과 첨부된 자료를 확인한 두 사람의 표정은 딱딱하게 굳어져 있었다.

“전 세계 마력 수치 7% 상승?”

언제나 부드럽던 목소리가 갈라져 나온다. 신음처럼 중얼거린 김 집사가 최 팀장을 향해 고개를 돌렸다.

“도련님.”

“예. 짐작했던 것 이상으로 진행 상황이 빠릅니다. 상황이 심각해요.”

7%면 상승이 아니라, 폭등(暴騰)이라고 부르는 것이 더 어울린다.

그리고 이러한 마력 수치의 급격한 변화는 영상 속에서 특히 두드러졌다.

“몬스터들이…….”

고개를 끄덕인 내가 최 팀장의 말을 받았다.

“예. 존나게 쎄졌어요.”

마력 수치의 상승은, 곧 몬스터의 힘이 강력해진다는 것을 의미한다.

첫 영상에서 자이언트 맨티스가 파이어 레인을 맞고도 그럭저럭 싸우는 것만 봐도 알 수 있는 사실이다.

‘치코리타가 리자몽 불꽃으로 선탠하는 꼴이지.’

엄연히 상성이라는 것이 존재하는 법인데, 상승한 마력 수치와 더불어 강해진 몬스터들은 그 상성을 조금씩 무시하고 있었다.

이런 개 같은 상황이니, 만일을 대비하여 헌터라는 귀한 인력을 최소한으로 운용하던 곳은 속수무책으로 무너질 수밖에.

지금 상황을 요약하자면 한마디로…….

“좆 됐습니다. 지금 개판 오 분 전이에요.”

미쳐 버린 진행 속도다. 이대로라면 당장 올해 연말쯤에는 일기 예보에 몬스터가 등장할지도 모른다.

미인 기상 캐스터 누나가 코딱지만 한 한반도 지도를 짚으며 조목조목 알려 주는 거지.

- 내일 강원도 철원에는 폭설 대신 고블린이 내릴 예정입니다. 20m 높이까지 쌓일 테니, 주민분들은 방패와 해독제를 챙겨 얼른 대피하세요.

“…….”

시벌, 폭설도 짜증 나는데 폭몬 실화냐.

하늘에서 펑펑 내려오는 몬스터라니, 생각만 해도 가슴이 옹졸해진다.

물론 나도 그때까지 손가락 빨면서 놀고 있지만은 않을 거다. 무슨 수를 써서라도 대한민국의 헬반도화를 막아야 한다.

‘만일을 대비해서 염두에 두긴 했지만…… 지금의 진행 속도는 확실히 너무 빨라.’

조금은 시간 여유가 있다고 생각했는데, 무림에서부터 조금씩 계획하던 ‘그 일’을 보다 앞당겨야 한다는 생각에 마음이 무거워진 그때였다.

“이 정도라면 더는 숨길 수도 없겠군요.”

홀로그램 영상을 끈 최 팀장이 가라앉은 목소리로 말을 이었다.

“국가 차원에서 은폐할 수 있는 한계는 이미 지났습니다. 여기서 더 늦게 알려진다면 혼란만 가중될 뿐이에요.”

이번 사태는 한 번 지나가는 파도가 아니라, 도시까지 쓸어 버릴지도 모르는 쓰나미다.

한숨을 내쉰 내가 입을 열었다.

“최 팀장님은 어떻게 할 생각이에요?”

“지금 당장은 게이트 방비가 최우선입니다. 쓰나미가 덮치기 전에 방파제를 세워야죠.”

“게이트 방비를 강화한다?”

“그렇게 되면 레이드 인력이 줄어들고, 우리 평화 길드가 가진 모든 게이트를 제대로 활용할 수 없겠죠. 하지만 저도 무엇이 우선인지는 압니다.”

“그거 다행이네요.”

듣던 중 반가운 소리에 피식 웃음이 나왔다.

확실히 최 팀장은 정도라는 것을 지킨다. 아레스 길드를 집어삼키겠다는 큰 야망을 갖고 있으면서도, 앞으로 나갈 때와 설 때를 아는 사람인 것이다.

‘그게 이정룡과의 가장 큰 차이점이기도 하지.’

마음속으로 뇌까린 내가 재차 입을 열었다.

“그럼 우선 게이트에 신경을 기울여야겠네요. 아쉽지만 아레스 길드 관련해서는 잠시 뒤로…….”

“진태경 씨.”

“예?”

어느새 최 팀장의 투명한 눈동자가, 나를 똑바로 응시하고 있었다.

“저는 게이트 방비를 최우선 목표로 삼겠다고 했지, 아레스 길드에 관련된 일을 뒤로 미룬다고 말한 적은 없습니다.”

“……!”

뭐라고?

나도 모르게 눈을 크게 뜬 그 순간, 최 팀장의 목소리가 이어졌다.

“말씀드렸잖습니까. 앞서 중요한 볼일이 있었다고요.”

“그럼 그 중요한 볼일이라는게……?”

“아레스 길드의 주요 인물입니다. 과거 제 외할아버님을 도와 대격변을 잠재운 전쟁 영웅이었고, 한때 이정룡이 가장 신임하던 친구였으며, 지금은 석고준을 위협하는 가장 큰 내부 파벌의 수장이기도 하죠.”

어느 때보다 부드러운, 그러나 가시를 숨긴 목소리가 귓가를 파고들었다.

“모든 것은, 내부에서부터 무너지는 법입니다.”
```

## Final English reading copy

```markdown
# Chapter 565

After Magic Johnson left, I sent a text to Team Leader Choi, who still wasn’t answering, then headed straight for the private office on the top floor of the Guild House.

*Bang.*

Hearing the door slam shut behind me, I dropped heavily onto the floor.

It was a space of over a hundred pyeong, but all it contained was a small desk and a single chair.

The place was called an office, but it was really a training ground. I immediately took out my smartphone and inserted the chip.

*Click.*

The latest model I had bought a while ago had every feature imaginable.

That included holographic video playback, which had begun to spread throughout society more than a decade ago.

*Bzzzz.*

Light flowed out of the player mounted on the smartphone with a faint hum.

I quickly used Seizing an Object Through Empty Space to draw the blackout curtains, then focused on the holographic footage beginning to fill the dark office.

*Crackle. Crackle.*

Noise.

*Boom! Kraaang!*

A deafening roar.

*Shrieeeek!*

A monster’s cry.

“Aaaah!”

A human scream.

All of it mixed together before my eyes, then scattered. The place, lined with large and small tents and buildings, had suddenly transformed into a horrific battlefield.

*Mutated Gate.*

Those five syllables naturally flashed through my mind.

Then—

“In the name of Allah!”

“Waaaaah!”

A group wearing military caps and turbans advanced with desperate shouts.

Their bodies, presumably Arab, were soaked in someone else’s red blood.

Among them was even a child who looked no older than an elementary school student.

*A child…*

There was no way people like these were regular soldiers.

I had suspected as much from their mismatched, chaotic clothing, but they were clearly Arab rebels—the same kind who had stained the Middle East with blood even before the Great Cataclysm began.

And then—

“Aaaah! G-God is great!”

Along with the terrified cry of a little boy, countless firearms in their hands opened fire.

*Rat-tat-tat-tat!*

*Whoosh! Boom!*

A torrent of firepower that would have turned ordinary humans into pincushions poured forth all at once.

But their enemies were neither ordinary nor human.

*Kraaang!*

A massive blaze rose with the explosion.

The rebels were panting roughly as they stared at the black smoke filling every direction.

Then the smoke split apart, and a flash of light gleamed.

*Whoosh. Shing!*

A single strike was enough.

Dark red mana shot outward in the shape of a crescent moon, cutting through everything in its path.

Necks, waists, chests. The exact wounds differed, but the result was the same.

Death.

*Splaaash!*

A moment later, fountains of blood erupted and stained the sand red.

The rebels stared wide-eyed at the horrific deaths of nearly twenty comrades before them.

“M-Masoud!”

“My God…”

But their god neither appeared nor answered the voices of his worshippers.

What appeared in his place was a monster covered from head to toe in green armor.

*Chirr. Chiriririk.*

With a triangular head, two trembling antennae, and forelegs curved like scythes, the monster was a mantis.

It was so enormous that it could look down at an adult man. Its body radiated powerful mana, yet it did not have a single scratch from the firepower the rebels had just unleashed.

“G-Giant Mantis…”

The instant someone muttered the name like a groan, the enormous foreleg once again swept down through the air.

*Whoom. Shing!*

The body of a rebel who had frozen in place was split in two.

The mana infused into the foreleg flew outward like arrows, shredding everything around it.

*Shing! Shing! Kraaang!*

Humans. Weapons. Even the tanks hurriedly sent into battle could not withstand the mana.

Explosions and screams rang out in succession as the attack cut through everything in every direction.

Before long, the number of Giant Mantises had increased to five, and they leaped toward the humans.

*Chit-chit-chit!*

*Chiriiit!*

*Crack! Splaaash!*

Whenever the strange cries rang out, the limbs of rebels numbering over a hundred went flying, and blood sprayed through the air.

Those who struggled while screaming for their god and those who fled in terror alike collapsed onto the desert sand, never to rise again.

“Aaah! Aaaaah!”

*Thud!*

A scythe-like foreleg slashed through the rebel’s back and shattered his breastbone.

The Giant Mantis that had driven its strike into the back of the last resisting rebel suddenly turned around.

A red eye protruding from the side of its face stared directly at the screen.

*It found the camera.*

It saw the camera, and I saw it.

Then, just as the Giant Mantis sensed something strange and cautiously began approaching the camera—

“May the flames of God descend upon this place. Fire Rain!”

*Fwoosh!*

An aged voice shouted. At the same time, dozens of fireballs formed from mana poured down like meteors over the Giant Mantis’s shoulder.

*Chiririririt!*

The Giant Mantis let out a strange cry and swung its foreleg at the fireballs.

*Boom!*

At the moment of impact, the screen—or rather, the entire room—was dyed red.

From far away, dozens of Hunters appeared and sprinted across the battlefield through the fireballs bursting around them.

“Allahu Akbar!”

“God is great! Kill every one of those devils!”

*Krrk, chiiit!*

Humans and monsters.

Monsters and humans.

The two species began killing one another once again.

But I couldn’t watch the outcome of this battle all the way to the end.

*Crackle. Crackle. Pop!*

It happened in the blink of an eye.

The holographic footage that had filled the room vanished without a trace amid a burst of intense static.

“…Whew.”

I exhaled the breath I had been holding and picked up the smartphone I had set aside.

When I checked the list stored on the chip, I found that more than twenty videos remained.

*Fuck. How long has it even been since the last time I got a batch of videos? And there are already more.*

Worldwide mana levels had risen by seven percent compared to the previous year.

Some idiots might think that was *only* seven percent.

But just as the world would be thrown into chaos if the oxygen concentration dropped by even a few percentage points, this was proof that things were going to hell.

No.

Maybe…

*This could be the beginning of the second Great Cataclysm.*

And the more I checked the remaining videos one after another, the anxiety I carried inside began to take shape.

*Europe. The Middle East. West Africa. Southeast Asia… What is this, some kind of worldwide festival?*

Changes were already taking place simultaneously all over the world.

A new Gate appeared amid the green hills of Switzerland, where you could imagine Patrache running around with a dog biscuit in his mouth.[^1]

While rebels and regular soldiers bombarded one another, monsters poured out of low-rank Gates that had been left unattended.

Some of the videos showed places where the defenses had been thorough enough to suppress the situation early.

But in more than half of them, the monsters could only be defeated after causing considerable damage.

*This…*

I continued replaying the videos, then suddenly furrowed my brow.

I had realized that the damage was not simply the result of inadequate Gate defenses.

And at that moment, more than insight came to me.

*Ding.*

Along with the faint sound of the elevator entering my ears, I sensed the presence of two people slowly drawing closer.

I recognized the identities of the uninvited guests and reached out.

*Fwoosh.*

A warm breeze blew through the room.

The qi flowing from my palm gently pushed the door open, bringing familiar faces into view.

“What took you so long? It’s been ages since I texted you.”

“I apologize. I was in a situation where I couldn’t receive any messages for a while.”

I had been about to chew out the latecomers, but I tilted my head.

“You couldn’t receive any messages? Did you go to a Gate or something?”

“Something like that.”

“…Either it happened or it didn’t. What does ‘something like that’ even mean?”

“There was somewhere I needed to stop by with Butler Kim. It was an important errand, so it couldn’t be helped.”

Team Leader Choi answered smoothly as he stepped inside.

Butler Kim followed naturally behind him, closing the door and giving me a slight nod.

*I haven’t seen that guy in a while.*

Butler Kim had hardly shown his face at the Guild lately. What kind of important errand had brought him here with Team Leader Choi?

Seeing him again after about a week left me with a lingering question, but something more urgent was waiting.

Team Leader Choi obviously knew that as well, because he spoke first.

“We can discuss this later. For now, we should check the information Mr. Johnson gave us.”

“Oh. Here.”

The holographic footage began playing again.

After some time had passed, the expressions of the two men who had checked every video and its attached materials had hardened.

“Worldwide mana levels up seven percent?”

Butler Kim’s usually gentle voice came out cracked.

He muttered the words like a groan, then turned toward Team Leader Choi.

“Young Master.”

“Yes. It’s progressing faster than we anticipated. The situation is serious.”

Seven percent could not be called a rise. A surge—or even a skyrocketing increase—would have been more appropriate.

And that sharp change in mana levels was especially obvious in the footage.

“The monsters…”

I nodded and picked up Team Leader Choi’s words.

“Yeah. They’ve gotten fucking strong.”

A rise in mana levels meant that monsters were becoming stronger as well.

The Giant Mantis holding its own even after being hit by Fire Rain in the first video was proof enough.

*It was like watching Chikorita get a tan from Charizard’s flames.*

Type advantages were supposed to exist for a reason, but along with the rise in mana levels, the strengthened monsters were gradually beginning to ignore them.

With things this fucking bad, places that had been deploying the bare minimum of precious Hunter manpower as a precaution had no choice but to collapse helplessly.

To sum up the current situation in one phrase…

“We’re fucked. We’re five minutes from total chaos.”

The pace of this madness was incredible.

If things continued like this, monsters might start appearing in the weather forecast by the end of the year.

Some beautiful weathercaster lady would point to a map of the Korean Peninsula no bigger than a booger and explain everything in detail.

“Tomorrow, goblins are expected to fall in Cheorwon, Gangwon Province, instead of heavy snow. They’re expected to pile up to a height of twenty meters, so residents should grab their shields and antidotes and evacuate immediately.”

“…”

*Fuck. Snow is annoying enough, and now monsterfall is for real?*

Monsters raining down from the sky.

Just imagining it made my heart shrivel.

Of course, I wasn’t going to sit around twiddling my thumbs until then. I had to stop Korea from becoming a hellish peninsula, no matter what it took.

*I had kept it in mind as a possibility, but… the situation is definitely progressing too quickly.*

I had thought we still had a little time.

But the realization that I needed to bring forward *that thing*—the plan I had been working on little by little ever since Murim—made my heart heavy.

That was when Team Leader Choi spoke.

“At this point, we can no longer keep it hidden.”

He turned off the holographic footage and continued in a subdued voice.

“We have already passed the limit of what can be concealed at the national level. If we wait any longer to announce it, we will only increase the confusion.”

This was not a wave that would simply pass.

It was a tsunami that might sweep away entire cities.

I sighed and opened my mouth.

“What are you planning to do, Team Leader Choi?”

“For now, reinforcing Gate defenses is our top priority. We need to build a breakwater before the tsunami hits.”

“Strengthen the Gate defenses?”

“If we do that, our raid personnel will decrease, and we won’t be able to make full use of every Gate owned by Peace Guild. But I know what needs to come first.”

“That’s a relief.”

I let out a quiet laugh at the welcome news.

Team Leader Choi definitely stuck to what was right.

Even though he had the grand ambition of swallowing up Ares Guild, he was someone who knew when to move forward and when to stand still.

*That’s also the biggest difference between him and Lee Jungryong.*

I muttered to myself and spoke again.

“Then we should focus on the Gates for now. It’s unfortunate, but we’ll have to put matters concerning Ares Guild on hold for a while…”

“Mr. Jin Taekyung.”

“Yes?”

By then, Team Leader Choi’s clear eyes were staring straight at me.

“I said that I would make Gate defenses my top priority. I never said I would put matters concerning Ares Guild on hold.”

“…”

*What?*

I involuntarily widened my eyes, and Team Leader Choi’s voice continued.

“I told you, didn’t I? I had an important errand to take care of first.”

“Then that important errand was…?”

“One of Ares Guild’s major figures. He was a war hero who helped my maternal grandfather suppress the Great Cataclysm in the past, once the friend Lee Jungryong trusted most, and is now the head of the largest internal faction threatening Go Jun.”

His voice was gentler than ever, but there were thorns hidden beneath it.

“Everything crumbles from the inside.”

[^1]: Patrache is the dog from the story commonly known in Korea as *A Dog of Flanders*.
```
