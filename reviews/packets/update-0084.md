<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0084.txt",
      "sha256": "9831007c132f8ac2853ef5beb447cdb3ea78471cd46c834e48441405701c5135",
      "bytes": 12739
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bc56f27ba0a2f67bd238dc10b365046c9361cec1f6722472e237d5898c6fef12",
      "bytes": 7561
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "cfa2656abf30e13073b69e0d32d02f168419161ac9d13965eb24d1c3ac05b669",
      "bytes": 7421
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "c93846f2f8b9a335da08614997a609385184ae57c6e42087fef8bd2896982f06",
      "bytes": 1608
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4e5dec4d6eac675cfaf452cd15eb5a8bc6972adbd0d7031da4a25789d84e7f80",
      "bytes": 1220
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ea608617cad712e4d70ccc28c105da08ff0ee31b03f70e44e2fe09b8e7dc464e",
      "bytes": 23807
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c89bfd0acb3f2c54c70c6efaecf3012a0949b6eff5dbc93e7754c18ea633f24e",
      "bytes": 6783
    }
  ],
  "estimated_tokens": 13466
}
-->

# Durable State Update — Chapter 84

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 84. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 84. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 84,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 84,
    "continuity_sources": [84],
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
    "Sangdong Guild and Peace Guild entered The Minotaur’s Labyrinth as a fifteen-person team with seven B-rank Hunters; Im Kkeokjeong was registered as an E-rank tank, and Taekyung received the restricted B-rank Gate Clear Quest. Taekyung is both a Hunter and a martial artist, and Choi has noticed that his behavior is inconsistent with an ordinary C-rank Hunter.",
    "Im Changsoo is the Sangdong Guild Master’s son, behaves abusively toward his team, maintains a sponsorship relationship with the C-rank mage Hye-rin, and is Level 65. Eight Minotaurs approached, causing his team members to retreat while Im Kkeokjeong remained positioned as the front-line tank.",
    "Im Changsoo offered Taekyung a wager to defeat the eight Minotaurs alone for 500 million won per monster, all byproduct rights, and a possible transfer of Song Song to Sangdong Guild. Taekyung accepted, Choi backed him with 4 billion won, and Taekyung charged the herd."
  ],
  "continuity_sources": [
    83
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed, as does any connection between the attack and Song Sword Sect.",
    "It remains unresolved whether Hyuk Mujin will become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung’s summons and whether he will become Alliance Leader.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung’s prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim’s former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung’s interrupted confession.",
    "Whether Taekyung defeats all eight Minotaurs and what consequences follow from the wager, including Song Song’s possible Guild transfer, remains unresolved."
  ],
  "safe_through": 83,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung’s deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year’s Day for 원단 and close the sect’s gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Render fist-and-kicking technique as 권각술, recognition as 인정, Falling Flow Sword as 낙류검, Twelve Gale Fists as 질풍십이권, Flame Divine Palm as 화염신장, and Tendon-Splitting and Bone-Twisting as 분근착골.",
    "Use Reformation Fist, Toughness, Heavenly Martial Physique, Jang Childeuk, Martial Artist Jang, benevolence/righteousness/propriety/wisdom, killed by a tiger, fifteen minutes, lifelong single, Let’s eat noodles, Squad Leader, Third Young Master, Designer-Brand Junkie, Qi Sense, Peace Guild, Essence of the Himalayas, Sooni’s Super, Song Song, Miss Song, Taurus, Ares Guild, Senior, Young Master, Guild Master, Minotaur, Bucheon Terminal Guild, The Minotaur’s Labyrinth, and Shit Changsoo as established.",
    "Use Sangdong Guild, Hunter Association, Black Drake, Masterwork Black Drake Leather Set, Masterwork Black Thorn Spear, Bleeding, artifact, gear advantage, Hye-rin, Cheongdam-dong, Matador’s Full-Body Armor, Matador’s Shield, Taunt, Hallucination, Minotaur Warrior, Top-tier, tongue-pulling hell, big bills, and the baram wind/infidelity pun as established terminology or translation choices."
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
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 임창수    | **Im Changsoo**   |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 임꺽정 | **Im Kkeokjeong** |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 83
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 74
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 83
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃84화



임꺽정은 생각했다.

‘미친 짓이야.’

진태경은 C급 헌터다. 반면 미노타우로스는 B급 몬스터.

게다가 한 마리도 아니고 여덟 마리나 된다. 그의 눈에 비친 상황은 무모함을 넘어 절망적이었다.

‘그깟 돈이 뭐라고.’

40억은 분명 인생을 바꿀 수 있을 만한 금액이지만 목숨을 버릴 정도는 아니다. 임창수는 돈으로 진태경의 눈을 가렸고, 진태경은 판단력을 상실했다.

‘내가, 내가 말려야 돼.’

저 악랄한 상동 길드 놈들도, 말리지 않는 김 집사도, 최 팀장도 전부 미쳤다. 아끼는 동생의 개죽음만큼은 막아야 했다.

“태경아!”

임꺽정이 막 창을 꼬나 쥔 진태경을 향해 손을 뻗으려던 그 순간이었다.

쉭-

“……어?”

바람 소리와 함께 진태경이 사라졌다. E급 헌터인 임꺽정은 닿을 수도, 제대로 볼 수도 없는 속도로 질주를 시작했다.

눈 깜짝할 사이에 벌어진 일. 임꺽정은 얼빠진 음성을 토해 냈다.

“어, 어어.”

이게 뭐지? 무슨 일이 벌어지고 있는 거지? 태경이가 저 정도였나? 아니, C급 헌터가 이렇게 빠를 수가 있나?

쉬이이익!

검은 번개가 동굴을 가로지른다. 한 걸음, 두 걸음, 세 걸음.

수십 미터의 거리가 단숨에 좁혀진 건 찰나에 불과했고 창날이 번쩍 빛났다.

쐐애애액! 서걱!

미노타우로스. 3미터가 넘는 놈의 거체가 기우뚱거린다.

어깨 위로 있어야 할 굵은 목은 이미 그 자리에 없었다.

인간의 몸과 소의 머리를 한 반인반수가 지금 이 순간만큼은 그저 평범한 인간 같다는 착각이 들었다.

툭.

순식간에 베인 머리가 동굴 바닥에 떨어지고.

쿵.

머리를 잃은 몬스터의 신형이 허물어진다. 깔끔하게 잘려 나간 목의 단면에서 핏물이 왈칵 쏟아졌다.

“이게 무슨……!”

누군가가 토해 낸 목소리가 모두의 마음을 대변한다.

보이지 않는 충격과 경악 속에서, 한 사람이 씩 웃었다.

“할 만한데?”

그 한마디가 결정타다.

임꺽정은 다리에 힘이 풀렸고, 임창수는 저도 모르게 중얼거렸다.

“시발…… 내 40억.”



* * *



미노타우로스는 근접 전투에 특화된 체형이다.

중형 몬스터답게 거구인 데다 엄청나게 단단한 근육으로 똘똘 뭉쳐 있고, 사용하는 무기도 메이스나 도끼 같은 중병기다.

콰쾅!

그러면 뭐 해. 못 맞추면 말짱 황인데.

있는 힘껏 휘둘러 봤자 애꿎은 동굴 바닥만 박살 낼 뿐이다.

‘힘 하나는 인정.’

하지만 싸움은 힘만으로 하는 게 아니다. 나는 한 놈의 품 안으로 파고들며 아랫배를 찔렀다.

푸푹.



- 정확한 공격!

- 상태 이상, [출혈]이 발동됩니다!



- 모오오오.

미노타우로스의 울음소리가 애처롭다. 처음처럼 광포하게 달려들기에는 이미 너무 많은 피를 흘렸다. 아마 조금 전의 그 공격이 마지막 힘을 쥐어짠 일격이었을 것이다.

- 모오, 모오오.

비틀거리며 뒷걸음질 치는 녀석에게로 다가갔다. 송아지 같은 눈망울을 보니 마음이 약해……지기는 개뿔, 이게 다 5억짜리 돈다발로 보인다.

“다음 생에는 부디 강원도 횡성에서 태어나라.”

- 모오오!

서걱.

미노타우로스의 숨이 끊겼다. 거대한 피 웅덩이가 여덟 개. 몬스터 사체도 여덟 구로 늘어난 순간이었다.

띠링.



- 레벨 업!



경쾌한 시스템 알림은 영화 BGM이고, 이 영화의 진짜 백미는 따로 있다. 나는 활짝 웃으며 돌아섰다.

“자, 즐거운 정산 시간.”

경악과 침묵에 휩싸여 있는 사람들 중 유독 한 사람이 눈에 띄었다.

나는 반쯤 얼어붙은 임창수가 들을 수 있도록 큰 소리로 정산을 시작했다.

“보자, 일단 두당 5억이니까…….”

움찔.

“하나, 둘, 셋, 넷. 여덟 마리. 도합 40억. 와, 몇 마리는 마정석도 떨궜네? 부산물도 다 내 거랬지?”

움찔. 움찔.

“창수야. 왜 대답이 없니? 설마 나한테 거짓말 친 거니?”

임창수가 어색한 미소를 지었다.

“당연히 아니지.”

“말이 짧다.”

“그럴 리가 있겠습니까. 저는 그냥…….”

“그냥. 뭐?”

“태경 씨. 잠시만 제 얘기를…….”

“태경 씨? 아까부터 물어보고 싶었는데 우리 창수 몇 살?”

“……스물다섯 살입니다.”

“어이구. 요, 요 잔망스러운 새끼. 스물다섯밖에 안 됐으면서 어른들한테 그렇게 싸가지 없게 군 거야?”

“…….”

“아까부터 혓바닥이 반 토막이 났나, 반말 찍찍 하길래 아흔다섯은 되는 줄 알았네. 얼굴은 왜 이렇게 삭았냐? 출생 신고 늦게 한 거 아니지?”

계속 이어지는 내 말에 임창수의 얼굴이 분노로 벌겋게 달아올랐다.

“표정 관리 잘하자. 한 번만 더 홍익인간 되면 진짜 빨갛게 만들어 준다.”

“……죄송합니다.”

가까스로 표정 관리에 성공한 녀석이 조심스럽게 입을 열었다.

“저어, 하나만 여쭤봐도 되겠습니까?”

“여쭤봐.”

“정말 C급 헌터 맞으신지…….”

“응. 맞는데?”

임창수는 불신에 찬 눈빛으로 나와 널브러진 미노타우로스 사체를 번갈아 바라봤다.

“뭐, 왜.”

“꼭 밝히고 싶지 않으시면 말씀 안 해 주셔도 됩니다.”

“그건 뭐 알아서 생각하고.”

“아, 아닙니다.”

말은 아니라고 했지만 머릿속으로는 상상의 나래를 펼치고 있는 게 분명하다. 평범한 C급 헌터라고 생각했던 내가 B급 몬스터를, 그것도 여덟 마리를 정면 승부로 발라 버렸으니까.

‘그래, 많이 상상해라.’

괜히 상동 길드랑 틀어져 봤자 좋을 게 없다. 저쪽에서 이렇게 알아서 숙여 주니 그냥 고마울 따름이다.

“그럼 혹시 신분 세탁…… 아니시죠. 아니시겠죠. 네.”

헛소리를 지껄이려던 임창수가 내 창을 곁눈질하더니 바로 말을 돌린다. 이거 은근히 반응 재밌네.

“그래서?”

“예?”

“예는 무슨. 돈 줘야지. 40억.”

사실 배 째라 식으로 나올까 봐 살짝 걱정이다.

40억이 뉘 집 개 이름도 아니고, 일반인들은 평생 벌어도 만져 보기 힘든 거금 아닌가.

하지만 임창수는 달랐다.

“아, 물론 드려야죠.”

“……확실해?”

“예. 약속은 지킵니다.”

너무 시원시원한 대답이라 의심이 갈 정도다.

제아무리 B급 헌터라고 해도 평균 수입이라는 게 있는데, 임창수는 수십억을 주머니 속 천 원처럼 말한다.

“이렇게 말해 놓고 잠수 타는 거 아니지? 계약서 없다고 쌩 까고 그러면 나 많이 섭섭하다.”

은근슬쩍 창을 쓰다듬자 녀석이 화들짝 놀란다.

“절대, 절대 아닙니다. 그 정도 능력은 충분히 됩니다.”

“흐음. 돈 좀 버나 보네. 상동 길드에서 대우 잘해 주나 봐?”

“아뇨. 남들이랑 다를 것도 없습니다.”

“당연히 다를 게 없겠지. 네가 무슨 길드장 아들이라도 되냐? 뭐 잘났다고 잘해 줘?”

“…….”

“……?”

“…….”

이거 뭔가 공기가 묘한데.

나는 곰곰이 생각하다가 물었다.

“아버님 성함이?”

“임, 춘 자에 수 자 쓰십니다.”

“상동 길드장님 성함은?”

“임, 춘 자에 수 자 쓰십니다.”

기묘한 우연이다. 임창수의 아버지와 상동 길드장의 이름이 같다니. 하긴, 세상은 넓고 동명이인은 많은 법이니까.

“야, 이건 혹시나 해서 물어보는 건데…… 실례지만 아버님 직업이 어떻게 되시냐?”

“헌터신데요.”

“그냥 헌터?”

“길드 운영하고 계십니다.”

“아, 그래.”

이 자식 상동 길드장 아들이었구나.

짧은 침묵이 흘렀고, 그 잠깐 사이 나는 임창수에게 느꼈던 낯익음의 정체를 깨달았다.

“네가 걔야?”

“개요?”

“아니, 너에 대해 들어 본 적이 있어서.”

재작년 이맘때쯤인가, 한 귀로 듣고 한 귀로 흘렸던 이야기다. 상동 길드장의 하나뿐인 늦둥이 아들이 B급 헌터로 각성, 아버지 길드에서 한자리 꿰찼는데 여자를 그렇게 밝혀서 골칫거리라더라.

그래서 붙여진 별명이…….

“껄떡쇠. 맞지?”

임창수는 고개를 푹 숙이는 것으로 대답을 대신했다.

하긴 사람들 앞에서 듣기에는 쪽팔린 별명이긴 하다. 하지만 40억을 수금해야 하는 나는 따뜻한 목소리로 녀석을 위로했다.

“괜찮아, 인마. 남자가 그럴 수도 있지. 나도 전에는 너처럼 사는 게 꿈이었어.”

하지만 현실은 냉혹한 법이었고, 꿈은 100TB USB로 스며들었다. 야동계의 이름난 권위자인 진호 형은 내 USB를 빌려 간 후, 퀭한 얼굴로 나타나 한 줄 평을 남기기도 했다.



‘이건 유네스코 세계 문화유산에 지정되어야 한다.’



뭐 어쨌든.

내 따뜻한 위로에 임창수가 고개를 들었다.

“정말이십니까?”

당연히 아니지. 내가 아무 여자한테나 들이대는 그런 놈으로 보이니? 나야말로 이 시대의 해바라기. 오직 송이 씨 한 사람만 바라보는…….

잠깐만, 이 새끼 아까 전에 송이 씨한테 집적거렸잖아.

“이 자식이.”

“헉!”

지레 겁을 먹은 임창수가 반사적으로 검 자루에 손을 올렸다.

스릉. 탁.

그러나 검날은 채 반도 빠져나오지 못하고 도로 모습을 감출 수밖에 없었다. 번개처럼 다가간 내가 놈의 검 자루를 내리누름과 동시에 다리를 걷어찼기 때문이다.

쿠당탕!

중심을 잃고 넘어진 녀석의 목을 지그시 누르자 안색이 하얗게 질린다.

“컥, 커컥!”

“이 새끼가. 어디서 연장을 꺼내?”

진무경에게 얻어맞으면서 배운 보람이 있다. 예전 같았으면 지금처럼 간단히, 부드러운 동작으로 B급 헌터를 제압할 수는 없었을 텐데. 임창수도 놀랐겠지만 내가 더 놀랐다.

“여기 게이트야, 인마. 아까 네가 했던 말인데 벌써 잊었어?”

“죄, 죄송합니다!”

마음 같아서는 흠씬 두들겨 패 주고 싶지만 미수에 그쳤으니 봐주기로 했다. 40억을 못 받아서 그런 게 절대 아니다.

“위자료.”

“컥. 네?”

“검 뽑았잖아. 살인미수 몰라? 거기에 나랑 송이 씨. 아니지, 우리 길드원들 모두에게 정중한 사과.”

“그게 무슨!”

임창수가 억울한 눈빛으로 사람들을 바라봤지만 도움의 손길은 없었다.

임창수의 팀원들은 내 눈이 닿기만 해도 찔끔 물러날 뿐이었고, 오히려 구경하고 있던 우리 길드원들은 한 술 더 떴다.

“협력 길드의 길드원을 상대로 검을 뽑다니. 이것 참.”

안타깝다는 듯 혀를 차는 김 집사.

“돈 주기 싫어서 그런 거 아니에요? 세상에, 창수 씨 너무 저질이다. 안 그래요, 아저씨?”

“응? 으응. 젊은 친구가 아주 악질이네!”

송이 씨와 임꺽정의 저질, 악질 콤보에 이어서.

“자, 다들 제 투구를 봐 주시겠습니까? 이 제품은 핀란드의 유명한 장비 제작사 자일리톤에서 제작한 맞춤 투구로서…… 온갖 기능이 있지만 가장 중요한 영상 녹화 마법이 걸려 있습니다.”

최 팀장의 마지막 한 방까지.

배신감과 황당함에 입을 딱 벌리고 사람들을 바라보던 임창수가 한숨을 푹 내쉬었다.

“하겠습니다.”

“뭐라고?”

“시키는 대로 다 한다고요!”

기다리던 대답이다.

나는 기쁜 마음으로 녀석을 일으켜 세워 주었다.

“자식, 잘 생각했다. 위자료는 천천히 논의해 보자.”

“……미치겠네. 우리 꼰대가 알면 저 죽어요.”

“여기서 죽을래?”

“40억 받기 싫으세요?”

“어쭈.”

다시 한숨을 푹 내쉰 임창수가 입을 열었다.

“질문 하나만 해도 됩니까?”

“하나당 1억.”

“…….”

“농담이야. 해 봐.”

“진짜 뭐 하시는 분입니까?”

그게 그렇게 궁금했나?

나는 피식 웃으며 대답해 주었다.

“투잡 뛰는 사람.”

헌터 겸 무림인.

이 세상에 하나뿐인 투잡이다.
```

## Final English reading copy

```markdown
# Chapter 84

Im Kkeokjeong thought.

*This is insane.*

Jin Taekyung was a C-rank Hunter. A Minotaur, on the other hand, was a B-rank monster.

And there wasn’t just one of them. There were eight. To Im Kkeokjeong, the situation looked like more than recklessness. It looked hopeless.

*What the hell does money matter?*

Four billion won was certainly enough to change a person’s life, but it wasn’t worth throwing away one’s life for. Im Changsoo had blinded Jin Taekyung with money, and Taekyung had lost his ability to think clearly.

*I have to stop him. I have to.*

Those vicious bastards from Sangdong Guild, Butler Kim for not stopping him, even Team Leader Choi—they were all insane. He had to prevent his cherished little brother from throwing his life away like a stray dog.

“Taekyung!”

It was at that very moment, when Im Kkeokjeong reached out toward Jin Taekyung, who had just gripped his spear at the ready.

Whoosh—

“…Huh?”

Along with the sound of wind, Jin Taekyung vanished. Jin Taekyung began sprinting at a speed that Im Kkeokjeong, an E-rank Hunter, could neither match nor properly see.

It had all happened in the blink of an eye. Im Kkeokjeong let out a dazed sound.

“Uh, uh-oh.”

What was this? What was happening? Had Taekyung always been this strong? No, wait. Could a C-rank Hunter really move that fast?

Whoooooosh!

A black bolt of lightning shot across the cavern.

One step. Two steps. Three steps.

The distance of several dozen meters vanished in an instant, and the spearhead flashed.

Swoooosh! Slice!

The Minotaur—the over-three-meter-tall monster’s enormous body tilted to one side.

The thick neck that should have been above its shoulders was already gone.

For one moment, it seemed as if the half-human, half-beast creature with a human body and a bull’s head were nothing more than an ordinary person.

Thump.

The head that had been severed in an instant dropped to the cavern floor.

Crash.

The headless monster collapsed. Blood burst from the cleanly severed cross-section of its neck.

“What the…!”

Someone’s voice spoke for everyone’s thoughts.

Amid the invisible shock and stunned disbelief, one person grinned.

“This is doable.”

That one remark delivered the final blow.

Im Kkeokjeong’s legs gave out, and Im Changsoo muttered without realizing it.

“Fuck… my four billion.”

* * *

Minotaurs had bodies specialized for close-quarters combat.

Like any mid-sized monster, they were huge, packed with incredibly dense muscles, and armed with heavy weapons such as maces and axes.

Boom!

But what good was that? If they couldn’t hit anything, it was all for nothing.

No matter how hard they swung, all they could do was smash the innocent cavern floor.

*I’ll give them one thing—their strength is impressive.*

But fights weren’t won with strength alone. I slipped inside one monster’s guard and stabbed it in the lower abdomen.

Squish.

> **System**
>
> **Precise Attack!**
>
> **Status Effect: Bleeding activated!**

—Mooooo.

The Minotaur’s cry was pitiful. It had already lost too much blood to charge in as ferociously as before. The attack it had launched moments ago had probably squeezed out the last of its strength.

—Moo. Mooooo.

I approached the creature as it staggered backward.

Looking into its calf-like eyes almost made me feel sorry for it…

*Like hell.*

All I could see was a stack of five hundred million won.

“In your next life, please be born in Hoengseong, Gangwon Province.”

—Mooooo!

Slice.

The Minotaur’s breathing stopped.

A moment later, there were eight enormous pools of blood.

And eight monster corpses.

Ding.

> **System**
>
> **Level Up!**

The cheerful System notification was the movie’s background music. The real highlight of the movie was something else entirely.

I turned around with a wide smile.

“Now, for the fun part—the settlement.”

Among the people engulfed in shock and silence, one person stood out in particular.

I began settling the accounts loudly enough for the half-frozen Im Changsoo to hear.

“Let’s see. Five hundred million per head to start with…”

He flinched.

“One, two, three, four… Eight of them. Four billion in total. Wow, a few of them even dropped Magic Gems. You said all the byproducts were mine, too, right?”

He flinched again. And again.

“Changsoo. Why aren’t you answering? Don’t tell me you lied to me.”

Im Changsoo forced an awkward smile.

“Of course not.”

“Watch your tone.”

“How could that possibly be the case? I was just…”

“Just what?”

“Mr. Taekyung. If you could just listen to me for a moment…”

“Mr. Taekyung? I’ve been meaning to ask you this for a while. How old is our Changsoo?”

“…I’m twenty-five.”

“Oh, my. What a cheeky little shit. You’re only twenty-five, and you’ve been acting so disrespectfully toward your elders?”

“…”

“What happened to your tongue? You kept spitting out casual speech, so I thought you were ninety-five. Why does your face look so weathered? You didn’t just register your birth late, did you?”

As I kept going, Im Changsoo’s face grew bright red with anger.

“Keep that expression under control. If you turn into a Hongik Ingan one more time, I’ll make you genuinely red.”[^1]

“I’m… sorry.”

After barely managing to compose his expression, he cautiously opened his mouth.

“Um, may I ask you one thing?”

“Ask.”

“Are you really a C-rank Hunter…?”

“Yeah. I am.”

Im Changsoo looked at me and the sprawled-out Minotaur corpses in turn, his eyes filled with disbelief.

“What? Why?”

“If you’d rather not reveal it, you don’t have to tell me.”

“Just think whatever you want.”

“Oh, no. That’s not what I meant.”

He said it wasn’t, but there was no doubt he was letting his imagination run wild.

He had thought I was an ordinary C-rank Hunter, yet I had just beaten eight B-rank monsters in a head-on fight.

*That’s right. Imagine away.*

There was nothing to gain from antagonizing Sangdong Guild for no reason. Since they were bowing their heads on their own, I was simply grateful.

“So, perhaps you’re laundering your identity—no, you aren’t. You wouldn’t be. Right.”

Im Changsoo had been about to spout some nonsense, but he glanced sideways at my spear and immediately changed the subject.

This guy’s reactions were kind of fun.

“So?”

“Pardon?”

“Don’t ‘pardon’ me. You have to pay me. Four billion.”

To be honest, I was a little worried that he might tell me to go to hell.

Four billion won wasn’t some random dog’s name. It was a huge sum of money that ordinary people could hardly hope to lay their hands on even after working their entire lives.

But Im Changsoo was different.

“Ah, of course I’ll pay you.”

“…Are you sure?”

“Yes. I keep my promises.”

His answer was so straightforward that it was almost suspicious.

No matter how much money a B-rank Hunter made, there was such a thing as an average income. Yet Im Changsoo talked about billions of won as casually as if it were a thousand-won bill in his pocket.

“You’re not going to disappear after saying that, are you? If you act like none of this matters because there’s no contract, I’ll be very disappointed.”

I casually stroked my spear, and he flinched violently.

“Absolutely not. Absolutely not. I can easily afford that.”

“Hmm. You must make pretty good money. Sangdong Guild treats you well?”

“No. There’s nothing particularly different about my treatment.”

“Of course there isn’t. It’s not like you’re the Guild Master’s son or something. Why would they treat you especially well?”

“…”

“…?”

“…”

Something about the atmosphere felt strange.

I thought about it carefully before asking:

“What’s your father’s name?”

“Im Chunsu.”

“What’s the Sangdong Guild Master’s name?”

“Im Chunsu.”

What a strange coincidence. Im Changsoo’s father and the Sangdong Guild Master had the same name.

Then again, the world was a big place, and there were plenty of people with the same name.

“Hey, I’m only asking just in case, so forgive me for prying…but what does your father do for a living?”

“He’s a Hunter.”

“Just a Hunter?”

“He runs a Guild.”

“Oh, I see.”

This bastard was the Sangdong Guild Master’s son.

A brief silence passed, and in that short interval, I realized what had seemed so familiar about Im Changsoo.

“Are you that guy?”

“A dog?”

“No, I’ve heard about you before.”

It was a story I had heard around this time the year before last and let pass in one ear and out the other.

The Sangdong Guild Master’s only late-born son had awakened as a B-rank Hunter and secured a position in his father’s Guild. But he was such a womanizer that he was apparently a constant headache.

And the nickname he had earned was…

“Horndog. Right?”

Im Changsoo answered by lowering his head.

It was an embarrassing nickname to hear in front of other people, to be sure.

But since I had to collect four billion won, I comforted him in a warm voice.

“It’s okay, man. Guys can be like that sometimes. I used to dream of living like you, too.”

But reality was cold, and that dream seeped into a 100-terabyte USB drive.

Jinho hyung, a renowned authority in the world of adult videos, once borrowed my USB. When he returned, he had a hollow-eyed expression and left me with a one-line review.

*This should be designated a UNESCO World Heritage Site.*

Anyway.

Im Changsoo lifted his head at my warm consolation.

“Really?”

*Of course not.*

Did I look like the kind of guy who hit on just any woman? I was the sunflower of this era, gazing at only one person in the entire world—Miss Song…

*Wait a second.*

This bastard had hit on Miss Song earlier.

“You little shit.”

“Gasp!”

Im Changsoo, frightened before I had even done anything, reflexively placed his hand on his sword hilt.

Shing. Clack.

But the blade had barely made it halfway out before it was forced back into its sheath.

I had moved like lightning, pressing down on his sword hilt while kicking his legs out from under him.

Crash!

When I pressed down on the neck of the man who had lost his balance and fallen, his face went white.

“Ghk! Cough!”

“You little bastard. Where do you get off pulling that thing on me?”

Getting beaten by Jin Mukyung had certainly paid off.

In the past, I wouldn’t have been able to subdue a B-rank Hunter with such a simple, fluid movement. Im Changsoo was probably surprised, but I was even more surprised.

“This is a Gate, you idiot. You already said that yourself. Did you forget so soon?”

“I’m sorry! I’m sorry!”

I wanted to beat him senseless, but since it had only been an attempt, I decided to let him off.

*It absolutely wasn’t because I hadn’t received the four billion yet.*

“Damages.”

“Ghk. What?”

“You drew your sword. Don’t you know that’s attempted murder? And you owe me and Miss Song—no, all our Guild members—a sincere apology.”

“What are you talking about?”

Im Changsoo looked around at the others with an aggrieved expression, but no one came to his aid.

His team members only shrank back whenever my eyes landed on them. Meanwhile, our Guild members, who had been watching the spectacle, took it one step further.

“Drawing a sword on a member of an allied Guild. Well, I never.”

Butler Kim clicked his tongue as if he felt sorry for him.

“You’re only doing this because you don’t want to pay, aren’t you? My goodness, Changsoo, that’s so low. Isn’t it, Uncle?”

“Hmm? Uh-huh. What a nasty young man!”

That was Miss Song and Im Kkeokjeong’s lowlife-and-nasty-man combo.

And then Team Leader Choi delivered the final blow.

“Now, would everyone take a look at my helmet? This product is a custom-made helmet produced by Xyliton, a famous Finnish equipment manufacturer. It has all sorts of functions, but most importantly, it has been enchanted with a video-recording spell…”

Im Changsoo stared at everyone with his mouth hanging open, betrayed and utterly dumbfounded. Then he let out a long sigh.

“I’ll do it.”

“What did you say?”

“I said I’ll do everything you tell me to!”

That was the answer I had been waiting for.

I happily helped him back to his feet.

“Good choice, kid. We can discuss the damages slowly.”

“…This is driving me crazy. If my old man finds out, I’m dead.”

“Would you rather die here?”

“You don’t want the four billion?”

“You’ve got some nerve.”

Im Changsoo let out another deep sigh before opening his mouth.

“May I ask one question?”

“One hundred million per question.”

“…”

“I’m kidding. Go ahead.”

“What do you really do?”

Was he really that curious?

I let out a quiet laugh and answered him.

“Someone with two jobs.”

A Hunter and a Murim martial artist.

The only two-job combination in the world.

[^1]: *Hongik Ingan*, meaning “to broadly benefit humanity,” is a Korean national founding ideal. Taekyung twists the phrase into a joke about Im Changsoo’s reddening face.
```
