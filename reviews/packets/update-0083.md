<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0083.txt",
      "sha256": "29b963865819197a4ff531dc0325a9650f9a7e37af191f8a1ff1bc362f67b47e",
      "bytes": 15045
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e8ffdc98d00cea0a5e6539f31a707197237b80434479cedfe3b53cfea72154b2",
      "bytes": 7497
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "cfa2656abf30e13073b69e0d32d02f168419161ac9d13965eb24d1c3ac05b669",
      "bytes": 7421
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "ec73935d9953227c4a048383bcc6cd454453025926e65378267623db07095028",
      "bytes": 1608
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4c844c0aef8beeae666c6f8d7183d32afb57eaa4b385951749a78213bde707a9",
      "bytes": 23807
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "c9adc17a5523d49298335f51eb2e6d0cf73a29ae0102b58fcb02be476f3edbd8",
      "bytes": 507
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "d8ae7808b65e04f9155660615363978f4cf2344a14bc5e905f897e7286a5460c",
      "bytes": 3852
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bf1fbacecca103cebf36aed1eee3f316935a6df1efe2dec5ca59135b1d8db4e5",
      "bytes": 6060
    }
  ],
  "estimated_tokens": 14402
}
-->

# Durable State Update — Chapter 83

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 83. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 83. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 83,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 83,
    "continuity_sources": [83],
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
    "After ten days of Mukyung’s training, Taekyung mastered the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique, and the Training? Trial! Quest succeeded with a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured after the attack, and the unidentified assassin may be the Head Elder’s hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training; Wikyung plans to summon every Shanxi sect on New Year’s Day and may seek to become Alliance Leader.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months, and five-year-old Soyul does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout; Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect; Taekyung received the forced Yesterday’s Enemy, Today’s Ally Quest to deliver an invitation for New Year’s Day.",
    "Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song. Butler Kim is Guild Master, Choi leads Team 1, and the other three are team members.",
    "The Peace Guild’s Guild house is Sooni’s Super in Bucheon’s Gate-dense district, on property purchased from the former owner’s surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong is married with two children and joined Peace Guild after Choi recruited him while hospitalized.",
    "Team Leader Choi formerly served in Ares Guild with Song Song; Butler Kim is a retired mage and former Hunter who trained at Nonsan’s 28th Regiment, 1st Battalion, as did Taekyung. Choi is Level 75, Kim Level 80, Song Song Level 64, and Im Hyeokjun Level 24.",
    "A Bucheon Terminal Guild raid against seven B-rank Minotaurs ended with the monsters defeated but two C-rank Hunters dead, making Taekyung judge the Peace Guild’s first raid dangerous.",
    "The Peace Guild joined Sangdong Guild’s party for its first official raid into The Minotaur’s Labyrinth; Sangdong’s team leader is Im Changsoo.",
    "Choi loaned Taekyung a Peak-grade Masterwork Black Drake Leather Set and a Peak-grade Masterwork Black Thorn Spear with a 90% chance to inflict Bleeding on hit.",
    "Sangdong Guild and Peace Guild entered The Minotaur’s Labyrinth as a fifteen-person team with seven B-rank Hunters; Im Kkeokjeong was registered as an E-rank tank, and Taekyung received the restricted B-rank Gate Clear Quest.",
    "Im Changsoo is the Sangdong Guild Master’s son, behaves abusively toward his team, maintains a sponsorship relationship with the C-rank mage Hye-rin, and intends to pursue Song Song.",
    "Taekyung is both a Hunter and a martial artist, giving him the advantages of both classes; Choi has noticed that Taekyung’s behavior is inconsistent with an ordinary C-rank Hunter.",
    "Im Kkeokjeong is positioned as the raid’s front-line tank with Choi’s Peak-grade Matador equipment, and eight Minotaurs emerge from the labyrinth’s five holes.",
    "Im Changsoo deliberately misnames Taekyung as Jang Taekyung, and Taekyung retaliates with the insult Shit Changsoo; their confrontation is now openly hostile."
  ],
  "continuity_sources": [
    82
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed, as does any connection between the attack and Song Sword Sect.",
    "It remains unresolved whether Hyuk Mujin will become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung’s summons and whether he will become Alliance Leader.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung’s prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim’s former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung’s interrupted confession.",
    "The reason Im Changsoo seems familiar to Taekyung, whether he can act on his interest in Song Song, and what will happen in The Minotaur’s Labyrinth remain unresolved."
  ],
  "safe_through": 82,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung’s deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year’s Day for 원단 and close the sect’s gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Render fist-and-kicking technique as 권각술, recognition as 인정, Falling Flow Sword as 낙류검, Twelve Gale Fists as 질풍십이권, Flame Divine Palm as 화염신장, and Tendon-Splitting and Bone-Twisting as 분근착골.",
    "Use Reformation Fist, Toughness, Heavenly Martial Physique, Jang Childeuk, Martial Artist Jang, benevolence/righteousness/propriety/wisdom, killed by a tiger, fifteen minutes, lifelong single, Let’s eat noodles, Squad Leader, Third Young Master, Designer-Brand Junkie, Qi Sense, Peace Guild, Essence of the Himalayas, Sooni’s Super, Song Song, Miss Song, Taurus, Ares Guild, Senior, Young Master, Guild Master, Minotaur, Bucheon Terminal Guild, and The Minotaur’s Labyrinth as established.",
    "Use Sangdong Guild, Hunter Association, Black Drake, Masterwork Black Drake Leather Set, Masterwork Black Thorn Spear, Bleeding, artifact, gear advantage, Hye-rin, Cheongdam-dong, Matador’s Full-Body Armor, Matador’s Shield, Taunt, Hallucination, Minotaur Warrior, Top-tier, and tongue-pulling hell as established terminology."
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
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |

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
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 임창수    | **Im Changsoo**   |
| 생도     | **cadet**                                    |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 귀가      | **your family**                                                 |
| 임꺽정 | **Im Kkeokjeong** |
| 평화 | **Peace Guild** | Guild name. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 82
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 82
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 81
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and occasionally teasing
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 79
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Former Ares Guild Team Leader; reawakened Hunter publicly classified as C-rank; leader and employer of Team 1, the Peace Guild’s E-rank Gate party
- **Personality:** Calm, observant, practical, and decisive under pressure
- **Voice:** Polite and measured in ordinary conversation; clipped and commanding during combat
- **Relationships:** Hires Jin Taekyung as a porter and leads him, Im Kkeokjeong, and three veteran E-rank Hunters through an E-rank Gate

## Korean source

```text
＃83화



임창수의 신경은 아까부터 온통 송송이를 향해 있었다.

‘젠장, 비싸게 굴기는.’

일부러 자꾸 근처를 맴돌고 지나가듯 말도 몇 번 붙여 봤지만 송송이의 반응은 무미건조했다. 아, 네. 감사합니다. 알겠어요.

자신이 거둔 소득치고는 너무 초라하다.

‘까다로운 년.’

여자가 남자를 볼 때 대부분 어릴 때는 얼굴, 나이 먹으면 몸과 능력을 본다고 했다. 이 세 가지를 모두 갖고 있는 임창수는 작업에 실패해 본 적이 없다.

가벼운 그의 인간관계에 환멸을 느낀 여자가 먼저 떠나거나, 그전에 그가 질려서 차 버린 일은 있었어도 지금 같은 무관심은 처음이다.

‘지 잘난 건 알아 가지고.’

짜증이 나다가도 송송이의 매끈한 몸매와 몽환적인 얼굴을 보면 화가 스르륵 풀렸다. 다른 여자들의 화장품 냄새와는 차원이 다른 향긋한 체취도 한몫했다.

‘조급해하지 말자. 어차피 넘어오게 되어 있어.’

아직 시간은 많다. 미노타우로스의 미로는 말 그대로 미로. 레이드 타임이 다른 게이트와 비교해 두 배까지도 늘어날 수 있다. 그 정도면 여자 하나 꼬시기에는 충분한 시간이다.

다만 한 가지 문제가 있다면…….

‘한 놈이 자꾸 거슬리네.’

최민우라고 했나? 게이트 속이 아니라 화보 잡지 속에 있는 게 더 어울릴 것 같은 놈이다. 번드르르한 얼굴도, 길쭉한 팔다리도. 특유의 덤덤한 표정도 마음에 안 들었다.

‘나머지는 뭐, 병신들이고.’

허허 웃고만 있는 할배와 산적 같은 아저씨는 애초부터 제외니까.

그나마 장태경이라고 젊은 놈이 하나 더 있긴 한데 경쟁자 축에도 못 낀다.

‘왠지 모르게 기분 나쁜 놈이지만.’

흔해 빠진 C급 헌터. 대형 길드 소속도 아니고, 주제에 안 맞는 고급 장비를 리스 해서 연명하는 하루살이에 불과한데 태도나 말투는 묘하게 당당하다.

조금 전 대화의 마지막에서는 자신을 향한 귀찮음마저 느껴질 정도였다.

‘가오는 살린다 이건가?’

장태경, 최민우. 거슬리는 두 놈이 붙어 있으니 임창수의 눈과 귀가 그쪽에서 떨어지지 않았던 것도 당연했다.

- 음모오오오!

미노타우로스가 줄줄이 등장하기 시작했을 때였다.

“어떻게 생각하십니까?”

“아마 힘들지 않을까요.”

이 자식들 봐라?

안 그래도 막 부하들을 물리려던 임창수가 입을 다물며 귀를 기울였다.

“태경 씨라면 어떻겠습니까?”

“저 말입니까?”

여기까지만 들어도 이미 기가 차는데, 더 가관인 것은 잠시 후 들려온 대답이었다.

“잘 모르겠네요.”

C급 헌터가 미노타우로스 여덟 마리를 상대로, 뭐? 잘 몰라?

일대일로 붙어도 1분 안에 시체가 될 놈이 입만 살았다.

‘미친놈들. 아주 소설을 써라.’

피식, 웃음을 흘리던 임창수가 순간 멈칫했다.

마음에 안 드는 두 놈을 송송이 앞에서 개망신 줄 수 있는 기회라는 생각이 뇌리를 스쳤기 때문이었다.

두 사람의 사이로 불쑥 끼어든 것도 그런 이유에서였다.

“워낙 재미있는 얘기들을 하고 계셔서 좀 들었습니다. 괜찮으시죠?”

사과도 받고, 비웃어 주고. 이참에 누가 더 우위에 있는지 확실히 각인시켜 줄 생각이었다.

그런데…….

“그럼 씹창수라고 불러 드려요?”

“뭐?”

“임창수든 씹창수든. 그쪽 성이 뭐든 내 알 바 아니잖아요.”

씹창수.

난생처음 들어 보는 폭언에 임창수의 뇌가 정지했다.



* * *



사방이 침묵에 잠겼다. 상동 길드, 평화 길드. 심지어는 미노타우로스들까지 울음소리를 멈춘 듯했다.

그 숨 막히는 정적 속에서, 굳게 닫혀 있던 놈의 입이 열렸다.

“……야, 이 새끼야.”

사실 이쯤 되면 존댓말을 쓰는 것도 우습다.

나도 시원시원하게 대답해 주었다.

“뭐, 이 새끼야.”

“너 진짜. 돌았냐?”

“원래 지구인들은 다 돌고 있어. 천동설도 모르냐? 이 무식한 새끼.”

그때 최 팀장이 끼어들었다.

“그건 지동설입니다. 천동설은 지구가 우주의 중심으로 고정되어 있어서 움직이지 않으며, 지구의 둘레를 달, 태양, 행성들이 각기 고유의 천구를 타고 공전한다고 하는 우주관…….”

텁.

은밀하게 다가온 임꺽정의 솥뚜껑만 한 손이 최 팀장의 입을 틀어막았다.

“읍. 이게 뭐 하는. 읍읍.”

“…….”

그냥 이대로 콱 죽어 버렸으면 좋겠다. 눈치가 없어도 정도가 있지. 상동 길드에서 돈이라도 받았나 의심될 정도다.

“내가 이런 놈들이랑 말을 섞다니.”

임창수가 어이없다는 듯한 얼굴로 나와 최 팀장을 바라봤다.

“너희같이 얼빠진 놈들이 어떻게 헌터가 된 거지?”

“그럼 뭐, 내신 등급 보고 뽑냐? 토익 900점 이상이면 B급이고 중국어까지 가능하면 A급이야?”

“그 입 닥치는 게 좋을 거다. 오래 살고 싶으면.”

“이야, 이제 협박까지? 무서워서 상동 길드 쪽으로 오줌도 못 싸겠어.”

으드득. 임창수의 두 눈에서 불꽃이 쏟아졌다.

“잊었나 본데…… 여긴 게이트야.”

“나도 알아, 인마. 저기 멀리에서 미노타우로스 여덟 마리가 우리 쪽으로 오는 중인 것도 알고.”

호랑이도 제 말 하면 온다더니.

딱 알맞은 타이밍에 황소의 울음소리가 울려 퍼진다.

- 모오오오!

“오, 온다!”

“어쩌지?”

“뭘 어떡해. 돌아가! 빨리!”

쿵. 쿵. 쿵.

미노타우로스 무리가 움직일 때마다 동굴 바닥이 진동한다.

꽁무니가 빠져라 도망쳐 오는 팀원들의 모습을 보며 임창수가 가래를 탁 뱉었다.

“너, 운 좋은 줄 알아라.”

“내가 좀 그런 편이지.”

시스템을 얻은 덕분에 제2의 인생을 살고 있다고 해도 과언이 아니다. 죽을 만한 고생도 했지만 운 하나는 기똥찬 편이지.

“저놈들을 처리한 후에 보자고.”

“그것도 괜찮고.”

“뱉은 말에 책임을 질 수 있는 놈이면 좋겠군.”

“책임질 수 있을걸.”

나는 놈의 머리 위에 둥둥 떠 있는 레벨 창을 바라봤다.



[Lv.65 임창수]



65레벨. 높다. 녀석의 다른 팀원들과 비교해도 10레벨 가까이 차이 나는 걸 보면 B급 헌터 중에서도 썩 괜찮은 실력일 것이다. 물론 나만큼은 아니겠지만.

‘뭐, 인성이랑 실력이 비례하는 건 아니지.’

헌터는 토익이나 내신 등급, 인성 적성 검사로 뽑히는 게 아니니까. 고개를 절레절레 흔들며 돌아선 그때였다.

“지금은 어때?”

“……?”

“미노타우로스. 혼자서도 자신 있다고 하지 않았나?”

아하. 무슨 말을 하려는 건지 대충 감이 잡힌다.

의도가 뻔히 보이는 말투와 표정에 피식 웃음이 새어 나왔다.

“글쎄, 그런 말을 한 기억은 없는데.”

“뱉은 말에 책임은 져야지.”

“유치해서 못 놀아 주겠네. 불만 있으면 레이드 끝나고 일대일로 해결해.”

평온한 얼굴로 상황을 지켜보던 김 집사와 송이 씨도 입을 열었다.

“두 분 모두 진정하는 게 좋겠군요.”

“저기요, 지금 이럴 때가 아닌 것 같은데.”

쿵쿵쿵.

이 순간에도 미노타우로스 무리는 시시각각 가까워지고 있었다. 놈들이 신중하게 접근해서 망정이지, 마음만 먹었다면 진작 전투가 벌어졌을 수도 있을 것이다.

“들었지? 괜한 사람들 피해 입히지 말고 나중에…….”

“다섯 장.”

“응?”

임창수가 손가락 다섯 개를 쫙 폈다.

저건 별이 다섯 개……가 아니고 다섯 장이라니. 설마?

“내가 생각하는 그건가?”

“저 미노타우로스 무리. 혼자 처리하면 마리당 큰 거 다섯 장씩 주지.”

“큰 거?”

“그래, 큰 거.”

한 마리당 5천만 원이니까 여덟 마리면 4억이다.

C급 헌터가 된 지금의 내게도 상당한 거금.

‘하지만…….’

모두가 보는 앞에서, 특히 송이 씨가 보는 앞에서 돈에 약한 모습을 보이기는 싫다. 이건 자존심 문제다!

‘송이 씨. 제 마음이 들리시나요.’

그윽한 눈길로 그녀를 바라본 내가 대답했다.

“거절한다.”

임창수의 눈썹이 꿈틀거린다.

“부산물에 대한 일체의 권한까지 준다고 해도?”

“싫어.”

“마정석이 나올 수도 있을 텐데.”

“안 돼.”

청소년 법원 판사처럼 단호한 내 대답에 임창수가 입술을 깨물었다.

“쓸데없이 자존심만 강한 놈이군. 40억에 부산물 권한까지 주겠다는데 그걸 거절하다니.”

“돌아가…… 잠깐. 지금 뭐라고?”

내 귀가 잘못됐나?

몇 초간 오만 가지 생각이 들었다. 머릿속을 정리한 뒤에야 간신히 입술을 뗄 수 있었다.

“얼마? 40억?”

“말하지 않았나? 큰 거 다섯 장이라고.”

“…….”

“그럼…… 한 마리당 5억?”

존나 큰 다섯 장이라고 했어야지.

세상에, 40억이라니. 상상을 초월하는 액수에 나는 물론이고 송이 씨와 임꺽정까지 입을 딱 벌렸다.

‘이 자식은 뭐 이렇게 통이 커?’

중견 길드의 팀장인 데다 B급 헌터니까 잘 벌기야 할 테지만 지금처럼 수십억을 툭 제시하는 건 말이 안 된다.

“그걸 그냥 준다고? 40억을?”

“그냥? 그건 곤란하지. 이건 내기야.”

“무슨 내기?”

“나도 얻는 게 있어야지.”

임창수의 입꼬리가 비틀렸다.

“네가 죽거나 도망칠 경우 지금까지의 보상은 무효다. 거기에 더해서…….”

놈의 고개가 스르륵 움직였다. 그 시선이 멈춘 곳에는 한 사람이 있었다.

“저요?”

“예, 송송이 씨를 저희 길드로 모시고 싶습니다.”

임창수가 예의 바르게 고개를 숙였다. 지금까지의 모습과는 너무 달라 소름 돋을 정도의 태세 전환이다.

“어우, 소름 돋아. 그냥 하던 대로 해요. 가식 떠는 것보다는 그게 훨씬 나아 보이니까.”

“…….”

“…….”

송이 씨, 솔직한 성격이구나.

진짜 소름이 돋았는지 몸을 부르르 떤 그녀가 팔짱을 꼈다.

“씹창, 아니 임창수 씨라고 했죠.”

“……네.”

“음. 단도직입적으로 말할게요. 그쪽, 내 취향 아니에요.”

시속 160km. 몸 쪽 꽉 찬 돌직구에 임창수의 눈빛이 흔들렸다.

“예?”

“키 크고 잘생겼는데 딱 바람 잘 피울 것 같아요. 제가 바람을 싫어하거든요. 간만에 머리 잘됐는데 헝클어지면…… 아, 이게 아닌가?”

“예, 예?”

“아무튼 내 타입 아니에요. 바람둥이에 너무 돈 자랑하는 사람은 딱 질색.”

처음 봤다. 임창수의 벙찐 모습.

아마 다른 사람이 보면 지금 나도 같은 표정이지 않을까.

“어, 방금 그 모습은 좀 괜찮네. 그런데 아까부터 쭉 지켜보니까 평소 인성이 좀, 그쪽 스스로도 느끼죠?”

가까스로 표정을 수습한 임창수가 대답했다.

“그거야 하나씩 맞춰 가면 되죠.”

“에이, 똥인지 된장인지 찍어 먹어 봐야 아나요. 그쪽은 나랑 배꼽 맞추는 것밖에 관심 없어 보이는데. 맞죠?”

“……!”

“……!”

나를 포함한 모두가 입을 딱 벌렸다. 수줍은 듯이 머리를 매만지며 한마디씩 하는데, 한 방 한 방이 거의 핵폭탄 급이다.

“그렇다고 뭐, 딱히 상동 길드가 싫은 건 아니에요.”

쉴 새 없이 두드려 맞던 임창수가 반색하며 물었다.

“정말입니까?”

“네. 어차피 다시 옮기면 되니까.”

“…….”

송이 씨, 천잰데?

해맑은 얼굴로 빅 엿을 먹인 송이 씨가 말을 이었다.

“그런데 일단 길드를 옮기려면 양해를 구해야 돼서요. 그렇죠, 길드장님?”

“아, 물론이죠.”

흥미로운 눈빛으로 구경하고 있던 김 집사의 대답에 송이 씨가 고개를 돌렸다.

“팀장님은 어떻게 생각하세요?”

“뭘 말입니까? 송이 씨가 길드를 옮기는 것?”

“이 내기에 졌을 경우에는 그렇게 되겠죠.”

최 팀장이 덤덤하게 고개를 끄덕였다.

“그러시죠.”

“……너무 쉽게 대답하는 것 아니에요?”

“쉬운 질문이라 쉽게 대답한 겁니다.”

순간 송이 씨의 눈빛에 서운함이 묻어 있다고 생각한 건 나만의 착각일까?

‘에이, 아니겠지.’

다시 보기에는 너무 빨리 스쳐 간 감정이었다. 시원 털털한 모습으로 돌아온 송이 씨가 이번엔 임창수에게 말했다.

“그럼 전 내기 찬성. 태경 씨는?”

“저는…….”

고민은 짧지 않았다. 처음 최 팀장의 질문을 들었을 때부터, 이미 마음 깊은 곳에서는 묘한 확신이 자리 잡았으니까.

내가 놈들보다 더 강하다는 확신이.

“내기에 응하겠습니다.”

최 팀장의 입가에 웃음이 번졌다.

“저도 참가하죠. 내기는 판이 커야 재밌지 않겠습니까.”

“이야, 아주 도박사 나셨구만. 그래서 얼마?”

“40억. 물론 진태경 씨가 여덟 마리 모두 쓰러트린다에 걸겠습니다.”

“뭐?”

잠시 최 팀장을 노려보던 임창수가 픽 웃었다.

“재밌는 놈들이네. 한 놈은 죽고 싶어서 난리고, 다른 한 놈은 돈 버리고 싶어서 안달 났고.”

“그래서 대답은?”

“당연히 예스지.”

“계약서라도 쓸까요?”

“계약서? 사람을 뭘로 보고. 난 한 번 뱉은 말은 지킨다. 그쪽은…… 안 지켜도 좋아. 지키게 만들어 줄 테니까. 모두 뒤로 물러나!”

거대하고 축축한 동굴이 콜로세움으로 바뀌는 순간이었다.

엄청난 액수가 걸린 투기장. 나는 미노타우로스 무리와 싸워야 하는 검투사다.

“최 팀장님. 제가 지면 어쩌시려고요?”

“이길 겁니다.”

이 자신감의 근원이 어딜까? 자기 자신에 대한 믿음? 아니면 그동안 지켜본 내 모습?

상관없다. 난 최선을 다해 목적을 달성할 뿐이다.

쿵쿵쿵쿵쿵!

- 모오오오!

20m 앞. 놈들의 하나하나가 똑똑히 눈에 들어온다.

뜨거운 콧김, 열기, 근육과 치켜올린 무기.

‘소랑 싸우는 건 처음인데.’

재밌는 경험이 되겠군.

나는 창을 쥐었다. 투우사처럼 소 떼를 향해 달려들었다.
```

## Final English reading copy

```markdown
# Chapter 83

Im Changsoo’s attention had been fixed entirely on Song Song for some time.

*Damn, she sure knows how to play hard to get.*

He had deliberately kept circling near her and tried striking up conversations in passing several times, but Song Song’s responses had been utterly matter-of-fact.

“Oh, okay.”

“Thank you.”

“I understand.”

For all his effort, the results were pathetic.

*What a difficult bitch.*

They said that when women looked at men, they cared about their faces when they were young, but their bodies and abilities once they got older. Im Changsoo possessed all three, and he had never failed at picking up a woman.

There had been women who became disgusted with his shallow relationships and left first, or ones he had grown tired of and dumped before they could leave.

But he had never encountered indifference like this.

*She sure knows she’s hot shit.*

Even when he grew irritated, the anger slowly melted away whenever he looked at Song Song’s sleek figure and dreamlike face. Her fragrant natural scent, completely different from the smell of other women’s cosmetics, helped, too.

*Don’t get impatient. She’ll fall for me eventually.*

There was still plenty of time. The Minotaur’s Labyrinth was a labyrinth in the truest sense of the word. Raid times could stretch to twice as long as those of other Gates.

That was more than enough time to pick up one woman.

There was only one problem…

*One guy keeps getting on my nerves.*

Choi Minwoo, was it? He looked more suited to a fashion magazine than a Gate. His polished face, his long limbs—even his characteristically impassive expression irritated Im Changsoo.

*The rest are just fucking idiots.*

The old geezer who did nothing but chuckle and the bandit-like middle-aged man were out of the running from the start.

There was one more young guy named Jang Taekyung, but he didn’t even qualify as competition.

*He’s weirdly irritating, though.*

A run-of-the-mill C-rank Hunter. He wasn’t even part of a major Guild, just a small-timer scraping by with high-end equipment he’d leased despite it being above his station. Yet his attitude and way of speaking were strangely confident.

In fact, at the end of their conversation a moment ago, Taekyung had seemed almost annoyed with him.

*Trying to save face, are we?*

With the two irritating bastards, Jang Taekyung and Choi Minwoo, standing together, it was only natural for Im Changsoo to keep his eyes and ears trained on them.

—Mooooo!

It was when the Minotaurs began appearing one after another.

“What do you think?”

“It would probably be difficult, wouldn’t it?”

*Well, look at these bastards.*

Im Changsoo, who had just been about to call his men back, closed his mouth and listened.

“What about you, Mr. Taekyung?”

“Me?”

That was already absurd enough, but the answer that came a moment later was even more ridiculous.

“I’m not sure.”

A C-rank Hunter facing eight Minotaurs, and what? He wasn’t sure?

The bastard would be a corpse within a minute even in a one-on-one fight, but all he had going for him was his mouth.

*Crazy bastards. Go ahead and write a novel.*

Im Changsoo let out a short laugh, then suddenly paused.

An idea had flashed through his mind: this was a chance to humiliate the two men he disliked in front of Song Song.

That was why he abruptly stepped between them.

“You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?”

He planned to get an apology, laugh at them, and make it unmistakably clear who held the upper hand.

But then…

“Then should I call you Shit Changsoo?”

“What?”

“Im Changsoo or Shit Changsoo. I don’t care what your surname is.”

Shit Changsoo.

Im Changsoo’s brain froze at an insult unlike anything he had ever heard in his life.



* * *

Silence fell all around us.

Sangdong Guild. Peace Guild.

Even the Minotaurs seemed to stop mooing.

In that suffocating silence, the man’s tightly closed mouth finally opened.

“…You little shit.”

At this point, using polite speech would have been ridiculous.

I gave him an equally breezy answer.

“What, you little shit?”

“You really… Are you insane?”

“Everyone on Earth is already spinning. Don’t you know geocentrism, you ignorant bastard?”

“That’s heliocentrism. Geocentrism is the cosmological view that the Earth is fixed at the center of the universe, unmoving, while the Moon, Sun, and planets orbit around it, each traveling along its own celestial sphere…”

*Smack.*

Im Kkeokjeong’s enormous, cauldron-lid-sized hand had approached so quietly that no one noticed it until it clamped over Team Leader Choi’s mouth.

“Mmph. What are you doing? Mmph, mmph.”

…

I wished he would just drop dead right there.

There was a limit to having no sense of the situation. I almost wondered whether Sangdong Guild had paid him.

“I can’t believe I’m talking to people like you.”

Im Changsoo looked at Team Leader Choi and me as if we were unbelievable.

“How did airheaded bastards like you even become Hunters?”

“What, do they recruit based on school transcripts? Get a TOEIC score of 900 and you’re B-rank, and if you can speak Chinese, you’re A-rank?”

“You’d better shut that mouth if you want to live a long time.”

“Wow, threats now? I’m so scared I won’t even be able to piss in Sangdong Guild’s direction.”

Im Changsoo ground his teeth, sparks flying from his eyes.

“You seem to have forgotten… This is a Gate.”

“I know, asshole. I also know that eight Minotaurs are coming toward us from over there.”

They say even a tiger comes when you talk about it.

Right on cue, the bellow of a bull echoed through the cavern.

—Moooooo!

“They’re coming!”

“What do we do?”

“What do you think? Get back! Hurry!”

*Boom. Boom. Boom.*

The cavern floor shook every time the herd of Minotaurs moved.

Watching his team members run back with their tails between their legs, Im Changsoo spat out a wad of phlegm.

“You should consider yourself lucky.”

“I tend to be pretty lucky.”

Thanks to the System, it wouldn’t be an exaggeration to say that I was living a second life. I had gone through enough hardships to die from, but I had always been blessed with incredible luck.

“We’ll see each other after I deal with those bastards.”

“That works, too.”

“I hope you’re prepared to take responsibility for what you said.”

“I think I can handle that.”

I looked at the Level window floating above his head.



> **System**
>
> **Level 65 Im Changsoo**

Level 65. High.

Compared to his other team members, he was nearly ten Levels higher, which meant he was probably quite capable even among B-rank Hunters.

Of course, he still wasn’t as good as me.

*Well, character and ability aren’t proportional.*

Hunters weren’t selected based on TOEIC scores, school grades, or personality tests.

I shook my head and turned away.

“How about now?”

“…?”

“The Minotaurs. Didn’t you say you were confident you could handle them alone?”

Ah. I had a rough idea of what he was getting at.

His intentions were obvious from his tone and expression, and a short laugh escaped me.

“I don’t remember saying anything like that.”

“You should take responsibility for what you said.”

“You’re too childish. I can’t indulge you. If you have a problem, settle it one-on-one after the raid.”

Butler Kim and Miss Song, who had been watching the situation with calm expressions, spoke up as well.

“It would be better if both of you calmed down.”

“Excuse me, but don’t you think this is a bad time?”

*Boom-boom-boom.*

Even now, the Minotaur herd was drawing closer by the second.

It was fortunate that they were approaching cautiously. If they had really wanted to, the battle could have begun long ago.

“You heard them, right? Don’t put innocent people in danger. We’ll deal with this later…”

“Five bills.”

“Huh?”

Im Changsoo spread all five fingers wide.

*That wasn’t five stars… it was five bills.*

Was he talking about the thing I thought he was?

“The Minotaur herd over there. If you handle them alone, I’ll give you five big bills per head.”

“Big bills?”

“Yeah. Big bills.”

That meant fifty million won per Minotaur, or four hundred million for all eight.

Even for me, a C-rank Hunter, that was a considerable sum.

*But…*

I didn’t want to look weak in front of everyone, especially Song Song, by showing how easily money swayed me.

This was a matter of pride!

*Miss Song. Can you hear my heart?*

I gazed deeply into her eyes and answered.

“I refuse.”

Im Changsoo’s eyebrow twitched.

“Even if I give you all rights to the byproducts?”

“No.”

“Magic Gems might come out of them.”

“Still no.”

My answer was as firm as a juvenile court judge’s. Im Changsoo bit his lip.

“What a pointlessly proud bastard. I’m offering four billion won and all rights to the byproducts, and you’re refusing?”

“Get lost… Wait. What did you just say?”

Had I heard him wrong?

All kinds of thoughts raced through my mind. Only after sorting them out could I finally part my lips.

“How much? Four billion won?”

“Didn’t I say? Five big bills.”

…

“Then… five hundred million per Minotaur?”

*You should’ve said five fucking huge bills.*

Four billion won.

The mind-boggling sum left not only me, but Song Song and Im Kkeokjeong, gaping.

*What the hell, is this guy made of money?*

He was the team leader of a mid-sized Guild and a B-rank Hunter, so he probably earned a lot.

But casually offering billions of won like this was absurd.

“You’re just giving me four billion?”

“Just? That won’t do. This is a bet.”

“What kind of bet?”

“I need something to gain, too.”

The corners of Im Changsoo’s lips curled.

“If you die or run away, all the rewards promised so far are void. On top of that…”

His head slowly turned.

His gaze stopped on one person.

“Me?”

“Yes. I’d like to invite Miss Song to join our Guild.”

Im Changsoo bowed politely.

The sudden change in attitude was so different from how he had acted until now that it was downright creepy.

“Ugh, that’s giving me goose bumps. Just act the way you were. It looks much better than putting on a fake act.”

…

…

Song Song had an honest personality.

She shuddered, as if she really had gotten goose bumps, and folded her arms.

“Shit Changsoo—no, Im Changsoo, right?”

“…Yes.”

“Okay. I’ll be blunt. You’re not my type.”

Her blunt declaration came in like a 160-kilometer-per-hour fastball, tight and inside. Im Changsoo’s gaze wavered.

“You’re tall and handsome, but you look exactly like you’d cheat. I hate wind, you see.[^1] I finally got my hair looking nice, and if it gets mussed up… Ah, no, that’s not what I mean, is it?”

“Y-yes? Yes?”

“Anyway, you’re not my type. I absolutely can’t stand womanizers who flaunt their money.”

I had never seen Im Changsoo look so dumbfounded.

To anyone else, I probably had the same expression right now.

“Oh, that look you just had was kind of okay. But I’ve been watching you for a while, and your personality is kind of… You can tell that yourself, can’t you?”

Im Changsoo barely managed to compose his expression before answering.

“We can work those things out one by one.”

“Do you really have to taste something to know whether it’s shit or soybean paste? You don’t seem interested in anything but bumping bellies with me. Am I right?”

“……!”

“……!”

Everyone, myself included, was left gaping.

As if bashful, she toyed with her hair while delivering one line after another, each blow landing like a nuclear bomb.

“It’s not like I particularly dislike Sangdong Guild.”

Im Changsoo, who had been taking hit after hit without a break, brightened and asked:

“Really?”

“Yes. I can always switch again anyway.”

…

*Miss Song, are you a genius?*

After delivering a massive fuck-you with an innocent expression, Song Song continued.

“But I’d need to ask permission before switching Guilds. Right, Guild Master?”

“Ah, of course.”

Butler Kim had been watching with an interested look in his eyes. Song Song turned toward him.

“Team Leader, what do you think?”

“What do you mean? About Song Song switching Guilds?”

“If we lose this bet, that’s what will happen, right?”

Team Leader Choi calmly nodded.

“Go ahead.”

“Isn’t that a little too easy an answer?”

“I answered easily because it was an easy question.”

For just a moment, I thought I saw hurt in Song Song’s eyes.

*No, surely not.*

The emotion had passed too quickly for me to be certain.

Returning to her frank, easygoing self, Song Song turned to Im Changsoo and said:

“Then I’m in on the bet. What about you, Mr. Taekyung?”

“I…”

My deliberation wasn’t short.

From the moment I first heard Team Leader Choi’s question, a strange certainty had already taken root deep in my heart.

The certainty that I was stronger than those bastards.

“I’ll take the bet.”

A smile spread across Team Leader Choi’s lips.

“I’ll join in, too. A bet is more fun when the stakes are high, isn’t it?”

“Wow, look at you, a proper gambler. How much?”

“Four billion won. Of course, I’m betting that Jin Taekyung will take down all eight.”

“What?”

Im Changsoo stared at Team Leader Choi for a moment, then let out a short laugh.

“You’re an interesting bunch. One of you is desperate to get himself killed, and the other is dying to throw away his money.”

“So what’s your answer?”

“Obviously, yes.”

“Should we write up a contract?”

“A contract? What do you take me for? I keep my word once I’ve given it. You don’t have to keep yours. I’ll make you keep it. Everyone, move back!”

The enormous, damp cavern transformed into a Colosseum.

An arena with an absurd amount of money at stake.

I was the gladiator who had to fight the Minotaur herd.

“Team Leader Choi. What will you do if I lose?”

“You will win.”

Where did this confidence come from?

Faith in himself? Or in what he’d seen of me so far?

It didn’t matter.

I would simply do my best to achieve my goal.

*Boom-boom-boom-boom-boom!*

—Moooooo!

Twenty meters ahead, I could see each of them clearly.

Hot breath steaming from their nostrils. Heat. Muscles. Weapons held high.

*This is my first time fighting a cow.*

It should be an interesting experience.

I gripped my spear and charged at the herd like a matador.

[^1]: The Korean word *baram* can mean either “wind” or an affair, making her next line a deliberate pun.
```
