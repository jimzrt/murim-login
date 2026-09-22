<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0684.txt",
      "sha256": "7e611dc1075363de13243f6215bae6578df89f3185b85e829bc9985eb14e6e1f",
      "bytes": 12809
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "849c5481ce67a8ba1e27851283a894189ddbdb797891a8613fbb2550240f86de",
      "bytes": 1073
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "22764fb38b28621564d76844c10cea4c71334f08d99cf84fb313c93d516bd87d",
      "bytes": 203778
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "4fc40a4e143e23e72d8025322bf9e3a19d24054bd1b9d232b79aca035ca6a890",
      "bytes": 763
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "5773ed7cae6afef980b9fb121d11e97fce0670ff2b0b943694c263658573902b",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8efe22644404144242885b020691750c5fe2542eb866439bb0d4e8075925349a",
      "bytes": 553
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "2d4b459dd9725ed1f4d220fcff12b2d3dee2cc256918648e25d61fcfb1a50c5b",
      "bytes": 919
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "53fc973ab311909cfc6e710f36fc53c02bf71eac6c7edffd64b66b51dfa78d72",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2a4e9458a329bd243b4349667ce194ccba5a82ed685a0327e12af59a35c546bc",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "85d42b50378da04588fc933780d95196f24a2f3c0ac873e2a7287a4939bca571",
      "bytes": 626
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "7b5911423d05dae5d63d2e60fe9aa7253bddc510b2d7f89b77c7aa955c548ad4",
      "bytes": 648
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "808dbd741c16c233930f37aaf05aac6a77a6bd137fb26e7757e0e9e8409522c0",
      "bytes": 888
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "9066e1d96e07f26f3eb65b571b939d9ba7077d571d90de95dc4a18974c4862a0",
      "bytes": 671
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bdb519c7bf57005ad6ed9051602dc3e0ada911bab0f037f1093f98e73fa29bb7",
      "bytes": 211187
    }
  ],
  "estimated_tokens": 11956
}
-->

# Durable State Update — Chapter 684

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 684. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 684. Profile updates may replace only one
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
  "chapter": 684,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 684,
    "continuity_sources": [684],
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
    "Jin's level-up from Black Hand Fist Demon's EXP restored his internal energy and enabled his survival, but his prior injuries remain severe.",
    "Fire Dragon Armor prevented the Great Snow Fiend's ice sword from fully penetrating Jin.",
    "Black Hand Fist Demon is dead.",
    "The Great Snow Fiend is severely injured but still has enough strength to continue fighting Jin.",
    "Jin and the Great Snow Fiend are engaged in a renewed fire-and-cold duel.",
    "An unidentified white-furred entity struck the Great Snow Fiend from behind during the duel."
  ],
  "continuity_sources": [
    683
  ],
  "open_questions": [
    "Will the Great Snow Fiend survive the rear attack and Jin's hellfire?",
    "Who or what is the unidentified white-furred attacker?"
  ],
  "safe_through": 683,
  "temporary_decisions": [
    "Render 대마불사 as the Go proverb \"a large group doesn't die easily.\"",
    "Render 육참골단 as \"Sacrifice flesh to break bone.\"",
    "Keep the white-furred attacker unidentified."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 무신     | **Martial God**               | —              |
| 십왕     | **Ten Kings**       |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 주화입마   | **qi deviation**                                 |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 상태               | **Status**                     |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 대라신선 | **Great Firmament Immortal** | Legendary immortal invoked by Mungyeong as unable to stop the dragon's death. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 흑수 | 요희 | hostile captor to captive | little bitch / little girl | cruel, mocking, and predatory | Black Hand taunts Yohi, threatens her life, and says the Demon Empress covets her. |
| 요희 | 흑수 | captured tribal chieftain to torturer | you | terrified and pleading | Yohi recognizes Black Hand as the Fiend who attacked her warriors and maimed Heugung. |
| 진태경 | 흑수 | hostile_martial_opponent | Black Hand | mocking and profane | Jin sarcastically addresses Black Hand after hearing his sobriquet. |
| 흑수 | 진태경 | hostile_Dark_Heaven_agent_to_enemy_martial_artist | Blazing Flame Divine Dragon Jin Taekyung | taunting and murderous | Black Hand identifies Jin while claiming that killing him will make the sobriquet famous. |
| 흑수권마 | 대설귀 | junior hostile subordinate to senior ally | Senior | deferential but urgent and protesting | Black Hand protests the Great Snow Fiend's order to capture Jin. |
| 대설귀 | 흑수권마 | senior hostile commander to junior subordinate | you | blunt, commanding, and threatening | The Great Snow Fiend orders Black Hand to stop questioning him. |
| 진태경 | 대설귀 | hostile_martial_opponents | old man | mocking, casual, and profane | Jin taunts the Great Snow Fiend while preparing to continue the fight. |
| 대설귀 | 진태경 | hostile_martial_opponent | Jin Taekyung | cold, incredulous, and confrontational | The Great Snow Fiend addresses Jin while demanding an explanation for his survival. |

## Listed compact profiles

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 683
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand is a sadistic Dark Heaven agent and Supreme Peak master acting under orders associated with the Southern Heaven Demon Empress.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand is the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; the Great Snow Fiend is his senior and can overrule him under the Southern Heaven Demon Empress's orders.

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 676
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven alongside the Western Heaven Demon Lord, has received the Lord of Heaven's power for the coming Great War, and still seeks to kill Cheongpung, Jeok Cheongang, and Jin Taekyung.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 683
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 683
- **Aliases:** None
- **Role:** The Great Snow Fiend is the former ruler of Great Snow Mountain and a fiend who killed Baekhwi and Venerable Wusang during the Great Faction War; the Southern Heaven Demon Empress has personally ordered him to capture Jin Taekyung alive if possible.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend is an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he is senior to Black Hand and acts under the Southern Heaven Demon Empress's orders.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 683
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 683
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 682
- **Aliases:** None
- **Role:** The Martial God is an unidentified legendary martial artist who defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone more than fifty years ago.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 680
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature currently accompanying Jin Taekyung through the Poisonblood Grounds.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and currently carries Jin while aiding his escape.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 676
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 678
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people and seeks to unite Nanman's four great tribes under Yao leadership; she manipulated Heugung while following Baeksang, deliberately suppressed suspicions about his Dark Heaven ties, and is now held captive with her internal energy sealed.

## Korean source

```text
＃684화



구구구궁!

굉음과 함께 대지가 흔들린다.

나이를 짐작할 수 없을 만큼 오랜 세월 뿌리내린 거목도, 만근의 무게를 지닌 바위도.

그리고 어딘가에 숨어서 이 싸움을 숨죽여 지켜보고 있었을 독혈지의 괴이한 생물체들도.

모든 것이 파도처럼 출렁이고 뒤집히는 대지에 파묻혔다.

콰드드득!

뜨겁다.

나는 파동의 중심에서 휘몰아치는 열풍(熱風)을 느꼈다.

후텁지근한 바람에서는 한 줄기의 서늘함도 찾아볼 수 없었고, 반경 수십 장을 뒤덮은 짙은 먼지구름은 조금의 시야도 허락하지 않았다.

그러나…… 코앞까지 들이닥친 창날을 향해 엄청난 음한지기가 담긴 쌍장(雙掌)을 쏟아 내던 노인의 모습만은 똑똑히 기억하고 있었다.

그의 몸에서 솟구치던 붉은 핏물과, 새하얀 털을 휘날리며 저 멀리 사라지던 백호의 신형도.

‘……저 녀석.’

마지막 순간, 대설귀를 향한 무야호의 갑작스러운 기습은 사전에 약속된 것이 아니었다.

아니, 오히려 녀석에게 전투를 피해 이곳 어딘가에 감금되어 있을 요희를 찾으라 했다.

만약 오늘 이 자리에서 내가 죽는다 해도, 저 영민한 맹수만큼은 살아서 독혈지를 빠져나가길 바랐으니까.

두 대족장과 함께 남만야수궁으로 향한다면, 향후 일어날 재앙을 막을 수 있다는 희망은 사라지지 않을 테니까.

그러나 무야호는 내 조언을 듣지 않았고, 무모하리만치 위험한 기습은 끝내 성공했다.

‘미세한 차이지만 분명해. 예상치 못한 공격 때문에 대설귀의 반응이 늦었다.’

분신이나 다름없는 백염을 쏘아 보낸 보람이 있었다.

평정심을 잃고 상처까지 입은 사냥꾼은 이제 사냥꾼이 아닌, 사냥감에 불과하다.

‘어디냐.’

팟.

나는 작은 뇌까림과 함께 쏘아졌다.

사방을 휘감은 짙은 먼지구름과 곳곳에서 쏟아지는 흙과 돌들. 시야과 기척을 가로막은 그것들을 향해 일권(一拳)을 뻗었다.

퍼엉!

공력을 실을 필요도 없었다. 음속을 돌파한 속도와 바람을 부수는 힘에 압축된 공기가 터져 나간다.

거대한 먼지구름이 반으로 찢겨 나가고 그 너머에 감춰져 있던 것들이 모습을 드러냈다.

화아아악!

주위를 휩쓰는 열풍. 먼지구름 너머에서 피에 젖은 누군가의 옷자락이 언뜻 스쳐 지나간 순간, 나는 망설임 없이 손을 뻗었다.

악전고투 끝에 얻어 낸 승기(勝機).

승부의 저울추가 조금씩 기울기 시작한 지금을 놓쳐서는 안 된다.

설사 아직 대설귀에게 보여 주지 않은 능력 중 일부가 드러난다 해도 마찬가지다.

‘인벤토리 오픈. 소환.’

나는 머릿속에 떠올린 명령어와 함께 손아귀에 잡힌 창을, 온 힘을 다해 흩뿌렸다.

쐐애애액! 쾅!

강렬한 파공성에 이어 울려 퍼지는 굉음. 하지만 그 모든 것이 끝나기도 전에 내 손에는 또 다른 창이 붙잡혀 있었다.

쐐액!

다시.

콰앙!

또 다시.

‘더. 더. 더, 더.’

생각과 동시에 몸이 움직인다. 허리를 비틀고, 어깨를 젖히고, 전신의 무게를 실어 쏘아 보낸 창들은 마치 폭격하듯 사방을 초토화시켰다.

구구구궁!

잠시 흩어지나 싶던 먼지구름이 다시 피어오르는 것도 신경 쓰지 않았다.

어차피 그보다 더한 공격들을 쏟아붓고 있었으니까.

하나하나가 백염과는 비교도 되지 않는 싸구려 철창들이지만, 내 손을 떠나 섬광처럼 쏘아지는 그것들에 한 번이라도 격중당한다면 누구도 무사할 수 없다.

‘그것이 설령 초절정 고수. 아니…….’

대설귀라 해도.

쾅! 콰앙! 콰아아앙!

쉴 새 없이 이어지는 폭발과 굉음. 그리고 찰나에 십여 개가 넘는 창을 벼락처럼 대지에 내리꽂은 나는 마침내 볼 수 있었다.

퍼걱! 푸화악!

짙은 먼지구름 너머, 섬뜩한 파육음과 함께 허공으로 흩뿌려지는 붉은 선혈을.

거기 있었구나.

확신과 동시에 발을 뻗었다. 천근의 무게를 실어 내디딘 발끝이 뒤집힌 대지를 깊숙이 파고들었다.

콰드득. 쾅!

공력의 압축과 동시에 이루어진 폭발. 십여 장의 공간을 단숨에 지우며 쇄도한 나는 먼지구름 사이로 파고들었다.

이미 전부터 사방에서 들려오는 소음과 쏟아지는 파편들로 인해 앞뒤조차 분간하기 힘든 상황.

하지만 공간을 헤쳐 나가는 내 움직임에는 한 치의 망설임도 없었다.

‘이미 봤으니까.’

날 선 감각은 비릿한 혈향을 감지해 냈고, 뛰어난 안력(眼力)은 또다시 먼지구름 사이로 누군가의 등을 발견했다.

백염을 막으며 부상을 입었을 대설귀는 나보다 빠를 수 없다.

나는 인벤토리에서 소환한 창을 비스듬히 내리그었다.

쉬잉.

나직한 파공성과 함께, 창날을 휘감으며 솟구친 청백색의 화염이 천천히 바람을 갈랐다.

아니, 느려진 것은 창날뿐만이 아니다. 극도의 집중력이 뇌를 마비시키고, 세상을 정지시켰다.

그리고 그 정지된 시간 속에서, 느릿하게 먼지구름을 베어 가른 화염이 마침내 옷자락에 닿은 그 순간. 한 줄기 확신이 뇌리를 스쳤다.

‘끝났……!’

하지만 도대체 어째서일까.

지금 느껴지는 이 알 수 없는 한기(寒氣)와 묘한 기시감은.

단 일 촌(寸)만 더 나아가면 모든 것을 끝낼 수 있는 상황에서, 머리에서 내려온 명령을 무시한 채 물러서고자 하는 몸뚱어리는.

동시에 나는 깨달았다.

그건 이성인 동시에 본능이었고, 이성보다 앞선 본능이었다.

‘대설귀.’

까마득한 과거의 구렁텅이에서 기어 올라온 노괴(老怪).

그러나 놈이 위험한 이유는 중단전을 개방한 초절정 고수이기 때문이 아니다.

압도적인 무위를 지닌 혈주와 서천마군이 갖지 못했던 것.

아니, 압도적이기에 가질 필요조차 느끼지 못했던 조심성과 철저함이 저 노괴가 지닌 가장 날카로운 무기다.

‘그런 대설귀가, 이렇게 쉽게?’

아니다. 적어도 지금껏 내가 상대해 온 대설귀라면 그럴 리 없다.

찰나를 쪼개고 쪼갠 짧은 순간, 나는 온 힘을 다해 몸을 비틀었다.

갑작스럽게 제동이 걸린 몸과 격랑(激浪)처럼 몰아치던 공력이 역류한다.

울컥, 뜨거운 핏물이 목구멍에 차오름과 동시에 허공에서 꺾여 나간 창날이 옷자락을 가른다.

그리고 다음 순간. 나는 똑똑히 볼 수 있었다.

서걱.

느리게 흐르는 시간 속, 창날에 의해 두부처럼 베어져 나가는 살점과 뼈를.

더불어 마치 무중력 상태인 것처럼 천천히 허공으로 떠오르는 핏물 너머로 흩날리는 산발의 머리카락과 이미 숨이 끊긴 시신의 어깨너머에서 빛나고 있는 한 쌍의 차가운 눈동자를.

다시 돌려주마. 네가 했던 방식 그대로.

들리지 않는 목소리가 그렇게 말을 건넸다고 느낀 순간. 뻥 뚫려 있던 흑수권마의 가슴에서 시리도록 차가운 섬광이 터져 나왔다.

슈화악!

나는 직감했다.

이 공격은 피할 수 없다고.

그러나 치명상만큼은 피할 수 있을 것이다. 지금 내 상반신에 걸쳐져 있는 것은 서천마군을 죽이고 얻은 희대의 신병이기, 바로 화룡갑(火龍鉀)이니까.

그러나…….

콰득! 푸푹!

차갑고, 동시에 뜨거웠다.

몸 안으로 스며드는 음한지기가.

그리고 화룡갑을 부수고 가슴에 틀어박힌 또 다른 신병이기, 백염(白炎)의 창날이.

삐빅. 삐빅. 삐비빅!



- [화룡갑]의 일부가 강력한 기운에 의해 파괴되었습니다!

- [화룡갑]의 자동 수복까지 남은 시간 : 3일

- [음한지기]가 내부를 진탕시킵니다!

- 상태 이상, [출혈]에 걸렸습니다!

- 상태 이상, [막대한 내상]을 입었습니다!

- [주화입마]의 위험이 있습니다! 한시라도 빨리 기운을 진정시키십시오!

- 신체의 내, 외부가 크게 손상되었습니다!

.

.

.

끔찍한 고통으로 아득해진 시야 속, 나는 쉴 새 없이 귓가를 파고드는 경고음을 들으며 생각했다.

정말이지, 운수 한 번 끝내주는 날이라고.



* * *



모든 것이 순식간에 스쳐 지나간 짧은 순간, 세상이 멈췄다고 느낀 것은 진태경뿐만이 아니었다.

그것은 먼지구름 사이에 숨어 마지막 기회를 노리던 대설귀 역시 마찬가지였고, 백여 년에 가까운 인생에서 가장 길고 힘든 기다림의 시간을 보내던 그는 마침내 참았던 숨을 토해 낼 수 있었다.

콰득. 푸푹!

한 사람의 가슴에 박힌 창날과 파르르 떨리는 신형. 그리고 고통과 절망에 물든 눈동자.

“쿠에에엑!”

촤악.

내장 조각이 섞인 검붉은 핏물이 대설귀의 얼굴을 적신다.

그러나 코를 파고드는 역한 비린내와 악취에도 그는 아무렇지 않았다.

아니, 오히려 아직까지도 살아 있는 저 어린놈의 모습에 기가 질렸다.

‘이런 미친놈.’

대설귀의 설계는 모든 것이 완벽했다.

마지막 순간, 진태경이 몸을 비틀어 피하지 않았다면 그랬을 것이다.

정확히 심장을 관통했어야 할 창날이 가슴 어림에 박힌 것은 바로 그 이유에서였다.

‘심지어 노부가 그에 따라 창날의 방향을 바꾸지 않았다면…… 고작 옆구리로 그쳤겠지.’

대설귀는 등골이 서늘해지는 것을 느꼈다.

전투가 막 시작될 무렵 그가 진태경에게 내렸던 평가는 이미 정정된 지 오래다.

‘향후 오십 년이 아니라 삼십 년. 아니, 어쩌면 이십 년 안에 무신(武神)과 천마(天魔)에 필적할 놈이다.’

괴물이라고 칭할 수밖에 없는 재능과 불꽃보다도 맹렬한 집념.

이건 무공의 문제가 아니다. 사람 그 자체에서 오는 강력함. 위험을 넘어 두려움을 불러일으키는 기세.

대설귀의 눈에 비친 진태경은 이미 강자였다.

구파일방과 오대세가의 주인들. 아니, 십왕(十王)과 비견해도 결코 부족함이 없는.

하지만.

‘그런 네놈도 여기까지다.’

으득.

이를 악문 대설귀는 창대를 쥔 손에 힘을 가했다.

무언가에 뜯겨 나간 듯 텅 빈 오른쪽 소매는 촌각 전, 백호의 기습에 이어 내리꽂힌 창날에 바쳐야 했지만 후회는 없다.

목숨이나 다름없는 팔을 잃었다지만 신묘하기 짝이 없는 암천의 술사(術士)들이라면 그리 어렵지 않게 방법을 찾아낼 터.

지금 그에게 중요한 것은…… 진태경, 저 두려울 만큼 지긋지긋한 괴물을 끝장낼 수 있다는 사실이었다.

‘말하지 않았더냐. 네놈이 죽고, 노부는 살아남는 것. 그것이 순리(順理)이자 천명(天命)이라고.’

두려움과 환희가 뒤섞인 얼굴로, 대설귀는 한 줌밖에 되지 않는 힘을 끌어모았다.

그와 동시에 만년한철로 이루어진 서늘한 창대가 진태경의 가슴을 더욱 깊숙이 파고들었다.

콰득!

화염 대신 냉기가 서린 창날이 주인의 가슴을 파고든다. 살을 가르고 뼈를 부수는 섬뜩한 소리와 함께 진태경의 신형이 퍼득 떨렸다.

푸슛. 촤아악!

분수처럼 솟구치는 핏물과 서서히 흐릿해지는 눈동자. 수많은 죽음을 지켜본 대설귀는 그 어느 때보다 확신했다.

‘이제 그 누구도 놈을 살릴 수 없다. 신의(神醫)가 아닌 대라신선(大羅神仙)이 온다 해도.’

그러나 대설귀는 잠시 잊고 있었다.

눈앞에서 죽어 가고 있는 젊은 청년은, 그의 판단으로는 예측할 수 없는 괴력난신(怪力亂神)과도 같은 존재라는 것을.

덥석. 푸우욱!

대설귀에게는 대처할 시간도, 대처할 힘도 주어지지 않았다.

한기 대신 경악이 서린 그의 눈동자에는 한 사람의 모습이 비치고 있었다.

온 힘을 다해 창대를 붙잡아 자신의 가슴에 더욱 깊숙이 박아넣은 채, 스스로 앞으로 나아간 진태경의 모습이.

그리고, 피에 젖은 그의 손에서 타오르고 있는 마지막 불꽃이.

“……!”

부릅떠진 대설귀의 눈동자에, 청백색 광염(光焰)이 번졌다.

화륵, 콰아앙!
```

## Final English reading copy

```markdown
# Chapter 684

RUMBLE!

The earth shook with a thunderous roar.

Ancient trees that had taken root so long ago that no one could guess their age. Boulders weighing ten thousand geun.

Even the strange creatures of the Poisonblood Grounds that had been hiding somewhere nearby, silently watching this battle.

Everything was swallowed by the earth as it heaved and overturned like a wave.

KRRRUNCH!

It was hot.

At the center of the shock wave, I felt the scorching wind whipping around me.

There was not a trace of coolness in the muggy air, and the thick cloud of dust covering a radius of dozens of yards allowed me no visibility whatsoever.

Yet I remembered one thing clearly: the old man who had unleashed both palms packed with immense Yin-Cold Qi at the spearhead that had lunged right up to his face.

I also remembered the red blood gushing from his body, and the figure of the White Tiger disappearing into the distance in a flurry of white fur.

*That bastard…*

At the last moment, Muyaho’s sudden ambush against the Great Snow Fiend had not been planned beforehand.

In fact, I had told him to avoid the battle and search for Yohi, who was probably being held captive somewhere in this place.

Even if I died here today, I wanted that clever beast, at least, to escape the Poisonblood Grounds alive.

If he went to the Nanman Beast Palace alongside the two Great Chieftains, there would still be hope of preventing the disasters that would follow.

But Muyaho had ignored my advice, and his reckless, dangerously risky ambush had ultimately succeeded.

*The difference was tiny, but it was clear. The unexpected attack delayed the Great Snow Fiend’s reaction.*

It had been worth sending White Flame—practically an extension of myself—flying.

A hunter who had lost his composure and been wounded was no longer a hunter.

He was nothing more than prey.

*Where are you?*

POP!

With a quiet mutter, I shot forward.

The thick dust cloud winding around me, the soil and stones pouring down from every direction—those things blocked my vision and masked every sign of movement.

I thrust a fist at them.

BOOM!

I did not even need to imbue it with internal energy. The air compressed by the speed that broke the sound barrier and the force that shattered the wind burst outward.

The enormous dust cloud split in two, revealing what had been hidden beyond it.

FWOOSH!

A hot wind swept through the surroundings. The instant I caught a glimpse of someone’s blood-soaked clothes beyond the dust cloud, I reached out without hesitation.

This was the opening I had won after an agonizing struggle.

Now that the scales of the battle had begun to tilt little by little, I could not let it slip away.

Not even if it meant revealing some of the abilities I had yet to show the Great Snow Fiend.

*Inventory Open. Summon.*

Along with the command that rose in my mind, I flung the spear in my hand with every ounce of my strength.

SHWAAAAK! BOOM!

A fierce sound of splitting air was followed by a thunderous roar. But before either sound had faded, another spear was already clutched in my hand.

SHWIK!

Again.

KWAANG!

Again.

*More. More. More, more.*

My body moved at the same instant as my thoughts. I twisted my waist, drew back my shoulder, and sent each spear flying with the weight of my entire body.

They devastated the surroundings like a bombardment.

RUMBLE!

I ignored the dust cloud as it began to rise again after briefly scattering.

I was pouring out attacks even more powerful than that.

Each spear was a cheap iron weapon that could not compare to White Flame, but if even one of those weapons, shot from my hand like a flash of light, struck its target, no one could escape unharmed.

*Even if he’s a Supreme Peak master. No…*

Even if he was the Great Snow Fiend.

BOOM! KWAANG! KRAAA-BOOM!

Explosions and thunderous roars continued without pause. After driving more than ten spears into the ground like bolts of lightning in the span of a moment, I finally saw it.

KRRK! SPLAAASH!

Beyond the thick dust cloud, bright-red blood scattered into the air with a grisly sound of flesh being torn.

There you are.

The instant I was certain, I thrust out my foot.

The tip of my foot, bearing the weight of a thousand geun, dug deeply into the overturned earth.

KRRRUNCH. BOOM!

An explosion occurred at the same time as I compressed my internal energy. I surged forward, erasing dozens of yards of space in an instant, and plunged into the dust cloud.

The noise coming from every direction and the falling debris had already made it impossible to tell front from back.

But my movements as I cut through the space held not the slightest hesitation.

*Because I’ve already seen him.*

My sharp senses detected the metallic scent of blood, and my keen eyesight once again found someone’s back through the dust cloud.

The Great Snow Fiend could not be faster than me after being injured while blocking White Flame.

I summoned a spear from my Inventory and slashed it down diagonally.

SHIIING.

With a low sound of splitting air, blue-white flames rose around the spearhead and slowly cut through the wind.

No. It was not only the spearhead that had slowed.

Extreme concentration paralyzed my brain and brought the world to a standstill.

Within that frozen time, the flame slowly slicing through the dust cloud finally touched the hem of the clothes.

At that instant, a single certainty flashed through my mind.

*It’s over—!*

But why?

Why was I feeling this inexplicable cold and strange sense of déjà vu?

Why was my body trying to retreat, ignoring the command descending from my brain, when moving even one inch farther would end everything?

At the same time, I realized.

It was reason and instinct at once.

And it was instinct that came before reason.

*The Great Snow Fiend.*

An old monster who had crawled up from the abyss of a distant past.

But the reason he was dangerous was not because he was a Supreme Peak master who had opened his Middle Dantian.

What he possessed that the Blood Lord and the Western Heaven Demon Lord did not—

No, what they had not even felt the need to possess because their strength was so overwhelming—

was caution and thoroughness.

Those were the old monster’s sharpest weapons.

*The Great Snow Fiend, this easy?*

No.

At least, the Great Snow Fiend I had faced until now could never have fallen this easily.

In the brief instant that was split into even briefer instants, I twisted my body with all my strength.

My body came to a sudden stop, and the internal energy surging through me like a raging sea reversed course.

A mouthful of hot blood surged up my throat, and the spearhead that had veered away in midair sliced through the clothes.

Then, in the next instant, I saw it clearly.

SHNK.

Within the slowly flowing time, I saw flesh and bone being sliced away like tofu.

Beyond the blood drifting through the air as if it were weightless, I saw disheveled hair fluttering in the breeze.

And beyond the shoulder of the corpse that had already stopped breathing, a pair of cold eyes gleamed.

*I’ll return it to you. Exactly the way you did.*

The instant I felt an inaudible voice speak those words, a painfully cold flash of light burst from the gaping chest of the Black Hand Fist Demon.

SHWAAASH!

I knew instinctively.

I could not avoid this attack.

But I could avoid a fatal wound.

Because covering my upper body right now was the peerless divine weapon I had obtained by killing the Western Heaven Demon Lord.

Fire Dragon Armor.

But…

KRRUNCH! THUD!

It was cold.

And at the same time, it was hot.

The Yin-Cold Qi seeping into my body.

And the spearhead of another divine weapon, White Flame, which broke through the Fire Dragon Armor and lodged itself in my chest.

BEEP. BEEP. BEEEEP!

> **System**
>
> - Part of **Fire Dragon Armor** has been destroyed by powerful energy!
>
> - Time remaining until **Fire Dragon Armor** is automatically repaired: **3 days**
>
> - **Yin-Cold Qi** is violently shaking your insides!
>
> - Status abnormality: **Bleeding**
>
> - Status abnormality: **Massive Internal Injury**
>
> - There is a risk of **qi deviation**! Calm your energy as soon as possible!
>
> - The internal and external parts of your body have suffered severe damage!

…

…

…

My vision grew hazy from the horrible pain. As warning sounds continued to pierce my ears without pause, I thought:

This was truly turning out to be one hell of a day.

* * *

In that brief instant when everything flashed by in the blink of an eye, Jin Taekyung was not the only one who felt that the world had stopped.

The Great Snow Fiend felt the same.

He had been hiding among the dust cloud, waiting for his final opportunity. After enduring the longest and most difficult wait of his nearly century-long life, he could finally exhale the breath he had been holding.

KRRUNCH. THUD!

A spearhead buried in a man’s chest.

A body trembling violently.

Eyes filled with pain and despair.

“Gueeek!”

SPLASH!

Dark-red blood mixed with pieces of internal organs splattered across the Great Snow Fiend’s face.

But the foul metallic smell and rank stench filling his nose did not bother him.

No, what stunned him was the sight of that young bastard still alive.

*What a lunatic.*

The Great Snow Fiend’s plan had been perfect.

It would have been, if Jin Taekyung had not twisted his body at the last moment.

The spearhead had been meant to pierce his heart cleanly. That was why it had become embedded in the vicinity of his chest instead.

*If this old man had not changed the direction of the spearhead along with him… it would have ended at his side.*

The Great Snow Fiend felt a chill run down his spine.

The assessment he had made of Jin Taekyung at the beginning of the battle had long since been corrected.

*Not in fifty years, but thirty. No… perhaps within twenty years, he’ll be able to rival the Martial God and the Heavenly Demon.*

A talent that could only be called monstrous.

A determination more ferocious than fire.

This was not a question of martial arts. It was a powerful strength that came from the man himself—a momentum that went beyond danger and inspired fear.

In the Great Snow Fiend’s eyes, Jin Taekyung was already a powerhouse.

He was in no way inferior to the masters of the Nine Sects and One Gang or the Five Great Families.

No, even when compared to the Ten Kings, he did not fall short in the slightest.

But—

*Even you end here.*

GRIND.

The Great Snow Fiend gritted his teeth and tightened his grip on the spear shaft.

His right sleeve hung empty, as though something had torn away the arm inside it. The arm had been sacrificed to the White Tiger’s ambush and the spear that came crashing down immediately afterward.

But he had no regrets.

He had lost an arm as precious as his life, but the uncanny sorcerers of Dark Heaven would surely find some solution without much difficulty.

What mattered to him now was the fact that he could finish Jin Taekyung—that terrifyingly tenacious monster.

*Did I not tell you? You will die, and this old man will survive. That is the natural order, and the mandate granted by Heaven.*

With fear and rapture mingling across his face, the Great Snow Fiend gathered what little strength remained to him.

At the same time, the cold spear shaft made of Ten-Thousand-Year Cold Iron drove deeper into Jin Taekyung’s chest.

KRRUNCH!

The spearhead, steeped in cold rather than flame, bored into its owner’s chest.

Along with the dreadful sound of flesh being split and bone being crushed, Jin Taekyung’s body jerked violently.

PFFT. SPLAAASH!

Blood spurted upward like a fountain, and his eyes slowly grew dim.

The Great Snow Fiend had watched countless deaths. He had never been more certain.

*Now no one can save him. Not even if the Great Firmament Immortal himself comes—not merely the Divine Physician.*

But the Great Snow Fiend had momentarily forgotten.

The young man dying right before his eyes was an existence akin to supernatural powers—something that could not be predicted by his judgment.

GRAB. THRUST!

The Great Snow Fiend was given neither the time nor the strength to respond.

Reflected in his astonished eyes was the sight of one man.

Jin Taekyung had seized the spear shaft with all his strength and driven it even deeper into his own chest.

Then he forced himself forward.

And in his blood-soaked hand, the final flame was burning.

“……!”

Blue-white light-flames spread across the Great Snow Fiend’s widened eyes.

FWOOSH—KWAANG!
```
