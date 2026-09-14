<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0082.txt",
      "sha256": "caac02c9e8aa82c010ef5c4104f1d98f241d66c179d916adea9c98c2326c3fec",
      "bytes": 12533
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "11279a02822028b6a1d78f4ff9612729c1a77ed9509994db1bfb9c96f8026fed",
      "bytes": 6788
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2934a46fb499e69c16a12af52da4ca71fbd891f057b7cb91f066c92ec6127f41",
      "bytes": 6604
    },
    {
      "path": "characters/Hye-rin.md",
      "sha256": "08b8f51a1b3042378d87aca6794eb2e4af6675d8a0f011fe53888f382ef6cb07",
      "bytes": 430
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "eb461593f89d2cf7c6ebeec8e4e3feab44583c79e34811646ac20ed5f0ce0031",
      "bytes": 1608
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "523cd6c554adaac218c3541653b646968e11fb9f05412b77b754d63f97effbe3",
      "bytes": 23807
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3a9548f5a1a75cadce1cd38b939bf682bf24cffd650c649fe32c017866c6a52a",
      "bytes": 5494
    }
  ],
  "estimated_tokens": 12822
}
-->

# Durable State Update — Chapter 82

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 82. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 82. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 82,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 82,
    "continuity_sources": [82],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Taekyung successfully logged out after roughly twenty days in Murim; his watch showed 2:05:35 in the modern world, and ten modern-world days now correspond to one hour in Murim.",
    "Taekyung currently has fifteen years of internal energy, and circulating his qi slightly increases it; Sleep Mode normally keeps his sleep below three hours except when seriously injured.",
    "Team Leader Choi owns the café where Taekyung signed a contract providing a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.",
    "After ten days of Mukyung's training, Taekyung mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique, and the Training? Trial! Quest succeeded with a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured after the attack, and the unidentified assassin may be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training; Wikyung plans to summon every Shanxi sect on New Year's Day and may seek to become Alliance Leader.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months, and five-year-old Soyul does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout; Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect; Taekyung received the forced Yesterday's Enemy, Today's Ally Quest to deliver an invitation for New Year's Day.",
    "Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song. Butler Kim is Guild Master, Choi leads Team 1, and the other three are team members.",
    "The Peace Guild's Guild house is Sooni's Super in Bucheon's Gate-dense district, on property purchased from the former owner's surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong is married with two children and joined Peace Guild after Choi recruited him while hospitalized.",
    "Team Leader Choi formerly served in Ares Guild with Song Song; Butler Kim is a retired mage and former Hunter who trained at Nonsan's 28th Regiment, 1st Battalion, as did Taekyung. Choi is Level 75, Kim Level 80, Song Song Level 64, and Im Hyeokjun Level 24.",
    "A Bucheon Terminal Guild raid against seven B-rank Minotaurs ended with the monsters defeated but two C-rank Hunters dead, making Taekyung judge the Peace Guild's first raid dangerous.",
    "The Peace Guild joined Sangdong Guild's party for its first official raid into The Minotaur's Labyrinth; Sangdong's team leader is Im Changsoo.",
    "Choi loaned Taekyung a Peak-grade Masterwork Black Drake Leather Set and a Peak-grade Masterwork Black Thorn Spear with a 90% chance to inflict Bleeding on hit.",
    "Sangdong Guild and Peace Guild entered The Minotaur's Labyrinth as a fifteen-person team with seven B-rank Hunters; Im Kkeokjeong was registered as an E-rank tank, and Taekyung received the restricted B-rank Gate Clear Quest.",
    "Im Changsoo is the Sangdong Guild Master's son, behaves abusively toward his team, maintains a sponsorship relationship with the C-rank mage Hye-rin, and intends to pursue Song Song."
  ],
  "continuity_sources": [
    81
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed, as does any connection between the attack and Song Sword Sect.",
    "It remains unresolved whether Hyuk Mujin will become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim's former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung's interrupted confession.",
    "The reason Im Changsoo seems familiar to Taekyung, whether he can act on his interest in Song Song, and what will happen in The Minotaur's Labyrinth remain unresolved."
  ],
  "safe_through": 81,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Render fist-and-kicking technique as 권각술, recognition as 인정, Falling Flow Sword as 낙류검, Twelve Gale Fists as 질풍십이권, Flame Divine Palm as 화염신장, and Tendon-Splitting and Bone-Twisting as 분근착골.",
    "Use Reformation Fist, Toughness, Heavenly Martial Physique, Jang Childeuk, Martial Artist Jang, benevolence/righteousness/propriety/wisdom, killed by a tiger, fifteen minutes, lifelong single, Let's eat noodles, Squad Leader, Third Young Master, Designer-Brand Junkie, Qi Sense, Peace Guild, Essence of the Himalayas, Sooni's Super, Song Song, Miss Song, Taurus, Ares Guild, Senior, Young Master, Guild Master, Minotaur, Bucheon Terminal Guild, and The Minotaur's Labyrinth as established.",
    "Use Sangdong Guild, Hunter Association, Black Drake, Masterwork Black Drake Leather Set, Masterwork Black Thorn Spear, Bleeding, artifact, gear advantage, Hye-rin, and Cheongdam-dong as established terminology."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 임창수    | **Im Changsoo**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 로그인              | **Login**                      |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 귀가      | **your family**                                                 |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 임꺽정 | **Im Kkeokjeong** |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |

## Listed compact profiles

### Hye-rin.md

# Hye-rin (혜린)

- **Safe through:** Chapter 81
- **Aliases:** None
- **Role:** C-rank mage and member of Sangdong Guild's raid team
- **Personality:** Not established in this chapter beyond seeking Im Changsoo's approval
- **Voice:** Not established in this chapter
- **Relationships:** Im Changsoo's lover and sponsored partner; participates in his raid team

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 81
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 81
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃82화



총원 열다섯. 그중 절반에 가까운 숫자가 B급 헌터다 보니 게이트 등급을 감안해도 호화스러운 레이드 팀이 꾸려졌다.

“원래 B급 헌터가 이렇게 흔했나?”

나도 임꺽정의 말에 동의했다.

“그러게요.”

전에는 찾으려고 해도 옷깃이나 보일까 말까 했던 사람들이다. 나나 임꺽정과는 애초에 노는 물부터가 달랐으니까.

“근데 태경이 넌 별 감흥이 없나 보다?”

“저요?”

“응. 아까 보니까 저쪽 팀장이랑도 얘기 잘하던데.”

“그럴 수도 있죠. 그냥 잡담 좀 한 건데.”

“그럴 수 있긴. 얼마 전만 해도 말 한번 붙여 보려면 고개 들다가 목 부러졌을 텐데.”

그 정도였나? 문득 생각해 보니 임꺽정의 말이 틀리지 않았다. 단지 내가 달라졌을 뿐이다.

‘서 있는 곳이 변하면 풍경도 변한다더니.’

B급 헌터. 손을 뻗어도 닿지 않았던 산등성이들이 눈앞에 있다. 하지만 내가 생각한 풍경만큼 아름답지는 않았다.

‘저 정도면 초일류? 아니, 일류 무인쯤 되려나.’

기감으로 확인한 레벨도, 저들에게서 느껴지는 마나의 크기도 딱 그 정도다. 시스템의 사기성으로 무장한 나는 말할 것도 없고 동 레벨의 무인과 비교해서도 한 수 아래일 것이다.

‘그게 무인과 헌터의 차이지.’

각각 장단점이 있지만 맨몸으로 맞붙는다면 헌터의 필패다.

무인들은 신체 내부의 기운을 효율적으로 사용할 수 있는 내공심법을 익혔고 그걸 무공을 통해 극대화시켰다.

‘헌터가 장비를 맞추고 마법까지 사용해야 해볼 만하겠지.’

결론은 간단하다. 개인 역량은 무인이, 집단으로서의 전투와 전술로는 헌터가 앞선다는 것.

그리고…….

‘나 완전 사기 캐릭터네.’

나는 헌터이면서 무인, 무인이면서 헌터다. 같으면서 다른 두 가지 직업의 장점을 모두 갖고 있다.

더 무서운 건 지금도 시스템을 통해 빠른 속도로 성장 중이라는 사실이다.

‘이거 살짝 소설 속 주인공이 된 기분인데.’

나중에 나이 먹고 은퇴하면 자서전이나 써 볼까.

로그인 무림. 뭐 그런 제목으로.

다른 사람이 보면 판타지 소설이 따로 없을 거다.

“자, 집합! 지금부터 호명하는 포메이션으로 이동해 주세요.”

들려오는 외침에 임꺽정이 심호흡했다.

“이제 시작이구나.”

임꺽정의 포지션은 탱커. 선두에서 팀을 지켜야 한다.

B급 게이트가 주는 압박감일까, 언제나 웃음 짓던 얼굴이 딱딱하게 굳어 있었다.

“내가 할 수 있을까?”

나는 그의 어깨를 툭툭 두드려 주었다.

“할 수 있어요.”

빈말이 아니다. 지금 내 눈앞에 떠 있는 시스템창이 그 증거다.



아이템창



[투우사의 전신 갑옷]

종류 : 갑옷

등급 : 절정

설명 : 투우사의, 투우사에 의한, 투우사를 위한 갑옷.

효과 : 근력, 체력, 맷집 +10

소(牛)형 몬스터 상대 시 능력치 모든 스탯 +20





아이템창



[투우사의 방패]

종류 : 방패

등급 : 절정

설명 : 투우사의, 투우사에 의한, 투우사를 위한 방패. 소의 피로 붉게 물든 방패는 보기만 해도 섬뜩해진다.

효과 : 근력, 체력, 맷집 +10

소(牛)형 몬스터 상대 시 일정 확률로 [도발] 발동

소(牛)형 몬스터 상대 시 일정 확률로 [환각] 발동





‘솔직히 처음에는 무리라고 생각했는데.’

이 정도면 안심이다. 적어도 이곳, 미노타우로스의 미로에서만큼은 훌륭한 탱커로 활약할 수 있을 것이다.

“임 헌터님.”

조용히 다가온 물주, 아니 최 팀장도 진지한 표정으로 입을 열었다.

“조심히 입으세요. 제가 아끼는 컬렉션입니다.”

“…….”

“…….”

거 되게 좋은 말 해 주네.



* * *



탱커인 임꺽정이 선두. 마법사인 김 집사와 힐러인 송이 씨가 후방으로 빠지자 내 곁에는 최 팀장밖에 남지 않았다.

“……왜 그렇게 보십니까?”

왜긴. 송이 씨랑 포지션을 좀 바꿨으면 해서 보는 거지.

오순도순 옆에서 걸으면서 게이트 산책하면 얼마나 좋아. 몬스터 나오면 서로 구해 주기도 하고.

‘하늘이 돕지 않는구나.’

한탄하며 고개를 들어 봐도 축축한 동굴 천장밖에 보이지 않는다. 물론 F급 게이트와는 차원이 다른 높이였다.

“확실히 엄청 크네요.”

“B급 게이트니까요.”

등급이 높은 게이트일수록 내부 공간이 넓고 출현하는 몬스터가 강력하다. 물론 나야 D급 게이트가 고작이라 더 높은 등급은 처음이지만 사람들이 그렇다더라.

“어떤 경우에는 설산도 타야 합니다. 2년 전에 한 번 가 봤는데 끔찍했죠.”

“아, 혹시 무슨 사고라도……?”

“아뇨. 신고 간 부츠가 방수 마법이 안 걸려 있었어요.”

“…….”

“제가 수족냉증이 있어서.”

“…….”

“아, 둘 다 농담입니다.”

당연히 농담이겠지. 60레벨이 넘는 인간이 수족냉증이라는 게 말이 되나. 내가 어이없는 표정으로 최 팀장을 바라보던 그때였다.

……드득.

“어?”

“왜 그러십니까?”

“잠시, 잠시만요.”

단순한 착각? 아니다.

동굴 바닥을 통해 감지되는 미세한 진동. 아주 짧은 순간이었지만 분명히 느꼈다.

드드득.

두 번째 진동은 보다 분명하고, 노골적이었다.

몇몇은 이미 그 사실을 알아차리고 전방을 주시하기 시작했다. 임창수도 그중 하나였다.

“전투 준비!”

짤막한 외침은 신속하고 침착했다. 팀원 중 절반이 B급 헌터인 데다 훌륭한 장비까지 갖췄으니 그로서는 당황할 이유가 없었을 것이다. 한 가지 문제는…….

“구멍 주시해!”

여기가 미로라는 거다. 당장 뻥 뚫려 있는 구멍만 다섯 개.

단순히 땅의 진동만으로는 놈들이 오는 정확한 방향을 찾기 힘들다.

“어디냐!”

“…….”

임창수 쟤는 누구한테 물어보는 걸까. 저런다고 미노타우로스가 대답해 줄 것 같진 않은데.

- 음모오오!

“저기다! 맨 왼쪽 구멍!”

“……실화냐.”

보면서도 믿기지 않는 광경이다.

나는 혀를 차며 창을 움켜쥐었다. [장인의 검은 가시 창]. 높은 확률로 적을 출혈 상태에 빠트릴 수 있는 흉악한 놈이다.

“그립감이 참 좋죠? 마감제를 꼼꼼히 발라서…….”

여기 흉악한 놈이 하나 더 있네. 만약 최 팀장이 죽는다면 발설지옥에 떨어지리란 걸 믿어 의심치 않는다.

다음 순간.

쿵쿵쿵.

- 음모오오오오!

놈들이 어둠 속에서 불쑥 솟구쳤다. 인간을 닮은 몸, 그러나 인간이라고 볼 수 없는 체격과 잔뜩 부풀어 오른 근육들.

먼지와 누군가의 피로 얼룩진 두 개의 뿔 위에 직사각형의 레벨창이 두둥실 떠다녔다.



[Lv.58 미노타우로스 전사]



- 모오오오!

영상으로 봤던 것보다 훨씬 박진감 넘치는 외관이긴 한데…….

“에게.”

“한 마리밖에 안 돼?”

말 그대로 달랑 한 마리뿐이다. 알고 보면 저 미노타우로스도 미로에서 길을 잃은 게 아닐까.

“저 정도면 원거리 지원 없이 처리해도 되겠는데요?”

“혜린아, 오빠 잠깐 다녀올게.”

상동 길드원들이 자신 있게 앞으로 나섰다. 탱커 둘에 딜러 둘. 모두 B급 헌터들이다. 여자들 앞에서 가오 좀 세워 보겠다는 의도가 뻔히 보였다.

‘어이고, 병신들.’

저런 놈들이 꼭 까불다가 골로 가더라. 물론 미노타우로스 한 마리에 그럴 일은 없겠지만.

“할 거면 빨리 처리해.”

임창수의 허락을 받은 네 사람이 무기를 빼 들고 몬스터를 향해 다가가던 그때였다.

쿵. 쿵.

“응?”

- 음모오.

다섯 개의 구멍 중 두 번째 구멍에서 미노타우로스 한 마리가 쏙 빠져나왔다.

“오, 두 마리 됐다.”

“쟤는 덩치가 좀 더 작네. 약할 것 같으니까 네가 맡아.”

“뭐래, 제일 약골인 새끼가.”

쿵. 쿵.

- 음모오.

세 번째 구멍.

“오, 세 마리. 이 정도면 나름 재밌게 싸울 것 같은데?”

“상처 하나라도 입는 놈이 오늘 술 사기. 어때?”

“콜.”

“콜. 이런 건 꼭 하자고 한 놈이 걸리더라.”

쿵. 쿵.

- 음모오.

“아니, 시바. 뭐야, 이거.”

“네 마리는 좀.”

“그냥 우리끼리 포메이션 짜서 한 놈씩 처리하는 게 좋을 것 같은데.”

“나도.”

상황을 지켜보던 최 팀장이 목을 긁적였다.

“좀 더 기다렸다가 작전을 짜는 게 나을 것 같은데.”

“네?”

“구멍이요. 왠지 더 나올 것 같지 않습니까?”

“설마요. 무슨 올림픽 선수 소개도 아니고.”

쿵쿵쿵쿵!

진짜 왔네.

5번 레인, 아니 다섯 번째 구멍에서도 소식이 왔다.

한 가지 예상치 못한 부분이 있다면 이번에는 혼자가 아니라는 사실이다.

- 음모오오오!

친구도 많은 놈인지 자그마치 네 마리나 우르르 몰려왔다. 앞서 나온 놈들까지 모두 합하면 총 여덟 마리. B급 헌터 넷으로는 어림없는 숫자다. 최 팀장이 입을 열었다.

“어떻게 생각하십니까?”

“아마 힘들지 않을까요.”

힘들긴 무슨, 뒈지기 싫으면 탱커 뒤에 있어야지.

그나마 듣는 귀가 있어서 순화시킨 거다.

“태경 씨라면 어떻겠습니까?”

“저 말입니까?”

“네. 태경 씨요.”

“음.”

B급 몬스터인 미노타우로스의 레벨은 50대 중후반.

무인이라면 초일류에 가까운 레벨이지만 놈들과 싸운다면 여러 가지 변수를 고려해야 한다.

간단하게 말해 붙어 봐야 안다는 거지.

“잘 모르겠네요.”

“잘 모르겠다…… 그거 아세요?”

최 팀장이 묘한 눈빛으로 나를 응시했다.

“보통 C급 헌터는 그렇게 대답 안 합니다. 방금 같은 질문에 고민하지도 않고, 진지하게 받아들이지도 않아요.”

나도 모르게 가슴 한구석이 뜨끔 했다. 힘을 숨길 이유는 없지만 그렇다고 동네방네 자랑할 마음도 없었다.

그저 아직은 주목을 피해 나만의 비밀로 남겨 두고 싶을 뿐이었다. 남들보다 약간 더 뛰어난 헌터. 딱 그 정도로.

“전부터 알고 있었지만 참 흥미로운 사람입니다, 진태경 씨는.”

“아니 저기, 팀장님. 뭔가 오해가 있으신 것 같은데.”

내가 막 입을 연 그 순간이었다.

“하하, 그러게요. 듣다 보니 나까지 흥미롭네.”

불쑥 끼어든 임창수의 시선이 나와 최 팀장을 훑었다.

“워낙 재미있는 얘기들을 하고 계셔서 좀 들었습니다. 괜찮으시죠?”

너희가 안 괜찮으면 어쩔 건데, 라고 들리는 건 착각일까?

“쥐뿔도 없는 C급 주제에 미노타우로스를 어쩌고저쩌고. 아주 소설을 쓰시던데.”

아, 착각이 아니구나.

나는 새삼스러운 눈으로 임창수를 바라봤다.

‘어울리네.’

사람마다 맞는 옷이 있다. 웃음도, 태도도.

지금 내 눈에 비친 임창수가 그랬다. 한껏 올라간 입꼬리에 맺힌 비웃음이 아주 그냥, 찰떡이다.

“기분을 상하게 할 의도는 없었습니다.”

최 팀장 특유의 무덤덤한 표정과 말투에 임창수가 피식 웃었다.

“상하고 말고 할 게 있나 사실인데, 뭘. 쟤들 실력 존나 구려요. 사람들이 B급, B급 해 주니까 있어 보이지, B급 중에서 보면 완전히 폐급이야. 그런데…….”

임창수가 나를 턱짓했다.

“C급보다는 낫지. 안 그래, 장태경 씨?”

나는 아까부터 참고 있던 말을 꺼냈다.

“진태경인데요.”

“진태경이든 장태경이든. 당신 성이 뭐든 내 알 바 아니지.”

“그럼 씹창수라고 불러 드려요?”

“뭐?”

“임창수든 씹창수든. 그쪽 성이 뭐든 내 알 바 아니잖아요.”

임창수의 얼굴에서 웃음이 사라졌다.
```

## Final English reading copy

```markdown
# Chapter 82

Fifteen people in total. With nearly half of them being B-rank Hunters, it had turned into a lavish raid team—even taking the Gate’s Grade into account.

“Were B-rank Hunters always this common?”

I agreed with Im Kkeokjeong.

“Exactly.”

Before, even when I went looking for them, I had been lucky to catch a glimpse of their coat tails. They had always lived in a completely different world from people like Im Kkeokjeong and me.

“But you don’t seem all that impressed, Taekyung.”

“Me?”

“Yeah. I saw you talking pretty comfortably with that other team leader earlier.”

“I suppose I can do that. We were just making small talk.”

“You suppose? Not long ago, you would’ve broken your neck just trying to raise your head high enough to talk to one of them.”

*Was it really that bad?*

Come to think of it, he wasn’t wrong. I was simply the one who had changed.

*They say the scenery changes when you change where you stand.*

B-rank Hunters. Mountain ridges that I couldn’t reach even by stretching out my hand were now right in front of me.

But the scenery wasn’t as beautiful as I had imagined.

*They’re around Top-tier? No, maybe First Rate martial artists.*

Their Levels, which I had checked with Qi Sense, and the amount of mana I felt from them were both right around that level. Needless to say, I was a cut above them, armed with the System’s cheat-like advantages. Even compared to martial artists of the same Level, they would probably be a step below.

*That’s the difference between martial artists and Hunters.*

Both sides had their strengths and weaknesses, but if they fought with nothing but their bodies, the Hunter would lose every time.

Martial artists learned cultivation techniques that allowed them to use the qi inside their bodies efficiently, then maximized it through martial arts.

*A Hunter would have a chance only after equipping proper gear and using magic, too.*

The conclusion was simple. Martial artists had the advantage in individual ability, while Hunters were superior in group combat and tactics.

And…

*I’m a total cheat character.*

I was a Hunter and a martial artist, a martial artist and a Hunter. I possessed all the advantages of two different classes that were alike and yet completely different.

The frightening part was that I was still growing at an incredible speed through the System.

*This feels a little like becoming the protagonist of a novel.*

Maybe I should write an autobiography after I got old and retired.

*Login Murim.*

Something like that for the title.

To anyone else, it would sound like a fantasy novel.

“Everyone, assemble! Move according to the formation I call out from now on!”

At the shout, Im Kkeokjeong took a deep breath.

“So it’s starting.”

Im Kkeokjeong’s position was tank. He had to protect the team from the front line.

Maybe it was the pressure of a B-rank Gate. His face, which was always smiling, had hardened.

“Can I do this?”

I patted him on the shoulder.

“You can.”

I wasn’t saying it just to make him feel better. The System window floating before my eyes was proof.



> **System**
>
> **Item Window**
>
> **Matador’s Full-Body Armor**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** Armor of the matador, by the matador, for the matador.  
> **Effect:** Strength, Stamina, Toughness +10  
> Against bovine-type monsters, All Stats +20.



> **System**
>
> **Item Window**
>
> **Matador’s Shield**
>
> **Type:** Shield  
> **Grade:** Peak  
> **Description:** A shield of the matador, by the matador, for the matador. Dyed red with bull’s blood, it is eerie just to look at.  
> **Effect:** Strength, Stamina, Toughness +10  
> Against bovine-type monsters, has a chance to activate **Taunt**.  
> Against bovine-type monsters, has a chance to activate **Hallucination**.

*Honestly, I thought it would be impossible at first.*

But this was enough to put my mind at ease. At least here, in The Minotaur’s Labyrinth, Im Kkeokjeong would be able to perform admirably as a tank.

“Hunter Im.”

The sponsor—or rather, Team Leader Choi—approached quietly and spoke with a serious expression.

“Put it on carefully. It’s part of my prized collection.”

“……”

“……”

*He sure knows how to say something nice.*

* * *

Im Kkeokjeong took the lead as the tank. Once Butler Kim, the mage, and Miss Song, the healer, moved to the rear, only Team Leader Choi remained beside me.

“……Why are you looking at me like that?”

Why else? I wanted him to switch positions with Miss Song.

Wouldn’t it be nice to walk side by side, enjoying a pleasant stroll through the Gate? We could even save each other if monsters showed up.

*The heavens clearly aren’t helping me.*

Even when I tilted my head up in lament, all I could see was the damp ceiling of the cavern. Of course, the ceiling was incomparably higher than in an F-rank Gate.

“It’s definitely huge.”

“It’s a B-rank Gate.”

The higher the Grade of a Gate, the larger its internal space and the stronger the monsters that appeared inside. D-rank was as high as I’d ever gone myself, so this was my first time seeing anything higher. That was what people said, anyway.

“In some cases, you even have to climb a snow-covered mountain. I went once two years ago. It was horrible.”

“Oh, did some kind of accident happen?”

“No. The boots I wore weren’t enchanted with waterproofing.”

“……”

“I have cold hands and feet.”

“……”

“Ah, both of those were jokes.”

Of course they were jokes. How could someone above Level 60 have cold hands and feet? I was staring at Team Leader Choi with an incredulous expression when—

*Drrrk.*

“Hm?”

“Is something wrong?”

“Wait. Just a moment.”

Was I imagining things? No.

There had been a faint vibration beneath the cavern floor. It had lasted only a brief moment, but I had definitely felt it.

*Drrrk.*

The second vibration was clearer and more obvious.

Several people had already noticed it and begun watching the area ahead. Im Changsoo was one of them.

“Prepare for battle!”

His short shout was quick and composed. With half his team being B-rank Hunters and all of them equipped with excellent gear, he had no reason to panic.

There was just one problem.

“Watch the holes!”

This was a labyrinth. There were five wide-open holes right in front of us.

It was difficult to determine exactly where the monsters were coming from based on the vibrations in the ground alone.

“Where are they?”

“……”

*Who is Im Changsoo asking? It’s not like the Minotaurs are going to answer him.*

“—Moooooo!”

“There! The hole on the far left!”

“……Is this for real?”

It was a sight I could hardly believe even while watching it.

I clicked my tongue and gripped my spear. The Masterwork Black Thorn Spear—a vicious weapon with a high chance of inflicting Bleeding on its enemies.

“Doesn’t the grip feel great? I applied the finishing coat very carefully—”

*There’s another vicious thing here.*

If Team Leader Choi died, I had no doubt he would fall straight into the tongue-pulling hell.[^1]

The next moment—

*Boom. Boom. Boom.*

“—Mooooooo!”

They burst out of the darkness.

Their bodies resembled humans, but their physiques were too massive to be human, and their muscles were grotesquely swollen.

Rectangular Level windows floated above two horns stained with dust and someone’s blood.



> **System**
>
> **Level 58 Minotaur Warrior**

“—Moooooo!”

They looked far more vivid and imposing in person than they had in the video, but…

“That’s all?”

“There’s only one?”

There really was just one.

*Could that Minotaur have gotten lost in the labyrinth, too?*

“At that level, we should be able to deal with it without ranged support, shouldn’t we?”

“Hye-rin, I’ll be right back.”

The Sangdong Guild members confidently stepped forward. Two tanks and two damage dealers. All of them were B-rank Hunters.

Their intention to show off in front of the women was painfully obvious.

*Oh, you morons.*

Guys like that always fooled around and ended up dead. Of course, that probably wouldn’t happen because of a single Minotaur.

“If you’re going to do it, finish it quickly.”

With Im Changsoo’s permission, the four men drew their weapons and started toward the monster.

That was when—

*Boom. Boom.*

“Hm?”

“—Moo.”

A Minotaur popped out of the second of the five holes.

“Oh, now there are two.”

“That one’s a little smaller. It looks weaker, so you take it.”

“What the hell are you saying? Says the weakest bastard here.”

*Boom. Boom.*

“—Moo.”

The third hole.

“Oh, three. At this rate, this might actually be a pretty fun fight.”

“Anyone who takes even one wound buys drinks tonight. How about it?”

“I’m in.”

“I’m in. The guy who suggests these things always ends up paying.”

*Boom. Boom.*

“—Moo.”

“Ah, shit. What is this?”

“Four might be a bit much.”

“We should probably form up and take them out one at a time.”

“Me too.”

Team Leader Choi, who had been watching the situation, scratched his neck.

“Maybe we should wait a little longer and come up with a strategy.”

“Huh?”

“The holes. Don’t you get the feeling more might come out?”

“No way. It’s not like they’re introducing Olympic athletes.”

*Boom-boom-boom-boom!*

*He was right.*

Lane five—no, the fifth hole—had news for us, too.

The only unexpected part was that this time, it wasn’t alone.

“—Moooooo!”

Maybe it had a lot of friends. Four Minotaurs came stampeding out together.

Including the ones that had appeared earlier, there were eight in total.

Four B-rank Hunters had no chance against that number. Team Leader Choi spoke.

“What do you think?”

“It might be difficult.”

*Difficult, my ass. If you don’t want to die, stay behind the tank.*

I had toned it down for the benefit of the ears around us.

“What about you, Mr. Taekyung?”

“Me?”

“Yes. You, Mr. Taekyung.”

“Hmm.”

The Minotaur, a B-rank monster, was in the mid-to-late fifties in Level.

For a martial artist, that would be close to Top-tier. But if I fought them, I would have to account for all sorts of variables.

Simply put, I would have to fight them to know.

“I’m not sure.”

“You’re not sure…… Do you know something?”

Team Leader Choi stared at me with a strange look in his eyes.

“Most C-rank Hunters don’t answer like that. They wouldn’t take time to think about a question like that, much less take it seriously.”

I felt a sudden twinge of unease.

I had no reason to hide my strength, but I also had no desire to brag about it to the whole neighborhood.

For now, I wanted to avoid attention and keep it as my own secret. A Hunter who was just a little more capable than everyone else. That was all.

“I’ve known this for a while, but you really are an interesting person, Jin Taekyung.”

“No, wait, Team Leader. I think there may be some misunderstanding here.”

I had just begun to speak when—

“Haha, I see. Listening to you, even I’m getting interested.”

Im Changsoo suddenly cut in, his gaze sweeping over Team Leader Choi and me.

“You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?”

*If we minded, what exactly would you do about it?*

“For a C-rank with fuck-all to his name, you sure had a lot to say about Minotaurs and whatnot. You were practically writing a novel.”

*Ah. So I wasn’t imagining it.*

I looked at Im Changsoo with fresh eyes.

*It suits him.*

Everyone had clothes that suited them. The same went for smiles and attitudes.

That was Im Changsoo in front of me. The mockery gathered in the corners of his raised mouth suited him perfectly. It was practically made for him.

“I didn’t mean to offend you.”

At Team Leader Choi’s characteristically impassive expression and tone, Im Changsoo let out a short laugh.

“Why would I be offended? It’s the truth. These guys are fucking lousy. They only look impressive because people keep calling them B-rank, but among B-ranks, they’re complete bottom-of-the-barrel trash. But……”

Im Changsoo jerked his chin toward me.

“They’re still better than a C-rank. Isn’t that right, Mr. Jang Taekyung?”

I finally said what I had been holding back since earlier.

“It’s Jin Taekyung.”

“Whether you’re Jin Taekyung or Jang Taekyung, I don’t care what your surname is.”

“Then should I call you Shit Changsoo?”

“What?”

“Im Changsoo or Shit Changsoo. I don’t care what your surname is, either.”

The smile disappeared from Im Changsoo’s face.

[^1]: The tongue-pulling hell is a Buddhist hell where liars and slanderers are punished by having their tongues pulled out.
```
