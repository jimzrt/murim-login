<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0714.txt",
      "sha256": "81ded127a9a1c158c62cba81cc3b06ee1a19724f9b948eb0598a04a8e2cc08ca",
      "bytes": 13756
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "40ae2435f4d52e1603a0e72800e8934ecdc77c37eed9ac1e46fa44574493619c",
      "bytes": 1297
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7ce48a59f3b73a2b3bd660e654426c3372f3b9e3d336a9b3f5e1b24771a3ec53",
      "bytes": 207565
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "e54d7e69517f72293196bbe5fe9dd18f41664e4d4229453fa923649530916ee3",
      "bytes": 958
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "3d584fdb3d032d91f86bc336b56dca05b22455a262f7b3d5fd44ac4ffcabfc44",
      "bytes": 792
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8e09d3bcb2c8b07b73ff9fbff8a98ee03bbd095a571113391c631d85700e2443",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "06b2705f9bd5087100365866bdae00d676fceada76417293350227dd92d5533f",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "fd6fa26452ceaec6d9890cd14cfb884677c329b5fa1e395ac3c3a6c7073c721f",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "e1dcba999fe0ca1bd7e76dabf5957d0436efcfdb9d63e83fd0409038b9daab2d",
      "bytes": 715
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "f09b4698ff1e10ebba9408cbdccbaf06902b42f14d5d1ae5e79d2859433b365e",
      "bytes": 787
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "7ba466ff370447a00a60ce209620324bd89e16fdb0ce3d4b0c8457f7d8c00e9c",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8ae62fdddb6bf29233c3958f1ed90caa4eb501d2d5a89d63ccbcc53ef92af4e7",
      "bytes": 218340
    }
  ],
  "estimated_tokens": 12228
}
-->

# Durable State Update — Chapter 714

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 714. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 714. Profile updates may replace only one
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
  "chapter": 714,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 714,
    "continuity_sources": [714],
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
    "The rift has closed, demonic qi has disappeared, and the sacred stone is purifying the corrupted energy.",
    "The mutated guardian spirit was killed by Jin Taekyung and Jeok Cheongang after sacrificing itself and requesting death.",
    "The Southern Heaven Demon Empress is dead.",
    "Baeksang knowingly served Dark Heaven's plan and sacrificed Nanman's forces to advance it.",
    "Dark Heaven has kept Baekhwi alive in a deep sleep, and Baeksang accepted the Southern Heaven Demon Empress's bargain to recover him.",
    "Baeksang created the Baekcheon Unit as a contingency to stop the catastrophe.",
    "Baeksang has asked the Beast Miao King to kill him."
  ],
  "continuity_sources": [
    713
  ],
  "open_questions": [
    "What is Baekhwi's condition, and can he be recovered from his deep sleep?",
    "Will the Beast Miao King grant Baeksang's final request?"
  ],
  "safe_through": 713,
  "temporary_decisions": [
    "Continue rendering the guardian spirit's 의념 as Will.",
    "Render the sacred stone's cleansing effect as purification.",
    "Retain Old Master as Jin Taekyung's address to Jeok Cheongang.",
    "Render 열화신장 as Blazing Flame Divine Palm.",
    "Render 희생과 안식 as Sacrifice and Rest."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 중원     | **Central Plains**                               |                                                       |
| 상태               | **Status**                     |
| 몬스터     | **monster**           |
| 공자      | **Young Master**                                                |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 인천 | **Incheon** | Location of the airport welcome and presidential greeting. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 713
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, now a wounded survivor who has confessed to serving Dark Heaven's plan and asked the Beast Miao King to kill him.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 713
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 713
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 713
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 713
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 713
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 702
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 704
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃714화



날 죽여 주시오, 형님.

그 한마디를 듣는 순간, 야수묘왕은 자신도 모르게 눈을 감았다.

가슴이 저릿하고 숨이 막힌다. 하나뿐인 의제(義弟)가 수십여 년 만에 건넨 부탁은, 마치 예리한 칼날처럼 그의 폐부를 쑤시고 베어 냈다.

‘형님. 형님이라.’

그토록 듣고 싶었던 말이었건만, 이제는 귀를 막고 싶다.

차라리 그 무엇도 본 적 없고 들은 적 없는 바보가 되고 싶었다. 무능한 궁주가 되더라도 이 순간을 피할 수 있다면.

그럴 수만 있다면.

“옛 기억이 떠오르는구려.”

나직한 목소리에 야수묘왕은 눈을 떴다. 희미한 웃음을 머금고 있는 백상이 그의 눈동자에 비쳤다.

“그 시절의 우리는 어렸고, 장차 남만야수궁의 궁주가 되고 싶었던 나는 늘 형님을 이기지 못해 안달이었소.”

“……그래, 그랬었지.”

새파랗다 못해 핏덩이나 다름없었던 소년 시절의 일이다.

백상은 몇 살 위의 야수묘왕을 경쟁자로 여겼고, 야수묘왕의 눈에는 그런 백상이 마냥 귀여워 보였다. 독자로 태어난 그에게는 형제가 없었다.

“하지만 나는 단 한 번도 형님을 따라잡은 적이 없었소. 가까이 다가왔다 싶으면, 어느새 저 멀리 멀어져 있었지.”

“그건 네가 나보다 어렸기 때문이었다. 만약 우리의 나이가 같았다면…….”

“그래도 결과는 변하지 않았을 거요. 애초부터 타고난 그릇이 달랐으니까.”

그러나 백상은 포기하지 않았다. 매일같이 야수묘왕에게 비무를 청했고, 항상 패배하면서도 다음 날이면 언제 그랬냐는 듯이 다시 그를 찾아갔다.

“그리고 어느 날 문득 깨달았소. 나보다 머리 두 개는 큰 저 얼간이가, 언제부턴가 썩 싫지 않았다는 걸 말이오.”

백상은 똑똑히 기억하고 있었다. 쓰러진 자신을 일으켜 세워 주고, 몸에 묻은 흙먼지를 툭툭 털어 주던 덩치 큰 소년의 모습을.

끙끙 앓던 날이면 슬쩍 처소 앞에 약재를 던져 놓고 가던 누군가의 그림자를.

“그래서 마지막 비무를 청했었지.”

그날도 비무의 결과는 다르지 않았다.

백상은 그 어느 때보다 온 힘을 다해 싸웠고, 졌다.

거기까지였다면 평소와 다를 것 없는 하루였을 것이다.

하지만 백상은 여느 때처럼 자신을 일으켜 세워 주는 손길을 뿌리치지 않았고, 씨근덕거리며 처소로 돌아가지도 않았다.

그 대신 어디선가 슬쩍해 온 과실주 두 병을 꺼내며 혼잣말처럼 중얼거렸다.

“술은 있는데, 같이 마실 사람이 없네. 혹시 생각 있으면 따라오시던가.”

나직하게 울려 퍼지는 야수묘왕의 목소리에, 일순간 눈을 크게 뜬 백상이 핏물을 토해 내며 웃었다.

“쿨럭. 그걸 아직도 기억하고 있었소?”

“어찌 잊겠느냐. 고작 열두 살밖에 안 된 주제에 그런 되바라진 말을 하는 아이는, 내 평생 너밖에 없었다.”

“그럼 내가 홀로 두 병을 통째로 비웠던 것도 기억하겠구려.”

“두 병을 통째로?”

백상의 말을 들은 야수묘왕은 참지 못하고 실소를 흘렸다. 반달처럼 휘어진 그의 눈가는 어느덧 알 수 없는 습기로 젖어 있었다.

“글쎄, 한 잔도 채 못 비우고 쓰러져 버린 어린놈은 생생하게 기억하고 있다. 풀린 눈으로 나를 바라보며 했던 말도.”

백상이 힘없이 고개를 끄덕였다. 흐릿한 눈동자는 그때 그 시절을 더듬고 있었다.

“나는 대족장으로 만족할 테니, 당신은 훌륭한 궁주가 되라고 했었지. 도무지 취하지 않고서는 형님에게 그 말을 할 수 없어 술을 마셔야 했소.”

“그 뒤에 했던 말도, 취하지 않고서는 할 수 없었던 말이었느냐?”

“그럴 리 있겠소.”

백상이 나직이 말을 이었다.

“형님은…… 그저 내 형님이었소. 어쩌면 우리가 처음 만난 그 날부터.”

태어나서 처음 술을 맛본 두 소년은 그렇게 쓰러져 잠이 들었고, 다음 날 아침 낡은 사당에서 눈을 뜬 그 순간부터 누구보다 가까운 의형제가 되었다.

산에서. 들에서. 강과 늪에서.

그리고 전장에서도 그들은 함께였다.

어느 날 찾아온 끔찍한 운명이 두 사람을 갈라놓기 전까지.

“형님.”

“…….”

“우리가 의형제의 연을 맺었던 그 날, 형님은 내게 맹세했었소. 누구보다 훌륭한 궁주가 되겠노라고. 누구보다 남만을 위하고, 이 땅의 사람들을 위해 싸우겠다고.”

“그만. 그만하거라.”

야수묘왕은 이미 짐작하고 있었다. 백상이 왜 이런 이야기를 꺼냈는지. 그가 말하고자 하는 것이 무엇인지.

“기어코 너를…… 내 손으로 죽여야 한단 말이냐?”

백상이 작게 고개를 끄덕였다.

“이미 너무나도 많은 피가 흘렀소. 모든 것이 내 그릇된 선택 때문이지.”

남만을, 수많은 부족민들을 배신한 역도를 처형하는 것.

그것이야말로 남만야수궁의 궁주가 직접 해야 하는 일이었고, 오래전 낡은 사당에서 한 맹세를 지킬 수 있는 유일한 길이었다.

“맹세하지 않았소. 누구보다 훌륭한 궁주가 되겠다고.”

힘겹게 들어 올려진 손이 석상처럼 굳어 버린 야수묘왕의 등 뒤를 가리켰다.

파르르 떨리는 손가락이 향하는 곳에는, 무너진 잔해를 넘어 내궁으로 돌아온 수많은 부족민과 전사들이 있었다.

“모두가 지켜보고 있소. 형님과 나를. 그리고 우리를.”

백상의 말은 한 치의 거짓도 없는 사실이었다.

끊임없이 내궁으로 쏟아지는 인파는 모든 재앙이 끝났음을 알고 환호했고, 이내 눈 앞에 펼쳐진 광경에 경악했으며, 마침내 귀환한 자신들의 궁주와 그 앞에 쓰러진 배반자를 보고 침묵했다.

아니, 분노했다.

“느껴지는구려. 나를 향한 저들의 분노가.”

그것은 백상이 가장 두려워했던 동시에, 누구보다 간절히 바랐던 순간이었다.

만약 이런 순간이 온다면, 그건 누군가가 자신을 저지했다는 뜻일 테니까. 암천과 남천마후의 대계도 물거품이 되었다는 것이니까.

그렇기에 소리 내어 웃을 수 있었다. 이미 죽어 가는 몸을 일으켜, 마지막 힘을 쥐어 짜내어 외칠 수 있었다.

“똑똑히 기억하라!”

금방이라도 꺼질 듯이 흐릿한 눈동자.

그러나 입술 밖으로 뛰쳐나온 외침은 내궁의 모두가 들을 수 있을 만큼 또렷하고 거대했다.

“비록 대계는 실패했지만, 언젠가 반드시 암천(暗天)의 하늘이 남만을 집어삼킬 터!”

“……!”

쩌렁쩌렁한 외침이 무수한 잔해와 시체의 산을 넘어, 모두의 귓가에 울려 퍼진다.

한 음절, 한 음절을 내뱉을 때마다 잇새 사이로 핏물이 터져 나오고 전신에 힘이 빠져나간다.

그러나 백상은 멈추지 않았다. 멈출 수 없었다.

그는 모두를 배신하고 재앙을 일으킨 역도니까.

용서받을 수 없는 죄를 저지른 죄인은, 어떠한 동정이나 사연도 없이 죄인으로 죽어야 한다.

그것이…… 백상이 할 수 있는 마지막 일이었다.

“머지않아 도래할 그 날……!”

울컥, 솟구치는 핏물을 삼킨 백상이 이를 악물며 외침을 이어 갔다.

“저 비열한 중원의 한족 놈들도, 미개하기 짝이 없는 너희 남만인들도 위대하신 천주의 발아래에 엎드려 복종할 것이다!”

백상은 피에 젖은 입꼬리를 말아 올리며 환하게 웃었다.

지금 이 순간, 그는 누구보다 충성스러운 천주의 종복이었고 암천의 개였다.

그리고 그런 의제(義弟)를 위해, 의형(義兄)이 할 수 있는 선택은 하나뿐이었다.

퍼걱!

공간을 가르며 쏘아진 주먹이 살을 짓이기고 뼈를 부수었다.

가슴 깊숙이 틀어박힌 일권(一拳)에는, 어린 시절 함께 뒹굴었던 너른 들판을 닮은 녹색 강기가 서려 있었다.

‘고맙소, 형님.’

약속대로 아주 훌륭한 궁주가 되었구려.

들리지 않을 중얼거림과 함께, 백상은 아득한 시야 너머로 보이는 한 사람의 얼굴을 응시했다.

‘그런데 왜…….’

왜 울고 있는 거요.

역도를 처단하고, 재앙을 막은 위대한 궁주는 울고 있었다. 아주 서럽게. 소중한 것을 잃어버린 아이처럼.

그리고 울부짖듯이 외쳤다.

“암천과 결탁한 역도, 백상을 처단했다!”

아스라이 울려 퍼지는 사람들의 환호가 귓가를 울린다. 힘없이 뒤로 젖혀진 백상의 고개가 하늘을 향했다.

맑고, 푸르렀다.

이 세상은 더 이상 어둡지 않았다.

‘그렇지 않으냐, 휘야.’

이지를 상실한 채 아비의 가슴에 검을 박아 넣었던 아들을 떠올리며, 이미 다른 세상에서 환하게 웃으며 자신을 기다리고 있을 자식을 떠올리며.

백상은 편안히 미소지었다.

툭.

힘을 잃은 채 허물어지는 신형.

세상은 여전히 밝았고, 사람들의 환호는 끝없이 이어졌다.

그리고 통곡조차 허락되지 않은 의형을 대신하여, 한 사람이 그의 눈을 감겨 주었다.

“……시발. 뭘 잘했다고 처웃고 있어.”

혼잣말처럼 중얼거린 진태경은 문득 손에 쥔 낡은 무언가를 바라보았다.

모르겠다. 분명 죽일 놈인데, 죽을 짓을 한 나쁜 놈인데. 왜 이렇게 기분이 더러운지. 자신은 왜 이걸 가져왔는지.

빌어먹을.

흘러나오지 않은 욕설과 함께, 진태경은 손에 쥔 것으로 백상의 얼굴을 덮었다.

백천(百天).

누군가의 세월과 염원이 담긴 그 낡은 비단이, 어디선가 불어온 선선한 바람에 실려 흩날렸다.

끝없이 울려 퍼지는 환호 속, 저 멀리서 메아리처럼 들려오는 외침들과 함께.

“조장니이이임!”

“각주, 아니 진 공자!”

“태산이가 왔다! 태산이 늦어서 미안하다!”

“야, 이놈아! 살아 있느냐!”

환청인가?

한 줄기 의문과 함께 돌아선 진태경은 서서히 가까워지는 낯익은 얼굴들을 멍하니 바라보다가, 비로소 피식 웃었다.

그리고 쓰러졌다.



* * *



아주 긴 꿈을 꿨다.

그것도 끔찍한 악몽을.

나는 꿈속에서도 고군분투하고 있었다. 현대에서는 몬스터와 싸웠고, 무림에서는 암천과 싸웠다.

그리고 이미 겪었던 것처럼 치열한 사투 끝에 남천마후를 쓰러트렸을 때, 웬 가면 쓴 놈이 나타나 이렇게 말했다.

- 서천마군에 이어 남천마후까지 쓰러트리다니, 제법이로군.

이건 또 어디서 굴러먹다 온 호로 새끼일까, 라고 생각하던 그때, 가면 쓴 놈이 말을 이었다.

- 하지만 서천마군과 남천마후는 우리 팔대천왕 중 최약체에 불과하지.

- ……?

- 나는 동쪽을 맡은 동천마군이다. 내 바로 아래 서열은 동서쪽을 맡은 동서천마후가 있지.

아니 시팔, 동서남북 네 개면 됐지 뭔 동서천마후야.

극한의 뇌절에 나는 할 말을 잃었다.

이대로면 현대에 돌아가도 동두천마군, 혹은 인천마후가 기다리고 있지 않을까 하는 두려움에 숨이 막혔다.

하지만 별수 있나. 꿈인 것도 모르는 상태로 박 터지게 싸웠다.

그리고 놈을 향해 한 걸음, 한 걸음을 뗄 때마다 지금껏 내가 죽였던, 혹은 내가 구하지 못했던 이들이 나타나 앞을 가로막았다.

- 조금만. 조금만 더…….

- 네가 빨리 움직였다면 우리가 살 수 있었을 텐데.

- 가족들에게 돌아갈 수 있었을 텐데.

- 왜 넌 살아남고, 우린 죽어야 하지?

- 왜. 왜. 왜?

나는 아무런 대답도 하지 못한 채 움직임을 멈췄고, 그들은 내 몸통에 이빨을 박아넣었다.

천천히. 하지만 쉼 없이.

하지만 나는 그저 석상처럼 굳은 채 지켜볼 수밖에 없었다.

변이체가 되어 버린 그들 사이로 보이던 낯익은 얼굴 때문이었다.

- 나는 누구보다 널 아꼈는데, 결국 너는 나를 구하지 못했구나.

저들 사이에 있을 수도 없고, 있어서도 안 되는 얼굴.

그건 적천강이었다.

양팔을 잃고, 가슴 한복판이 뻥 뚫린 채 다가온 그는 내 목덜미에 이빨을 박아넣었다.

탐욕스럽게 살점과 핏물을 집어삼키던 적천강이, 낮은 목소리로 내 귓가에 속삭였다.

- 그런데, 이 괘씸한 놈이 언제쯤 깨어난다는 말이냐?

그리고 그 순간. 나는 불현듯 눈을 떴다.

“……!”

알 수 없는 진한 냄새가 맴도는 가운데 낯선 천장이 눈에 들어온다.

멍하니 눈을 깜빡이며 현실을 인지해 가던 그때, 낯익은 목소리가 귓가를 파고들었다.

“지금이라도 순순히 고한다면 살짝 지지는 정도로 끝내주마. 네놈, 돌팔이지?”

“아, 아닙니다요.”

“애가 칠 주야가 지나도록 안 깨어나는데 이게 말이 된단 말이냐? 야수묘왕 불러와.”

“헉. 그, 그것은…….”

“야울척 불러오라고!”

쩌렁쩌렁한 외침을 따라 고개를 돌린 곳에는, 의원의 멱살을 붙잡고 짤짤이 흔들고 있는 적천강의 모습이 있었다.
```

## Final English reading copy

```markdown
# Chapter 714

“Please kill me, hyung.”

The moment he heard those words, the Beast Miao King closed his eyes without realizing it.

His chest ached, and he could barely breathe. The request his only sworn younger brother had made after several decades stabbed and carved into his heart like a sharp blade.

*Hyung. He called me hyung.*

It was the word he had wanted to hear more than anything.

And now he wanted to cover his ears.

He would rather become a fool who had never seen or heard anything. He would even accept becoming an incompetent Palace Lord if it meant he could escape this moment.

If only he could.

“This brings back old memories.”

The Beast Miao King opened his eyes at the quiet voice. Baeksang’s face, wearing a faint smile, was reflected in his eyes.

“We were young back then, and I was always desperate to beat you, because I wanted to become the Palace Lord of the Nanman Beast Palace someday.”

“……Yes. You were.”

It had been back when they were so young that they had barely been more than children.

Baeksang had regarded the Beast Miao King, who was several years older, as a rival. To the Beast Miao King, Baeksang had simply been adorable. He had been born an only child and had no siblings.

“But I never caught up to you even once. Whenever I thought I had drawn close, you were suddenly far ahead of me again.”

“That was because you were younger than me. If we had been the same age…”

“Even then, the result would not have changed. We were born with different potential from the start.”

But Baeksang had never given up. Every day, he challenged the Beast Miao King to a duel. Even after losing every time, he would come looking for him again the next day as though nothing had happened.

“And then one day, I suddenly realized that the idiot who was two heads taller than me wasn’t actually all that bad.”

Baeksang remembered it clearly. The sight of the big boy who had pulled him to his feet whenever he fell and brushed the dirt from his clothes.

The shadow of someone who would quietly leave medicinal herbs outside Baeksang’s quarters whenever he was sick, then slip away.

“So I challenged you to one last duel.”

The result had been no different that day.

Baeksang had fought with more strength than ever before—and lost.

If it had ended there, it would have been an ordinary day, no different from any other.

But Baeksang did not push away the hand that helped him up as he usually did, nor did he return to his quarters while huffing in anger.

Instead, he pulled out two bottles of fruit wine he had stolen from somewhere and muttered as though speaking to himself.

“I have wine, but no one to drink it with. If you’re interested, you can come along.”

At the Beast Miao King’s quiet voice, Baeksang’s eyes widened for a moment. Then he coughed up blood and laughed.

“Cough. You still remember that?”

“How could I forget? In my entire life, you were the only twelve-year-old brat who could say something so insolent.”

“Then you must remember how I emptied both bottles by myself.”

“Both bottles?”

The Beast Miao King let out a laugh before he could stop himself. The corners of his crescent-shaped eyes were already damp for reasons he could not name.

“Well, I vividly remember the little brat who collapsed before he had even finished a single cup. I also remember what you said while looking at me with those unfocused eyes.”

Baeksang nodded weakly. His blurred eyes were searching through the distant past.

“I said I would be content with becoming the Great Chieftain, so you should become a great Palace Lord. I had to drink because I couldn’t say those things to you unless I was drunk.”

“And what you said after that? Was that something you could not say unless you were drunk as well?”

“Of course not.”

Baeksang continued in a quiet voice.

“You were… simply my hyung. Perhaps you had been ever since the day we first met.”

The two boys had tasted alcohol for the first time, then collapsed and fallen asleep. When they opened their eyes the next morning in an old shrine, they had become sworn brothers closer than anyone else.

In the mountains. In the fields. By the rivers and in the marshes.

And they had been together on the battlefield as well.

Until a terrible fate came one day and tore them apart.

“Hyung.”

“…….”

“The day we became sworn brothers, you made a vow to me. You said you would become a better Palace Lord than anyone else. That you would care for Nanman above all others and fight for the people of this land.”

“Enough. Stop.”

The Beast Miao King already knew why Baeksang had brought up these memories.

He knew what Baeksang was trying to say.

“Do I really have to… kill you with my own hands?”

Baeksang gave a small nod.

“Far too much blood has already been spilled. Everything happened because of my misguided choices.”

Executing the traitor who had betrayed Nanman and countless tribespeople.

That was precisely what the Palace Lord of the Nanman Beast Palace had to do himself. It was the only way to keep the vow they had made long ago in that old shrine.

“You made a vow, didn’t you? That you would become a better Palace Lord than anyone else.”

A hand that had been raised with difficulty pointed behind the Beast Miao King, whose body had stiffened like a stone statue.

Beyond the fallen ruins stood countless tribespeople and warriors who had returned to the Inner Palace.

“Everyone is watching. You and me. And us.”

Baeksang’s words were the undeniable truth.

The people constantly pouring into the Inner Palace had learned that the catastrophe was over and cheered. Then they were horrified by the sight that unfolded before their eyes. Finally, they fell silent at the sight of their returning Palace Lord and the traitor collapsed before him.

No.

They were furious.

“I can feel it. Their anger directed at me.”

It was the moment Baeksang had feared most, and also the moment he had longed for more than anything.

Because if such a moment had come, it meant someone had stopped him. It meant Dark Heaven and the Southern Heaven Demon Empress’s grand plan had come to nothing.

That was why he could laugh aloud. He could raise his dying body, squeeze out the last of his strength, and shout.

“Remember this clearly!”

His eyes were dim, as though they might go out at any moment.

But the cry that burst from his lips was so clear and powerful that everyone in the Inner Palace could hear it.

“Though the grand plan has failed, the day will surely come when Dark Heaven’s sky devours Nanman!”

“……!”

His ringing cry reverberated in everyone’s ears, passing over countless piles of rubble and corpses.

With every syllable he forced out, blood burst between his teeth and strength drained from his entire body.

But Baeksang did not stop.

He could not stop.

He was a traitor who had betrayed everyone and brought about this catastrophe.

A criminal who had committed an unforgivable crime had to die as a criminal, without sympathy or any tale of why he had done it.

That was… the last thing Baeksang could do.

“That day, which will come before long…!”

Baeksang swallowed the blood surging up his throat, clenched his teeth, and continued shouting.

“Those contemptible Han Chinese bastards of the Central Plains, and you Nanman people who are as primitive as can be, will all kneel and submit at the feet of the great Lord of Heaven!”

Baeksang curled his bloodstained lips into a radiant smile.

At this moment, he was the most loyal servant of the Lord of Heaven and Dark Heaven’s dog.

And for that sworn younger brother, there was only one choice his sworn elder brother could make.

Crack!

The fist that shot through the air crushed flesh and shattered bone.

The single punch buried deep in Baeksang’s chest carried green Force, like the broad fields where they had rolled around together as children.

*Thank you, hyung.*

*You became a truly great Palace Lord, just as you promised.*

Along with a murmur no one could hear, Baeksang stared at the face of one person visible beyond his fading field of vision.

*But why…?*

*Why are you crying?*

The great Palace Lord who had executed a traitor and prevented a catastrophe was crying.

He was crying bitterly, like a child who had lost something precious.

And he shouted as though howling.

“I have executed Baeksang, the traitor who joined forces with Dark Heaven!”

The people’s cheers echoed faintly in the distance. Baeksang’s head, limp and tilted backward, turned toward the sky.

It was clear and blue.

The world was no longer dark.

*Isn’t that right, Hwi?*

He thought of the son who had lost his reason and driven a sword into his father’s chest.

He thought of the child who was already waiting for him in another world, smiling brightly.

Baeksang smiled peacefully.

Thud.

His body collapsed as it lost all strength.

The world was still bright, and the people’s cheers continued without end.

And in place of his sworn elder brother, who was not even allowed to wail, someone closed Baeksang’s eyes.

“……Fuck. What the hell are you grinning about? It’s not like you did anything right.”

Jin Taekyung muttered to himself, then suddenly looked down at the old thing clenched in his hand.

*I don’t know.*

He was definitely someone who had to die. A bad person who had done more than enough to deserve death.

So why did he feel so damn awful?

Why had he brought this here?

*Damn it.*

Along with the curses that never left his mouth, Jin Taekyung covered Baeksang’s face with the object in his hand.

Baekcheon.

The old silk, carrying someone’s years and hopes, fluttered in a cool breeze that had come from somewhere.

Amid the endless cheers, along with voices echoing like distant cries, he heard them.

“Captain!”

“Pavilion Master—no, Young Master Jin!”

“Taishan came! Taishan is sorry he was late!”

“Hey, you bastard! Are you alive?”

*Is this an auditory hallucination?*

With that single question, Jin Taekyung turned around. He stared blankly at the familiar faces slowly drawing nearer, then finally let out a quiet laugh.

And collapsed.

* * *

I had a very long dream.

A terrible nightmare, at that.

Even in the dream, I was struggling desperately. In the modern world, I fought monsters. In Murim, I fought Dark Heaven.

And when I defeated the Southern Heaven Demon Empress after a fierce battle, just as I had already experienced, some masked bastard appeared and said:

—You defeated the Western Heaven Demon Lord and even the Southern Heaven Demon Empress. Not bad.

I was wondering what hole this bastard had crawled out of when the masked man continued.

—But the Western Heaven Demon Lord and the Southern Heaven Demon Empress are nothing more than the weakest of our Eight Great Heavenly Kings.

—……?

—I am the Eastern Heaven Demon Lord, who commands the east. Directly beneath me in rank is the East-West Heaven Demon Empress, who commands the east and west.

*No, fuck this. Four directions were plenty. What the hell is an East-West Heaven Demon Empress?*

The bit had been run so far into the ground that I was speechless.

At this rate, I feared that even if I returned to the modern world, I might find the Dongducheon Demon Lord or the Incheon Demon Empress waiting for me.

But what could I do?

Without even realizing that it was a dream, I fought like hell.

And every time I took another step toward that bastard, people I had killed—or failed to save—appeared before me and blocked my path.

—Just a little more. Just a little farther…

—If you had moved faster, we could have lived.

—We could have returned to our families.

—Why did you survive while we had to die?

—Why? Why? Why?

I could not answer them. I stopped moving, and they sank their teeth into my torso.

Slowly.

But without pause.

I could only stand there and watch, my body frozen like a statue.

Because of the familiar face visible among those who had become mutants.

—I cared for you more than anyone, but in the end, you couldn’t save me.

It was a face that could not be among them.

A face that should not have been among them.

It was Jeok Cheongang.

He approached with both arms gone and a gaping hole through the center of his chest, then sank his teeth into the back of my neck.

Jeok Cheongang greedily swallowed flesh and blood. Then, in a low voice, he whispered into my ear.

—But when is this infuriating bastard supposed to wake up?

And at that moment, I suddenly opened my eyes.

“……!”

A strong, unfamiliar smell hung in the air as an unfamiliar ceiling came into view.

I blinked blankly, slowly becoming aware of reality. Then a familiar voice pierced my ears.

“If you come clean now, I’ll let you off after singeing you a little. You’re a quack, aren’t you?”

“N-no, sir.”

“The child hasn’t woken up for seven days and nights. Does that make any sense? Go get the Beast Miao King.”

“Gasp. Th-that is…”

“I said bring Yayul Cheok here!”

I turned toward the ringing voice and saw Jeok Cheongang gripping a physician by the collar and shaking him violently.
```
