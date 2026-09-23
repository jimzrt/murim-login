<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0833.txt",
      "sha256": "736bb5a20ca949fc12970988c9a8e5609d47433003e5c67ab8132f38d3d9e207",
      "bytes": 14041
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b2c14048528cb50c470ce6c8bd224a8b30bad1ae4f44e1403296f3f67d55d0c9",
      "bytes": 1798
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ad6965cfcc54bdbb79c84cfefd2d5c0b76d1e8fdd3994cdc0d6cd2934374048b",
      "bytes": 226906
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8b5610e4dd8c76414861d0e9a24caf5517414a68832c0faca160eaea28920c92",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "4f13df75fe4d7d57672b57dd43d1d4476a0bce3b9859df85d9c6f1bdcc1e57bf",
      "bytes": 866
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "f976a52922d30a81e2fa3c3de9722ab66b13034333f82ee9e034fad4c05ff677",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "6895f9faa77f578778890f3cea8e05d82f982a2736022a4673785141a8a0c320",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "bc35421de6665e27492283e4c4f3786340e26bf50d67e143791c24b956bd44f3",
      "bytes": 1848
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d9319d021c3c0bcb4cd122f1aabdf4c4fd0eabae083ef6aa21f8ceaa8121dba2",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "96134f11296a554834a3797645761a500b2edddca81f38a49e5f9f489cb4e023",
      "bytes": 622
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "61c78349919c31300581fe9dbed0888a1a87fa87db93522c07143c7c94609139",
      "bytes": 755
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9efad41a2b865bcf5c939bc36568267e2332e7ce051f57c19cbf5cf82b65cc36",
      "bytes": 251423
    }
  ],
  "estimated_tokens": 12133
}
-->

# Durable State Update — Chapter 833

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 833. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 833. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 833,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 833,
    "continuity_sources": [833],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The Doppelganger’s prepared summoning plan proceeded despite its death; the Demon Realm’s boundary temporarily opened and unidentified beings invaded.",
    "The Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "Jin collapsed from exhaustion after warning the Skeleton King to notify the World Hunter Federation.",
    "The System automatically transferred Jin to Murim while he was unconscious; Login succeeded.",
    "Ahomed Jemal Pasha led the Prophet’s remaining mage disciples in completing their prepared ritual; a red-eyed being emerged."
  ],
  "continuity_sources": [
    831,
    832
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and what is the identity of the summoned being?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?"
  ],
  "safe_through": 832,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 살기     | **killing intent**                               |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 로그인              | **Login**                      |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 대지모신 | **Earth Mother Goddess** | New deity proclaimed by Jin Taekyung as Nanman's One God. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |
| 선지자 | 아호메드 | The Prophet regards Ahomed as his brother and Disciple. | Ahomed | Familiar but respectful. | The Prophet entrusts Ahomed with carrying on the mission. |
| 아호메드 | 선지자 | Ahomed is the Prophet’s Disciple and regards him as a spiritual brother. | Prophet | Honorific and deferential. | Ahomed addresses him as 선지자시여. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 832
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 832
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 825
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 724
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 795
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 830
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 830
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 832
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** A calculating, ruthless impostor who exploits followers’ faith and turns to brutal violence when they question or outlive their usefulness.
- **Voice:** Mysterious, genderless, and age-indeterminate, shifting from solemn religious reassurance to cold, contemptuous taunts.
- **Relationships:** The Prophet was revered by his followers and regarded Ahomed as a brother and Disciple; he made a pact with Michael Silbert during the 2020 Battle of Paris.

## Korean source

```text
＃833화



몽롱하다.

마치 중력이 존재하지 않는듯한 부유감이 전신을 지배한다.

그 이질적인 감각 속에서 눈을 뜬 진태경은 고장 난 TV 화면처럼 노이즈 낀 시야 너머로 펼쳐진 낯선 광경을 멍하니 지켜보았다.

‘여긴 어디지?’

주위를 둘러보자 답은 금방 나왔다.

천장에 매달린 종유석(鐘乳石)과 축축한 바닥과 공기.

기존의 상식을 벗어날 만큼 넓었기에 곧장 알아차리지 못했을 뿐, 그곳은 동굴이었다.

그리고 곳곳에 인위적인 손길이 닿아 있는 그곳에는, 어림잡아 수만에 달하는 인파가 모여 있었다.

- 오오. 오오오……!

- 인샬라!

마치 메아리처럼 아득하게 들려오는 외침.

긴 로브를 걸친 누군가가 부르짖자, 수많은 이들이 도미노처럼 물결치듯 무릎을 꿇는다.

허리가 굽어 있는 노인도, 두 손을 꼭 붙잡고 있는 남녀도, 순진하게 눈망울을 반짝이고 있던 아이들도 예외는 아니었다.

아니, 오직 그들만이 전부였다.

중동 어디에서나 볼 수 있을 만큼 흔하고, 평범한 이들.

그들 중 눈에 띄는 것은, 알 수 없는 문양으로 가득한 로브를 걸친 일단의 무리뿐이었다.

스륵.

긴 로브의 옷자락이 바닥을 스친다. 느슨하게 싸맨 터번 사이로 새하얀 백발을 드러낸 늙은이가 두 손을 활짝 펼쳤다.

- 신의 사자시여! 이 더럽혀진 세상을 바로 세우실 신의 철퇴시여!

그 외침을 들은 순간, 진태경은 눈 앞에 펼쳐진 낯선 광경 속에서도 가장 이질적인 무언가를 발견했다.

‘저건…….’

그것은 어둠이었고, 불이었다.

드넓은 동공의 절반을 메우고도 모자라, 천장에 닿을 만큼 높게 쌓인 무수한 마정석을 장작 삼아 타오르는 불길.

지금껏 알아차리지 못한 것이 이상하게 느껴질 정도로 짙은 어둠이 불길처럼 일렁였다.

그 안에 실린 미증유의 기운이 당장이라도 터져 나올 것처럼 꿈틀거렸다.

스아아아.

그 기이한 광경을 바라보는 늙은 마법사의 눈동자가 환희에 젖었다.

전율로 몸을 떨면서도 토해 낸 마지막 외침과 함께, 그의 손에 들린 지팡이가 빛을 내뿜었다.

- 마침내, 저희에게 임하소서!

그 순간.

쩌억.

마치 태중의 아이가 스스로의 힘으로 세상에 나오듯, 굳게 닫혀 있던 어둠 너머의 공간이 아가리를 벌렸다.

동시에 용틀임하듯 거세게 몸부림친 검은 불길이 헤아릴 수 없을 만큼 많은 마정석들을 집어삼켰다. 정제되지 않은 순수한 마력(魔力)이 지면에 아로새겨진 마법진을 타고 불길로 이어졌다.

끝없이. 모든 기운을 쏟아붓고 잿가루가 되어 사라질 때까지.

파스스슥.

바스러진다. 마정석의 산이 허물어진다.

진태경은 아연한 시선으로 제 역할을 다한 마력의 덩어리가 모든 힘을 잃고 흩날리는 모습을 지켜보았다.

자신이 그토록 찾고자 했던 거대한 폭탄이, 지난 수십여 년간 세상의 눈을 피해 어딘가로 흘러 들어갔던 재앙의 씨앗이 발화하는 그 광경을.

그리고 마침내 만개(滿開)한 재앙이, 갈라진 공간의 틈새로 걸어 나오는 광경을.

저벅.

새하얀 맨발이 지면을 밟았다. 인간과 다를 것 없는 두 다리와 팔. 그러나 동시에 그 누구와도 다르다는 것을 증명하듯 번뜩이는 붉은 안광(眼光).

하아아.

실오라기 하나 걸치지 않은 흑발의 사내는 느릿하게 호흡했다.

기나긴 항해 끝에 고향으로 돌아온 뱃사람처럼. 혹은 먹음직스러운 먹잇감을 앞에 둔 포식자처럼.

그리고 조금 전 보였던 안광이 무색할 만큼, 어느덧 새카맣게 물든 눈동자로 새로운 세상을 눈에 담았다. 주위를 둘러싼 그 모든 것을 보고 느꼈다.

희미한 햇빛이 스며드는 천장.

습기를 머금은 공기와 신께 경배하듯 축축한 바닥에 바짝 엎드린 수만 명의 사람.

마지막으로 비틀거리며 자신을 향해 다가오는 늙은 마법사까지.

- 아아. 아아아.

마법사, 아호메드는 눈물을 줄줄 흘리며 사내를 바라보았다.

핏줄이 비칠 만큼 투명한 피부와 믿어지지 않을 만큼 아름다운 용모. 그리고 그 안에서 용솟음치는 아득한 기운까지.

틀림없다.

눈앞의 사내야말로 신이 내린 사자요, 그야말로 신인(神人)이라 부를 수 있는 존재였다.

- 선지자시여, 보고 계시나이까. 마침내 당신의 예언이 이루어졌습니……!

아호메드가 사내에게 양팔을 벌린 그 순간.

서걱.

전율로 가득하던 목소리가 뚝 끊겼다. 동시에 늙은 마법사의 육신이 썩은 통나무처럼 허물어졌다.

투둑. 툭.

조각난 팔과 다리가, 분리된 상반신과 하반신이.

그리고 마지막으로 몸뚱어리에서 비스듬히 미끄러진 목이 땅에 떨어졌다.

마치 실 공처럼 데굴데굴 굴러 발치에 닿은 망자의 얼굴을, 사내는 물끄러미 내려다보았다.

- 수고했다.

그것이 전부였다.

수십 조각으로 나뉜 노 마법사의 시체를, 사내의 주위에서 꿈틀거리던 어둠이 끌어당겨 삼켰다. 분해하고 녹여서 소화해 냈다.

콰드드득.

뼈와 살이 분쇄되는, 끔찍한 소리가 침묵에 빠진 동굴 내부를 울렸다.

- ……!

믿을 수 없는 광경을 두 눈으로 목격한 수만 명의 인간이 얼어붙었다.

조금 전까지만 해도 성공의 기쁨에 가득 차 있던 마법사들도, 꿈인 듯 현실인 듯 몽롱한 시야 속에서 이 모든 것을 지켜본 한 사람도 마찬가지였다.

‘놈이다.’

진태경은 본능적으로 깨달았다.

홀로 우뚝 선 저 이질적인 사내가 이 땅에 존재해서는 안 되는 무언가라는 것을.

서서히 닫혀 가는 저 공간의 틈새 속에서, 신에게 저주받은 죽음의 세상에서 건너온 악마라는 것을.

스르륵.

핏방울 하나 없이 게걸스럽게 시체를 집어삼킨 어둠이 사내를 휘감았다. 머리부터 발끝까지. 고풍스러운 흑색 비단이 되어 사내를 치장한 그것이 망토가 되어 어깨에 내려앉았다.

아니, 동시에 거대한 날개처럼 솟구쳤다.

파아아앗!

진태경은 보았다.

끝없이 뻗어 나가는 어둠을. 천장 틈새로 새어 들어온 햇빛을 지우고, 석상처럼 굳어 있는 인간들의 머리 위로 드리워지는 죽음을.

산 것과 죽은 것.

그 모든 것을 집어삼키는 마력의 폭풍.

산산이 부서지는 동굴과 끔찍한 비명 속에서, 진태경을 둘러싸고 있던 악몽이 조각나며 깨어졌다.

콰드드드득!



* * *



흡.

나는 눈을 뜸과 동시에 참았던 숨을 토해 냈다.

동시에 보이는 낯선 천장. 그리고 어디선가 들려오는 말발굽 소리에 맞춰 조금씩 흔들리는 몸뚱어리.

“아.”

외마디 신음과 함께 눈을 깜빡였다. 마음을 가다듬으며 한 차례 심호흡하자, 습한 열기를 머금은 공기가 폐로 스며들었다.

‘이곳은…….’

굳이 주위를 자세히 둘러보지 않더라도 알 수 있었다.

나는 마차에 누워 있었고, 두어 달 만에 다시 느끼는 남만(南蠻) 특유의 뜨겁고 습한 공기는 익숙했다.

물론 현대와의 시간 차이를 생각한다면, 두 달이 아니라 몇 시진 정도겠지만.

‘마지막에 들었던 그 시스템 알림이, 꿈이 아니었어.’

갑작스럽게 찾아온 안도감에 맥이 탁 풀린다.

현대에서의 마지막 순간. 심력(心力)이 바닥난 나는 로그인조차 시도하지 못할 정도로 지쳐 있었다.

아마도 시스템이 반강제적으로나마 돕지 않았더라면, 무슨 일이 일어나는지도 모르는 채 며칠 동안은 쓰러져 있었을 것이 분명 하…… 아니, 잠깐만.

‘시스템 업데이트?’

혼잡한 기억 속에서도 유독 선명하게 남아 있는 단어.

내가 들었던 시스템 알림이 모두 사실이라면, 지금까지 단 한 번도 없었던 변화가 생겼음이 분명하다.

황급히 상반신을 일으킨 나는 마음속으로 중얼거렸다.

‘상태창 오픈.’

그러나 설마 했던 마음처럼, 아무 일도 일어나지 않았다.

아무리 허공을 노려봐도 반투명한 홀로그램 창은 나타나지 않았고, 명령어와 동시에 울렸어야 할 맑은 종소리도 어디에서도 들리지 않았다.

“……이런 시벌.”

당혹스러운 마음에 나도 모르게 욕설이 튀어나왔지만, 갑작스러운 시스템 먹통의 원인에 대해 내심 짐작 가는 바가 있었다.

시스템 업데이트.

‘업데이트가 완료되기까지는 사용 불가, 뭐 그런 건가?’

어릴 때부터 몸 쓰는 걸 워낙 좋아해서 컴퓨터와는 거리가 먼 삶을 살아온 나지만, 업데이트는 스마트폰을 사용하는 현대인이라면 누구나 경험해 본 일이다.

다만 이 정도로까지 당황스러운 건, 도무지 예측하지 못한 일이었기 때문이다.

‘생각해 보면 이것도 하나의 프로그램이니까 업데이트를 할 수도 있긴 한데.’

도대체 어떤 미친놈이 이런 걸 만들고 업데이트까지 하나 싶지만, 그 일이 실제로 벌어졌다.

아니, 어쩌면 이건 당연한 일이다.

두 세상을 연결하고 게임처럼 레벨 업도 시켜 주는, 이런 정신 나간 시스템도 존재하는데 업데이트 정도는 약과지.

더군다나…….

‘그런 일까지 벌어졌으니까.’

나는 문득 떠올렸다. 도플갱어를 소멸시킨 직후, 시스템이 내게 알려 주었던 그 믿을 수 없는 정보들을.

더불어 지금 이 순간 다시 한번 깨달았다. 내가 끝끝내 막지 못한, 거대하고도 끔찍한 재앙이 시작되었다는 사실을.

꾸욱.

나도 모르게 힘이 들어간 손아귀. 새하얗게 물든 주먹이 파르르 떨린다. 동시에 악몽으로 찾아왔던 꿈속의 광경이 눈앞을 스쳤다.

사실 지금도 모르겠다.

내가 본 그 광경들이 시스템이 내 꿈을 통해 은밀하게 전달한 현실인지, 아니면 혼란스러운 내 무의식이 빚어낸 악몽인지.

혹은, 예지몽(叡智夢)이라 부르는 무언가인지.

하지만 그저 악몽이길 바라는 마음과는 달리, 나는 이미 본능적으로 짐작하고 있었다.

‘그건…… 단순한 악몽이 아니었어.’

노이즈 낀 시야 속에서도 똑똑히 보았다. 선명하게 기억난다.

수많은 마정석과 마법진을 매개체 삼아 잠시나마 벌어진 공간의 틈새, 그리고 끔찍하리만치 거대한 마력을 휘감은 채 아무런 저항도 못 하는 수만 명의 광신도를 도륙하던 사내의 모습이.

아니, 어째서인지 인간의 모습을 하고 있던 악마의 모습이.

‘설마.’

순간 머릿속에 떠오른 한 존재의 이름을, 나는 애써 지워 냈다.

놈의 정체가 무엇인지는 아직 모른다.

그러나 도플갱어와 대화를 나누며 느꼈던 태도와 돌아가는 상황을 짐작해 보았을 때, 그 사내의 이름은 아스모데우스가 아니다.

만에 하나. 정말 놈의 정체가 마왕이라 하더라도…….

‘내게는 충분한 시간이 있다.’

구화산(九華山)에 틀어박혀 수련했듯, 무림에서 일 년 남짓한 시간을 보내더라도 현대에서는 고작 며칠이 흐를 뿐이다.

시스템이 존재하는 한, 시간은 내 편이었다.

‘암천(暗天)은 내 편이 아니겠지만.’

내심 중얼거린 나는 자리에서 일어나 마차 내부를 둘러보았다.

요새 남만야수궁에서 차박이라도 유행하는지, 과장 좀 보태서 대형 객잔의 별채만큼이나 넓은 공간에는 나 혼자뿐이었다.

‘뭐 조용해서 좋긴 한데, 다들 어디 간 거야?’

응당 곁에 있어야 할 익숙한 얼굴들이 보이지 않는다.

화룡각의 인원들도. 호법을 선답시고 옆자리에 앉아서 꾸벅꾸벅 졸고 있어야 할 혁무진과 내 고백에 현대를 선계(仙界)로 이해하고 입이 쩍 벌어졌던 적천강의 모습도 보이지 않았다.

‘도대체 어디…… 응?’

몸도 풀 겸 마차 안을 어슬렁거리던 그때, 나는 문득 귓가를 파고드는 익숙한 목소리를 들었다.

“지금 중원은 이미 대지모신님이 폐기 처분 했어요. 지금 중원 무림은 누구 중심으로 돌아가는 것이냐, 우리 조장님. 대태원진가의 열화신룡을 중심으로 돌아가게 되어 있다고.”

“오오. 오오오.”

이게 도대체 뭔 소리지.

나는 웅성거림 속에서 유독 크게 울려 퍼지는 목소리에 귀를 기울였다.

“바로 그 열화신룡 믿고 따르는 것이 누구냐. 바로 나요. 왜 그런지 아시오? 나는 조장님의 보좌를 딱 잡고 살기 때문에! 가장 신뢰하는 수하이기 때문에 딱 잡고 있어요.”

“딱 잡아? 어떻게 말이오?”

“조장님. 꼼짝 마! 열화신룡 까불면 나한테 죽어! 내가 이렇게 우리 조장님하고 친하단 말이에요. 엄청나게 친해.”

“허어어.”

“대지모신의 아들이 누구냐, 바로 열화신룡. 그런데 그 열화신룡을 꽉 붙잡고 있는 것이 누구냐!”

클라이맥스로 치닫는 그 순간. 나는 창문 사이로 고개를 내밀었다.

“듣다 보니까 궁금하네. 그게 누군데.”

혁무진이 호탕하게 웃으며 고개를 돌렸다.

아니, 나와 눈이 마주친 순간 딱딱하게 굳어버렸다.

“나! 혁무……어, 시발.”

“시발?”

“아.”

“아?”

따라와, 이 새끼야.
```

## Final English reading copy

```markdown
# Chapter 833

Dazed.

A sensation of floating, as though gravity didn’t exist, took over my entire body.

Jin Taekyung opened his eyes amid that alien sensation and stared blankly at the unfamiliar sight spread out before him, beyond a field of vision full of static like a broken television screen.

*Where am I?*

He looked around, and the answer came quickly.

Stalactites hanging from the ceiling. A damp floor and humid air.

He hadn’t recognized it right away only because it was so vast that it defied common sense, but this was a cave.

And in that place, where the hand of man had clearly been at work, a crowd of tens of thousands had gathered, by his rough estimate.

“Ooh. Ooooooh…”

“Inshallah!”

Shouts reached him from far away, like echoes.

At the cry of someone wearing a long robe, countless people sank to their knees, rippling through the crowd like dominoes.

The hunched old men, the men and women clasping both hands together, even the children whose innocent eyes had been sparkling—all of them did the same.

No. They were the only ones there.

Ordinary people, the kind you could see anywhere in the Middle East.

The only ones who stood out among them were a group wearing robes covered in mysterious patterns.

*Swish.*

The hem of a long robe brushed the floor. An old man with snowy white hair showing through his loosely wrapped turban spread both arms wide.

“O Messenger of God! O God’s hammer, come to set this defiled world right!”

At the sound of that shout, Jin Taekyung spotted something in the unfamiliar scene before him that was stranger than anything else.

*That’s…*

It was darkness. And fire.

The flames blazed using countless Magic Gems as kindling, filling half the vast cavern and piling so high they nearly touched the ceiling.

The darkness rippled like flames, so dense that it seemed strange he hadn’t noticed it until now.

An unprecedented energy seethed within, as if it might burst out at any moment.

*Fwoooooosh.*

The old mage’s eyes shone with rapture as he gazed at the bizarre sight.

His body trembled with awe, but he still managed to cry out one last time. The staff in his hands blazed with light.

“At last, descend upon us!”

At that moment—

*Crack.*

Like a child in the womb forcing its way into the world, the space beyond the tightly closed darkness opened its jaws.

At the same time, the black flames writhed violently like a twisting dragon and devoured countless Magic Gems. Unrefined, pure magical power raced along the magic circle carved into the ground and flowed into the flames.

On and on. Until the Magic Gems had poured out all their energy and crumbled to ash.

*Crackle.*

The mountain of Magic Gems crumbled. It collapsed in on itself.

Jin Taekyung watched, stunned, as the mass of magical power that had served its purpose lost all its strength and scattered.

He watched the enormous bomb he’d been searching for with such desperation ignite—the seed of calamity that had slipped away somewhere, hidden from the world’s eyes for decades.

And at last, the calamity in full bloom stepped through a crack in space.

*Step.*

A snow-white bare foot touched the ground. Two legs and two arms, no different from a human’s. And yet, his glinting red eyes proved that he was unlike anyone else.

*Haaah.*

The black-haired man, wearing not a single thread of clothing, breathed slowly.

Like a sailor returning home after a long voyage. Or a predator facing a mouthwatering meal.

Then, with the red glint from moments ago all but forgotten, he took in the new world through eyes that had turned pitch-black. He looked around and sensed everything.

The faint sunlight filtering through the ceiling.

The damp air, and tens of thousands of people pressed flat against the wet floor as if worshiping God.

And lastly, the old mage staggering toward him.

“Ah… Ahhh…”

The mage, Ahomed, stared at the man with tears streaming down his face.

Skin so translucent his veins showed through. A face so beautiful it was hard to believe. And a distant power surging within him.

There was no doubt.

The man before him was the messenger sent by God—a being who could truly be called a divine man.

“O Prophet, are you watching? At last, your prophecy has come true—!”

The instant Ahomed opened his arms toward the man—

*Slice.*

His voice, trembling with emotion, cut off abruptly. At the same time, the old mage’s body collapsed like a rotten log.

*Thump. Thud.*

His arms and legs, torn apart. His upper and lower body, severed.

And last of all, his head slid diagonally off his torso and hit the ground.

The man stared down at the dead face that rolled like a ball of thread until it reached his feet.

“You did well.”

That was all.

The darkness writhing around the man pulled in the old mage’s corpse, now split into dozens of pieces, and swallowed it. It broke it down, melted it, and digested it.

*Crunch.*

The horrible sound of bones and flesh being crushed echoed through the silent cavern.

“……!”

Tens of thousands of people froze as they witnessed the unbelievable sight with their own eyes.

So did the mages who, until just moments ago, had been filled with the joy of success—and the one man who had watched it all through a dreamy, half-real haze.

*That’s him.*

Jin Taekyung knew it instinctively.

That strange man standing alone was something that had no place in this world.

A demon who had crossed over from a world of death, cursed by God, through that slowly closing crack in space.

*Rustle.*

The darkness, which had greedily swallowed the corpse without a single drop of blood, coiled around the man from head to toe. It adorned him like luxurious black silk, then settled across his shoulders as a cloak.

No—at the same time, it surged upward like a pair of enormous wings.

*Flash!*

Jin Taekyung saw it.

The darkness stretching out without end, blotting out the sunlight seeping through cracks in the ceiling and casting death over the heads of the people frozen like statues.

The living and the dead.

A storm of magical power that swallowed everything.

As the cavern shattered and terrible screams filled the air, the nightmare surrounding Jin Taekyung broke apart, and he woke.

*CRUUUUNCH!*

* * *

*Hah.*

I opened my eyes and let out the breath I’d been holding.

At the same time, I saw an unfamiliar ceiling. My body swayed gently in time with the sound of hooves coming from somewhere.

“Ah.”

I let out a short groan and blinked. I steadied myself with a deep breath, and air thick with damp heat filled my lungs.

*This is…*

I didn’t need to look around carefully to know.

I was lying in a carriage, and the hot, humid air unique to Nanman—something I hadn’t felt in a couple of months—was familiar.

Of course, given the time difference with the modern world, it had probably been a few shichen, not two months.

*That last System notification wasn’t a dream.*

The sudden rush of relief drained the tension right out of me.

In my final moments in the modern world, my mental strength had been so completely depleted that I hadn’t even been able to attempt Login.

If the System hadn’t helped, even by force, I would’ve stayed collapsed for days without knowing what was happening… No, wait.

*System update?*

Those words had stuck out sharply amid my jumbled memories.

If all the System notifications I’d heard were true, then something had changed—something that had never happened before.

I hurriedly sat up and murmured to myself.

*Open Status Window.*

But, just as I’d half expected, nothing happened.

No matter how hard I stared into the air, no translucent holographic window appeared. I didn’t hear the clear chime that should’ve sounded along with the command, either.

“……Shit.”

The curse slipped out before I could stop it. I was taken aback, but I had a pretty good idea why the System had suddenly gone dead.

System update.

*Maybe I can’t use it until the update is complete? Something like that?*

I’d loved physical activity ever since I was a kid, so I’d lived far removed from computers. But any modern person with a smartphone had experienced an update.

Still, I was this flustered because I’d never expected anything like this.

*Come to think of it, this is a program too, so I guess it could update.*

I couldn’t help wondering what kind of lunatic made something like this and then updated it, but it had happened.

No, maybe it was only natural.

A System this insane existed—one that connected two worlds and let me level up like a game. An update was nothing by comparison.

And besides…

*After everything that happened.*

I remembered the unbelievable information the System had given me right after I erased the Doppelganger.

And in that moment, I realized once again that the enormous, horrible calamity I’d failed to stop had begun.

*Clench.*

My hand tightened without me realizing it. My fist had gone white and trembled. At the same time, the scene from the nightmare flashed before my eyes.

Honestly, I still didn’t know.

Was what I’d seen reality, secretly delivered to me by the System through a dream? Or was it a nightmare conjured by my confused subconscious?

Or was it something you might call a prophetic dream?

But despite my wanting it to have been nothing but a nightmare, I already had an instinctive suspicion.

*That wasn’t… just a nightmare.*

I’d seen it clearly, even through the static in my vision. I remembered it vividly.

The crack in space that had opened, if only for a moment, through the countless Magic Gems and magic circles—and the man wrapped in power so monstrously vast that he slaughtered tens of thousands of fanatics who couldn’t offer the slightest resistance.

No—the demon who, for some reason, looked human.

*No way.*

I forced myself to push the name that surfaced in my mind away.

I still didn’t know who he was.

But judging by the Doppelganger’s attitude when we talked and how things had played out, that man wasn’t Asmodeus.

Even if—if he really was a Demon King…

*I have plenty of time.*

Just as I’d shut myself away to train on Mount Jiuhua, I could spend a little over a year in Murim while only a few days passed in the modern world.

As long as the System existed, time was on my side.

*Dark Heaven might not be, though.*

I muttered to myself and got to my feet, looking around inside the carriage.

Had sleeping in a carriage become popular at the Nanman Beast Palace lately? The place was so spacious, even by my exaggeration, it was about the size of a large inn’s private wing—and I was alone.

*Well, it’s quiet, at least. But where is everyone?*

The familiar faces who should’ve been by my side were nowhere to be seen.

The people from the Fire Dragon Pavilion. Hyuk Mujin, who should’ve been sitting beside me as my guard and nodding off. And Jeok Cheongang, whose jaw had dropped when I told him about the modern world and he mistook it for the realm of immortals.

*Where the hell… Hm?*

Just then, as I wandered around the carriage to stretch my legs, a familiar voice reached my ears.

“The Central Plains have already been scrapped by the Earth Mother Goddess. Now, who does the Central Plains martial world revolve around? Our Captain. The Blazing Flame Divine Dragon of the great Jin Family of Taiyuan—that’s who.”

“Ooh. Ooooooh.”

What the hell was he talking about?

I listened to the voice ringing out louder than the surrounding hubbub.

“And who is it that believes in and follows that Blazing Flame Divine Dragon? It’s me. Want to know why? Because I’ve got my place at the Captain’s side locked down! I’m his most trusted subordinate—that’s why my place is secure.”

“A firm grip? How so?”

“Captain, don’t move! Blazing Flame Divine Dragon, mess with me and you’re dead! That’s how close I am to our Captain. We’re very close.”

“Ohhh.”

“Who is the Earth Mother Goddess’s son? The Blazing Flame Divine Dragon! And who’s the one holding on tight to that Blazing Flame Divine Dragon?!”

As the speech reached its climax, I stuck my head out through the window.

“Listening to all that has me curious. Who is it?”

Hyuk Mujin laughed heartily and turned his head.

Then his eyes met mine, and he went completely stiff.

“Me! Hyuk Mu—uh, fuck.”

“Fuck?”

“Ah.”

“Ah?”

“Come here, you bastard.”
```
