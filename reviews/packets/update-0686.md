<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0686.txt",
      "sha256": "4c4a37d71fe3d35e4872765b4824a0028a31d64fdb687802b005d4f4294d6387",
      "bytes": 13199
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "35b31e002892e51fdb828e0c4df76504308c2aa9c9961dbcba719129388af679",
      "bytes": 1366
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3cebb0a6157c00730724eece50a5c1b04414d933259d1af6c6a1c1d082598409",
      "bytes": 203985
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "8d4d18b3fbd702265a6d47fd42e58a3cb06c180bd21a7789d1541ead29c1f49b",
      "bytes": 980
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "2e8ab3d0c0c4f502b4125dc32e3c8cb9e17210eb80808106f0b6cd6386547a97",
      "bytes": 830
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "a67134c508336a258446697dd86dcca62a5c3b91e75dc2e40304c51cf8d7fe49",
      "bytes": 788
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4b8f1d182ff3217dc755fd07498aa9329a3cd2a139d312f1d5f8e46a83e04fd9",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "e7453cf1b2f6195f5789f00b460f45c047eaef98a33dcfc3a426d7f320857c00",
      "bytes": 705
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "14f6c248aeb137f901979604a720857f69412e89eab509bbc45710404af1fa6e",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4c9f0012391e16ee7fa359d1e557399533aa9896aca7c390f3c8301d53d5dff6",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "c2f86b14afcd331e029420b9ded87d0ef54a82e3e355193242bf02af761ddd2d",
      "bytes": 613
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "794aa7cb1e2f4d8f9bea7c236f6061953519661a87f34e7f1591cac2686406bd",
      "bytes": 678
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c732c6e0b915fb40ebc0712e4137a1d00d0de261ab8f5e3a98f70aa047ca1d3f",
      "bytes": 211718
    }
  ],
  "estimated_tokens": 11934
}
-->

# Durable State Update — Chapter 686

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 686. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 686. Profile updates may replace only one
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
  "chapter": 686,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 686,
    "continuity_sources": [686],
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
    "The Great Snow Fiend, Hanbaek, is dead.",
    "Jin remains critically injured after killing Hanbaek and is rapidly losing blood and strength.",
    "Jin summoned the Water God Dragon's Origin Essence, whose water qi conflicts dangerously with his Scorching Yang Qi.",
    "Jin was about to consume the Origin Essence when Muyaho returned with Heugung and Yohi.",
    "The Quest to find Yohi was completed, granting EXP, Fame, and a level-up.",
    "Jin sensed death receding and warmth surrounding him before losing consciousness.",
    "The Fire Dragon Armor remains partially destroyed and requires three days to repair."
  ],
  "continuity_sources": [
    685
  ],
  "open_questions": [
    "Will the Water God Dragon's Origin Essence save Jin or kill him because of its incompatibility with his Scorching Yang Qi?",
    "What is the condition of Heugung and Yohi after returning with Muyaho?",
    "What will happen to the Fire Dragon Armor while Jin is incapacitated?"
  ],
  "safe_through": 685,
  "temporary_decisions": [
    "Render 한백 as Hanbaek and identify him as the Great Snow Fiend's personal name.",
    "Render 수신룡의 원정 as Water God Dragon's Origin Essence.",
    "Render 광염 as light-flames.",
    "Render 회광반조 as final rally.",
    "Render 칠공 as seven apertures."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 문주     | **Sect Leader**                              |
| 상태               | **Status**                     |
| 도사      | **Daoist**                                                      |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 외공 | **external arts** | Martial arts focused on extreme bodily training. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 복마전 | **demon-slaying battleground** | A possible description for Sichuan if Dark Heaven attacks it. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |
| 요서부 | **Western Yao Estate** | Estate inherited by Yohi when she became a Great Chieftain. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 흑수 | 요희 | hostile captor to captive | little bitch / little girl | cruel, mocking, and predatory | Black Hand taunts Yohi, threatens her life, and says the Demon Empress covets her. |
| 요희 | 흑수 | captured tribal chieftain to torturer | you | terrified and pleading | Yohi recognizes Black Hand as the Fiend who attacked her warriors and maimed Heugung. |
| 진태경 | 흑수 | hostile_martial_opponent | Black Hand | mocking and profane | Jin sarcastically addresses Black Hand after hearing his sobriquet. |
| 흑수 | 진태경 | hostile_Dark_Heaven_agent_to_enemy_martial_artist | Blazing Flame Divine Dragon Jin Taekyung | taunting and murderous | Black Hand identifies Jin while claiming that killing him will make the sobriquet famous. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 679
- **Aliases:** None
- **Role:** Baeksang is the temporary Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the leader of Nanman's general mobilization, with nearly ten thousand troops stationed in the Inner Palace.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 679
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 685
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand was a sadistic Dark Heaven agent and Supreme Peak master who acted under orders associated with the Southern Heaven Demon Empress before his death.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand was the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; the Great Snow Fiend was his senior and could overrule him under the Southern Heaven Demon Empress's orders.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 685
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 685
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; Black Hand captured him and Yohi, and by the end of Chapter 685 he has returned with Yohi on Muyaho to find Jin.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 685
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 685
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 685
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 685
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people and seeks to unite Nanman's four great tribes under Yao leadership; she manipulated Heugung while following Baeksang and deliberately suppressed suspicions about his Dark Heaven ties before returning with Heugung on Muyaho to find Jin Taekyung.

## Korean source

```text
＃686화



진태경이 기절하듯 깊은 잠에 빠진 것과 바람처럼 질주하던 무야호의 발걸음이 멈춘 것은 거의 동시였다.

툭.

부서진 바위에 등을 기댄 채 힘없이 꺾이는 고개.

그 모습을 목격한 요희가 헛숨을 삼킨 그때, 한발 빠르게 무야호의 등에서 내린 흑웅이 진태경의 맥을 확인하고 한숨을 내쉬었다.

“후우. 다행히 아직 살아 있소.”

희소식이었지만 요희의 안색은 밝아지지 않았다.

“아직, 이라고요?”

그제야 자신의 말실수를 알아차린 흑웅이 정정했다.

“다급한 마음에 실언을 했구려. 생사를 헤맬 정도는 아니니 크게 걱정할 필요는 없을 것 같소.”

“생사를 헤맬 정도가 아니라니, 저 상태가요?”

요희의 의문은 결코 과한 것이 아니었다.

현재 진태경은 머리부터 발끝까지 핏물로 흠뻑 젖어 있었고, 전신의 옷자락은 찢기고 베인 흔적이 가득했으며, 상반신에 걸쳐져 있는 정체불명의 갑옷은 무언가에 관통당한 것처럼 가슴 부위가 부서져 있었으니까.

되려 살아 있다고 생각하는 것이 이상할 정도의 모습.

그러나 요희의 의문이 당연한 것처럼, 흑웅의 말 또한 틀림없는 사실이었다.

“직접 살펴본 바에 의하면 그가 입은 부상은 우리가 생각하는 것만큼 심각하지 않소. 허나 이 흔적들은…… 나 역시 보면서도 쉽게 믿어지지 않는구려.”

비록 지금은 공력이 금제당했다고는 해도 두 사람 역시 절정의 경지에 오른 무인이다.

두 대족장은 자신들이 파악한 상흔(傷痕)과 상반된 진태경의 상태에 의문을 품긴 했지만, 진태경이 경각을 다투지 않는다는 사실에 안도의 한숨을 내쉬었다.

그리고 안도가 채 사라지기도 전에, 그가 등을 기대고 있던 거대한 바위에 처박혀 있던 한 사람을 발견하고 경악했다.

“흡.”

짧은 비명을 삼킨 요희는 다음 순간 깨달았다. 두 눈을 부릅뜬 채 굳어 버린 저 정체불명의 노인은 이미 숨이 끊겼다는 것을.

새하얀 창날에 의해 관통당한 목에서는 지금도 핏물이 흐르고 있었다.

툭. 투두둑.

진태경과 마찬가지로 혈인과 같은 몰골을 한 노인을 바라보던 요희가 문득 중얼거렸다.

“그 사람이군요.”

“누굴 말하는 거요?”

“흑수(黑手), 그 늙은이를 아랫사람 대하듯이 굴었던 목소리의 주인이요.”

“아.”

“그리고 아마 제 짐작이 맞다면…….”

빠르게 주위를 훑던 요희의 시선이 멈춘 곳에, 흑수권마의 시신이 있었다.

실로 악귀와도 같은 무위로 요서부의 전사를 학살하던 그는 가슴이 뻥 뚫린 채 죽어 있었다.

‘이건 말도 안 돼.’

요희의 눈썹이 파르르 떨렸다.

조금 전 이름을 알 수 없는 노인의 시체를 발견했을 때부터 설마 했지만, 지금 이 상황은 그녀의 예상을 아득하게 벗어났다.

아니, 그것은 비단 요희 혼자만의 생각이 아니었다.

“도대체 어떻게…….”

낮게 뇌까리던 흑웅은 뒷말을 삼켰다.

도저히 이해할 수 없는 일이었으나, 지금 그들의 눈 앞에 펼쳐진 광경은 엄연한 현실이었으니까.

미증유(未曾有)의 거력에 의해 초토화된 사방. 숨이 끊긴 채 쓰러진 두 노인과 홀로 깊은 잠에 빠진 한 청년.

이것을 통해 나온 결론은 명백했다.

진태경은 싸웠고, 승리했다. 그것도 자신보다 몇 배나 많은 인생을 무공에 바친 두 초절정 고수를 상대로.

“……열화신룡(烈火神龍).”

붉은 입술 사이로 신음처럼 흘러나온 네 글자의 별호. 진태경을 바라보는 요희의 눈동자에 경외가 깃들었다.

이러한 일이 가능한가에 대해서는 더 이상 중요하지 않았다.

진태경은 불가능을 가능으로 만들었고, 남방 이민족에 불과한 자신들을 구하고자 기꺼이 목숨을 걸었으니까.

그러니 이제는, 자신들이 그를 위해 움직여야 한다.

‘이미 너무 늦었을지도 모르지만, 지금이라도.’

남만의 어떤 독물은 특정한 시기마다 허물을 벗는다.

이른바 탈각(脫殼)이라 불리는 행위가 그것이다.

하지만 새로운 몸을 얻는 것이 어찌 쉬울 수 있을까. 탈각에 성공한다면 더욱 아름답고 강해진 몸을 얻을 수 있겠지만, 만약 실패한다면 늙고 병든 몸으로 서서히 죽어 간다.

그리고 요희가 택한 길은 전자였다.

‘더 지체한다면 전부 끝장이야. 어떻게든 이 사실을 사람들에게 알려야 해.’

지금이라도 백상과 관련된 흉계를 밝히고 암천을 저지해야 한다.

그 과정에서 요희가 저지른 과오(過誤) 역시 드러나겠지만, 그녀는 이미 마음의 결정을 내린 상태였다.

자신이 택한 길에 대한 모든 대가를 감수하기로.

‘그러지 말았어야 했는데.’

돌이켜 생각해보면 후회뿐이다.

백상은 요희에게 넓고 아름다운 비단길을 깔아 주었고, 그녀는 주위에서 벌어지는 모든 일을 묵인하며 비단길을 따라 이곳까지 왔다.

하지만 끝에 다다라 문득 밑을 내려다보니 요희의 발은 어느덧 피투성이가 되어 있었다.

그녀의 피가 아닌, 다른 남만인들이 흘린 피였다.

이제는…… 그 피를 닦고 싶다. 닦을 수 없다면 발을 잘라서라도.

그리고 요희가 이런 결심을 내리기까지는, 한 사람의 존재가 큰 영향을 미쳤다.

‘진태경.’

낯선 땅에서 온 이방인.

그러나 그는 누구보다 더 남만을 위해 싸웠다. 수백 년 전, 이제는 전설로 남은 열화문의 옛 문주가 그러했듯이.

‘명색이 대족장인데, 한족보다 못할 수는 없지.’

나 같은 년도 대족장이라고 할 수 있다면.

자조 섞인 뒷말을 삼킨 요희는 즉시 행동에 나섰다.

찌익. 새하얀 섬섬옥수가 한 치의 망설임도 없이 화려한 궁장을 잡아 뜯는다.

금은으로 치장된 장신구도 떼어 내고 팔과 다리를 드러낸 그녀의 모습에, 흑웅의 눈동자가 커졌다.

“요희.”

“더 말할 시간 없어요. 지금 당장 움직여야 해요.”

잠시 말없이 요희를 응시하던 흑웅이 고개를 끄덕였다.

“옳은 말이오. 언제 다른 적들이 몰려올지도 모르니.”

“지금까지 주위가 잠잠한 걸 보면 다른 적들은 없다고 봐도 무방해요. 아니, 초절정 고수가 둘이나 있으니 암천으로서도 더 이상의 지원은 필요 없다고 생각했겠죠.”

“그렇겠지. 놈들은 이미 당신이 지닌 추종향(追蹤香)의 존재를 알고 있었고, 우리를 미끼 삼아 야율 궁주를 끌어들일 생각이었을 거요. 암천에게 있어 현재 가장 큰 걸림돌은 바로 그였을 테니까.”

그러나 미끼를 문 것은 야수묘왕이 아닌 진태경이었고, 사냥을 준비하고 있던 사냥꾼들은 되려 그에게 사냥당했다.

그 누구도, 심지어는 암천도 예측하지 못했을 상황.

하지만 이야기가 이어질수록 요희의 마음은 무거워졌다.

“한데 만약 진태경이 궁주님을 대신해서 온 것이 아니라…… 궁주님께서 오지 못할 상황에 처한 거라면요?”

“그건…….”

“제 부족민들이, 요서부가 몰살당했어요. 유례없는 사상 초유의 사건이니 아마 지금쯤이면 내궁도 난리가 났겠죠.”

“그러니 한시라도 빨리 내궁으로 가야 하지 않겠소?”

요희는 흑웅의 말에 말없이 고개를 저었다. 야망을 위해 눈과 귀를 막았을 뿐, 그녀는 바보가 아니었다.

야수묘왕의 의형제인 백상을 포섭하여 수십여 년간 때를 기다린 암천이다.

그녀는 문득 바위를 관으로 삼아 죽어 있는 저 정체불명의 노인이 했던 말을 떠올렸다.



‘대계(大計)를 코앞에 두고 경거망동했다가는 내가 용서치 않을 것이다.’



대계. 분명 대계라 했다.

요희는 저 두 글자에서 이루 말할 수 없는 위험과 불안감을 느꼈고, 자신들을 납치한 것 역시 치밀하게 계산된 행동이라는 것을 깨달았다.

몰살당한 요서부. 혼란에 휩싸였을 내궁. 궁주에게 비견되는, 혹은 그 이상의 지지 세력을 구축한 백상.

그리고 이 모든 것을 계획한 암천.

답을 찾는 것은 그리 어려운 일이 아니었다.

“요희?”

흑웅의 부름에 퍼뜩 상념에서 깨어난 요희는 입술을 깨물었다.

만약, 만약 지금 머릿속에 떠오른 이 생각이 맞다면…… 현재 내궁은 복마전(伏魔殿)이나 다름없다. 온갖 악귀와 흉계가 도사린.

“우리는 내궁이 아니라, 서쪽으로 가야 해요.”

“서쪽이라면 혹시.”

“네. 보산(保山)으로 갈 생각이에요.”

각 부족은 남만 땅 전체에 퍼져 살고 있지만, 본거지는 존재한다. 그중에서도 보산은 족히 수천에 달하는 요족이 정착한 땅이었다.

“지금쯤이면 암천과 손잡은 백상이 내궁을 장악했을 거예요. 그를 부족장들과 대회의의 결정이라면 궁주님도 어찌할 수 없었겠죠.”

“음.”

“제 말을 믿으세요. 지금 내궁으로 향하면, 아니 내궁에 들어서기도 전에 제거되고 말 테니까.”

흑웅은 깊게 가라앉은 눈동자로 요희를 응시했다.

“만약 보산으로 향한다면?”

“전 요족의 대족장이에요. 더 이상 말이 필요한가요?”

“동원할 수 있는 전사의 숫자가 얼마나 되오?”

“최대한 끌어모은다면 일천. 암천을 등에 업은 백상과 맞서기에는 턱없이 부족하지만, 과연 그들이 이 상황을 알고도 백상을 따를지 모르겠네요.”

“틀림없이 민심(民心)이 흔들리고, 전사들이 이탈하겠지.”

“각 부족과 마을에 전서구를 띄우고 전령을 보낼 거예요. 늦어도 칠 주야. 그 안에 남만 전체가 백상의 만행을 알게 되겠죠.”

거침없이 말을 이어 가는 요희의 모습에, 흑웅이 나직한 탄성을 흘렸다.

“과연 영민하구려. 내가 알고 있던 그대보다 더.”

그 말에 요희는 잠시 상황을 잊고 실소를 흘렸다.

“당신한테 들으니 기분이 이상하네요. 완전히 다른 사람으로 변했으면서.”

“어쩔 수 없었소. 백상의 이목을 피하기 위해서는 나 자신부터 숨겼어야 했으니까.”

담담하게 대답한 흑웅이 무언가를 건넸다. 누런 면지에 쌓인 그것은 둥그런 단환이었다.

“드시오.”

“이건…….”

“흑수권마가 지니고 있던 해약(解藥)이오. 조금 전 그의 품을 뒤지다가 발견했지. 지금처럼 공력이 금제 당한 상황에서는 보산에 다다르기도 전에 백상이 보낸 전사들에게 추살 되고 말 거요.”

흑웅의 말은 정확했다. 아무리 뛰어난 전사라 해도 외공(外功)을 익히지 않는 이상 추격대를 뿌리칠 수 없다. 하물며 요희의 무위는 그리 높은 편이 아니었다.

스륵.

요희는 사양하지 않고 단환을 씹어 삼켰다.

씁쓸한 맛에 절로 미간이 찡그려졌지만, 제대로 된 반항 한 번 못 해 보고 죽는 것보다는 백번 낫다.

“보산까지 어느 정도 시일이 걸릴까요? ”

“우리가 있는 이곳이 애뇌산이니…… 사나흘 정도면 족할 것 같소. 우선 이 독혈지를 빠져나가는 것이 우선이겠지만.”

그들은 오는 길에 난생처음 보는 독물들과 극독으로 이루어진 늪을 보았고, 이미 자신들의 위치를 파악한 후였다.

“그때쯤이면 그도 깨어나겠군요.”

“그래, 그렇겠지. 깨어나기만 한다면 천군만마가 될 거요.”

나직하게 대답한 흑웅이 진태경의 신형을 들쳐 엎자, 죽은 흑수권마의 얼굴에 오줌을 갈기고 있던 무야호가 달려와 등을 내밀었다.

- 크릉.

낮은 울음소리를 흘리는 백호의 청백색 눈동자를, 흑웅은 물끄러미 바라보았다.

“참으로 희한하지 않소?”

“네?”

“소궁주가 부리는 이 녀석 말이오. 내궁에서 종종 마주칠 때마다 내게는 늘 이빨을 드러내더니, 진태경이 옆에 있는 지금은 순한 양이 따로 없구려.”

“그에게는 스스로 마음을 연 거겠죠. 예로부터 영물은 사람을 알아본다고 하니까.”

무심코 대답한 요희가 문득 이상함을 느낀 그때, 흑웅이 피식 웃었다.

“그래, 그 말이 맞는 것 같소.”

퍼걱! 쿵.

핏물이 튀고, 커다란 은빛 동체가 기울었다. 그 광경을 멍하니 바라보는 요희의 귓가에, 흑웅의 목소리가 닿았다.

“말하지 않았소. 나 자신부터 숨겼어야 했다고.”
```

## Final English reading copy

```markdown
# Chapter 686

Jin Taekyung’s plunge into a deep sleep that was almost like unconsciousness and Muyaho’s halt after racing like the wind occurred almost simultaneously.

THUD.

His head drooped weakly as he leaned his back against a shattered boulder.

Yohi swallowed a sharp breath at the sight. Heugung had already climbed down from Muyaho’s back and was checking Jin Taekyung’s pulse.

He let out a sigh.

“Whew. Fortunately, he’s still alive.”

It was good news, but Yohi’s complexion did not brighten.

“Still?”

Only then did Heugung realize his mistake and correct himself.

“I misspoke in my haste. He doesn’t seem to be at the point of hovering between life and death, so I don’t think you need to worry too much.”

“Not at the point of hovering between life and death? In that condition?”

Yohi’s doubt was hardly excessive.

Jin Taekyung was currently drenched in blood from head to toe. His clothes were covered in tears and cuts, while the unidentified armor draped over his upper body had been shattered around the chest as though something had pierced straight through it.

He looked so bad that it was strange to think he was alive at all.

Yet just as Yohi’s question was reasonable, Heugung’s words were also an undeniable fact.

“Having examined him directly, I can say that his injuries aren’t as serious as we thought. However, these marks… Even I find them difficult to believe, despite seeing them with my own eyes.”

Although their internal energy had been sealed for the time being, both of them were martial artists who had reached the Peak realm.

The two Great Chieftains found Jin Taekyung’s condition difficult to reconcile with the wounds they had identified, but they still let out relieved sighs at the fact that he was not hovering on the brink of death.

Before that relief had even faded, however, they discovered someone embedded in the massive boulder Jin had been leaning against—and were stunned.

“Hup.”

Yohi swallowed a short cry and realized it the next moment.

The unidentified old man, frozen in place with his eyes wide open, was already dead.

Blood was still flowing from his throat, which had been pierced by a snow-white spearhead.

THUD. DRIP, DRIP.

Yohi stared at the old man, who looked just as blood-soaked as Jin Taekyung, then suddenly muttered:

“That’s him.”

“Who are you talking about?”

“Black Hand. The owner of the voice that treated that old man like a subordinate.”

“Ah.”

“And if my guess is right…”

Yohi’s gaze swept rapidly across the surroundings before stopping.

There lay the corpse of the Black Hand Fist Demon.

The man who had slaughtered the warriors of the Western Yao Estate with a martial prowess worthy of a fiend was dead, his chest blown wide open.

*This is impossible.*

Yohi’s eyebrows trembled.

She had wondered if it might be so when she discovered the corpse of the unidentified old man, but the situation before her went far beyond anything she had imagined.

And it was not just Yohi who thought so.

“How could this…”

Heugung muttered under his breath, then swallowed the rest of his words.

It was utterly incomprehensible, but the scene spread out before them was undeniably real.

The surroundings had been turned to rubble by an unprecedented force. Two old men lay dead, while a lone young man had fallen into a deep sleep.

The conclusion was obvious.

Jin Taekyung had fought—and won.

He had defeated two Supreme Peak masters who had devoted several times as much of their lives to martial arts as he had.

“…The Blazing Flame Divine Dragon.”

The four words slipped between Yohi’s red lips like a groan. Awe filled her eyes as she looked at Jin Taekyung.

Whether such a thing was possible no longer mattered.

Jin Taekyung had made the impossible possible, willingly risking his life to save them, who were nothing more than southern tribespeople.

So now, they had to act for him.

*It may already be too late, but I have to act now.*

At certain times, some of Nanman’s venomous creatures shed their skins.

This process was known as molting.

But how could gaining a new body ever be easy? If the molting succeeded, the creature would gain a more beautiful and powerful body. If it failed, it would slowly die in its old, diseased one.

Yohi had chosen the former path.

*If I delay any longer, it’ll all be over. I have to let everyone know about this somehow.*

They had to expose the conspiracy connected to Baeksang and stop Dark Heaven.

Yohi’s own mistakes would be revealed in the process, but she had already made her decision.

She would accept the full price for the path she had chosen.

*I never should have done it.*

When she looked back, all she felt was regret.

Baeksang had laid out a broad and beautiful silk road before her, and Yohi had come all the way here by walking along it, turning a blind eye to everything happening around her.

But when she reached the end and happened to look down, she saw that her feet had long since become covered in blood.

Not her own blood.

The blood of other Nanman people.

Now…

She wanted to wipe that blood away. And if she could not, she would cut off her feet and be done with it.

One person had played a major role in bringing Yohi to this decision.

*Jin Taekyung.*

A stranger from a foreign land.

Yet he had fought for Nanman more than anyone else—just as the former Sect Leader of the Fire Gate Clan, now nothing more than a legend, had done centuries ago.

*I may be a Great Chieftain, but I can’t be worse than a Han Chinese person.*

*If a bitch like me can even call herself a Great Chieftain…*

Yohi swallowed the self-mocking words and immediately sprang into action.

RRRIP.

Her slender white hands tore into her ornate gown without a moment’s hesitation.

She removed the jewelry adorning her in gold and silver, exposing her arms and legs. Heugung’s eyes widened at the sight.

“Yohi.”

“There’s no time to talk. We have to move right now.”

Heugung stared at Yohi in silence for a moment, then nodded.

“You’re right. We don’t know when more enemies might come rushing in.”

“Considering how quiet it’s been around us until now, it’s safe to assume there aren’t any others. No, they probably decided Dark Heaven didn’t need to send more support after arranging for two Supreme Peak masters to come here.”

“That must be it. They already knew you possessed the tracking scent, and they probably intended to use us as bait to draw in the Palace Lord, Yayul. He would have been Dark Heaven’s greatest obstacle at present.”

But the bait had been taken by Jin Taekyung instead of the Beast Miao King, and the hunters who had prepared the hunt had been hunted by him.

No one could have predicted such a situation—not even Dark Heaven.

Yet the more the conversation continued, the heavier Yohi’s heart became.

“But what if Jin Taekyung didn’t come in the Palace Lord’s place… What if the Palace Lord was in a situation where he couldn’t come?”

“That…”

“My tribespeople—the Western Yao Estate—were massacred. It’s an unprecedented disaster, so by now the Inner Palace must be in an uproar.”

“Then shouldn’t we go to the Inner Palace as quickly as possible?”

Yohi silently shook her head.

She had merely closed her eyes and ears for the sake of her ambition. She was not a fool.

Dark Heaven had won over Baeksang, the Beast Miao King’s sworn younger brother, and waited for the right moment for several decades.

Yohi suddenly remembered the words spoken by the unidentified old man who had used the boulder as his coffin.

> “If you act rashly with the grand plan right before you, I will never forgive you.”

*The grand plan.*

He had definitely called it the grand plan.

Yohi sensed indescribable danger and anxiety in those two words. She also realized that their abduction had been a carefully calculated act.

The Western Yao Estate, massacred.

The Inner Palace, which must have been swept up in chaos.

Baeksang, who had built a support base comparable to—or even greater than—the Palace Lord’s.

And Dark Heaven, which had planned all of it.

Finding the answer was not difficult.

“Yohi?”

Heugung’s voice abruptly pulled Yohi from her thoughts. She bit her lip.

*If the thought that just crossed my mind is correct…*

The Inner Palace was no different from a demon-slaying battleground, with all sorts of fiends and sinister schemes lying in wait.

“We shouldn’t go to the Inner Palace. We have to go west.”

“The west? Could it be…”

“Yes. I intend to go to Boshan.”

Each tribe was scattered throughout Nanman, but they all had a base. Of them, Boshan was home to several thousand Yao people.

“By now, Baeksang has joined hands with Dark Heaven and taken control of the Inner Palace. If the tribal chieftains and the Tribal Grand Council decided to put him in power, even the Palace Lord wouldn’t be able to do anything.”

“Hmm.”

“Believe me. If we head to the Inner Palace now, we’ll be eliminated before we even manage to enter it.”

Heugung stared at Yohi with deeply sunken eyes.

“What if we head to Boshan?”

“I’m the Great Chieftain of the Yao people. Do I really need to say more?”

“How many warriors can you mobilize?”

“A thousand if I gather every last one. That’s nowhere near enough to stand against Baeksang with Dark Heaven at his back, but I don’t know if they’ll continue following him after learning what happened.”

“The people’s hearts will surely waver, and the warriors will defect.”

“I’ll send messenger pigeons and messengers to every tribe and village. Seven days at most. Within that time, all of Nanman will know about Baeksang’s atrocities.”

Heugung let out a quiet exclamation as Yohi continued speaking without hesitation.

“You’re truly astute. More so than the woman I knew.”

At those words, Yohi briefly forgot the situation and let out a quiet laugh.

“It feels strange hearing that from you. Especially since you’ve become a completely different person.”

“I had no choice. To avoid Baeksang’s eyes and ears, I had to hide myself first.”

Heugung calmly replied and handed her something.

Wrapped in yellow paper was a round pill.

“Take it.”

“What is this?”

“An antidote the Black Hand Fist Demon was carrying. I found it when I searched his clothes a moment ago. With our internal energy sealed like this, Baeksang’s warriors will hunt us down before we reach Boshan.”

Heugung was right.

No matter how outstanding a warrior was, they could not shake off a pursuit party unless they had trained in external arts. Yohi’s martial prowess was not particularly high to begin with.

SWISH.

Yohi did not hesitate. She chewed and swallowed the pill.

Its bitter taste made her brow wrinkle involuntarily, but it was still a hundred times better than dying without putting up a proper resistance even once.

“How long will it take us to reach Boshan?”

“We’re in Ailao Mountain, so… Three or four days should be enough. First, though, we need to get out of these Poisonblood Grounds.”

On the way there, they had seen venomous beasts they had never encountered before and a swamp made of deadly poison. They had already determined their location.

“By then, he should have woken up.”

“Yes, he should. If he wakes up, he’ll be an army unto himself.”

As Heugung quietly answered, he lifted Jin Taekyung’s body and slung it over his back.

Muyaho, who had been urinating on the dead Black Hand Fist Demon’s face, came running over and lowered his back.

“Grrr.”

Heugung gazed at the White Tiger’s blue-white eyes.

“Isn’t he truly strange?”

“Pardon?”

“I’m talking about this one the Young Palace Lord commands. Whenever I encountered him in the Inner Palace, he always bared his teeth at me. But now that Jin Taekyung is beside him, he’s as gentle as a lamb.”

“He must have opened his heart to him. They say spiritual creatures have always been able to recognize people.”

Yohi answered absentmindedly, then suddenly sensed that something was strange.

Heugung let out a quiet laugh.

“Yes. I think you’re right.”

THWACK! THUD.

Blood sprayed, and the enormous silver body tilted.

As Yohi stared blankly at the sight, Heugung’s voice reached her ears.

“Didn’t I tell you? I had to hide myself first.”
```
