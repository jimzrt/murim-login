<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0679.txt",
      "sha256": "95331121eda796f295a3abd57efd329ae2115141b812b1bbdfd4538a01a57655",
      "bytes": 13138
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ed54112b4bcef801367588d386996473341188ddbbff6fa48f112f418c0ad77b",
      "bytes": 1635
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b351f5178dba4d41730778b0904769d9208406a8782b25a6eb5ac14ba5e3e006",
      "bytes": 203156
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "5198356766ee8226bd0b5cadb2cb018e6c6e2263407ba05d78cc5edeea239683",
      "bytes": 980
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "023f8b88ca99d438ab41072d70eacdee978a538714b4e472f47e4510a0b74dbf",
      "bytes": 830
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "d734acf6bcec1f5c3de090e117546e4f8397723a25b7882ed1026ca1ade7302d",
      "bytes": 732
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "08dcb00ab02332edb94760ff8f5457c8951a45da2c91d8097facf2b116733ca0",
      "bytes": 589
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2d25db834ee89c3490c60c92d647dcd4c6ab125c56ea741f5b3aebc7e498b57a",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "a96a302d488b9d50e90c6ab2be580aaa5c909d9603d2982a651256e04303921f",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7b4d363a93c7d4eb10073e613172a7aaa74bbb27160fc5fffa900936ab395a47",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e3f09d1d1aa01d22e8ee9580c7b55dcda9ed98b22d636ff18b9c65db97e9b0b8",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "3c0384e87b3d6a95ad8d0c8b0deb75ccfd87ef12235024189b48c1e6f491f9db",
      "bytes": 648
    },
    {
      "path": "characters/Namho.md",
      "sha256": "f4bddf0a3ed458e576526f66449544b5192a2b784771fb92006bd480fb8bd602",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "c72a3f8af301c59f2767252ceffa991fe79b8a16200b376acec5721f87249c6e",
      "bytes": 936
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "95019b426cd26b793b6336a56f19f5acc5e4afaa94ea3fa86ad4db8442a44666",
      "bytes": 787
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "32e8180b0faffcfe996353c8985a960d2fe6e06f2fd2e2bfd9d0a040e2cfc646",
      "bytes": 864
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3789fd9d21db9bde2dc36ae0d866d00efbdcc2e9935f47281c3d86704d58cb0d",
      "bytes": 210225
    }
  ],
  "estimated_tokens": 13356
}
-->

# Durable State Update — Chapter 679

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 679. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 679. Profile updates may replace only one
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
  "chapter": 679,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 679,
    "continuity_sources": [679],
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
    "Jin Taekyung is facing two Supreme Peak masters in the Poisonblood Grounds after deliberately provoking them.",
    "The disheveled master is Black Hand Fist Demon, who confirms responsibility for the Western Yao Estate killings.",
    "Yohi and Heugung remain captive and alive, awaiting the Southern Heaven Demon Empress's return.",
    "The Southern Heaven Demon Empress is currently absent from the battlefield but has warned her agents to fear Jin.",
    "An unnamed slender Supreme Peak master knows Jin's identity and has begun fighting him with twin wheels.",
    "Jin has awakened the fire dragon in his lower dantian and is fighting with White Flame enveloped in blue-white fire.",
    "Muyaho remains with Jin and refuses to retreat despite the danger.",
    "Namho and three companions have reached the Nanman reconnaissance squad advancing toward the northern border."
  ],
  "continuity_sources": [
    678,
    677
  ],
  "open_questions": [
    "What is the identity and full strength of the slender Supreme Peak master?",
    "Can Jin survive the two-master battle and prevent the Southern Heaven Demon Empress from reaching Yohi and Heugung?",
    "Can Jin protect Muyaho during the fight?",
    "What will Namho and the reconnaissance squad do after reaching the northern border?"
  ],
  "safe_through": 678,
  "temporary_decisions": [
    "Use Black Hand Fist Demon for 흑수권마 while retaining Black Hand for 흑수.",
    "Preserve Jin's abrupt register changes and profanity as deliberate psychological provocation.",
    "Render 쌍륜 as twin wheels."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 은인     | **Benefactor**                               |
| 사천     | **Sichuan**            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 진태경 | 흑수 | hostile_martial_opponent | Black Hand | mocking and profane | Jin sarcastically addresses Black Hand after hearing his sobriquet. |
| 흑수 | 진태경 | hostile_Dark_Heaven_agent_to_enemy_martial_artist | Blazing Flame Divine Dragon Jin Taekyung | taunting and murderous | Black Hand identifies Jin while claiming that killing him will make the sobriquet famous. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 678
- **Aliases:** None
- **Role:** Baeksang is the temporary Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the leader of Nanman's general mobilization, with nearly ten thousand troops stationed in the Inner Palace.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 677
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 678
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand is a sadistic Dark Heaven agent and Supreme Peak master acting under orders associated with the Southern Heaven Demon Empress.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand is the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; a colder senior figure can command him to obey the Demon Empress's orders.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 664
- **Aliases:** None
- **Role:** The Blood Monk is an unidentified, apparently middle-aged bald and beardless martial artist who carries a steel Zen staff and has killed several hundred people in Guizhou; his current destination is unknown.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 677
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 675
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 678
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 678
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 678
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature currently accompanying Jin Taekyung through the Poisonblood Grounds.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and currently carries Jin while aiding his escape.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 678
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 669
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 674
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 676
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger and speaks Han Chinese haltingly but capably.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

## Korean source

```text
＃679화



발 빠른 정예로 꾸려진 척후대의 이동 속도는 쾌속했다.

자그마치 이백여 명이 넘는 머릿수에도 불구하고, 틈틈이 휴식을 취하면서 불과 사흘 남짓한 짧은 시간 만에 북동쪽 경계선에 도달했으니까.

그러나 이들 중 누구도, 심지어 척후대를 이끄는 두 명의 부족장조차도 혈승(血僧)이라는 정체불명의 괴물을 맞닥트리기 전에 또 다른 불청객들이 찾아올 것이라고는 생각하지 못했다.

그리고 이 뜻밖의 상황은, 그들이 전해 준 소식에 비하면 아무것도 아니었다.

“지금…… 뭐라고 했소?”

“그게 무슨!”

장 족장과 고 족장은 믿을 수 없다는 듯이 눈을 부릅떴다.

그 누구도 예상치 못했던 충격적인 정보.

만약 이 정보를 말해 준 것이 남만야수궁의 소궁주가 아니었다면, 단순한 헛소리로 치부하고도 남았을 것이다.

아니, 오히려 헛소리이길 바랐다.

하지만 그들의 간절한 바람에도 불구하고, 야율목의 대답은 바뀌지 않았다.

“전부 사실입니다.”

파르르 떨리는 눈동자에 깃든 진실. 마침내 이 모든 것이 현실임을 자각한 두 부족장은 탄식할 수밖에 없었다.

“이게 도대체…….”

“궁주께서는 왜 그런 선택을 하셨단 말이오, 왜!”

피가 흐를 만큼 주먹을 꽉 움켜쥔 야율목이 입을 열었다.

“아버님께서는 이미 많은 부족장들이 백 숙부, 아니 백상의 손을 잡은 이상 대세를 거스를 수 없으리라 짐작하셨습니다.”

“아무리 그렇다 한들, 한족 몇을 구하기 위해 그런 위험을 자초하셨단 말이오?”

“위험을 자초한 것이 아닙니다.”

“뭐라?”

“아버님께서는 저를 비롯한 이들을 뇌옥으로 보내며 말씀하셨습니다. 옳은 행동에는 옳게 보답하는 것이 신의(信義)이며, 도움을 준 이를 외면하는 것은 불의(不義)다. 그러니 오늘 나는 신의에 명운을 걸어 보려 한다. 진태경과 백상, 그 두 사람에게.”

“……!”

“……!”

두 부족장은 얕은 침음성과 함께 눈을 감았다.

오랫동안 야수묘왕의 곁을 보필한 그들도 어렴풋이 짐작은 하고 있었다. 그가 어떤 사람인지, 어떤 선택을 할지.

하지만…….

“이번만큼은 궁주께서 틀렸소. 차라리 당신을 따르는 부족들과 묘족의 모든 힘을 끌어모아 내궁 안의 역도들을 처단했어야 했어.”

“백번 양보해서 진태경을 믿으신 건 옳은 선택이실지도 모르지. 소궁주가 전한 이야기가 사실이라면 결국 그는 신의를 지키기 위해 홀로 떠났으니. 허나 백상, 그자는 다르오.”

단언하듯 말하는 두 부족장의 모습에, 혹시나 하는 희망을 담아 바라보던 야율목이 입을 열었다.

“아직 섣불리 판단하기에는 이릅니다. 만약 백상이 아버님의 청을 들어주었다면…….”

“소궁주.”

야율목의 말을 끊어 낸 장 족장이 허탈한 목소리로 말을 이었다.

“척후대 내의 한족들을 제압하여 내궁으로 호송하라. 우리가 처음이자 마지막으로 받은 전서는 이게 전부요. 이것이 무슨 뜻인지 알겠소?”

야율목이 멈칫한 그때, 뒤에서 조용히 상황을 지켜보던 남호가 문득 무언가를 깨닫고 신음처럼 중얼거렸다.

“일부러 알리지 않았군.”

“남 노인, 그 말씀은.”

“두말할 것도 없이 여기 있는 두 부족장과 척후대의 전사들은 궁주를 따르는 이들이다. 내궁에서 벌어진 우환(憂患)을 알린다면, 필시 어떤 식으로든 방해가 될 테니 모든 것이 마무리된 다음에 불러들일 생각이었겠지. 혹은…….”

남호가 심유한 눈빛으로 말을 이었다.

“혈승(血僧). 그 노괴에게 처리를 맡길 작정이거나.”

“……!”

“차도살인지계(借刀殺人智計)라, 백상과 암천이 쓸 만한 칼을 골랐구나. 아니, 이 상황이라면 남의 칼도 아니겠군. 혈승 역시 그들과 한패일 가능성이 농후할 테니.”

좌중을 감싸는 싸늘한 침묵. 그들의 흔들리는 시선에 남호는 마음이 무거워지는 것을 느꼈다.

‘좋지 않다. 최악이야.’

뒤에는 지금쯤 백상과 암천에게 장악당했을 남만야수궁. 앞에는 자신들만으로 대적할 수 없는 정체불명의 초절정 고수.

더군다나 이러한 상황에서 누구보다 믿음직한 진태경조차 없다.

‘도대체 어찌해야 한단 말인가.’

은영각에 일평생을 몸담은 그로서도 쉽게 답이 나오지 않는 상황. 그러나 더 늦기 전에 결단을 내려야 한다.

마치 보이지 않는 쇠사슬이 전신을 옭아매고 있는 듯한 답답함 속에서, 남호는 어렵게 입술을 뗐다.

“다른 이들은 어디 있나?”

남호의 말뜻을 파악한 장 족장이 대답했다.

“한족들이라면 만일을 대비하여 억류해 두었소. 어떠한 위해도 가하지 않고 수혈(睡穴)만 짚어 두었지.”

“…….”

“그들을 중원으로 돌려보낼 생각이오?”

정확히 의표를 찌르는 한마디. 잠시 침묵하던 남호가 무겁게 고개를 끄덕였다.

“미안하군. 허나 지금으로서는 이것이 최선일세. 저들이 장강을 건너 남만의 소식을 알린다면, 무림맹은 결코 남만의 상황을 좌시하지 않을 거야.”

“……무림맹이라.”

“나는 남만에서 태어나 중원에서 반평생을 보냈네. 비록 힘없는 늙은이에 불과하지만, 남만과 중원의 사정을 동시에 누구보다 잘 이해하고 있는 사람이야. 내가 아는 무림맹이라면 어떻게든 남만을 도울걸세.”

담담하지만 강한 의지가 실린 목소리.

자신들이 매복해 있는 무성한 풀숲 너머, 끝없이 펼쳐진 너른 장강의 물결을 바라보며 갈등하던 두 부족장은 한숨처럼 입을 열었다.

“빌어먹을.”

“우리가 어찌하면 되겠소?”

이미 생각을 끝마친 남호의 대답은 거침없었다.

“두 가지 방법이 있네. 첫째는 한족들을 풀어 주고, 당장 이곳을 벗어나 백상의 눈을 피해 때를 기다리는 것. 두 번째는 한족들과 함께 중원으로 향하는 것.”

“함께 중원으로 향하라니. 이 근방에는 그만한 규모의 선박이 없는데, 도대체 무슨 수로…….”

“있소. 모두를 실어나를 만한 선박이.”

어디선가 불쑥 들려온 목소리. 동시에 움직인 사람들의 시선 끝에, 태산의 부축을 받아 비틀비틀 일어나는 사마표가 있었다.

“그게 사실인가?”

장 족장의 물음에 사마표가 창백한 얼굴로 대답했다.

“우리가 어찌 남만까지 올 수 있었다고 생각하시오?”

“그 말은 혹시…….”

“장강수로맹의 쾌조선이 그리 멀지 않은 곳에 있소. 서쪽으로 한나절. 어쩌면 반나절만 간다면 합류할 수 있을 거요.”

뜻하지 않은 희소식에 두 부족장의 낯빛에 희망이 떠올랐다.

장강의 지류를 따라 사천까지만 닿아도 중원 무림의 영역권 안에 들어온다.

설령 백상과 암천이 남만야수궁을 장악했더라도, 구파일방과 오대세가를 선봉에 세운 무림맹의 원군이 당도한다면 상황을 뒤집고도 남았다.

‘당장 사천에만도 세 개의 명문대파가 존재한다. 무림맹의 정식 원군이 늦더라도, 그들은 다르지.’

남호는 침착하게 상황을 정리했다.

아미파와 청성파. 그리고 사천당문.

지난 사천 혈사로 많은 피를 흘리고 힘이 약화되었을지언정, 그들의 뿌리는 암천조차 단번에 뽑지 못했을 만큼 깊고 단단하다.

더군다나 세 문파 모두 진태경을 은인으로 생각하고 있으니, 그들이 부름에 응하여 사천 무림의 전력을 이끌고 남만으로 향한다면…….

‘다시 돌아오는 데까지 빠르면 칠주야. 늦어도 열흘이겠지.’

남호는 피 끓는 청년도 아니고, 스스로의 무공을 믿는 무림인도 아니다. 그렇기에 그의 판단은 이 자리의 누구보다 냉정하고도 정확했다.

‘지금 이들을 이끌고 왔던 길을 돌아간다면 필사(必死). 하지만 중원의 힘을 끌어온다면 승산은 충분하다. 그때까지 진태경과 야수묘왕은…….’

그저 믿는 수밖에 없다.

부디 버텨 주기를. 자신들이 돌아오는 그때까지 살아 있기를.

그리고 남호 스스로도 확신하지 못할 소망을 마음속으로 뇌까린 그때.

둥. 둥. 두웅!

남호는. 아니, 끝없이 펼쳐진 강물이 내려다보이는 숲속에 매복해 있던 모두는 보고 들을 수 있었다.

낮은 울림을 토해 내는 북소리와 도도하게 흐르는 장강의 물결을 타고 다가오는 날렵한 선체(船體)를.

“저건…….”

“장강수로맹. 장강수로맹의 쾌조선이군!”

하지만 다음 순간, 화색이 돈 얼굴로 기뻐하던 두 부족장은 이내 이상함을 느끼며 입을 다물었다.

서쪽으로 족히 반나절 이상은 가야 할 쾌조선이, 왜 이곳에 나타났는가.

문득 그들의 뇌리를 스친 의문은 딱딱하게 굳은 남호와 사마표의 표정을 본 순간 불안감으로 변모했고, 신음처럼 흘러나온 남호의 한마디에 현실로 드러났다.

“전투를…… 준비하시오.”

“……!”

서늘한 공포에 휩싸인 좌중 속, 남호는 떠올렸다.

지금 곁에 없는 한 사람을. 그 어느 때보다 간절한 그의 존재를.

‘빌어먹을. 미안하구나.’

어쩌면 그를 구하기도 전에 죽을 수도 있겠다는 생각과 함께.

촤아악. 쿵.

거침없이 물살을 가르며 다가온 선체가 모래밭 위로 거칠게 올라섰다.

그리고…….

저벅.

한바탕 물결이 휩쓸고 지나간 그 자리에, 한 사람의 발걸음이 아로새겨졌다.



* * *



슈확!

공간을 가르며 날아드는 두 개의 빛줄기.

기묘한 움직임과는 달리 섬광처럼 들이닥친 쌍륜(雙輪)을 향해, 나는 백염을 비스듬히 내리그었다.

꽈앙! 구구궁!

엄청난 굉음과 동시에 터져 나온 충격파가 공간을 뒤흔들었지만, 이것으로 끝이 아니다.

칼날처럼 예리한 오감(五感)은 등 뒤에서 일어나는 쌍륜의 움직임을 낱낱이 읽고 있었다.

‘다시 온다.’

나는 주르륵 밀려 나가는 무야호의 목덜미를 붙잡는 동시에 몸을 비틀었다.

쉬익, 서걱!

아슬아슬하게 몸뚱어리를 스치는 푸른 섬광. 예리한 절삭음과 함께 백호의 새하얀 터럭이 허공에 흩날리는 것이 보인다.

기울어진 시야 속에서 미친 들소처럼 달려드는 산발 머리의 괴인(怪人)도 함께.

“놈-!”

흑수권마(黑手拳魔).

그 생소한 별호만큼이나 거무튀튀한 주먹 위로 흑색 강기(罡氣)가 덧씌워지고, 이내 내 가슴을 향해 쏘아졌다.

후웅!

느껴진다. 공기의 파동이. 그리고 놈의 일권에 담겨 있는 무시무시한 힘이. 하지만…….

‘이 정도로는 안 되지.’

작은 뇌까림과 함께, 한껏 비틀었던 신형을 바로 세웠다. 그사이 어느덧 코앞까지 들이닥친 흑색 강기가 불길한 빛을 토해 낸다.

그 너머에서 광기로 번들거리는 흑수권마의 눈동자가 내게 속삭이는 듯했다.

이제 넌 죽었어.

확신에 차 있는 눈빛. 지금까지 마주친 많은 적들에게서 봐 왔던 바로 그 눈빛이다.

삼류 칼잡이부터 초절정 고수까지. 무공의 고하에 상관없이 그들은 늘 그랬고, 결국 모든 것이 끝났을 때 두 발로 서 있던 것은 나였다.

스윽.

느려진 세상 속, 서늘한 창대의 감촉이 손아귀에서 멀어진다.

절묘한 흐름으로 치고 들어온 흑수권마에 의해 창이 가진 이점이 사라진 상황.

한 치의 망설임도 없이 창대를 놓은 나는 그대로 일장(一掌)을 뻗었다.

꽈앙!

굉음과 함께 각기 다른 색을 지닌 두 개의 강기가 맞부딪힌다.

반경 십여 장의 모든 것이 끔찍한 열기에 녹아내리고, 흑수권마의 눈동자가 크게 뜨였다.

“너…….”

단 한 번의 격돌. 하지만 서로의 힘을 가늠하기에는 충분하다.

쌍륜의 영향으로 반 박자 늦게 대처했음에도 흑수권마의 일권을 손쉽게 막아 낸 나는, 흔들리는 놈의 눈동자를 바라보며 담담하게 입을 열었다.

“듣보잡. 맞는데?”

“……!”

잘못되었다는 걸 알아차렸겠지만, 이미 늦었다.

나는 비어 있는 다른 한 손을 그러쥐었다.

화륵.

주먹을 휘감으며 솟구치는 청백색의 화염.

멸염신권(滅炎神拳).

꽈아아앙!
```

## Final English reading copy

```markdown
# Chapter 679

The reconnaissance squad, made up of swift-footed elites, moved at a rapid pace.

Despite numbering more than two hundred people, they reached the northeastern border in barely three days, taking breaks whenever they could along the way.

However, none of them—not even the two tribal chieftains leading the reconnaissance squad—had expected another group of unwelcome visitors to arrive before they encountered the mysterious monster known as the Blood Monk.

And this unexpected situation was nothing compared to the news those visitors had brought.

“What… did you just say?”

“What are you talking about?”

Chief Jang and Chief Go stared wide-eyed in disbelief.

It was shocking information that no one could have anticipated.

If the one who had delivered it had not been the Young Palace Lord of the Nanman Beast Palace, they would have dismissed it as nothing more than absurd nonsense.

No. They had actually hoped it was nonsense.

But despite their desperate wish, Yayul Mok’s answer did not change.

“It is all true.”

The truth shone in his quivering eyes. At last realizing that all of this was reality, the two chieftains could do nothing but sigh.

“What in the world…”

“Why did the Palace Lord make such a choice? Why?”

Yayul Mok clenched his fists so tightly that blood ran from his palms before opening his mouth.

“My father had already guessed that he would be unable to resist the tide of events once so many chieftains had joined hands with Uncle Baek—no, with Baeksang.”

“Even so, did he really bring this danger upon himself just to save a few Han Chinese?”

“He did not bring danger upon himself.”

“What?”

“My father said this when he sent me and the others to the underground prison. He said that repaying a righteous act with righteousness was keeping faith, and that turning away from someone who had helped us was injustice. So today, I intend to stake my fate on keeping faith. On those two people—Jin Taekyung and Baeksang.”

“……!”

“……!”

The two chieftains closed their eyes with quiet groans.

Having served at the Beast Miao King’s side for a long time, they had vaguely guessed what kind of person he was and what choices he would make.

But…

“This time, the Palace Lord was wrong. He should have gathered all the strength of the tribes that followed him and the Miao people, then executed the traitors in the Inner Palace.”

“Even if we give Jin Taekyung every benefit of the doubt, trusting him may have been the right choice. If the Young Palace Lord’s story is true, Jin Taekyung ultimately left alone in order to keep faith. But Baeksang is different.”

As the two chieftains spoke with such certainty, Yayul Mok, who had been looking at them with a trace of hope, opened his mouth.

“It is too early to judge. If Baeksang honored my father’s request…”

“Young Palace Lord.”

Chief Jang cut him off and continued in a hollow voice.

“Subdue the Han Chinese within the reconnaissance squad and escort them to the Inner Palace. This is the first and last missive we received. Do you understand what it means?”

Yayul Mok stopped short.

Behind him, Namho had been quietly watching the situation. Then he suddenly realized something and muttered as if groaning.

“He deliberately didn’t tell us.”

“Elder Namho, what do you mean?”

“There is no need to say more. The two chieftains here and the warriors in the reconnaissance squad are all people who follow the Palace Lord. If they were told about the trouble in the Inner Palace, they would surely interfere somehow. He probably intended to call them back after everything was finished. Or…”

Namho continued with a grave look in his eyes.

““Or… the Blood Monk. He may have planned to let that old monster deal with them.””

“……!”

“A borrowed knife to kill others. Baeksang and Dark Heaven chose a useful blade. No, in this situation, it isn’t even someone else’s blade. There is a strong possibility that the Blood Monk is in league with them as well.”

A frigid silence descended over the group. Seeing their unsteady gazes, Namho felt his heart grow heavy.

*This is bad. The worst.*

Behind them was the Nanman Beast Palace, which was likely under Baeksang and Dark Heaven’s control by now. Ahead of them was a mysterious Supreme Peak master they could not oppose on their own.

And in this situation, even Jin Taekyung—the person they trusted more than anyone—was absent.

*What in the world are we supposed to do?*

Even after a lifetime in the Hidden Shadow Pavilion, Namho could not easily find an answer. But they had to make a decision before it was too late.

Amid the suffocating feeling that invisible chains were wrapped around his entire body, Namho finally forced his lips apart.

“Where are the others?”

Chief Jang understood what he meant and answered.

“If you mean the Han Chinese, we detained them as a precaution. We did not harm them in any way. We merely struck their Sleep Acupoints.”

“……”

“Do you intend to send them back to the Central Plains?”

The question caught Namho squarely off guard. After a brief silence, Namho nodded heavily.

“I’m sorry. But for now, this is the best option. If they cross the Yangtze and report what is happening in Nanman, the Murim Alliance will never stand by and do nothing.”

“……The Murim Alliance.”

“I was born in Nanman and spent half my life in the Central Plains. Though I am nothing more than a powerless old man, I am someone who understands the circumstances of both Nanman and the Central Plains better than anyone. If it is the Murim Alliance I know, they will find a way to help Nanman.”

His voice was calm, but it carried a powerful resolve.

Beyond the dense grass where they were lying in ambush, the two chieftains gazed at the broad, endless waters of the Yangtze before opening their mouths with sighs.

“Damn it.”

“What should we do?”

Namho had already finished thinking. His answer came without hesitation.

“There are two ways. First, release the Han Chinese, leave this place at once, avoid Baeksang’s eyes, and wait for the right moment. Second, head to the Central Plains together with the Han Chinese.”

“Head to the Central Plains together? There is no ship of sufficient size anywhere around here. How are we supposed to—”

“There is one. A ship large enough to carry everyone.”

The voice came from somewhere nearby.

Everyone turned at once to see Sama Pyo staggering to his feet with Taishan’s support.

“Is that true?”

At Chief Jang’s question, Sama Pyo answered with a pale face.

“How do you think we managed to come all the way to Nanman?”

“Could that mean…”

“The swift ship of the Yangtze River Channel League is not far from here. It’s half a day to the west. If we travel for even half that time, we might be able to rendezvous with it.”

Unexpected good news brought hope to the two chieftains’ faces.

Even reaching Sichuan by following one of the Yangtze’s tributaries would bring them within the domain of the Central Plains Murim.

Even if Baeksang and Dark Heaven had seized control of the Nanman Beast Palace, the arrival of reinforcements from the Murim Alliance—with the Nine Sects and One Gang and the Five Great Families at the forefront—would be more than enough to turn the situation around.

*There are already three prestigious great sects in Sichuan alone. Even if the Murim Alliance’s official reinforcements are delayed, those three will be different.*

Namho calmly sorted through the situation.

The Emei Sect, the Qingcheng Sect, and the Sichuan Tang Clan.

Even though they had shed much blood and weakened during the Sichuan Bloodbath, their roots ran deep and firm enough that even Dark Heaven could not tear them out in a single stroke.

Moreover, all three sects considered Jin Taekyung their Benefactor. If they answered the call, gathered the strength of Sichuan Murim, and headed for Nanman…

*It would take seven days and nights at the fastest to return. Ten days at the latest.*

Namho was neither a hot-blooded youth nor a martial artist who trusted in his own martial arts. That was why his judgment was colder and more accurate than anyone else’s in this place.

*If I lead these people back the way we came, we will certainly die. But if we bring in the strength of the Central Plains, we have more than enough of a chance. Until then, Jin Taekyung and the Beast Miao King will…*

They had no choice but to trust them.

To hope they would hold out. To hope they would remain alive until Namho and the others returned.

And just as Namho was muttering that hope—one he could not even fully convince himself of—in his heart…

Boom. Boom. Booooom!

Namho heard it.

No—everyone lying in ambush within the forest overlooking the endless river could both see and hear it.

A drumbeat that rumbled low, and a sleek hull riding the currents of the Yangtze as it approached.

“What is that…?”

“The Yangtze River Channel League. That’s the Yangtze River Channel League’s swift ship!”

But the next moment, the two chieftains, who had been celebrating with brightened faces, sensed something strange and fell silent.

The swift ship should have been at least half a day away to the west.

Why had it appeared here?

The question flashed through their minds. Then, when they saw Namho and Sama Pyo’s rigid expressions, it transformed into unease.

Namho’s words, which escaped like a groan, revealed the truth.

“Prepare for battle.”

“……!”

As the group was swept up in a chill of fear, Namho thought of the one person who was not beside him.

The one whose presence he needed more desperately than ever.

*Damn it. I’m sorry.*

Along with the thought that they might die before they could save him.

*Crash. Boom.*

The hull cut fiercely through the water and ran hard aground on the sandy shore.

And then…

*Step.*

In the place where a wave had swept through, one person’s footsteps were etched into the ground.

* * *

Whoosh!

Two streaks of light flew through the air, cleaving space.

Despite their strange movements, the twin wheels came at me like flashes of light. I swung White Flame diagonally downward to meet them.

KWA-BOOM! Rumble-rumble!

A tremendous roar erupted as a shockwave tore through the area and shook the air. But it was not over yet.

My five senses, sharp as blades, tracked every movement of the twin wheels behind me.

*They’re coming again.*

As Muyaho slid backward, I caught him by the nape and twisted my body.

Whoosh—shhk!

A blue flash barely grazed my body. Along with the sharp sound of something being sliced, I saw the White Tiger’s snow-white fur scatter through the air.

In my tilted field of vision, another sight came into view: a wild-haired freak charging at me like a mad bison.

“You bastard—!”

The Black Hand Fist Demon.

Black Force layered itself over his dark fist, and then he shot it straight toward my chest.

Whoom!

I could feel it—the wave of air, and the terrifying power contained in his punch. But…

*That won’t be enough.*

With a brief mutter, I straightened the body I had twisted as far as it would go. By then, the black Force had already reached point-blank range and was giving off an ominous light.

Beyond it, the Black Hand Fist Demon’s eyes gleamed with madness, as if whispering to me.

*You’re dead now.*

It was a gaze filled with certainty. I had seen that same look in the eyes of many enemies before.

From Third Rate swordsmen to Supreme Peak masters. Regardless of their level of martial arts, they had always worn that expression.

And when everything was over, I was always the one still standing on two feet.

*Swish.*

In the slowed-down world, the cool feel of the spear shaft slipped away from my hand.

The Black Hand Fist Demon had entered with such exquisite timing that the spear’s advantage had disappeared.

Without a moment’s hesitation, I let go of the spear and thrust out a palm.

KWA-BOOM!

Two Forces of different colors collided with a deafening roar.

Everything within a radius of ten-odd jang[^1] melted beneath the horrific heat, and the Black Hand Fist Demon’s eyes flew wide open.

“You…”

A single clash. But it was enough to measure each other’s strength.

Even though the twin wheels had made me react half a beat late, I had easily blocked the Black Hand Fist Demon’s punch. Looking into his wavering eyes, I spoke calmly.

“A nobody. Right?”

“……!”

He had realized that something had gone wrong, but it was already too late.

I clenched my empty hand.

Fwoosh.

Blue-white flames surged up around my fist.

Flame-Extinguishing Divine Fist.

KWA-AAANG!

[^1]: A *jang* is a traditional Korean unit of length, roughly three meters.
```
