<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0081.txt",
      "sha256": "acf056178100f671134f8eafbe321763e889077d12f28e8f478fa90cde8ea227",
      "bytes": 14824
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1e9c00ad0176dd581d7405aeb76a868d0b6e1df0f70b04eb88a41346daa02e9e",
      "bytes": 7185
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a316819db409f5bdbb512145df0afe964fa5e8d9c544b343a8c1af4e62751a0f",
      "bytes": 6422
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "aaeee8686ef089a22a4703af3ddaccd6cd9f26995f9cbfaab5d59f03e5c962a4",
      "bytes": 1610
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ec7f4a49310f29b73eb520435484260bb2f4e1a6931c00f51fe890a18090d39a",
      "bytes": 23807
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "ddaf035da31d1b28aaa3bab8e5627379119e7cf752147c37236b2d1888f8290a",
      "bytes": 507
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8217834ff68c2d3022c7ee5c0460029217fe3749d298ec7864fbe6a3a050340e",
      "bytes": 5331
    }
  ],
  "estimated_tokens": 13800
}
-->

# Durable State Update — Chapter 81

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 81. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 81. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 81,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 81,
    "continuity_sources": [81],
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
    "Seong Jinho has lived with Taekyung as a friend and brother for years and plans to move out of the goshiwon, though the date is not fixed.",
    "Team Leader Choi owns the café where Taekyung signed a contract; the contract provides a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.",
    "After ten days of Mukyung's training, Taekyung mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique, and the Training? Trial! Quest succeeded with a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured after the attack, and the unidentified assassin may be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training; Wikyung plans to summon every Shanxi sect on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin, delivered Wikyung's summons to Song Sword Sect, and found no information on Dark Heaven in the family records.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months, and five-year-old Soyul does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout; Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect; Taekyung received the forced Yesterday's Enemy, Today's Ally Quest to deliver an invitation for New Year's Day, and he, Mukyung, and Hyuk Mujin departed for Eung-hyeon at her request.",
    "Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song. Butler Kim is Guild Master, Choi leads Team 1, and the other three are team members; Taekyung's Guild Membership achievement granted 10 points.",
    "The Peace Guild's Guild house is Sooni's Super in Bucheon's Gate-dense district, on property purchased from the former owner's surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong is married with two children, joined Peace Guild after Choi recruited him while hospitalized, and is now established as a D-rank Hunter.",
    "Essence of the Himalayas increases Taekyung's Intelligence by 1 for one hour.",
    "Team Leader Choi formerly served in Ares Guild with Song Song; Butler Kim is a retired mage and former Hunter who trained at Nonsan's 28th Regiment, 1st Battalion, as did Taekyung. Choi is Level 75, Kim Level 80, Song Song Level 64, and Im Hyeokjun Level 24.",
    "A Bucheon Terminal Guild raid against seven B-rank Minotaurs ended with the monsters defeated but two C-rank Hunters dead, making Taekyung judge the Peace Guild's first raid dangerous.",
    "During the safety-inspection period, Peace Guild joined Sangdong Guild's party for its first official raid into The Minotaur's Labyrinth; Sangdong's Level 65 team leader is Im Changsoo.",
    "Choi loaned Taekyung a Peak-grade Masterwork Black Drake Leather Set granting Strength, Stamina, Agility, and Toughness +10, and a Peak-grade Masterwork Black Thorn Spear with a 90% chance to inflict Bleeding on hit. Butler Kim uses artifact jewelry instead of a staff, and Taekyung is uneasy about Im Changsoo's apparent interest in Song Song."
  ],
  "continuity_sources": [
    80
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed, as does any connection between the attack and Song Sword Sect.",
    "It remains unresolved whether Hyuk Mujin will become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim's former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung's interrupted confession.",
    "The reason Im Changsoo seems familiar to Taekyung, whether he is interested in Song Song, and what will happen in the first Peace Guild raid remain unresolved."
  ],
  "safe_through": 80,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Render fist-and-kicking technique as 권각술, recognition as 인정, Falling Flow Sword as 낙류검, Twelve Gale Fists as 질풍십이권, Flame Divine Palm as 화염신장, and Tendon-Splitting and Bone-Twisting as 분근착골.",
    "Use Reformation Fist, Toughness, Heavenly Martial Physique, Jang Childeuk, Martial Artist Jang, benevolence/righteousness/propriety/wisdom, killed by a tiger, fifteen minutes, lifelong single, Let's eat noodles, Squad Leader, Third Young Master, Designer-Brand Junkie, Qi Sense, Peace Guild, Essence of the Himalayas, Sooni's Super, Song Song, Miss Song, Taurus, Ares Guild, Senior, Young Master, Guild Master, Minotaur, Bucheon Terminal Guild, and The Minotaur's Labyrinth as established.",
    "Use Sangdong Guild, Hunter Association, Black Drake, Masterwork Black Drake Leather Set, Masterwork Black Thorn Spear, Bleeding, artifact, and gear advantage for the new chapter terminology."
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

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 송송이    | **Song Song**     |
| 임창수    | **Im Changsoo**   |
| 일류     | **First Rate**    |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 귀가      | **your family**                                                 |
| 임꺽정 | **Im Kkeokjeong** |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 80
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter; veteran member of the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 78
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 79
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and occasionally teasing
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild

## Korean source

```text
＃81화



게이트 앞, 헌터 복장을 한 열 명의 남녀가 화기애애한 분위기 속에 대화를 나누고 있었다.

“오빠들, 우리 괜찮은 거 맞지?”

여자 헌터의 말에 상동 길드 소속의 B급 헌터가 흉갑을 두드렸다.

“걱정 말라니까. 우리 못 믿어?”

“아이, 믿지. 그런데 지난주에 여기서 사람 죽었다잖아.”

“그 병신들은 신경 쓰지 마. 실력도 안 되는 놈들이 깝치다가 뒈진 걸 누굴 탓해? 안 그래요, 창수 형?”

가만히 듣고 있던 임창수가 허공에 담배 연기를 내뿜으며 말했다.

“불안하면 집에 가라. 분위기 좆같이 만들지 말고.”

순간 싸해진 분위기. 앞서 말을 꺼냈던 여자 헌터가 억지로 입꼬리를 끌어 올렸다.

“아니 오빠, 나는 그냥.”

“닥치고. 어쩔래.”

“……미안.”

“그럼 구석에 찌그러져 있어. 너 아니어도 데려올 년들 차고 넘치니까.”

거친 언행에도 누구 하나 반발하는 법이 없다. 그저 어색한 웃음으로 분위기를 환기시키려 애쓸 뿐이다.

이런 광경이 임창수에게는 익숙하고도 당연했다.

‘병신들.’

게이트는 마정석이라는 황금 알을 낳는 거위고 헌터는 황금 알을 수확하는 일꾼이다. 마름 집안에서 태어난 그는 시작점부터 달랐다.

“지금 호텔 갈 거 아니면 작작 붙어 있어. 괜히 또 좆 같은 소문 퍼지면 귀찮아지니까.”

“형, 얘들은 믿어도 돼요.”

“안 믿어, 새꺄. 지난번 걔들도 믿을 만하다며?”

“그건, 뭐…….”

상동 길드가 인근에서 방귀깨나 뀌는 중견 길드라지만 대중의 시선을 무시할 정도는 아니다. 지금까지 몇 번 여자를 잘못 건드렸다가 길드장인 아버지에게 경고를 듣기도 했다.

“문제 생기지 않게 잘하자. 응?”

“넵. 명심하겠습니다. 충성!”

“쯧. 대답은 잘해요.”

임창수가 반쯤 타들어 간 담배를 튕겼다. 기다렸다는 듯 옆에서 주문이 들려왔다.

“윈드(Wind).”

마법으로 생성된 바람이 담배꽁초와 냄새를 저 멀리 날려 보낸다. 주문을 외운 여 마법사가 매력적인 웃음을 지어 보였다.

“나 잘했지?”

임창수는 여 마법사를 위아래로 훑었다. 매끈한 몸매에 뇌쇄적인 미녀인 그녀와는 일종의 스폰 관계였다.

뛰어난 미모와는 달리 형편없는 실력의 C급 헌터. 그러나 길드장 아들의 애인이라는 사실만으로 상동 길드에 들어왔다.

그밖에도 집, 차, 수많은 명품…… 모두 임창수의 주머니에서 나왔지만 아깝다는 생각은 안 해 봤다.

‘뭐, 지금까지는 그랬지.’

하지만 오늘 생각이 바뀌었다. 몸매, 외모, 분위기. 30분 전쯤 만났던 그 여자에 비하면 촌스럽고 싸 보인다.

‘송송이라고 했나?’

떠올리는 것만으로도 아랫배가 묵직해졌다.

허접한 신생 길드에 있기에는 너무 아까운 꽃. 잔뿌리 하나 상하지 않게 뽑아서 자신의 화분에 심을 생각이었다.

“오빠, 뭐 좋은 일 있어? 왜 그렇게 웃어?”

임창수는 대답하지 않았다. 대신 저 멀리서 모습을 드러낸 다섯 사람을 향해 손을 흔들었다.

“아, 여깁니다!”

물론 전(前) 애인을 향해 작은 목소리로 한마디 덧붙이는 것도 잊지 않았다.

“누가 네 오빠야, 썅년아.”



* * *



껄떡쇠, 아니 임창수가 환하게 웃으며 말했다.

“오셨군요. 아, 여기는 제 팀원들입니다.”

상동 길드 소속으로 보이는 이들이 고개를 꾸벅 숙였다.

임창수를 포함하면 딱 남자 다섯에 여자 다섯이다. 하나같이 번쩍거리는 고가의 장비를 착용했는데, 실용성보다는 디자인을 중시한 차림이었다.

특히…….

‘오우야.’

여성 헌터들 같은 경우에는 눈을 어디에 둬야 할지 모르겠다. 애 둘 딸린 유부남인 임꺽정은 굳은 얼굴로 속삭였다.

“끝내주는데.”

“…….”

나도 모르게 고개를 끄덕일 뻔했지만 간신히 참았다.

송이 씨가 좋지 않은 표정으로 우리를 바라보고 있었기 때문이다.

‘그나저나…….’

이게 레이드냐, 소개팅이냐. 잘생기고 예쁜 남녀가 짝을 맞춰서 하하 호호 웃으며 게이트에 들어갔다가는 골로 가기 십상이다.

뭐, 레벨이나 장비를 봐서는 괜찮을 것 같긴 하지만.

“다들 모이셨습니까?”

게이트를 담당하는 중년 공무원이 인원과 자격증을 체크했다. 진입 전 반드시 거쳐야 하는 절차 중 하나다.

“상동 길드, B급 다섯 분에 C급 다섯 분. 맞으시죠?”

임창수가 예의 바른 웃음을 지어 보였다.

“맞습니다.”

“그럼 평화 길드. B급 두 분에 C급 두 분, 그리고…….”

헌터 자격증을 휙휙 넘기던 공무원의 손이 멈칫했다.

“E급 한 분? 어디 계시죠?”

임꺽정이 털이 숭숭 난 팔을 번쩍 치켜들었다.

“어, 납니다.”

“혹시 포지션이?”

“담당자님께서 눈썰미가 없으시네. 이런 무식한 방패 들고 다니면서 마법 쓰겠소? 흐흐.”

“탱커시군요.”

공무원이 미간을 찡그렸다.

탱커는 말 그대로 최전방에서 몬스터들의 공격을 막아 내는 인간 방패다. 그 위험 때문에 힐러와 함께 헌터 중 가장 많은 수당을 지급받기도 하고, 사망률도 높다.

“E급이 여길 왜 와. 그것도 탱커? 나 참.”

“한 방에 많이 땡길 수 있잖아. 혹시 아냐? 마정석이라도 우르르 떨구면 로또 맞은 거지.”

“오빠, 오늘 정말 괜찮은 거 맞지?”

“걱정 마. 혜린이 너는 이 오빠가 지킨다.”

임창수의 팀원들 사이로 수군거림이 번졌다. 우리를 들여보내야 하는 공무원도 예외는 아니었다.

“E급 탱커라…….”

그의 우려 섞인 목소리에 김 집사가 나섰다.

“그는 20년 경력의 베테랑입니다. 위험을 대비해서 충분한 장비도 착용했으니 문제는 없다고 생각합니다만.”

“베테랑 좋죠, 좋긴 한데. 아시잖아요. 지난주에 사망 사고. C급 탱커 둘이 죽었어요. 이런 상황에 이게 참.”

뜻밖의 지원군이 나타난 건 그때였다.

“담당자님, 어떻게 안 되겠습니까?”

임창수다. 그는 조곤조곤 말을 이었다.

“이미 협동 레이드 계약서에 사인도 했고, 이렇게 좋은 분들을 만났는데 무효로 돌리는 건 좀 아쉬워서요.”

“저, 그러니까 이게.”

“살짝 유도리 있게 넘어가 주시면 참 감사할 것 같은데…… 부탁드립니다.”

신기한 놈일세. 입에서 나오는 말은 감사와 부탁인데, 목은 뻣뻣하고 행동은 고압적이다.

순간 움찔한 공무원이 이내 한숨을 내쉬었다.

“좋습니다. 대신 팀장님께서 잘 단속해 주셔야 합니다.”

“물론이죠.”

단속이라. 어감이 영 별로다.

임창수의 도움으로 허가는 내려졌지만 개미가 기어가는 것처럼 가슴 한구석이 근질거렸다.

‘뭐, 좋은 게 좋은 거겠지.’

당사자인 임꺽정도 덤덤한 표정인데, 내가 기분 나빠하는 것도 우습다.

“그럼 진입하셔도 좋습니다.”

공무원의 말에 사람들이 게이트 앞에 섰다. 상동 길드 열 명, 평화 길드 다섯 명. 총합 열다섯에 B급 헌터만 일곱에 달하는 정예 레이드 팀이다.

“그럼…….”

당연하다는 듯 선두에 선 임창수가 윙크했다.

“게이트에서 뵙죠.”

쏴아악-!

임창수가 마력장 너머로 사라지자 송이 씨가 중얼거렸다.

“재수 없어.”

저도 그렇게 생각합니다.



* * *



쏴악.

마력 특유의 음습하고 끈적끈적한 기운이 몸을 휘감은 것도 잠시. 눈을 뜨자 새로운 공간이 펼쳐져 있었다.

F급 게이트와는 비교도 되지 않는 거대한 크기의 동굴. 그리고 아가리를 쩍 벌린 입구 세 개. 오는 길에 영상으로 봤던 그곳이다.

‘다른 게 있다면…….’

띠링.



- [미노타우로스의 미로]에 입장하셨습니다.

- 퀘스트, [B급 게이트 클리어]가 생성되었습니다.



나한테만 들리는 시스템 알림이 있다는 거지. 거기에 더해 퀘스트도.

“자, 들어가기 전에 인원, 장비 점검 한 번씩 합시다.”

사람들이 각자 물건을 확인하는 사이, 슬그머니 동굴 구석으로 이동한 나는 마음속으로 뇌까렸다.

‘퀘스트 확인.’

띠링.



퀘스트



[B급 게이트 클리어]

당신은 난생처음 B급 게이트에 진입했습니다.

최초 1회에 한해 레이드 성공 시, 그에 상응하는 보상이 주어집니다.



등급 : 일류

제한 : 진태경

임무 : B급 게이트 클리어 (미완료)

보상 : ???

실패 : ???





산뜻한 시작이군. 내가 훈훈한 미소와 함께 퀘스트창을 닫은 그때였다.

“혼자서 뭐 해요?”

등 뒤에서 불쑥 들려온 목소리. 고개를 돌리자 이쪽으로 걸어오는 임창수의 모습이 보였다.

“저요?”

사람 잘못 봤나 했는데, 아니었다.

“평화 길드의 장태경 씨. 맞죠?”

“진태경인데요.”

“네, 장태경 씨.”

이 인간이 귀가 먹은 건지, 내 혀가 잘못된 건지는 모르겠지만 일단 고개를 끄덕여 줬다.

‘어차피 한번 보고 말 사이니까.’

앞서 임꺽정의 일로 나름 힘써 준 터라 약간의 고마움도 남아 있었다.

“저한테 무슨 용무라도?”

“하하, 용무라고 할 것까진 없고요. 이것도 인연인데 통성명이나 하자는 거죠. 제 소개는 아까 했으니 아실 테고. 잘 부탁드립니다.”

누가 그랬다. 웃는 얼굴에 침 못 뱉는다고. 조금 껄끄럽긴 했지만 얼굴 가득 미소를 머금고 악수를 청하는 임창수의 손을 맞잡았다.

“아, 예. 저도 잘 부탁드립니다.”

일면식도 없는 타 길드의 팀장이 먼저 악수를 청한다?

지난 7년간 협동 레이드도 몇 번 뛰어 보고 일용직 헌터 경험도 꽤 있지만 지금 같은 경우는 처음이다.

‘하긴, 그때는 F급이었으니까.’

그 시절에는 완전히 공기 취급이었는데, C급 헌터라고 사람대접해 주는 건가 싶어 기분이 묘해진다.

‘그런데 왜 하필 나지?’

의문은 금방 풀렸다.

“흑색 드레이크 가죽 세트. 맞죠?”

“아.”

이 자식도 명품충이구나. 내 장비를 위아래로 훑어본 임창수가 연신 감탄사를 내뱉었다.

“이야, 이거 사진으로나 보던 건데. 어디서 사셨어요? 해외 직구? 아니면 청담동?”

“대여했어요.”

“업체에서 리스 하셨구나. C급 헌터이신 걸로 알고 있는데 이게 유지가 되나……. 아, 죄송합니다. 악의가 있어서 한 말은 절대 아닙니다. 혹시 기분 나쁘셨어요?”

당연히 기분 나쁘지, 인마.

하지만 속마음을 대놓고 티 낼 정도로 멍청하진 않다.

임창수가 한 말이 사실 냉정한 현실이기도 하고.

‘그런데 인간이 좀 눈치가 없네.’

나는 점잖게 손을 내저었다. 약간의 넉살도 섞어서.

“안 그래도 허리 휘고 있어요. 버는 족족 유지비로 다 나갑니다. 주위 사람들은 미친놈이라고 욕하고.”

“하하, 그래도 목숨보다 중요한 게 있겠습니까. 안 그래요?”

“그렇죠.”

“그럼 다른 분들도 마찬가지겠네요.”

“네?”

“다른 분들이요. 평화 길드원분들. 다들 장비가 좋으시던데.”

“그런가요? 제가 그쪽은 잘 몰라서.”

임창수가 재미있는 농담을 들은 것처럼 웃었다.

“에이, 거금 들여서 장비 리스까지 하시는 분이 하실 말씀은 아니다.”

리스는 맞지만 거금을 들이진 않았다. 최 팀장이 무상 대여 해 주는 거니까. 사실대로 얘기해야 하나 잠깐 고민했지만 이내 마음을 접었다.

‘그런 거 말해 봐야 뭐 해.’

설명해 봤자 내 입만 아프지.

더 이상 장비에 대해 얘기하는 것도 귀찮아진 나는 적당히 얼버무렸다.

“다들 저랑 비슷해요.”

“그렇군요.”

그때, 임창수의 팀원 중 하나가 달려와 준비가 끝났다고 알렸다.

“이런, 너무 잡담이 길었네요. 그럼 전 이만. 마지막으로 팀원들 점검하고 다 같이 움직여야 할 것 같아서요.”

“수고하세요.”

“옙.”

예의 바르게 꾸벅 고개를 숙이고 떠나려던 임창수가 대뜸 물었다.

“맞다. 아까부터 묻고 싶었던 건데.”

“……?”

“혹시 우리 어디서 본 적 있나요?”

송이 씨한테 들었다면 날아갈 듯 기뻤겠지만 중갑옷을 걸친 수컷한테 들으니 기분이 별로다.

“초면입니다.”

“그래요?”

“네.”

어디선가 들어본 듯한 이름이라고 생각했을 뿐이지, 초면은 맞다. 내 단호한 대답에 임창수의 웃음이 진해졌다.

“알겠습니다. 그럼 이만.”

뭐지. 마지막 웃음은 왠지 기분 나쁜데.

그의 뒷모습을 응시하고 있을 때, 어느샌가 다가온 최 팀장이 물었다.

“아는 사입니까?”

“아뇨. 그냥 친하게 지내자는데요.”

“흠. 스카우트 제의는 아니고요?”

“전혀요. 그냥 장비 덕후라 말 건 것 같은데. 대뜸 오더니 어디서 샀냐고 물어보더라고요.”

“청담동에서 샀습니다.”

“…….”

난 안 궁금해.



* * *



“창수 형, 저 새끼는 갑자기 왜요?”

“그냥. 보니까 장비 괜찮아서 슬쩍 떠본 거지.”

“헐, 진짜네. 저거 자기 거래요?”

“생각을 해, 이 새끼야. C급 주제에 저런 걸 어떻게 입고 다녀.”

“그럼 리스? 미친놈이네요. 유지비 장난 아닐 텐데.”

“놔둬라. 귀엽잖아. 지도 나름 살아 보겠다고 무리하는 게.”

임창수는 피식 웃었다.

‘역시 별것 아닌 놈들이었어.’

난데없이 고가의 장비를 쫙 빼입고 오기에 혹시나 하는 마음이 든 건 사실이다. 괜히 잘못 건드렸다가 일이 커질 수도 있을 테니까.

하지만 파악이 끝난 지금은 마음이 편해졌다.

‘송송이.’

돈과 능력. 두 가지만 있으면 뭐든 할 수 있다. 여자 하나 얻는 건 일도 아니다. 임창수는 그렇게 믿었다.

“슬슬 출발하자. 전달해.”

“옙!”
```

## Final English reading copy

```markdown
# Chapter 81

In front of the Gate, ten men and women dressed as Hunters were chatting in a friendly atmosphere.

“Oppas, we’re really okay, right?”

At the female Hunter’s question, a B-rank Hunter from Sangdong Guild thumped his breastplate.

“Don’t worry. Don’t you trust us?”

“Of course I do. But I heard someone died here last week.”

“Don’t worry about those idiots. They died mouthing off despite not having the skill to back it up. Who can they blame? Right, Changsoo hyung?”

Im Changsoo, who had been listening quietly, exhaled a cloud of smoke into the air.

“If you’re nervous, go home. Don’t make the mood fucking miserable.”

The atmosphere instantly turned cold. The female Hunter who had spoken first forced the corners of her mouth upward.

“No, oppa, I was just—”

“Shut up. What are you going to do?”

“…Sorry.”

“Then go make yourself scarce in a corner. I’ve got more than enough bitches to bring along even without you.”

Despite his rough words and behavior, not one of them dared to object. They merely tried to lighten the mood with awkward smiles.

This sort of thing was familiar—and perfectly natural—to Im Changsoo.

*Idiots.*

Gates were geese that laid golden eggs called Magic Gems, and Hunters were the laborers who harvested them. Born into a family of estate managers, he had started out on a completely different footing.

“If you’re not heading to a hotel right now, quit clinging to each other. It’ll be a pain if another shitty rumor starts spreading.”

“Hyung, these ones are trustworthy.”

“I don’t trust them, asshole. Didn’t you say those last ones were trustworthy too?”

“Well, that was…”

Sangdong Guild might have been a respectable mid-sized Guild that threw its weight around in the area, but it wasn’t powerful enough to ignore public scrutiny. Im Changsoo had already received warnings from his father, the Guild Master, several times for messing with the wrong women.

“Let’s make sure there aren’t any problems, okay?”

“Yes, sir. We’ll bear it in mind. Loyalty!”

“Tsk. You’re good at answering.”

Im Changsoo flicked away his half-burned cigarette. As if she had been waiting for it, someone beside him called out a spell.

“Wind.”

A magically generated breeze sent the cigarette butt and its smell flying far away. The female mage who had cast the spell gave him a charming smile.

“I did good, right?”

Im Changsoo looked her up and down. She had a sleek figure and was an alluring beauty, and the two of them had a sort of sponsorship arrangement.

Despite her outstanding looks, she was a C-rank Hunter with pathetic skills. But the fact that she was the Guild Master’s son’s lover had been enough to get her into Sangdong Guild.

Her house, her car, and countless designer goods—all of them had come out of Im Changsoo’s pocket. But he had never once thought it was a waste.

*Well, that was true until now.*

But today, his mind had changed. Her figure, her looks, her entire air—all of it seemed tacky and cheap compared to the woman he had met about thirty minutes earlier.

*Was her name Song Song?*

Just thinking about her made his lower abdomen feel heavy.

She was a flower far too precious for some pathetic new Guild. He intended to pull her out without damaging a single root and plant her in his own flowerpot.

“Oppa, did something good happen? Why are you smiling like that?”

Im Changsoo didn’t answer. Instead, he waved toward the five people who had appeared in the distance.

“Ah, over here!”

Of course, he didn’t forget to add a quiet remark to his ex-girlfriend.

“Who the hell are you calling oppa, you fucking bitch?”

* * *

That lech—or rather, Im Changsoo—spoke with a bright smile.

“You’ve arrived. Ah, these are my team members.”

The people who appeared to belong to Sangdong Guild bowed their heads.

Including Im Changsoo, there were exactly five men and five women. Every one of them wore expensive, gleaming equipment, and their outfits clearly prioritized design over practicality.

Especially…

*Oh, wow.*

When it came to the female Hunters, I had no idea where to look. Im Kkeokjeong, a married man with two children, whispered with a stiff expression.

“They’re incredible.”

“……”

I almost nodded before managing to stop myself.

Miss Song was looking at us with a displeased expression.

*Come to think of it…*

Was this a raid or a blind date? Handsome and beautiful men and women pairing up, laughing and chatting as they entered a Gate—it was a perfect recipe for getting themselves killed.

Well, judging by their Levels and equipment, they would probably be fine.

“Is everyone here?”

The middle-aged official in charge of the Gate checked our numbers and Hunter licenses. It was one of the procedures we had to complete before entering.

“Sangdong Guild. Five B-ranks and five C-ranks. Correct?”

Im Changsoo gave him a courteous smile.

“That’s right.”

“Then Peace Guild. Two B-ranks, two C-ranks, and…”

The official’s hand paused as he flipped through the Hunter licenses.

“One E-rank? Where is he?”

Im Kkeokjeong thrust up his heavily furred arm.

“Uh, me.”

“What’s your position?”

“Sir, you’re not very observant. Would I carry around a huge brute of a shield like this if I were a mage? Heh heh.”

“You’re a tank.”

The official furrowed his brow.

A tank was exactly what the name suggested: a human shield who stood on the front line and blocked monster attacks. Because of the danger, tanks were among the best-paid Hunters, along with healers. They also had a high fatality rate.

“Why is an E-rank coming here? And he’s a tank, no less? Good grief.”

“You can make a lot in one go. Who knows? If the Magic Gems come tumbling out, we’ll have hit the jackpot.”

“Oppa, we’re really okay today, right?”

“Don’t worry. This oppa will protect you, Hye-rin.”

Murmurs spread among Im Changsoo’s team members. The official who had to let us enter was no exception.

“An E-rank tank…”

Butler Kim stepped forward at the concern in his voice.

“He is a veteran with twenty years of experience. He is also wearing sufficient equipment to prepare for any danger, so I don’t believe there will be a problem.”

“Veteran is good, of course. But you know what happened last week. Two C-rank tanks died. In a situation like this, letting him…”

That was when an unexpected ally appeared.

“Sir, can’t you make an exception?”

It was Im Changsoo. He continued in a soft voice.

“We’ve already signed the cooperative raid contract, and after meeting such fine people, it would be a shame to render it invalid.”

“Well, I mean…”

“If you could be just a little flexible, we’d really appreciate it… Please.”

What a strange guy. The words coming out of his mouth were all gratitude and requests, but his neck was stiff and his manner was high-handed.

The official flinched for a moment, then sighed.

“All right. But Team Leader, you’ll have to keep them under control.”

“Of course.”

*Keep them under control.* What an unpleasant way to put it.

With Im Changsoo’s help, permission was granted, but an ant seemed to be crawling around in one corner of my chest.

*Well, better to let it go.*

Even Im Kkeokjeong, the person involved, looked completely unfazed. It was ridiculous for me to take offense on his behalf.

“You may enter, then.”

At the official’s words, everyone stepped in front of the Gate. Ten Hunters from Sangdong Guild and five from Peace Guild. Fifteen people in total, including no fewer than seven B-rank Hunters—a highly elite raid team.

“Well, then…”

Im Changsoo, who had naturally taken the lead, winked.

“See you inside the Gate.”

Whoosh!

As Im Changsoo disappeared beyond the field of magic, Miss Song muttered,

“What a creep.”

*I agree.*

* * *

Whoosh.

The damp, sticky energy unique to magic wrapped around my body for a moment. When I opened my eyes, a new space unfolded before me.

It was a cavern so vast that it couldn’t even be compared to an F-rank Gate. Three entrances gaped open like enormous maws. It was the place we had seen in the video on the way here.

*The only difference was…*

Ding.



> **System**
>
> You have entered **The Minotaur’s Labyrinth**.
>
> Quest **B-rank Gate Clear** has been created.

There was a System notification that only I could hear. And, on top of that, a Quest.

“All right, let’s check our numbers and equipment one more time before we go in.”

While everyone checked their belongings, I quietly moved to a corner of the cavern and muttered inwardly.

*Check Quest.*

Ding.



> **System**
>
> **Quest**
>
> **B-rank Gate Clear**
>
> You have entered a B-rank Gate for the first time in your life.
>
> Upon successfully completing the raid, you will receive a corresponding Reward. This applies only once.
>
> **Grade:** First Rate
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Clear the B-rank Gate *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

What a refreshing start.

I had just closed the Quest window with a warm smile when—

“What are you doing over here by yourself?”

A voice suddenly came from behind me. I turned my head and saw Im Changsoo walking toward me.

“Me?”

I thought he had mistaken me for someone else, but he hadn’t.

“You’re Jang Taekyung from Peace Guild, right?”

“I’m Jin Taekyung.”

“Yes, Jang Taekyung.”

I wasn’t sure whether he was deaf or my tongue was malfunctioning, but I nodded for the moment.

*We’ll probably only see each other once, anyway.*

He had helped out over the matter with Im Kkeokjeong, so I still felt a little grateful toward him.

“Did you need something?”

“Haha, it’s nothing I’d call business. This is fate, so I thought we could at least exchange names. You heard my introduction earlier, so you already know who I am. I look forward to working with you.”

Someone once said you couldn’t spit in a smiling face. It was a little awkward, but I clasped the hand Im Changsoo offered with a broad smile on his face.

“Ah, yes. I look forward to working with you too.”

A Team Leader from another Guild—someone I had never even met before—had offered me a handshake first.

I had participated in cooperative raids several times over the past seven years and had plenty of experience as a day-labor Hunter, but this was the first time something like this had happened.

*Then again, I was an F-rank back then.*

In those days, people had treated me like air. Maybe being a C-rank Hunter meant I was finally being treated like a person. It left me with a strange feeling.

*But why me?*

The question was answered almost immediately.

“That’s a Black Drake Leather Set, right?”

“Ah.”

*This guy’s a Designer-Brand Junkie too.*

Im Changsoo looked over my equipment from head to toe and let out one exclamation after another.

“Wow, I’d only ever seen this in pictures. Where did you buy it? Did you order it from overseas? Or get it in Cheongdam-dong?”

“I rented it.”

“You leased it from a company, then. I heard you’re a C-rank Hunter, but can you really keep something like this maintained? Ah, I’m sorry. I absolutely didn’t mean anything by it. Did I offend you?”

*Of course I’m offended, you moron.*

But I wasn’t stupid enough to let my true feelings show so openly.

What Im Changsoo had said was also a cold reality.

*Still, this guy really has no tact.*

I waved a hand with deliberate composure and added a little self-deprecating humor.

“It’s already breaking my back. Every penny I earn goes toward maintenance. The people around me call me crazy.”

“Haha, but is there anything more important than your life? Right?”

“That’s true.”

“Then I suppose the same goes for the others.”

“Sorry?”

“The others. The Peace Guild members. Their equipment looked pretty good too.”

“Did it? I don’t know much about that sort of thing.”

Im Changsoo laughed as if he had heard an amusing joke.

“Come on. That’s not something someone who spends a fortune leasing equipment gets to say.”

The equipment was leased, but it hadn’t cost me a fortune. Team Leader Choi had loaned it to me free of charge. I briefly considered explaining that, but soon abandoned the thought.

*What’s the point of bringing that up?*

Explaining it would just be a waste of breath.

I was already tired of talking about equipment, so I gave him a vague answer.

“They’re all about the same as mine.”

“I see.”

At that moment, one of Im Changsoo’s team members ran over and told him that preparations were complete.

“Oh, dear. We’ve been chatting for too long. I’d better go. I need to check on my team members one last time, and then we should all move together.”

“Take care.”

“Yes.”

Im Changsoo politely bowed his head and was about to leave when he suddenly asked,

“Oh, right. There’s something I’ve been meaning to ask you.”

“……?”

“Have we met somewhere before?”

I would have been overjoyed if Miss Song had asked me that, but hearing it from a male in heavy armor left me feeling less than pleased.

“This is our first meeting.”

“Really?”

“Yes.”

I only thought his name sounded familiar, but this was definitely our first meeting. At my firm answer, Im Changsoo’s smile deepened.

“All right, then. I’ll be going.”

What was that? His final smile rubbed me the wrong way.

As I watched his back, Team Leader Choi approached without my noticing and asked,

“Do you know him?”

“No. He just said he wanted to be friends.”

“He didn’t make a recruitment offer?”

“Not at all. I think he only came over because he’s a gear enthusiast. He suddenly walked up and asked where I bought my equipment.”

“I bought it in Cheongdam-dong.”

“……”

*I wasn’t asking.*

* * *

“Changsoo hyung, why did you suddenly go talk to that bastard?”

“Nothing. His equipment looked decent, so I sounded him out.”

“Holy crap, seriously? Is that stuff really his?”

“Use your brain, asshole. How could a C-rank wear something like that?”

“Then he leased it? Crazy bastard. The maintenance costs must be insane.”

“Leave him alone. It’s cute, watching him overextend himself trying to make something of himself.”

Im Changsoo let out a quiet laugh.

*As expected, they were nothing special.*

It was true that he had felt a little uneasy when they showed up out of nowhere decked out in expensive equipment. If he messed with the wrong people, things could get out of hand.

But now that he had them figured out, he felt at ease.

*Song Song.*

Money and ability. With only those two things, he believed he could do anything. Getting his hands on one woman would be no trouble at all.

“Let’s get moving. Pass it on.”

“Yes, sir!”
```
