<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0682.txt",
      "sha256": "e8e1f2cdc3acb612c47dbda9e9f94c373aa1cc1202f84cee837c1fc70f127798",
      "bytes": 12797
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "61a84f33542dbbeb21e0a9504dd10edba13e2f3837f980c7a7f36a4e362a9e14",
      "bytes": 2251
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2e426e19e3322dc40c82e31e0823ab238132180a4a4936d60bb754a6b73f07e4",
      "bytes": 203506
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "36e9478598e3e1b69a7869b74ccf9c9828b8d357b9e9982666f11a24841ec1aa",
      "bytes": 763
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "3aecf36eb0e138c4ac992bc7bd73240834dad036527a993d88483829502118f2",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3febde908a1e33b2d3af27be3ced9510d21732f74fb01d3dbb7887a49f0700d8",
      "bytes": 553
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "c27615c4ac8a6478cc26dc805407f36c2eaa4eeae1cae5f1d334cc2bd634f1cd",
      "bytes": 919
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2dc45573ed4c23ca12efe2fc1bd95c7f6958763b72ec6e422d72294e0d0490c4",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "aeebe6686df4c44e2a9281a2da964f8c568bed7e56566405b810282ec66a31ae",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "97d4c96d8178c0a9491896a53355642439be8993ed6ab87d8c401fdd7c3c80d8",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "412bf6cac42dd1ab52f04ff108a0328b89945c92277058939189461b52961b71",
      "bytes": 1061
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "9ab1823e4729dd18b5da239ae1655fc620aac779a6e11d83bb988cdbdf322b7c",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ce8129c193a78b37cbe9727552a254ff51c134d12f8554e281db6d525431052f",
      "bytes": 210824
    }
  ],
  "estimated_tokens": 12677
}
-->

# Durable State Update — Chapter 682

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 682. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 682. Profile updates may replace only one
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
  "chapter": 682,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 682,
    "continuity_sources": [682],
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
    "Jin survived the Great Snow Fiend's attack but has severe internal injuries and extreme Yin-Cold Qi; he has temporarily stabilized himself and remains able to fight.",
    "The Great Snow Fiend and Black Hand Fist Demon are attacking Jin together in the Poisonblood Grounds, and Jin has resumed the fight.",
    "The Southern Heaven Demon Empress ordered the Great Snow Fiend to capture Jin alive if possible because he may become a major future threat.",
    "The Great Snow Fiend is senior to Black Hand and can command him; Black Hand obeyed after protesting the capture order.",
    "The Great Snow Fiend killed the former Sect Leader of the Zhongnan Sect during the Great Faction War and later escaped from Great Snow Mountain.",
    "White Tiger remains beside Jin and warned him while he was incapacitated.",
    "The Yangtze River Channel League's swift ship has arrived at the reconnaissance squad's position with an unidentified person aboard.",
    "Namho plans to escort the detained Han Chinese reconnaissance members to the Central Plains for aid to Nanman.",
    "Yohi and Heugung remain captive and alive, awaiting the Southern Heaven Demon Empress's return."
  ],
  "continuity_sources": [
    681,
    680
  ],
  "open_questions": [
    "Can Jin survive and defeat the Great Snow Fiend and Black Hand Fist Demon?",
    "Who arrived on the Yangtze River Channel League's swift ship, and why did it come directly to the reconnaissance squad's position?",
    "Can Namho's group reach the Central Plains and bring reinforcements before Nanman is overwhelmed?",
    "Will the Blood Monk act with Baeksang and Dark Heaven, and what will happen to the Beast Miao King's loyalists in the Inner Palace?",
    "What will happen to Yohi and Heugung when the Southern Heaven Demon Empress returns?"
  ],
  "safe_through": 681,
  "temporary_decisions": [
    "Use Demon Empress for 마후, referring to the Southern Heaven Demon Empress.",
    "Use White Rice Cake for 백설기 as the Great Snow Fiend's mocking near-sobriquet.",
    "Use Ice God for 빙신 and preserve the accompanying pun on the insult 병신.",
    "Use Yin Freak for 음괴 as one member of the Yin-Yang Twin Freaks."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 권법     | **fist technique**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 백중 | **Baekjung** | Traditional Buddhist observance during which the Shaolin attack occurs. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 사검 | **Snake Sword** | Crooked-bladed weapon resembling a snake. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 진태경 | 흑수 | hostile_martial_opponent | Black Hand | mocking and profane | Jin sarcastically addresses Black Hand after hearing his sobriquet. |
| 흑수 | 진태경 | hostile_Dark_Heaven_agent_to_enemy_martial_artist | Blazing Flame Divine Dragon Jin Taekyung | taunting and murderous | Black Hand identifies Jin while claiming that killing him will make the sobriquet famous. |
| 흑수권마 | 대설귀 | junior hostile subordinate to senior ally | Senior | deferential but urgent and protesting | Black Hand protests the Great Snow Fiend's order to capture Jin. |
| 대설귀 | 흑수권마 | senior hostile commander to junior subordinate | you | blunt, commanding, and threatening | The Great Snow Fiend orders Black Hand to stop questioning him. |

## Listed compact profiles

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 681
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand is a sadistic Dark Heaven agent and Supreme Peak master acting under orders associated with the Southern Heaven Demon Empress.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand is the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; the Great Snow Fiend is his senior and can overrule him under the Southern Heaven Demon Empress's orders.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 661
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 681
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 681
- **Aliases:** None
- **Role:** The Great Snow Fiend is the former ruler of Great Snow Mountain and a fiend who killed Baekhwi and Venerable Wusang during the Great Faction War; the Southern Heaven Demon Empress has personally ordered him to capture Jin Taekyung alive if possible.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend is an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he is senior to Black Hand and acts under the Southern Heaven Demon Empress's orders.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 681
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 681
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 681
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 676
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 680
- **Aliases:** None
- **Role:** The Martial God is an unidentified legendary martial artist who defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone more than fifty years ago.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

## Korean source

```text
＃682화



쐐애애액!

정면으로 쇄도해 오는 진태경을 바라보며, 대설귀(大雪鬼)는 마음속으로 뇌까렸다.

‘그래, 오너라.’

어린놈의 세 치 혓바닥에 오랜만의 동요를 느꼈지만, 달라지는 것은 없다.

상대가 새파랗다 못해 핏덩이나 다름없는 약관의 애송이라는 것은 진작 머릿속에서 지워 버린 지 오래였으니까.

어찌 감히 그럴 수 있겠는가. 대설귀가 파악한 진태경은 고금을 통틀어도 유례를 찾기 힘든 괴물이었다.

이미 아득한 무림 역사에 거대한 족적을 남긴 거인들, 삼성(三星)과 십왕(十王)조차 최소 이립이 넘은 후에야 초절정의 경지에 올랐다는 것을 생각하면 더더욱 그랬다.

무시무시한 재능. 그리고 턱없이 젊은 나이.

검성 매종학의 진전을 이었다는 또 다른 천재, 화산파의 청풍과 함께 가장 위험한 걸림돌이 될 것이 분명했다.

‘적어도 향후 오십 년 안에 무신(武神)과 천마(天魔)에 필적할 괴물로 성장할 터. 반드시 지금 처리해야 한다.’

자신의 직속 상관인 남천마후가 무슨 의중으로 진태경의 생포를 명했는지, 대설귀는 정확한 내막을 알지 못했다.

다만 이 순간만큼은 자신의 판단을 확신할 뿐이었다.

‘마후(魔后), 이번엔 당신이 틀렸소. 놈은…… 결코 살려 둬서는 안 되는 존재요.’

닿지 않을 한 마디와 함께, 대설귀의 소매 사이로 쌍륜(雙輪)이 거친 울음소리를 토해 냈다.

우우우웅!

이미 무공과 정체가 드러난 이상, 힘을 숨긴다 한들 얻을 수 있는 이득은 없다.

전신의 감각을 집중한 채 빠르게 가까워지는 진태경의 신형을 주시하던 대설귀의 눈이 번뜩였다.

‘지금!’

바로 그 순간이었다.

쉬잉!

가파르게 회전하던 쌍륜(雙輪)이 주름진 손을 떠난 것은.

슈화아악!

극한의 음한지기를 한껏 머금은 쌍륜이 공간을 얼리며 쏘아졌다.

오직 대설귀의 의지에 따라 기괴한 움직임을 그린 두 개의 날붙이가 떨어져 내린 그곳에는, 어느덧 삼 장 앞까지 들이닥친 진태경이 있었다.

콰앙!

굉음과 함께 푸르고 흰 섬광이 뒤섞인다.

화염과 얼음의 격돌. 단 한 번의 휘두름으로 쌍륜을 튕겨 낸 진태경이 안개처럼 내리깔린 수증기를 뚫고 튀어나왔다.

쐐액!

처음과 다를 것 없어 보이는 쾌속한 움직임. 하지만 대설귀의 날카로운 안력(眼力)은 모든 것을 낱낱이 파악하고 있었다.

‘잠시 억누르고 있는 것일 뿐. 놈에게는 분명 내상의 여파가 남아 있다.’

아주 미세한 차이였지만 분명히 보인다. 처음과는 달리 미묘하게 흐트러진 움직임과 거칠어진 기세가.

이 순간, 대설귀의 눈동자에 비친 진태경은 상처 입은 맹수였다. 여전히 날카로운 발톱을 지녔음에도 빠르게 지쳐 가고 있는.

그리고 대설귀는 이런 맹수를 사냥하는 법을 누구보다 잘 알고 있는 숙련된 사냥꾼이었다.

‘이대로라면 놈을 쓰러트리는 것은 시간문제.’

심지어 지금 그의 곁에는 흑수권마(黑手拳魔)라는 사냥개가 함께하고 있었다.

비록 맹수의 목덜미에 이빨을 박아 넣을 만큼 강하지는 않지만, 사냥꾼을 대신해서 맹수에게 달려들 수 있을 만큼은 난폭한 사냥개가.

파팟!

“흑수!”

사냥꾼은 뒤로, 사냥개는 앞으로.

정확히 진태경이 다가오는 거리만큼, 훌쩍 뒤로 물러난 대설귀의 외침에 흑수권마가 진태경을 향해 달려들었다.

“노옴!”

분노에 가득 찬 노호성과 함께, 강대한 공력을 머금은 수십여 개의 장력(掌力)이 쏘아졌다.

콰아아아!

파도처럼 덮쳐 오는 흑색 강기. 동시에 진태경의 손에 들려 있던 창이 흐릿해졌다.

슈화악!

선택받은 자들만이 발을 들일 수 있다는 초절정의 영역.

불과 약관 어림의 나이로 그 경지에 오른 젊은 괴물은 한 치의 망설임도 없이 창을 내뻗었고, 창날을 휘감은 청백색의 화염은 검은 파도의 중심을 파고들었다.

퍼엉!

정확히 일점(一點)을 찌른 일격.

강기의 파도를 반으로 가르고 터트리며 쏘아지는 진태경의 모습에 대설귀는 허공을 향해 양손을 내리그었다.

그와 동시에 앞서 창날에 튕겨 나간 채 허공 어딘가를 배회하던 쌍륜이 밑으로 내리꽂혔다.

쉬이이이잉!

마치 살아 있는 생물과도 같은 움직임.

누군가는 이것을 허공섭물(虛空攝物), 혹은 줄이나 실 따위를 이용하여 펼치는 사검(絲剣)이라 부르겠지만, 둘 다 틀렸다.

쌍륜을 움직이는 것은 대설귀의 의지 그 자체였고, 오직 중단전(中丹田)의 힘으로 움직이는 쌍륜에는 한 가지 목표만이 담겨 있었다.

‘죽어라.’

오직 한 사람을 향한, 얼음처럼 서늘한 살의(殺意).

각기 다른 방향으로 꺾이며 섬광처럼 떨어져 내리는 두 개의 륜과 광폭한 기세를 흘리며 쏘아지는 흑수권마의 신형까지.

쉬잉! 쐐애애액!

삼면(三面)에서 동시다발적으로 들이닥치는 세 개의 섬광.

그 죽음의 교차점에 존재하는 진태경을 바라보며 대설귀는 확신했다.

‘이대로 흑수권마와 맞붙는다면 무사하지 못할 터. 놈은 반드시 물러날 테니 그 틈을 노려서…….’

하지만 그 순간, 진태경의 움직임은 대설귀의 생각을 송두리째 무용지물로 만들었다.

파팟!

진태경은 나아갔다. 한 치의 물러섬도, 망설임도 없이.

머리 위로 날아드는 쌍륜을 향해 벼락처럼 창을 휘두르고, 절벽 끝에 몰려 달려드는 호랑이의 앞발처럼 일권(一拳)을 떨쳤다.

꽈앙! 콰드드득!

곧이어 대설귀는 똑똑히 볼 수 있었다.

터어엉!

하늘이 쪼개지는 듯한 굉음과 번쩍이는 섬광 속, 진태경의 어깨너머로 솟구치는 한 자루의 창.

쉬이이익! 서걱!

그리고 손에서 놓쳐 버린 애병을 뒤로한 채, 흑수권마와 격돌한 진태경의 어깨를 벼락처럼 가로지르는 쌍륜을.

서걱! 푸화아악!

분수처럼 터져 나오는 선홍빛 핏물과 비틀거리는 신형.

순식간에 벌어진 이 예상치 못한 상황에, 그토록 냉철했던 대설귀조차 석벽 깊숙이 파고든 쌍륜을 회수하지 못하고 멈칫했다.

‘도대체 왜 그런 선택을.’

대설귀로서는 이해할 수 없는 일이었다. 만약 자신이 같은 입장이었다면 일말의 망설임도 없이 회피를 택했을 테니까.

그러나 그의 생각은 더 이상 이어지지 못했다.

구구구궁!

진태경과 흑수권마. 두 초절정 고수를 중심으로 터져 나온 기파가 공간을 뒤흔들었다.

허공에서 맞닿은 각자의 일권은 물러서지도, 나아가지도 못한 채 파르르 떨리고 있었다,

백중세(伯仲勢).

순간 뇌리를 스치는 세 글자와 함께, 대설귀의 신형이 흐릿해졌다.

쉬익!

지금의 진태경은 연이은 부상으로 지쳐 있는 상태.

같은 초절정 고수임에도 명백하게 한 수 아래인 흑수권마가 잠시나마 동수를 이루고 있는 것이 그 증거였고, 대설귀는 예상보다 일찍 찾아온 기회를 놓칠 만큼 어설픈 사냥꾼이 아니었다.

‘지금이야말로 적기(適期).’

비록 상처 입고 피 흘리는 맹수라 해도, 맹수는 맹수다. 흑수권마라는 사냥개는 결코 저 어린 맹수를 당해 내지 못한다.

맹수의 숨통을 끊을 수 있는 유일한 존재, 사냥꾼이 나서지 않는다면.

‘놈을 죽여야 한다. 지금 당장.’

찰나의 순간 이루어진 판단은 냉정했고, 나아가는 신형은 섬전과도 같았다.

파스슥. 내딛는 걸음마다 대설귀의 전신에서 흘러나온 음한지기가 공기를 얼린다.

단 삼보(三步) 만에 이십여 장의 거리를 지우며 쏘아진 그는, 흑수권마의 어깨너머로 보이는 한 사람을 확인할 수 있었다.

‘진태경.’

보인다. 느껴진다.

하아. 하.

거친 호흡과 창백한 얼굴. 쌍륜이 스치듯 머물다 떠난 상반신은 선홍빛 핏물로 흠뻑 젖어 있었고, 어느덧 코앞까지 들이닥친 사냥꾼의 존재를 발견한 맹수의 눈동자는 잘게 흔들렸다.

‘내 판단이 옳았다.’

차갑게 가라앉아 있던 대설귀의 눈동자에 확신이 깃들었다.

열화신룡 진태경. 열화문의 계승자이자 화왕 적천강의 후인.

먼 훗날, 언젠가 새로운 무신(武神)이 되어 천하를 굽어볼 중원의 신룡은 구름 위의 존재가 되기 전에 죽을 것이다.

다름 아닌 오늘 이 자리에서.

바야흐로…… 사냥의 시간이다.

스아아아.

바람이 불었다. 잠시 뜨겁게 달아올랐던 공기와 대지에 냉기를 불어넣고, 산천초목을 서리로 뒤덮을 바람이.

그리고 그것은 누군가에게 절망을, 다른 누군가에게는 희망을 심어 주는 설풍(雪風)이었다.

‘왔다. 그가 왔어!’

흑수권마는 입술 사이로 튀어나오려는 환호를 간신히 참았다.

그는 평소 대설귀를 좋아하지 않았다. 아니, 평상시 대설귀가 보인 태도를 생각하면 이런 표현조차 후하다.

항상 종놈을 대하는 듯한 고압적인 말투와 자신을 한참 밑으로 보는 듯한 눈빛. 무공만 따라 줬다면 진즉 남천마후의 눈을 피해 죽여 버렸을지도 모른다.

하지만 지금 같은 상황에서 대설귀의 존재는 천군만마나 다름없었다.

흑수권마는 어느새 황급히 신형을 빼려는 진태경을 바라보며 광기 어린 미소를 지었다.

‘이 찢어 죽여도 시원치 않을 열화문의 제자 놈. 네놈은 절대 빠져나가지 못한다.’

콰드득!

찰나의 순간, 갈고리처럼 펼쳐진 손이 막 떨어지려던 진태경의 주먹을 감싸 안았다.

흑수권마가 권법만큼이나 오랜 세월 익혀 온 금나수(禁拿囚)다.

치지지직. 용암과도 같은 열기에 금방이라도 두 손이 타오를 것 같았지만, 흑수권마는 개의치 않았다.

단 한 순간이면 충분하다. 그럼 이 고통도, 진태경의 목숨도 끝장날 테니까.

흑수권마는 진태경의 부릅떠진 눈동자를 바라보며, 환호하듯 외쳤다.

“선배!”

그리고 대설귀는 흑수권마의 외침이 끝나기도 전, 그의 부름에 응답했다.

오직 극한의 음한지기만으로 만들어낸 빙검(氷劍)을, 흑수권마의 등에 쑤셔 넣는 것으로.

퍼걱!

“……!”

느려진 세상 속, 한 줄기 파육음과 동시에 덜컥 굳는 흑수권마의 신형.

하지만 대설귀에게 있어 임무를 다한 사냥개의 반응 따위는 아무런 상관도 없었다.

차갑게 가라앉은 그의 시선은 오직 한 곳, 고통과 경악으로 부릅떠진 눈을 한 진태경을 향하고 있었다.

아니, 분명 그랬어야 할 터였다.

먼 옛날, 대설산에서 마주했던 종남파의 전대 장문인이 그랬던 것처럼.

그리고 이미 죽음을 맞이한 흑수권마처럼.

강대한 음한지기를 품은 빙검에 꿰뚫려 죽었어야 했다.

하지만…….

‘이게 무슨.’

얼어붙은 것처럼 미동도 하지 않던 대설귀의 눈빛이 파르르 떨렸다.

천천히 내리깐 그의 시선이 도달한 곳에, 자신의 가슴에 닿아 있는 누군가의 손이 보였다.

대설귀가 내지른 빙검과 동시에, 아니. 그보다 미세하게 앞서 흑수권마의 가슴을 관통한 그 손은, 붉으면서도 푸르렀고 푸르면서도 눈부셨다.

화륵.

뜨겁다. 살과 뼈. 육신 안의 영혼마저 타들어 갈 만큼.

핏물을 머금고 타오르는 청백색의 겁화를 바라보며, 대설귀는 끓어오르는 듯한 목소리로 중얼거렸다.

“도대체. 어떻게?”

그리고 다음 순간, 진태경의 담담한 목소리가 그의 귓가를 파고들었다.

“좀 더 위로 찔렀어야지. 나한테 경험치를 줄 생각이 아니었다면.”

뭐?

대설귀는 다시 한번 묻고 싶었지만, 진태경은 그의 질문을 허락하지 않았다.

퍼엉!

전신을 불태우는 듯한 끔찍한 열기 너머, 대설귀는 볼 수 있었다.

‘저건.’

허물어지는 흑수권마의 몸뚱어리와, 진태경의 상반신에 걸쳐진 정체모를 붉은 갑옷을.

콰드드득!
```

## Final English reading copy

```markdown
# Chapter 682

SHWAAAAK!

As he watched Jin Taekyung charge straight toward him, the Great Snow Fiend muttered inwardly.

*Yes. Come.*

The boy’s three-inch tongue had stirred him for the first time in a long while, but nothing had changed.

He had erased from his mind long ago the fact that his opponent was a green youngster barely twenty, so young he was practically a newborn.

How could he dare to do otherwise? The Jin Taekyung the Great Snow Fiend had assessed was a monster without equal throughout all of history.

The Three Saints and Ten Kings—giants who had already left enormous footprints across the distant history of the Murim—had not reached the Supreme Peak realm until after they were at least thirty.

That made Jin Taekyung all the more astonishing.

Terrifying talent. And an absurdly young age.

Alongside another genius who had inherited Sword Saint Mae Jonghak’s legacy, Cheongpung of Huashan, he was certain to become one of the most dangerous obstacles.

*At the very least, within the next fifty years, he will grow into a monster capable of matching the Martial God and Heavenly Demon. He must be dealt with now.*

The Great Snow Fiend did not know the full reason why his direct superior, the Southern Heaven Demon Empress, had ordered Jin Taekyung captured alive.

But at this moment, he was certain of his own judgment.

*Demon Empress, you are wrong this time. He… is not someone who can ever be allowed to live.*

Along with words that would never reach their intended listener, the twin wheels let out a harsh howl from within the Great Snow Fiend’s sleeves.

WOOOOONG!

Now that his martial arts and identity had been exposed, there was nothing to gain from holding back his strength.

The Great Snow Fiend focused every sense throughout his body and watched Jin Taekyung’s rapidly approaching figure. His eyes flashed.

*Now!*

It happened at that very moment.

SHWING!

The rapidly spinning twin wheels left his wrinkled hand.

SHWAAAAK!

The twin wheels, filled to the brim with extreme Yin-Cold Qi, shot forward, freezing the space around them.

The two blades traced grotesque paths according to the Great Snow Fiend’s will. At the point where they descended, Jin Taekyung had already closed to within three jang.[^1]

KWAANG!

A tremendous roar erupted as blue and white flashes collided.

Fire and ice clashed.

With a single swing, Jin Taekyung knocked the twin wheels away, then burst through the mistlike steam that had settled over the ground.

SHWAAK!

His movement was swift, appearing no different from before.

But the Great Snow Fiend’s sharp eyes had grasped every detail.

*He is only suppressing it for the moment. The aftereffects of his internal injuries are certainly still with him.*

The difference was minuscule, but it was clear.

His movements were subtly disordered compared to before, and his momentum had grown rougher.

In the Great Snow Fiend’s eyes, Jin Taekyung was a wounded beast.

His claws were still sharp, but he was rapidly growing tired.

And the Great Snow Fiend was a seasoned hunter who knew better than anyone how to hunt such a beast.

*At this rate, bringing him down is only a matter of time.*

He even had a hunting dog beside him in the form of the Black Hand Fist Demon.

The dog was not strong enough to sink its teeth into the beast’s neck, but it was savage enough to charge at the beast in place of the hunter.

PAT-PAT!

“Black Hand!”

The hunter moved back. The hunting dog moved forward.

The Great Snow Fiend retreated a great distance, matching exactly the distance Jin Taekyung had advanced, and shouted. In response, the Black Hand Fist Demon charged toward Jin Taekyung.

“Youuu!”

Along with a roar filled with rage, dozens of palm strikes packed with powerful internal energy shot forward.

KRAAAAA!

A wave of black Force surged toward him.

At the same time, the spear in Jin Taekyung’s hand blurred.

SHWAAAAK!

The realm of Supreme Peak, where only the chosen could set foot.

The young monster who had reached that realm at barely twenty thrust out his spear without a moment’s hesitation. Blue-white flames coiling around the spearhead bored into the center of the black wave.

BOOM!

A strike that pierced a single point exactly.

As Jin Taekyung split the wave of Force in half and blasted through it, the Great Snow Fiend swept both hands downward through the air.

At the same time, the twin wheels that had been knocked away by the spearhead and were circling somewhere in the air plunged downward.

SHWIIIIING!

Their movements were like those of living creatures.

Some might have called it Seizing an Object Through Empty Space, or Snake Sword, a technique performed with cords or threads.

Both would have been wrong.

What moved the twin wheels was the Great Snow Fiend’s own will. And the twin wheels, moved solely by the power of his Middle Dantian, contained only one purpose.

*Die.*

A killing intent as cold as ice, directed at one person alone.

The two wheels bent in different directions and descended like flashes of light. At the same time, the Black Hand Fist Demon’s figure shot forward, trailing a savage momentum.

SHWING! SHWAAAAK!

Three flashes arrived at once from three directions.

The Great Snow Fiend looked at Jin Taekyung, standing at the intersection of death, and felt certain.

*If he clashes with the Black Hand Fist Demon like this, he will not come away unharmed. He will retreat. I will use that opening to…*

But at that moment, Jin Taekyung’s movement rendered the Great Snow Fiend’s entire line of thought useless.

PAT!

Jin Taekyung advanced.

He did not retreat even an inch. He did not hesitate.

He swung his spear like lightning toward the twin wheels flying overhead, then dropped one fist like the forepaw of a tiger charging after being driven to the edge of a cliff.

KWAANG! KRRRUNCH!

The Great Snow Fiend saw it all clearly.

THOOM!

Within the tremendous roar that sounded as if the sky were splitting apart and the flash of light that followed, a spear rose over Jin Taekyung’s shoulder.

SHWIIIIK! SHRAK!

And then the twin wheel that slashed across Jin Taekyung’s shoulder like a bolt of lightning, while he clashed with the Black Hand Fist Demon and left the beloved spear that had slipped from his hand behind.

SHRAK! FWOOSH!

Bright-red blood burst out like a fountain, and Jin Taekyung’s figure staggered.

At this wholly unexpected development that had unfolded in an instant, even the normally cold Great Snow Fiend faltered. He could not retrieve the twin wheels buried deep in the stone wall.

*Why would he choose that?*

The Great Snow Fiend could not understand.

If he had been in the same position, he would have chosen to evade without the slightest hesitation.

But his thoughts could go no further.

RRRRUMBLE!

A shock wave burst from Jin Taekyung and the Black Hand Fist Demon, shaking the space around them.

Their fists had met in midair.

Neither could retreat. Neither could advance. Both fists trembled violently.

An even match.

Along with the three words that flashed through his mind, the Great Snow Fiend’s figure blurred.

SHWIK!

Jin Taekyung was exhausted from his successive injuries.

The fact that the Black Hand Fist Demon—despite being a Supreme Peak master like him, clearly a level below—had managed to match him for even a brief moment was proof.

And the Great Snow Fiend was not an inept hunter who would miss an opportunity that had arrived earlier than expected.

*Now is the perfect time.*

Even if it was wounded and bleeding, a beast was still a beast. The hunting dog called the Black Hand Fist Demon could never handle that young beast on its own.

Unless the hunter—the only one capable of tearing out the beast’s throat—stepped forward.

*He must die. Right now.*

The decision made in that split second was cold, and his advancing figure was like a flash of lightning.

FSSSH. With every step he took, the Yin-Cold Qi leaking from the Great Snow Fiend’s entire body froze the air.

He crossed more than twenty jang in only three steps and shot forward. Over the Black Hand Fist Demon’s shoulder, he saw one person.

*Jin Taekyung.*

He could see him. He could sense him.

Haa. Hah.

Ragged breathing and a pale face.

The upper half of his body, where the twin wheel had skimmed him before moving on, was drenched in bright-red blood. The eyes of the beast that had discovered the hunter rushing right up to him trembled faintly.

*My judgment was correct.*

Certainty filled the Great Snow Fiend’s cold, composed gaze.

Blazing Flame Divine Dragon Jin Taekyung.

The heir to the Fire Gate Clan. The successor of the Fire King Jeok Cheongang.

The Divine Dragon of the Central Plains, who would one day become a new Martial God and look down upon the world, would die before he ever rose above the clouds.

Right here.

Today.

The time for the hunt had finally arrived.

Ssssss.

The wind blew.

It carried cold into the air and earth that had briefly heated to a fever, and it would cover the mountains, rivers, plants, and trees with frost.

It was a snow wind that planted despair in one person and hope in another.

*He’s here. He came!*

The Black Hand Fist Demon barely managed to suppress the cheer trying to escape between his lips.

He had never liked the Great Snow Fiend.

No. Considering the attitude the Great Snow Fiend usually showed him, even that description was generous.

The condescending way he spoke, as though addressing a slave. The way he looked at him as if he were far beneath him.

If his martial arts had been strong enough, he might have killed the man long ago without alerting the Southern Heaven Demon Empress.

But in a situation like this, the Great Snow Fiend’s presence was worth a thousand troops.

The Black Hand Fist Demon watched Jin Taekyung hurriedly try to pull away and smiled with madness.

*You bastard disciple of the Fire Gate Clan. Even tearing you apart limb by limb wouldn’t be enough. You will never escape.*

KRRUNCH!

In that instant, a hand spread like a hook wrapped around Jin Taekyung’s fist just as it was about to fall.

It was a grappling technique the Black Hand Fist Demon had practiced for as many years as his fist technique.

ZZZT. The heat was like lava, hot enough to make both his hands seem ready to burn, but the Black Hand Fist Demon did not care.

A single moment would be enough.

Then both this pain and Jin Taekyung’s life would come to an end.

The Black Hand Fist Demon looked into Jin Taekyung’s wide-open eyes and shouted as though cheering.

“Senior!”

Before the Black Hand Fist Demon’s shout had even ended, the Great Snow Fiend answered his call.

He drove an ice sword created solely from extreme Yin-Cold Qi into the Black Hand Fist Demon’s back.

SQUELCH!

“……!”

In the slowed world, a single sound of tearing flesh rang out, and the Black Hand Fist Demon’s body stiffened with a jolt.

But to the Great Snow Fiend, the hunting dog’s reaction after completing its mission was irrelevant.

His cold gaze was fixed on only one place: Jin Taekyung’s eyes, wide with pain and shock.

Or at least, it should have been.

Just as the former Sect Leader of the Zhongnan Sect had been, when the Great Snow Fiend encountered him long ago on Great Snow Mountain.

Just as the Black Hand Fist Demon, who had already met his death, had been.

Jin Taekyung should have been pierced and killed by the ice sword filled with powerful Yin-Cold Qi.

But…

*What is this?*

The Great Snow Fiend’s gaze, frozen as though it could not move, trembled.

His eyes slowly lowered.

There, he saw someone’s hand pressed against his chest.

At the same moment the Great Snow Fiend thrust out his ice sword—no, a fraction of a moment before it—the hand that had pierced through the Black Hand Fist Demon’s chest was red, yet blue, and blue, yet dazzling.

FWOOSH.

It was hot.

Hot enough to burn flesh and bone, even the soul inside the body.

As he gazed at the blue-white hellfire burning while drenched in blood, the Great Snow Fiend muttered in a voice that seemed to boil.

“How? How did you…?”

The next moment, Jin Taekyung’s calm voice pierced his ears.

“You should’ve stabbed a little higher. Unless you were trying to give me EXP.”

What?

The Great Snow Fiend wanted to ask again, but Jin Taekyung did not allow him to.

BOOM!

Beyond the terrible heat that seemed to burn through his entire body, the Great Snow Fiend saw it.

*That…*

The Black Hand Fist Demon’s collapsing body.

And an unidentified red armor draped across Jin Taekyung’s upper body.

KRRRUNCH!

[^1]: A *jang* is a traditional Korean unit of length, roughly three meters.
```
