<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0593.txt",
      "sha256": "307478262d812b6d2171f51a013a0471b501427cb2f1e356a1861e4b191f4649",
      "bytes": 16860
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "330ab24910162156eddf0c63fe73fe7ec4b3127c53bc48eeb9f526384156c387",
      "bytes": 2907
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "89ec79b2d537971f97e80eec6c669e64a6cd46e43d2c3e5ad0cb9499b4c340b6",
      "bytes": 185016
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fc9a57b2d380b72416a46e1312ea57c33faee367d1c68f777f9a053aff3fa18a",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "176323f112db089dce3d727d9792cf35768ed6b461dd91f54fd5f01b61da4bde",
      "bytes": 1076
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "aabd49a55fc93d322ac534060cf9efd96ad1b5d1f2bb34e898600153f0936195",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c517dfe42684cfdca80a996e61eff85d9abefe42019ad72a43882a29c87d899b",
      "bytes": 2315
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d4bf9bbfe19c4f7414657f343de7ce84cdd93f3ba29e50a9f6a85b4eb430b0b2",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "52aa5ffb223f05b99600b2afcb275df7dcc30e06d80ebcc597788fe9dd1fdb02",
      "bytes": 694
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "79ed8ad4254c27b7c327510f5c28d16874023bc50eb34f91824e88413a5024d8",
      "bytes": 939
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "a66618e0dcd31ac8fc8e2f8b36b5e99aaa9a9f48f5ff3071ceca5c655d4f6930",
      "bytes": 528
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "199bb6b87ba908d5dec935b4b06771f4cfccbb1095d158fe1d3cc89bb55da85c",
      "bytes": 1035
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61ef24047780dd8c8c21961c6c1395fd6b17ffe5fa8a5aeb489fa4744575956d",
      "bytes": 182490
    }
  ],
  "estimated_tokens": 13764
}
-->

# Durable State Update — Chapter 593

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 593. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 593. Profile updates may replace only one
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
  "chapter": 593,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 593,
    "continuity_sources": [593],
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
    "Kim Hwajong died after sacrificing himself to restrain Behemoth, and Choi Minwoo remains unconscious after being transported from the battlefield.",
    "Behemoth's Turbid Abyss is a Supreme Peak Magic Gem that absorbed another source of mana and requires purification before use.",
    "Jin has devastated Ares Guild headquarters, incapacitated its elite defenders, triggered an internal revolt, and entered concealed Area A while pursuing Go Jun.",
    "Go Jun is Lee Jungryong's Disciple and direct protégé; Lee found him among the war orphans and recognized him as special.",
    "Go Jun remained in Area A to confront Jin and now possesses immense power attributed by Jin to Magic Gem enhancement.",
    "Go Se-won openly opposed Go Jun's crimes, intended to resign, revealed Area A, and has a pregnant wife and a four-year-old child.",
    "Cheon Taemin collapsed more than twenty years ago and remains unconscious at an unknown location, with Area A only suspected.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition and purged those who knew the truth.",
    "Busan's Kraken is dead, but more than one thousand Mermen remain across Haeundae and Gwangalli.",
    "Go Jun seized Song Cheonwoo's children, used an S-grade Magic Gem to cause the Busan Monster Wave, and targeted Choi Minwoo.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss; the object in his pocket released darkness that became light.",
    "Jin and Go Jun are fighting inside Area A, with Jin exhausted but determined to kill him."
  ],
  "continuity_sources": [
    592
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is inside Area A, and what is the unidentified being involved in Go Jun's plan?",
    "What was the object Song Cheonwoo kept in his pocket, and what did its release of darkness and light accomplish?",
    "What is the black jewel in Go Jun's necklace, and what function does it serve?"
  ],
  "safe_through": 592,
  "temporary_decisions": [
    "Use Area A for A구역, White Flame for 백염, Flamefire Path for 염화일로, Tower Shield for 타워 실드, and hellfire for 겁화.",
    "Use Scorching Yang Qi for 열양지기 and Force for 강기; distinguish Sword Energy from Aura when the source contrasts them, and use Aura Blade for 오러 블레이드.",
    "Use Seizing an Object Through Empty Space for 허공섭물, Flame Divine Palm for 화염신장, Finger Qi for 지풍, and grappling technique for 금나수.",
    "Use hunting dog for 사냥개 and impregnable fortress for 철옹성.",
    "Use Executive Director for 전무 and Managing Director for 상무 in Ares Guild's executive hierarchy."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 내가중수법 | **Inner-Family Heavy Hand** | Taekyung's joking comparison for his mother's painful palm strike. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 후발선제 | **Striking Second, Hitting First** | Principle describing the Western Heaven Demon Lord's counterattack. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 기경팔맥 | **Eight Extraordinary Meridians** | The eight extraordinary meridians of wuxia physiology. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진호 | 태경 | Older male friend addressing a younger male friend in a close hyung relationship | Taekyung | Informal and familiar | Jin-ho addresses Taekyung as 태경아 in recalled advice; Taekyung refers to him as Jin-ho hyung. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 최민우 | 화종 | Young Master to butler | Butler Kim | formal and respectful | Choi refers to Hwa-jong as 김 집사님 while discussing the concealed truth. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 592
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 592
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and the fugitive occupant of the concealed Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Lee Jungryong recognized Go Jun as special after meeting him while he was drifting among orphanages, then made him his Disciple and direct protégé; after Lee's death, Go Jun inherited his Ares Guild legacy, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, has seized Song Cheonwoo's children as leverage, and used an S-grade Magic Gem to trigger the Busan Monster Wave while targeting Choi.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 591
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 592
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, has withdrawn from the Peace Guild, and has entered Ares Guild headquarters to confront Go Jun.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 592
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 591
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 564
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 551
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 587
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and is mobilizing every available power to unseat Go Jun from Ares Guild leadership; he was rendered unconscious in the Pyeongchang battle and carried away by Hwa-jong.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃593화



뻑!

둔탁한 타격음과 함께 힘껏 내지른 일권(一拳)이 석고준의 가슴팍을 후려쳤다.

중첩된 방어 마법이 단번에 파훼되고 단단하기 그지없는 전신 갑주의 일부가 움푹 주저앉는다. 이를 악문 놈이 분노를 담아 부르짖었다.

“진태경-!”

어지간한 상위 헌터나 절정 고수였다면 조금 전의 일권으로 극심한 내상을 입고 전투 불능 상태에 빠졌을 것이다.

그러나 석고준은 달랐다. 마정석의 영향인지, 내가중수법(內家重手法)조차 놈에게 큰 타격을 입히지 못했다.

‘S급 헌터. 그 이상.’

전후 사정이 어찌 되었건 간에, 놈은 이미 공인받은 S급 헌터였다.

현대에서는 마나 연공법이라는 이름으로 불리는 내공심법을 익혔을뿐더러, 네임드 몬스터에게서 얻을 수 있는 S급 마정석의 기운까지 흡수했으니 그 힘은 엄청났다.

“죽엇!”

콰아아아! 쿠궁!

이제는 붉은 것을 넘어, 완연한 핏빛으로 접어든 기운이 폭사하듯 뿜어진다.

거대한 오러 블레이드로부터 가해지는 태산 같은 압력에 백염의 창대가 부르르 떨렸다.

‘최근 들어 이렇게까지 밀린 적은 없었는데.’

지금 이 순간만큼은 삼 갑자의 공력도, 인간의 한계를 벗어난 신체 능력도 부족하게 느껴졌다.

오늘 하루 끊임없이 누적된 피로의 영향인지, 그게 아니라면 석고준이 흡수한 마력의 양이 그만큼 막대했던 건지도 모르겠다.

다만 한 가지 확실한 것은…… 지금 상대하고 있는 이 얼간이가 내 예상을 훌쩍 뛰어넘는 힘을 얻었다는 것이다.

드드드득. 콰직!

머리 위로 가해지는 엄청난 압력에 몸과 지면이 함께 내려앉는다. 어느덧 복사뼈까지 지면에 파묻힌 내 모습에 석고준이 이를 드러내며 웃었다.

“조금씩 감이 잡히나? 응? 이제야 슬슬 좆 된 것 같다는 느낌이 들어?”

낮은 웃음소리가 흘러나온다.

지금의 석고준은 진심으로 즐거워하고 있었다. 마침내 스승의 복수를 할 수 있다는 생각에 환희하고 있었다.

“스승님께서 돌아가신 그날부터, 나는 매일 밤 네놈을 죽이고 또 죽였다. 바로 지금 같은 순간을 기다리며 살았지.”

나는 놈의 빈틈을 살피며 대꾸했다.

“어쩐지 아침마다 다시 태어나는 기분이더라. 난 또 밤마다 정룡이 뒈지는 꿈을 꿔서 상쾌해진 줄 알았지.”

후우웅!

핏빛 기운이 거칠게 흔들린 순간, 나는 깊이 파묻혀 있던 발을 뽑아 차올렸다.

쾅!

빛살처럼 휘둘려진 발끝이 굉음과 함께 놈의 정강이에 가로막힌다. 왈칵 분노를 쏟아내려던 석고준이 실소를 흘렸다.

“이제 와서 발악해 봤자 이미 늦었다. 어차피 이렇게 된 이상, 싹 다 죽이는 건 일도 아니야.”

“뭐?”

순간 그 말의 의미를 제대로 이해하지 못해서 눈을 깜빡이던 그때, 석고준의 나직한 목소리가 귓가를 파고들었다.

“너와 그 빌어먹을 평화 길드. 그리고 집에서 기다리고 있을 부모와 동생 년…… 아. 애비는 이미 죽고 없었나? 뭐 별 상관은 없지. 지금까지 살아 있었어도 곧 아들놈 따라서 뒈졌을 테니까.”

“…….”

“세상이 영웅이라고 불러 주니 좋았나? 모두 함께 영원히 행복할 줄 알았어? 전부 개소리지. 김화종, 그 늙은이는 시작에 불과해.”

끈적하고 불쾌한 숨결이 흘러나와 얼굴에 닿았다. 낄낄거리는 웃음소리가 뒤를 이어 울려 퍼진다.

“이번에는 네놈이고, 그다음에는 최민우다. 이후로는 아무래도 상관없으니 네놈과 조금이라도 연관이 있는 것들을 차례차례 죽여 주지. 몬스터 웨이브로 한번에 쓸어 버리는 것도 좋을 것 같은데. 네 생각은 어때?”

계속해서 귓가로 흘러드는 목소리에, 나는 멍하니 눈을 깜빡였다.

이 새끼가 지금…… 뭐라고 지껄이는 거지?

희한한 일이다. 분명히 내 눈앞에 있는 이놈은 사람의 모습을 하고 있는데, 쉴 새 없이 놀려 대는 아가리에서는 개 짖는 소리밖에 나오지 않는다.

사람의 껍데기를 뒤집어쓴 괴물이 여기에 있었다.

‘그래서 죽이겠다고? 내 사람들을 전부?’

나는 문득 속이 메스꺼워졌다.

이런 말을 단순한 위협이 아니라 실천에 옮길 수 있는 석고준의 존재가 혐오스러웠고, 이제는 내게 없어서는 안 될 그들이 죽어 있는 모습을 상상하자 머릿속이 텅 빈 듯했다.

‘어머니. 하연이. 최 팀장. 꺽정 아저씨, 송송이, 진호 형…….’

익숙한 얼굴들이 차례차례 눈앞을 스친다. 눈 덮인 설산에서 죽음을 맞이한 반백의 노집사도 함께.

‘그 사람들을 다 죽일 건데, 어떻게 생각하냐고?’

다음 순간. 입술 사이로 담담한 목소리가 흘러나왔다.

“그래, 알았다.”

“뭐?”

“해 봐. 어디 한 번.”

석고준의 입가에 맺혀 있던 미소가 흐릿해진 그때, 나는 전신의 모든 힘을 끌어올렸다.

그그그극.

무시무시한 압력에 의하여 조금씩 내려가던 창이, 굽혀지던 무릎이 그 자리에서 멈춘다.

적어도 지금 이 순간만큼은, 난 피로를 잊었다. 아직도 채 가시지 않은 일섬의 여파로 근육이 찢어질 듯 아파 왔으나 그 통증마저도 잊었다.

피로와 통증 위에 덧칠된 분노가 모든 것을 가리고 마비시켰다.

몸속 깊숙한 곳에 자리 잡은 기경팔맥(奇經八脈)과 수백 개의 혈도에서 용암과도 같은 공력이 들끓었다.

벌어진 입술 사이로 화염처럼 뜨거운 목소리가 흘러나왔다.

“그 말은 하지 말았어야지.”

“……!”

“적어도 내 사람들을, 그런 식으로 말하지는 말았어야지.”

짐작하고 있었다. 석고준이 그러고도 남을 만한 놈이라는 것 정도는.

하지만 나 스스로 짐작하는 것과 놈의 입을 통해 직접 듣는 것은 차원이 다른 문제다.

“안 그러냐. 이 인간 같지도 않은 새끼야.”

석고준은 괴물이다. 처음부터 그랬는지, 내가 만들어 낸 괴물인지는 모르겠으나 이제는 아무것도 중요하지 않다.

놈이 죽어야 내 사람이 산다. 그들이 살아야 내가 산다.

그그그그극!

지면 깊숙이 박혀 있던 발을 힘주어 뽑았다. 멈춰 있던 무릎이 곧게 펴진다.

허리와 팔에 힘을 가하자 오러 블레이드의 압력에 밀려 내려가던 창대가 거슬러 오르기 시작했다.

조금씩 천천히. 그러나 멈추지 않고.

“너, 어떻게……!”

석고준의 눈을 부릅떠진 그 순간. 나는 누구에게도 들리지 않을 명령어를 마음속으로 속삭였다.

‘인벤토리 오픈. 백염 수납.’

팟.

그야말로 찰나에 벌어진 일이었다.

거대한 오러 블레이드에 맞서던 청백색의 불꽃이 창과 함께 사라지자, 팽팽하던 힘겨루기의 균형이 무너지며 핏빛 기운이 그대로 내리꽂혔다.

후우우웅! 서걱!

무시무시한 파공성과 함께 베어지는 공간. 하지만 나는 이미 그 자리에 없었다.

검압에 의해 잘려 나간 수십 가닥의 머리카락이 어깨너머로 흩날렸고, 그보다 먼저 석고준의 몸 안쪽으로 깊숙이 파고든 내 주먹은 청백색의 겁화에 휩싸여 있었다.

‘멸염신권(滅炎神拳).’

세상이 느려졌다. 초고온의 열기에 공간이 일그러진다. 마치 지금 석고준이 짓고 있는 표정처럼.

“안-”

이미 늦었어.

나는 들리지 않을 대답과 함께 일권을 내질렀다.

화륵, 콰앙!

이어지려던 놈의 목소리가 굉음에 파묻힌다. 공기를 태우며 빛살처럼 뻗어 나간 주먹이 놈의 명치를 후려친다.

나는 엄청난 충격에 의해 대포알처럼 튕겨 나가는 놈의 신형을 쫓아 몸을 날렸다.

쉬이이익!

맹렬한 바람이 귓가를 스쳤다.

찰나라고 부를 수도 없을 만큼 짧은 시간 속. 단숨에 십여 미터의 거리를 격하고 석고준을 추월한 나는, 정확히 내가 서 있는 쪽을 향해 튕겨 나온 놈을 향해 깍지 낀 양손을 망치처럼 내리찍었다.

꽝! 콰지지직!

복부를 강타한 일격. 연달아 충격을 받은 갑옷의 상반신 부분이 열양지기를 견디지 못하고 녹아내린다.

등으로 지면을 부수며 처박힌 석고준의 입에서 피분수가 뿜어져 나왔다.

푸우우웃!

쓰러진 석고준을 향해 곧장 주먹을 내리꽂으려던 나는 핏물을 고스란히 뒤집어썼다.

온통 붉게 물든 시야. 본능적으로 움직임이 흔들린 그때, 날 선 감각이 경고등을 울렸다.

‘위험!’

이건 실수가 아닌, 다분하게 의도된 공격의 한 과정이다.

나는 깨달음과 동시에 땅을 박찼다. 뒤로 이동하는 내 신형을 향해 붉은 기운이 뻗어 나왔다.

쉭, 서걱!

옆구리로부터 전해지는 뜨거운 통증.

최대한 신속하게 움직였지만, 석고준이 끝끝내 놓치지 않았던 검에서 솟구친 오러는 완벽히 피해 내기에는 너무나도 크고 거대했다.

투둑. 투두둑.

나는 옆구리에서 쏟아지는 핏물을 지혈함과 동시에 핏물을 닦아 냈다.

맑아진 시야 속에서 어느새 몸을 일으킨 석고준이 투구도 벗어 던진 채 쇄도하고 있었다.

감출 수 없는 분노가 담긴 외침이 초토화된 복도를 울렸다.

“이 개새끼가!”

쉬이이잉!

맹렬한 파공성과 함께 검 끝에서 발출된 핏빛 오러가 허공을 관통한다.

연달아 신형을 물리며 아슬아슬하게 공격을 피해 낸 나는 신속하게 양팔을 흩뿌렸다.

오직 내게만 허락된 마법과 함께.

‘인벤토리 오픈. 소환.’

쉬쉬쉭!

불과 일 초 전까지만 하더라도 텅 비어 있던 손아귀에 비수의 손잡이가 붙잡힘과 동시에 쏘아진다.

갑작스럽게 날아드는 여러 개의 빛줄기. 다급해진 석고준이 검신을 가로로 세워 전방을 가로막았다.

카카카캉!

날카로운 마찰음과 함께 네 자루의 비수가 튕겨 나가 벽과 천장에 박힌 순간, 나는 공력을 끌어올려 하반신으로 흘려보냈다. 내디딘 발끝에서 화염이 피어올랐다.

‘염화일로(炎火一路).’

화륵! 쐐애애액!

나는 한 줄기의 불꽃이 되어 석고준을 향해 쏘아졌다. 창도 없이 달려드는 내 모습을 확인한 놈이 고함을 내질렀다.

“죽여 주마!”

어느덧 완연한 핏빛을 띤 눈동자. 붉은 안광이 어둠 속에서 빛난다.

다음 순간, 놈의 전신으로부터 미증유(未曾有)의 기운이 터져 나와 사방을 휩쓸었다.

콰아아아아!

그건 휘몰아치는 폭풍이었고, 벗어날 수 없는 안개였다. 놈은 지치기는커녕 오히려 더욱 강한 기파를 뿜어내고 있었다.

그러나 나는 멈추지 않고 나아갔다. 혼탁하고 거친 마력의 안개를 뚫고 쏘아졌다.

그리고 그것은 안개 너머의 적 역시도 마찬가지였다.

츠츠츠츠!

길이만 2m에 달하는 무식한 크기의 오러 블레이드가 공간을 가르며 날아든다.

신형을 뒤집으며 아슬아슬하게 공격을 피할 때마다 사방을 난도질하는 검압(劍壓)에 살이 터져 나가고 피가 흘렀다.

하지만 괜찮다. 쓰러지지만 않는다면.

놈을 쓰러트려 김화종의 죽음에 대한 대가를 치르고, 남아 있는 이들을 또 다른 위협으로부터 지킬 수만 있다면.

서걱!

순간, 불에 덴 듯한 통증이 가슴을 훑고 지나간다.

지금까지 격전의 여파로 옷과 갑옷은 떨어져 나간 지 오래. 훤히 드러난 맨살 위로 미세한 실선이 그어지고, 이내 붉은 빛을 띠었다.

푸화악!

가슴에서 솟구치는 핏물. 비록 상처는 얕지만, 상흔을 비집고 내부로 스며든 막대한 기운에 눈앞이 아찔했다.

나는 비틀거리는 신형을 바로잡으며 땅을 박찼다.

쾅!

굉음을 뒤로하고 빛살처럼 쏘아진 그 방향의 끝에, 스스로 인간이길 포기한 괴물이 있었다.

“진태겨엉-!”

검을 곧추세운 석고준이 고함과 함께 쇄도했다. 검신을 휘감은 놈의 오러 블레이드는 어느덧 혼탁한 검붉은 빛을 띠고 있었다.

가까워질수록 느껴지는, 이 끈적하면서도 불쾌한 기운.

저것은 더 이상 마나(Mana)라 부를 수 없다.

순수한 마나와는 반대되는 오염되고 불길한 기운을, 이 세상은 다른 이름으로 부른다.

‘마력(魔力).’

그 두 글자가 뇌리에 떠오른 순간. 나는 현재 내가 가진 모든 수를 꺼내야 한다는 것을 깨달았다.

나와 석고준. 석고준과 나.

어느덧 우리 둘 사이의 거리는 서로를 죽일 수 있을 만큼 가까워져 있었다.

나는 놈의 눈동자에 서린 분노를 볼 수 있었고, 뜨거운 숨결에 섞인 악취를 맡을 수 있었다.

그리고…….

나와 석고준은 거의 동시에 팔을 뻗었다.

쉭!

한없이 느려진 세상 속. 바람이 갈라지고 공간이 지워졌다.

내 가슴을 향해 검을 내지른 석고준의 얼굴 위로 희미한 환희가 번졌다.

이겼다.

놈의 눈빛이 그렇게 말하는 듯했다.

맨손인 나와 달리, 혼탁한 마력에 휩싸인 검은 강력하면서도 사정거리가 길었으니 석고준이 승리를 확신하는 것은 당연한 일이었다.

하지만 놈의 생각은 틀렸다.

‘인벤토리 오픈. 소환.’

생각은 빛보다 빨랐고, 시스템은 단 한 치의 망설임도 없이 내 부름에 응답했다.

온통 새하얗게 빛나는 애병(愛兵)은 처음부터 그 자리에 있던 것처럼 내 손아귀에 들어왔다.

투명한 창날 위로 청백색의 겁화를 덧씌우면서.

화륵!

초고온의 열기가 주위의 공기를 태우며 쏘아졌다.

분명 석고준의 검보다 늦게 출발했으나, 혼탁한 오러 블레이드를 스치듯 지나쳐 목표에 도달하는 속도는 기이할 만큼 빨랐다.

푸확!

섬뜩한 파육음과 함께 찾아온 살 타는 냄새.

금방이라도 튀어나올 듯이 부릅떠진 한 쌍의 눈동자에는 더 이상의 환희를 찾아볼 수 없었다.

경악과 고통이 어린 눈빛으로 자신의 가슴을 관통한 창을 내려다보던 석고준이 목소리를 쥐어 짜냈다.

“이게, 무슨.”

나는 담담하게 대답했다.

“후발선제(後發先制). 마정석 따위로 힘을 얻은 너는 죽었다 깨어나도 모르겠지.”

모든 전투와 움직임에는 흐름이 있는 법.

상대방의 움직임을 알고, 예측한다면 출발이 느리다 하여도 더욱 빠르게 도착할 수 있다.

나는 지금까지의 수련과 경험을 통해 후발선제의 묘리를 체득한 상태였고, 석고준은 더욱 큰 힘만을 갈구했다.

그것이 이 싸움의 승패를 갈랐다.

“병신. 죽은 네 스승이 왜 진작 네게 마정석을 권하지 않았었는지 그 돌대가리로 한 번쯤은 생각해 봤어야지.”

“……!”

분노와 혐오가 담긴 내 목소리에, 석고준의 눈동자가 체념한 듯 파르르 떨린 그 순간.

미처 내게 닿지 못한 채 힘없이 내려갔던 검이 번개처럼 솟구쳤다.

쉬잉!

그야말로 순식간이었다.

전과 비교하여 확연히 크기가 줄어든 혼탁한 기운이 검 끝에 맺히고, 내 심장을 향해 찔러 들어온 것은.

그리고 그보다 미세하게 앞선 내가 마음속으로 명령어를 읊은 것은.

‘인벤토리 오픈. 소환.’

카가각!

무시무시한 파괴력과 절삭력을 지닌 기의 집합체가 가로막힌다.

다시 한번 부릅떠진 석고준의 눈동자에 은은한 붉은 빛을 띤 갑옷. 화룡갑(火龍鉀)이 비쳤다.

“이, 이게 뭐…….”

“뭐긴, 병신아. 생명 보험이지.”

최상층까지 돌파하고 가슴에 미약한 상처를 입으면서까지 끝끝내 화룡갑을 꺼내지 않았던 이유는, 지금처럼 혹시 모를 순간을 위해서다.

그리고 내 예상은 정확히 들어맞았다.

“너, 넌 도대체…….”

나는 두려움이 담긴 놈의 눈동자를 바라보았다.

막바지에 몰린 한 인간, 아니 괴물의 눈을.

그리고 석고준의 가슴에 틀어박힌 창에 힘을 가했다.

콰지직!
```

## Final English reading copy

```markdown
# Chapter 593

*Wham!*

With a dull impact, the punch I threw with all my strength slammed into Go Jun’s chest.

The layered defensive Magic shattered in an instant, and part of his impossibly sturdy full-body armor caved inward. Gritting his teeth, he roared in fury.

“Jin Taekyung!”

An ordinary high-level Hunter or Peak master would have suffered severe Internal Injury from that punch and been rendered unable to fight.

But Go Jun was different. Perhaps because of the Magic Gem, even my Inner-Family Heavy Hand failed to inflict any serious damage on him.

*An S-rank Hunter. And more.*

Whatever the circumstances, he was already a formally recognized S-rank Hunter.

Not only had he learned internal cultivation techniques known in the modern world as mana cultivation techniques, he had also absorbed the energy of an S-grade Magic Gem obtained from a Named Monster. His strength was tremendous.

“Die!”

*Whoooooom! KABOOM!*

The energy, which had gone beyond red and taken on the unmistakable color of blood, burst outward like an explosion.

White Flame’s shaft trembled under the Taishan-like pressure pouring from the enormous Aura Blade.

*I’ve never been pushed back this badly before.*

At this moment, even three jiazi of internal energy and physical abilities beyond the limits of humanity felt insufficient.

Perhaps it was the fatigue that had accumulated without pause throughout the day. Or perhaps the amount of magical power Go Jun had absorbed was simply that immense.

But one thing was certain……

This idiot I was fighting had gained strength far beyond anything I had expected.

*Rrrrrumble. Crack!*

Under the tremendous pressure descending from above, my body and the ground sank together. By the time I was buried in the ground up to my ankles, Go Jun bared his teeth and grinned.

“Starting to get the picture? Hmm? Are you finally beginning to feel like you’re well and truly fucked?”

A low laugh escaped him.

Go Jun was genuinely enjoying himself now. He was delighted by the thought that he could finally avenge his Master.

“From the day my Master died, I killed you every night, over and over again. I lived while waiting for a moment just like this.”

I watched for an opening and answered.

“No wonder I felt like I was being reborn every morning. I thought it was because I kept dreaming about Jungryong dying every night and waking up refreshed.”

*Fwoosh!*

The instant the blood-red energy shook violently, I pulled my deeply buried foot free and kicked upward.

*Boom!*

My toes, swinging like a beam of light, were blocked by his shin with a thunderous crash. Go Jun, who had been about to pour out his anger, let out a hollow laugh.

“It’s too late to struggle now. Since things have come this far, killing every last one of them will be easy.”

“What?”

I blinked, unable to properly understand what he meant. Then Go Jun’s quiet voice pierced my ear.

“You and that goddamned Peace Guild. And your parents and that bitch of a little sister waiting at home… Ah. Your old man was already dead, wasn’t he? Well, it doesn’t really matter. Even if he were still alive, he would’ve died following his son soon enough.”

“……”

“Did you enjoy being called a hero by the world? Did you think you’d all live happily ever after? It was all bullshit. Kim Hwajong, that old man, was only the beginning.”

His sticky, unpleasant breath washed over my face. A cackling laugh followed.

“This time it’s you, then Choi Minwoo. After that, I don’t care who it is. I’ll kill everyone with even the slightest connection to you, one by one. Sweeping them all away with a Monster Wave sounds good, too. What do you think?”

As his voice continued to pour into my ears, I blinked blankly.

*What the fuck is this bastard saying right now……?*

It was strange. The thing standing before me clearly had the appearance of a human being, but the mouth that kept taunting me without pause produced nothing but the barking of a dog.

A monster wearing a human shell stood before me.

*So he’s going to kill them? All my people?*

I suddenly felt nauseated.

I hated Go Jun for being the kind of person who could turn words like these into action. And when I imagined the people who had become indispensable to me lying dead, my mind seemed to go blank.

*Mother. Hayeon. Team Leader Choi. Uncle Kkeokjeong, Song Song, Jin-ho hyung……*

Familiar faces flashed before my eyes one after another. The silver-haired old butler who had met his death on the snow-covered mountain was among them.

*He’s going to kill them all, and he’s asking what I think?*

The next moment, a calm voice escaped between my lips.

“Fine. I understand.”

“What?”

“Go ahead. Just try.”

The smile lingering around Go Jun’s mouth faded. At the same time, I summoned every last bit of strength in my body.

*Grrrrrkk.*

The spear that had been slowly sinking under the terrifying pressure stopped. My knees, which had been bending, stopped in place as well.

At least for this moment, I forgot my fatigue. The muscles throughout my body still throbbed as though they might tear from the lingering aftermath of One Annihilation, but I forgot that pain, too.

The anger layered over my fatigue and pain covered and paralyzed everything else.

Internal energy like molten lava boiled within the Eight Extraordinary Meridians buried deep inside my body and hundreds of acupoints.

A voice as hot as flame flowed from between my parted lips.

“You shouldn’t have said that.”

“……!”

“You shouldn’t have talked about my people that way. At the very least, you shouldn’t have.”

I had suspected it. I knew that Go Jun was the kind of bastard who was capable of doing something like this.

But suspecting it myself and hearing it directly from his mouth were entirely different matters.

“Don’t you agree, you inhuman piece of shit?”

Go Jun was a monster. I did not know whether he had been one from the beginning or whether I had created him, but none of that mattered anymore.

He had to die for my people to live. They had to live for me to live.

*Grrrrrrkk!*

I forcefully pulled my foot from the ground. My stalled knee straightened.

When I put strength into my waist and arms, the spear shaft that had been forced downward by the Aura Blade began to rise against it.

Slowly, little by little. But without stopping.

“How are you……?”

The instant Go Jun’s eyes widened, I whispered a command that no one else could hear.

*Inventory open. Store White Flame.*

*Pop.*

It happened in the blink of an eye.

The blue-white flames that had been opposing the enormous Aura Blade vanished together with the spear. The balance of the tense struggle collapsed, and the blood-red energy slammed downward.

*Whoooooom! Slice!*

Space was cleaved apart amid a terrifying shriek of displaced air.

But I was no longer there.

Dozens of strands of hair severed by the sword pressure scattered over my shoulder. Before they even fell, my fist was already deep inside Go Jun’s guard, wreathed in blue-white hellfire.

*Flame-Extinguishing Divine Fist.*

The world slowed.

Space warped in the ultra-high temperature heat. It looked almost like the expression Go Jun was making now.

“No—”

Too late.

Along with a reply he could not hear, I threw my punch.

*Fwoosh—KABOOM!*

His voice, which had been about to continue, was buried beneath the thunderous impact. My fist, extending like a beam of light while burning through the air, slammed into his solar plexus.

I launched myself after his body as the tremendous impact sent him flying like a cannonball.

*Whoooooosh!*

A fierce wind brushed past my ears.

In a moment too brief to even call an instant, I crossed more than ten meters in a single burst and overtook Go Jun. As his body flew back toward the spot where I stood, I brought my clasped hands down like a hammer.

*CRASH! KRAKAKAK!*

The blow struck his abdomen. His armor’s upper body, battered by the consecutive impacts, melted under the Scorching Yang Qi.

Go Jun slammed into the ground, shattering it with his back, and a fountain of blood burst from his mouth.

*Pshhh!*

I moved to drive my fist down into the fallen Go Jun, only to be drenched in the blood he spat out.

My vision turned completely red. My movements instinctively faltered, and a sharp instinct rang out like a warning alarm.

*Danger!*

This was not a mistake. It was part of an attack he had deliberately set up.

The instant I realized it, I kicked off the ground. Red energy shot toward my body as I moved backward.

*Shhk! Slice!*

Hot pain spread from my side.

I had moved as quickly as possible, but the Aura erupting from the sword Go Jun had never once let go of was too large and massive to evade completely.

*Drip. Drip-drip.*

I staunched the blood pouring from my side while wiping the blood from my eyes.

Through my cleared vision, I saw Go Jun charging toward me after rising to his feet. He had thrown off his helmet.

A furious shout filled the devastated corridor.

“You fucking bastard!”

*Whoooooosh!*

The blood-red Aura released from the tip of his sword pierced through the air with a fierce shriek.

I narrowly avoided the attack by repeatedly retreating, then quickly flung both arms outward.

Along with the Magic that only I was permitted to use.

*Inventory open. Summon.*

*Shhk-shhk-shhk!*

Handles appeared in my empty hands, and several daggers shot forward at the same time.

Multiple streaks of light flew toward him without warning. Go Jun, now desperate, turned his sword sideways and held the blade across his front.

*Clang-clang-clang-clang!*

The four daggers bounced away amid sharp scraping noises and embedded themselves in the walls and ceiling. At the same moment, I drew up my internal energy and sent it flowing into my lower body. Flames rose from the tip of my advancing foot.

*Flamefire Path.*

*Fwoosh! Whoooooosh!*

I became a streak of flame and shot toward Go Jun. Seeing me charging without my spear, he let out a roar.

“I’ll kill you!”

His eyes had taken on the unmistakable color of blood. Red light gleamed from them in the darkness.

The next moment, an unprecedented energy burst from his entire body and swept in every direction.

*WHOOOOOOOOOM!*

It was a raging storm and an inescapable fog. Rather than tiring, Go Jun was emitting an even stronger wave of energy.

But I continued forward without stopping. I shot through the murky, violent fog of magical power.

And the enemy beyond the fog was doing the same.

*Zzzzzzzzz!*

An absurdly oversized Aura Blade, a full two meters long, flew toward me and cleaved through space.

Every time I twisted my body and narrowly avoided an attack, flesh tore and blood flowed beneath the Sword Pressure cutting through everything around me.

But it was fine.

As long as I did not fall.

As long as I could bring him down, make him pay the price for Kim Hwajong’s death, and protect those who remained from another threat.

*Slice!*

A moment later, pain like a burn swept across my chest.

My clothes and armor had long since been torn away by the aftermath of the fierce battle. A thin line appeared across my exposed skin, then turned red.

*Fwoosh!*

Blood surged from my chest. The wound was shallow, but the immense energy forcing its way inside through the cut made my vision swim.

I straightened my staggering body and kicked off the ground.

*Boom!*

I shot forward like a beam of light, leaving the thunderous boom behind me. At the end of my path stood a monster that had willingly abandoned its humanity.

“Jin Taekyuuung!”

Go Jun charged with a shout, his sword held upright. The Aura Blade wrapped around the weapon had taken on a murky, dark-red glow.

The closer I drew, the more clearly I felt that sticky, unpleasant energy.

*That can no longer be called mana.*

The corrupted and ominous energy opposite to pure mana was known by another name in this world.

*Demonic energy.*

The instant those two words surfaced in my mind, I realized that I had to bring out every move I had.

Me and Go Jun. Go Jun and me.

The distance between us had grown close enough for either of us to kill the other.

I could see the fury in his eyes and smell the foul odor mixed into his hot breath.

And then……

Go Jun and I extended our arms at almost the exact same moment.

*Shhk!*

The world slowed to a crawl. The wind split apart, and space was erased.

Faint delight spread across Go Jun’s face as he thrust his sword toward my chest.

*I won.*

His eyes seemed to say as much.

Unlike me, who was empty-handed, Go Jun wielded a sword wrapped in murky magical power. It was powerful, and it had a long reach. Of course he was certain of victory.

But he was wrong.

*Inventory open. Summon.*

Thought was faster than light, and the System answered my call without a moment’s hesitation.

My beloved weapon, shining pure white, appeared in my grasp as though it had been there from the beginning.

Blue-white hellfire coated its transparent spearhead.

*Fwoosh!*

Ultra-high-temperature heat shot forward, burning the surrounding air.

It had clearly started later than Go Jun’s sword, yet its speed was so strangely fast that it brushed past the murky Aura Blade and reached its target.

*Fwoosh!*

The horrifying sound of flesh being pierced was followed by the smell of burning skin.

Go Jun’s eyes were wide open as though they might burst from their sockets, but there was no longer any delight in them.

He looked down at the spear piercing through his chest, his eyes filled with shock and pain, and forced the words out of his throat.

“What is this……?”

I answered calmly.

“Striking Second, Hitting First. Someone who gained strength from a Magic Gem like you would never understand it, even if you died and came back to life.”

Every battle and every movement had a flow.

If you knew and predicted your opponent’s movements, you could arrive faster even if you started later.

Through my training and experience, I had mastered the intricacies of Striking Second, Hitting First. Go Jun had sought nothing but greater power.

That was what decided the outcome of this fight.

“Idiot. You should’ve used that rock of a head at least once to think about why your dead Master never recommended Magic Gems to you in the first place.”

“……!”

At the sound of my voice, filled with anger and disgust, Go Jun’s eyes trembled as though he had resigned himself to his fate.

Then the sword that had dropped limply without reaching me shot upward like lightning.

*Shing!*

It happened in an instant.

The murky energy, visibly smaller than before, gathered at the tip of the sword and stabbed toward my heart.

And just before it reached me, I recited another command in my mind.

*Inventory open. Summon.*

*KRAK!*

The mass of energy, packed with terrifying destructive and cutting power, was blocked.

In Go Jun’s eyes, which had widened once more, the armor with a faint red glow was reflected.

Fire Dragon Armor.

“What, what is this……?”

“What do you think it is, idiot? Life insurance.”

The reason I had kept the Fire Dragon Armor hidden all the way to the top floor—even after taking a minor wound to the chest—was to save it for an unexpected moment like this.

And my prediction had been exactly right.

“You…… What the hell are you……?”

I looked into the fear in his eyes.

Into the eyes of a human—or rather, a monster—driven to the edge.

Then I put strength into the spear embedded in Go Jun’s chest.

*KRAK!*
```
