<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0085.txt",
      "sha256": "12622fdcc08c631aee61ab9a081c012f231b238e5e7af889b1de938b366cf58e",
      "bytes": 13004
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "84d5b6b8028b09d15830447c59e6e80298619a4ec0b3cb4d015b8b9cd78c02ed",
      "bytes": 7663
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d4699f35114192039de660f0e9231f0f2ed8b33744eedfe3dda64268676f043c",
      "bytes": 7884
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9b2e7ea628d051c221a428c97250c035320909780200f8bd8e2434cd14aba715",
      "bytes": 5010
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "19a7fd1ff0fe1fa3387c296c43734a8232973d18cb7fa2ae05fb8bc731a71da9",
      "bytes": 1608
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "48f9a6ef24954237952b9e4e2ecc8894db9e889eed6b698341d5cf15f8d77e9d",
      "bytes": 23843
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "fb2cafe532c1359e0ed7773b06f1fb11de87f7e63fd4cfc5f7895b34aca8588d",
      "bytes": 524
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "f6f2abd264d6d5526cd28b5ee5c9822fe4f651568f4ba84307646803f019077d",
      "bytes": 3852
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1ca7a8224faf0cdc1914e2179bf2e9922360944aba454a27f766b1df68ff62f5",
      "bytes": 7127
    }
  ],
  "estimated_tokens": 14100
}
-->

# Durable State Update — Chapter 85

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 85. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 85. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 85,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 85,
    "continuity_sources": [85],
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
    "Taekyung defeated all eight Minotaurs, received a Level Up, and established that Changsoo owes him 4 billion won and all byproducts. Changsoo is the Sangdong Guild Master’s son, is nicknamed Horndog, agreed to pay and apologize after drawing his sword, and learned that Taekyung works as both a Hunter and a Murim martial artist."
  ],
  "continuity_sources": [
    84
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed, as does any connection between the attack and Song Sword Sect.",
    "It remains unresolved whether Hyuk Mujin will become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung’s summons and whether he will become Alliance Leader.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung’s prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim’s former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung’s interrupted confession.",
    "Whether Im Changsoo fulfills his promised payment, surrenders the byproducts, and gives the demanded apology and damages remains unresolved."
  ],
  "safe_through": 84,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung’s deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year’s Day for 원단 and close the sect’s gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Render fist-and-kicking technique as 권각술, recognition as 인정, Falling Flow Sword as 낙류검, Twelve Gale Fists as 질풍십이권, Flame Divine Palm as 화염신장, and Tendon-Splitting and Bone-Twisting as 분근착골.",
    "Use Reformation Fist, Toughness, Heavenly Martial Physique, Jang Childeuk, Martial Artist Jang, benevolence/righteousness/propriety/wisdom, killed by a tiger, fifteen minutes, lifelong single, Let’s eat noodles, Squad Leader, Third Young Master, Designer-Brand Junkie, Qi Sense, Peace Guild, Essence of the Himalayas, Sooni’s Super, Song Song, Miss Song, Taurus, Ares Guild, Senior, Young Master, Guild Master, Minotaur, Bucheon Terminal Guild, The Minotaur’s Labyrinth, and Shit Changsoo as established.",
    "Use Sangdong Guild, Hunter Association, Black Drake, Masterwork Black Drake Leather Set, Masterwork Black Thorn Spear, Bleeding, artifact, gear advantage, Hye-rin, Cheongdam-dong, Matador’s Full-Body Armor, Matador’s Shield, Taunt, Hallucination, Minotaur Warrior, Top-tier, tongue-pulling hell, big bills, baram wind/infidelity pun, Horndog, Hoengseong, Gangwon Province, Xyliton, and Hongik Ingan as established terminology or translation choices."
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
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |

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
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 임창수    | **Im Changsoo**   |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
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
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 미노타우로스 | **Minotaur** | B-rank monster species. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 74
- **Aliases:** None revealed
- **Role:** Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 84
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 84
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 83
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 83
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Former Ares Guild Team Leader; reawakened Hunter publicly classified as C-rank; leader and employer of Team 1, the Peace Guild’s E-rank Gate party
- **Personality:** Calm, observant, practical, and decisive under pressure
- **Voice:** Polite and measured in ordinary conversation; clipped and commanding during combat
- **Relationships:** Hires Jin Taekyung as a porter and leads him, Im Kkeokjeong, and three veteran E-rank Hunters through an E-rank Gate

## Korean source

```text
＃85화



“형. 괜찮으세요?”

“안 다치셨어요?”

팀원들의 말에 임창수가 이를 악물었다.

“입 닥쳐, 이 새끼들아. 그동안 내가 해 준 게 얼만데 구경만 하고 있어?”

“아니, 저 그게…….”

“그때 상황이 좀 그랬어요. 죄송해요.”

“의리 없는 새끼들.”

팀원들과 의리로 묶인 관계는 아니지만 그래도 줄 건 주고, 받을 건 받았다고 생각했다. 훈련소 낙제생들을 억지로 길드에 꽂아 넣고, 차도 사 주고 용돈도 준 게 누군가.

그 대가로 충성을 받았는데…… 가장 중요한 순간에 외면당하니 뒤통수가 얼얼했다.

‘시발, 뭐 이런 엿 같은 경우가.’

수십 억? 분명 큰돈이긴 하지만 임창수로서는 감당 못 할 금액은 아니었다. 그의 명의로 잡힌 건물 한두 개만 팔아도 충분히 지급할 수 있다.

그러나 자존심이 짓밟힌 건 도저히 용납할 수 없었다.

‘쳐 죽일 놈.’

임창수가 부릅뜬 눈으로 한 사람의 등을 노려봤다.

검은 가죽 갑옷을 입고 있는 저놈, 진태경이 모든 일의 원흉이다.

‘어디서 뭐 하다 온 놈인지는 모르겠지만…… 이 치욕은 반드시 갚아 주마.’

놈의 정체가 뭔지는 아직 정확히 모르겠다. 확실한 건 결코 평범한 C급 헌터는 아니라는 거다.

B급 몬스터 여덟 마리를 정면 승부로 박살 낼 수 있는 C급 헌터는 세상 어디에도 없으니까.

‘정체는 왜 숨긴 거지? 혹시 도피 중인 범죄자? 아니면 부정 등록자? 일단 게이트에서 나가기만 하면 싹 다 털어 주마.’

임창수가 은밀히 복수심을 불태우고 있던 그때였다.

휙!

돌연 그쪽으로 고개를 돌린 진태경이 눈을 가늘게 떴다. 먹이를 바라보는 포식자의 눈빛에 임창수의 가슴이 덜컥 내려앉았다.

“야.”

“예, 예?”

“너 방금 내 욕 했지.”

“아, 아, 아닌데요.”

“아니긴. 말 더듬는 것만 봐도 사이즈 나오는데. 어쩐지 아까부터 뒤통수가 따끔따끔하더라.”

임창수는 대격변 시대의 헌터이자 전쟁 영웅인 아버지의 말씀을 떠올렸다. 위험한 상황일수록 의연하게 대처해라.

“진짜 아닙니다.”

“내 관심법은 네가 거짓말을 하고 있다고 알려 주는데?”

“관심법이라니, 그런 게 어디 있어요?”

“마법도 있는데 관심법이 왜 없어. 구태의연한 사고방식을 버려.”

“어쨌든 맹세코 아닙니다.”

“아냐. 맹세코 맞아. 그리고 너도 한 대 맞아.”

빡!

눈물이 핑 돌았다. 스무 살 이후로는 아버지한테도 맞아 본 적이 없는 꿀밤이다. 그런데 기껏해야 또래로 보이는 놈한테, 그것도 팀원들과 여자들 앞에서 이런 굴욕을 당하다니.

“제법 손맛이 있네. 딱 혁무진 때릴 때 느낌인데, 이거. 아무튼 조심해라. 응?”

혁무진이 누군지는 모르겠지만 어쨌든 임창수는 고개를 푹 숙였다.

“……예.”

“근데 이놈의 미로는 끝도 없네. 야, 여기 보스 존 얼마나 남았어?”

“저도 몰라요. 미로라서.”

“몬스터도 더 이상 안 나오고. 심심해 죽겠다.”

“…….”

보이는 족족 때려잡으니까 안 나오지!

임창수와 팀원들이 나설 필요도 없었다. 저 다섯 명만으로도 충분, 아니 진태경 한 명으로도 충분했다.

‘괴물 같은 놈. 진짜 A급 헌터라도 되나?’

진태경 혼자서만 서른 마리는 넘게 쓰러트린 것 같다. 좀 지쳤나 싶다가도 어느 순간을 기점으로는 또 펄펄 날아다녔다.

‘레이드 속도가 더 빨라지고 있어.’

보통은 레이드의 끝으로 갈수록 피로 축적으로 느려지는 게 정상이다.

그런데도 같은 몬스터를 상대하는데 레이드 속도가 빨라진다는 건…….

‘계속해서 강해진다?’

임창수는 순간 떠오른 생각을 애써 부정했다.

무슨 게임 캐릭터가 레벨 업 하는 것도 아니고 그게 말이 되나. 꿀밤을 맞더니 머리가 고장 난 기분이다.

“후우.”

깊은 한숨을 내쉬는 그에게 팀원들이 우물쭈물 다가왔다.

“창수 형…….”

“오빠, 괜찮아? 어떡해. 이마에 혹 났어.”

“기분 안 좋으니까 다 꺼져. 너희는 나가기만 하면 싹 다 모가지야. 알아?”

아무리 체면을 구겨도, 이빨이 뽑혀도 호랑이는 호랑이다.

임창수의 으름장에 팀원들이 숨을 삼켰다.

‘할부 안 끝났는데.’

‘상동 길드 나가면 어디에서 받아 주나.’

‘이번 달 카드값이…….’

이제껏 풍족한 생활을 영위할 수 있었던 이유는 임창수의 원조 덕분이다. 그들 모두 헌터니만큼 굶어 죽을 일은 없겠지만 어디를 가도 지금 같은 대우는 기대하기 어렵다.

“거기서 끝낼 줄 알아? 기대해. 어딜 가더라도 상동 길드 이름으로 전화 한 통씩 꼭 넣어 줄 테니까. 이 바닥 좁은 거 알지?”

쫓아내는 것도 모자라 앞길까지 방해한다는 말에 팀원들의 얼굴이 급변했다.

“창수 형, 그건 좀.”

“형? 너 좋을 때만 형이냐?”

“오빠, 꼭 그렇게까지 해야겠어?”

“그러니까 이 자식들아. 사람 잘 보고 줄을 댔어야지.”

당장 모두 뺨이라도 한 대씩 올려붙이고 싶었지만 꾹 참았다.

큰 소리를 냈다가는 언제 또 진태경이 돌아볼지 모르기 때문이다.

‘시발, 내가 어쩌다가…….’

꿀밤이 무서워서 화도 마음대로 못 내는 꼴이라니. 임창수가 바닥에 침을 탁 뱉고 돌아선 그때였다.

덥석.

“창수 형. 아니 임 팀장님, 이러시면 어떡해요.”

“한 번만 다시 생각해 줘, 오빠. 응?”

“놔라. 두 번 말하기 싫다.”

“이번엔 진짜. 진짜로 시키는 거 다 할게요. 예?”

“……시키는 거 다 한다고?”

동료의 손을 뿌리치려던 임창수가 문득 동작을 멈췄다.

힐끗 고개를 돌리니 길드원들과 실랑이를 벌이는 사이 거리가 벌어져 저 멀리 앞서가는 진태경 일행이 보인다.

멀리서도 눈에 띄는 송송이의 환상적인 뒤태도.

‘잠깐. 방법이 있을 것 같기도 한데.’

그의 눈에 비친 진태경은 괴물이지만 딱 한 가지 약점이 있어 보였다. 송송이라는 여자.

‘아까 보니까 완전 뻑이 갔던데.’

눈치채고 말고 할 것도 없다. 누구나 한 번 본 것만으로도 그가 송송이를 마음에 품고 있다는 사실을 알아차릴 수 있을 정도니까.

‘분명 C급 힐러라고 했지.’

힐러를 제압하는 것은 닭목 비트는 것보다 쉽다. 좋아하는 여자가 붙잡혀 있다면 진태경도 쉽게 손을 쓸 수 없을 것이다.

‘그럼 끝이지.’

진태경을 제외하면 나머지 셋은 큰 걱정거리가 아니다.

길드장이라는 노인네는 B급이지만 마법사라 근접전은 쥐약일 테고, E급 탱커인 아저씨는 논할 가치도 없다.

약간 마음에 걸리는 사람이 있다면 최민우. 그놈인데…….

“방금 그 말, 믿어도 되냐?”

“물론입니다.”

“저희만 믿으세요.”

“오빠, 사람을 왜 이렇게 못 믿어? 우리가 이 정도 사이밖에 안 돼?”

그에겐 명령에 복종할 B급 헌터 넷과 C급 헌터 다섯으로 이루어진 레이드 팀이 있다. 모두 임창수가 주는 먹이만 먹도록 길들여진 녀석들이다.

“좋아. 그럼 지금부터 내가 하는 말 똑똑히 들어…….”

짤막한, 그리고 간단한 설명이 끝나자 팀원들은 긴장된 기색을 숨기지 못했다.

“될까요?”

“가능성 있어 보이기는 하는데.”

“오빠, 설마 내가 생각하는 그거, 아니지? 사람 죽이는 거면 나는 좀.”

“시키는 대로 다 한다고 하지 않았냐?”

“그래도 그건 좀…….”

“됐어. 마음 같아서는 그러고 싶지만 내가 그 정도로 막 나가는 놈은 아니야. 일단 카메라 뺏고, 저 빌어먹을 놈한테 씻지 못할 굴욕을 안겨 줘야지.”

“휴우. 다행이다. 그럼 난 무조건 오빠 편이지.”

“잘해. 이번에 망설이거나 조금이라도 뒤로 빼는 놈 있으면 알지?”

“당연하죠.”

“저희만 믿으십쇼, 팀장님. 아니, 형님. 헤헤.”

임창수의 입가에 비릿한 미소가 맺혔다.

‘내 자존심을 짓밟았으면 그만한 대가를 치러야지.’

곧 나오는 보스 존(Boss Zone)에서 겁도 없이 누굴 건드렸는지 똑똑히 깨닫게 해 줄 생각이었다.

마침 진태경에게 대적할 만한 몬스터도 그곳에 있다.

‘미노타우로스 대전사.’

이곳, ‘미노타우로스의 미로’의 보스 몬스터.

B급 몬스터 주제에 육체 능력만큼은 A급에 맞먹는다는 괴물 같은 놈이다.

‘대전사가 놈의 힘을 소진시키면 그때 결행한다.’

이이제이(以夷制夷).

오랑캐는 오랑캐로. 괴물은 괴물로 물리친다.

양쪽 모두 지친 그때가 바로 기회다. 어이없이 잃게 될 돈도, 땅에 떨어진 자존심도 한 번에 회복할 수 있다.

“야, 빨리 와! 보스 존이잖아!”

다음 순간 진태경의 외침이 들려왔다. 임창수가 활짝 웃었다.

“예! 갑니다!”

보스 존을 향해 걸어가는 그의 발걸음은 경쾌하기 그지없었다.



* * *



“일섬(一殲).”

콰아아아.

창날 끝에서 하늘이 쪼개지는 소리가 났다. 닿는 모든 것을 찢고 집어삼키는 백색 와류가 근육질의 가슴에 닿았다.

- 모오?

콰드드득.

살았는지, 죽었는지 굳이 확인할 필요도 없었다.

놈의 가슴에서 창을 뽑아낸 순간 시스템 알림이 울렸으니까.

띠링.



- [Lv.70 미노타우로스 대전사]를 처치했습니다!

- 레벨 업!

- 퀘스트, [B급 게이트 클리어]를 완료했습니다!

- 당신의 기여도를 계산 중입니다…… 완료되었습니다!

- 퀘스트 성공 보상이 인벤토리로 지급됩니다!



“휴우.”

역시 마지막은 큰 거 한 방이지. 몸이 엄청 피곤하긴 하지만. 나는 창에 묻은 피를 털며 돌아섰다.

“빨리 부산물 챙겨서 나가죠. 배고파 죽겠…… 다들 왜 그러세요?”

임꺽정이 대표로 입을 열었다.

“그걸 몰라서 묻냐?”

그가 죽은 보스 몬스터의 사체와 나를 번갈아 바라봤다.

한 방에 B급 보스 몬스터를 끝장냈으니 무슨 변명이라도 해보라는 눈빛이다.

“음, 운이 좋았던 걸로 해 두죠.”

“운?”

“네, 운.”

정말 운이 좋아서다.

내가 고시원에 살았던 것도, 고시원 앞에 캡슐이 버려진 것도. 전부 다.

“허허, 기가 차서 말도 안 나오는구먼. 됐다.”

다른 사람들도 임꺽정과 비슷한 반응이다. 이미 나와 레이드를 경험한 적 있는 최 팀장도 어안이 벙벙한 표정으로 한마디를 건넸다.

“이 정도일 줄은 몰랐습니다만.”

“지금 알면 됐죠.”

“이에 관해 대화를 나눌 수 있을까요?”

“물론입니다.”

지금은 아니고, 나중에. 더 중요한 볼일이 남았거든.

나는 최대한 매력적인 미소를 지으며 한 사람에게 다가갔다.

“송이 씨, 저 힐 좀 부탁드려도 될…… 너희들은 거기서 뭐 하냐?”

“아.”

“뭐냐고. 왜 여기 있어?”

“그냥, 그냥 있는데요.”

“저, 저는 언니가 너무 예쁘셔서.”

송이 씨 옆에 붙어 있던 상동 길드원들이 화들짝 놀라며 아무 말 대잔치를 시작한다.

‘뭐야, 이것들.’

나랑 송이 씨 사이에서 방해되니까 꺼지란 소리였는데. 내가 그렇게 무섭게 보이나?

“임창수 어디 있어?”

한마디에 상동 길드원들이 홍해처럼 쫙 갈라졌다. 임창수가 백지장처럼 하얀 얼굴로 대답했다.

“여기 있습니다.”

“너 얼굴 왜 그래? 어디 아파?”

“모, 몸살 기운이 조금.”

“쯧쯧. 포션도 챙겨 먹고 그래, 인마. 너 집에 돈 많잖아.”

“…….”

“어쨌든 빨리 부산물 수거하고 가자. 피곤하다.”

“네, 넵.”

임창수가 방해꾼들을 데리고 사라지자 기다렸던 순간이 찾아왔다. 나는 송이 씨를 향해 활짝 웃어 보였다.

“배고프시죠? 저녁으로 근사한 레스토랑에서 스테이크 어떠세요?”

송이 씨도 나를 따라 웃었다.

“죄송하지만 제가 채식주의자라.”

“이상하네. 어제 고기 잘 드셨던 것 같은데. 그럼 샐러드 바 가실래요?”

“제가 육식주의자라.”

“…….”

이거 까인 거 맞지?
```

## Final English reading copy

```markdown
# Chapter 85

“Changsoo hyung. Are you okay?”

“Were you hurt?”

At his team members’ questions, Im Changsoo clenched his teeth.

“Shut up, you bastards. After everything I’ve done for you, you’re just standing around watching?”

“No, it’s just…”

“The situation was a little complicated then. I’m sorry.”

“You disloyal bastards.”

They weren’t bound together by loyalty, but Im Changsoo thought he had given them what they were due and received what he was owed in return. Who had been the one to force the training-camp washouts into the Guild, buy them cars, and give them spending money?

He had received their loyalty in exchange…but being abandoned at the most important moment felt like a stinging blow to the back of the head.

*Fuck, what kind of bullshit is this?*

Several billion won? It was certainly a large amount of money, but it wasn’t beyond Im Changsoo’s means. He could pay it in full by selling just one or two buildings registered under his name.

But he couldn’t tolerate having his pride trampled.

*That bastard deserves to be beaten to death.*

Im Changsoo glared at one person’s back with wide-open eyes.

That bastard in the black leather armor—Jin Taekyung—was the root cause of everything.

*I don’t know where he came from or what he was doing before this…but I’ll make him pay for this humiliation.*

He still didn’t know exactly what Taekyung’s identity was. The one thing he knew for certain was that Taekyung was no ordinary C-rank Hunter.

There wasn’t a single C-rank Hunter in the world who could crush eight B-rank monsters in a head-on fight.

*Why is he hiding his identity? Is he a fugitive criminal? Or someone with a fraudulent registration? The moment we get out of this Gate, I’ll dig up every last thing about him.*

It was at that moment that Jin Taekyung suddenly turned his head toward him and narrowed his eyes.

The predator’s gaze, fixed on its prey, made Im Changsoo’s heart drop.

“Hey.”

“Y-yes?”

“You were just cursing me in your head, weren’t you?”

“N-no, I didn’t.”

“Don’t give me that. The way you stammered gives it away. No wonder the back of my head has been prickling since earlier.”

Im Changsoo recalled the words of his father, a Hunter and war hero from the Great Cataclysm era.

*The more dangerous the situation, the more calmly you have to deal with it.*

“I really didn’t.”

“My mind-reading technique says you’re lying.”

“Mind-reading? There’s no such thing.”

“There’s magic, so why not mind-reading? Let go of your hidebound thinking.”

“Regardless, I swear I didn’t.”

“No, I swear you did. And you’re getting one too.”

Bonk!

Tears sprang to Im Changsoo’s eyes.

It was a forehead flick. He hadn’t even been hit by his father since turning twenty. And now, in front of his team members and several women, he had suffered this humiliation at the hands of someone who looked barely his age.

“Not bad. The feel is exactly like when I hit Hyuk Mujin. Anyway, watch yourself, okay?”

Im Changsoo didn’t know who Hyuk Mujin was, but he lowered his head anyway.

“…Yes.”

“But this damn labyrinth really doesn’t end. Hey, how much farther to the Boss Zone?”

“I don’t know. It’s a labyrinth.”

“And no more monsters are coming out. I’m bored to death.”

“…”

*Of course they aren’t coming out when you beat down every single one you see!*

Im Changsoo and his team didn’t even need to step in. Those five were more than enough. No, Jin Taekyung alone was enough.

*What a monster. Is he really an A-rank Hunter?*

Taekyung alone seemed to have brought down more than thirty monsters. Just when it seemed like he was getting tired, he would suddenly start flying around again.

*The raid is getting faster.*

Normally, a raid slowed down toward the end as fatigue accumulated.

But the raid was getting faster even though they were fighting the same monsters…

*Is he getting stronger the whole time?*

Im Changsoo desperately rejected the thought that had flashed through his mind.

*What is he, a game character leveling up? How could that make any sense?*

Getting hit on the forehead must have broken his brain.

“Hoo.”

As Im Changsoo let out a deep sigh, his team members approached him hesitantly.

“Changsoo hyung…”

“Oppa, are you okay? What do we do? You’ve got a bump on your forehead.”

“I’m in a bad mood, so get lost. The moment you leave, you’re all fired. Got it?”

No matter how badly his dignity had been crushed, even a tiger with its teeth pulled was still a tiger.

His team members swallowed nervously at Im Changsoo’s threat.

*My car payments aren’t even finished.*

*Where will I get accepted if I leave Sangdong Guild?*

*My credit-card bill this month…*

The reason they had been able to enjoy such comfortable lives was Im Changsoo’s support. Since they were all Hunters, they weren’t going to starve to death, but wherever they went, it would be difficult to expect the same treatment.

“You think you’re getting away with it just because you’re leaving? Just wait. Wherever you go, I’ll make sure to place a call in Sangdong Guild’s name. You know this field is small, right?”

At the threat that he would not only drive them out but also ruin their futures, their expressions changed completely.

“Changsoo hyung, that’s going too far.”

“Hyung? I’m only hyung when things are going your way?”

“Oppa, do you really have to take it that far?”

“That’s why you bastards should’ve picked the right person to hitch your wagon to.”

He wanted to slap every one of them across the face, but he forced himself to hold back.

If he raised his voice again, there was no telling when Jin Taekyung might turn around.

*Fuck, how did I end up…*

What kind of pathetic situation was this, being too afraid of a forehead flick to even get angry properly?

Im Changsoo spat on the floor and turned away.

That was when someone grabbed him.

“Changsoo hyung. No, Team Leader Im, you can’t do this.”

“Think it over one more time, oppa. Please?”

“Let go. I don’t want to say it twice.”

“This time, for real. I’ll do everything you tell me. Okay?”

“…Everything I tell you?”

Im Changsoo, who had been about to pull away from his colleague’s hand, suddenly stopped.

He glanced back and saw Jin Taekyung’s group far ahead of them. They had gotten some distance away while he was arguing with his Guild members.

Even from that distance, Song Song’s stunning figure from behind was impossible to miss.

*Wait. Maybe there is a way.*

To Im Changsoo, Jin Taekyung looked like a monster—but he seemed to have one weakness.

A woman named Song Song.

*He was completely smitten earlier.*

There was no need to be perceptive about it. Anyone could tell from a single glance that Jin Taekyung had feelings for Song Song.

*She said she was a C-rank healer, right?*

Subduing a healer was easier than twisting a chicken’s neck. If the woman he liked were being held hostage, Jin Taekyung wouldn’t be able to act freely.

*Then it’s over.*

Apart from Taekyung, the other three weren’t much of a concern.

The old man who was supposedly the Guild Master was a B-rank Hunter, but he was a mage, so close combat would be his worst area. The middle-aged man who was an E-rank tank wasn’t even worth discussing.

The only person who bothered Im Changsoo a little was Choi Minwoo. That guy…

“Can I trust what you just said?”

“Of course.”

“Just trust us.”

“Oppa, why don’t you trust people at all? Are we really only this close?”

Im Changsoo had a raid team made up of four B-rank Hunters and five C-rank Hunters who would obey his commands. They were all people he had trained to live solely on the scraps he handed them.

“Fine. Then listen carefully to what I’m about to say…”

After a short and simple explanation, the team members couldn’t hide their nervousness.

“Will it work?”

“It does seem possible.”

“Oppa, it’s not what I think it is, right? If you’re talking about killing someone, I’m not sure I can.”

“Didn’t you say you’d do everything I told you?”

“Even so, that’s a little…”

“Forget it. I’d like to do that, but I’m not reckless enough to go that far. First, we take the camera. Then we give that son of a bitch a humiliation he’ll never live down.”

“Whew. What a relief. Then I’m definitely on oppa’s side.”

“Do your best. You know what happens if anyone hesitates this time or holds back even a little, right?”

“Of course.”

“Just trust us, Team Leader. No, hyungnim. Hehe.”

A sinister smile spread across Im Changsoo’s lips.

*If he trampled on my pride, he has to pay the price.*

In the Boss Zone they were about to enter, Im Changsoo intended to make Jin Taekyung understand exactly whose toes he had stepped on.

There was even a monster there capable of standing against Jin Taekyung.

*The Minotaur Warrior.*

The boss monster of **The Minotaur’s Labyrinth**.

Despite being only a B-rank monster, it was a monstrous creature whose physical abilities rivaled those of an A-rank.

*Once the Minotaur Warrior wears him down, we’ll make our move.*

Set a barbarian against a barbarian.

Defeat a monster with a monster.

The moment both sides were exhausted would be their opportunity. He could recover both the money he was about to lose for no good reason and the pride that had been dragged through the dirt.

“Hey, hurry up! This is the Boss Zone!”

Jin Taekyung’s shout rang out the next moment.

Im Changsoo smiled broadly.

“Yes! Coming!”

His steps toward the Boss Zone were remarkably light.

* * *

“One Annihilation.”

Kraaaaaash!

From the tip of the spear came the sound of the sky splitting apart.

A white vortex that tore through and devoured everything it touched slammed into the muscular chest of the Minotaur Warrior.

—Moo?

Crack-crack-crack!

There was no need to check whether it was alive or dead.

The moment I pulled my spear from its chest, the System notification rang out.

Ding.

> **System**
>
> - Defeated **Lv. 70 Minotaur Warrior**!
>
> - Level Up!
>
> - Quest, **B-rank Gate Clear**, completed!
>
> - Calculating your contribution… Complete!
>
> - The Quest Success Reward has been deposited into your Inventory!

“Whew.”

The last one should always end with one big hit.

My body was incredibly tired, though.

I shook the blood from my spear and turned around.

“Let’s collect the byproducts and get out of here. I’m starving to dea—why are you all looking at me like that?”

Im Kkeokjeong spoke for everyone.

“You really have to ask?”

He looked back and forth between the dead boss monster’s corpse and me.

His eyes demanded some kind of explanation for how I had finished a B-rank boss monster with a single blow.

“Hmm. Let’s just say I got lucky.”

“Lucky?”

“Yes. Lucky.”

It really was because I had been lucky.

The fact that I had lived in a goshiwon.[^1] The fact that a capsule had been discarded in front of my goshiwon.

All of it.

“Good grief. I’m speechless. Fine.”

The others reacted much the same way as Im Kkeokjeong. Even Team Leader Choi, who had already experienced a raid with me, addressed me with a stunned expression.

“I didn’t expect you to be this capable.”

“If you know now, that’s enough.”

“Could we discuss this?”

“Of course.”

Not now. Later.

I still had something more important to take care of.

With my most charming smile, I approached one person.

“Miss Song, could I ask you for a heal—what are you guys doing over there?”

“Ah.”

“What are you doing? Why are you here?”

“We’re just… just standing here.”

“I-I just think she’s so beautiful.”

The Sangdong Guild members who had been standing next to Song Song jumped in surprise and began spouting all kinds of nonsense.

*What’s wrong with these guys?*

I only meant that they should get lost because they were getting in the way between me and Miss Song.

*Do I really look that scary?*

“Where’s Im Changsoo?”

At a single word from me, the Sangdong Guild members split apart like the Red Sea.

Im Changsoo answered from behind them, his face white as a sheet.

“I’m here.”

“What’s wrong with your face? Are you sick?”

“I-I think I’m coming down with something.”

“Tsk, tsk. Take a potion, you idiot. You’ve got plenty of money at home.”

“…”

“Anyway, hurry up and collect the byproducts. Let’s go. I’m tired.”

“Yes, yessir.”

Once Im Changsoo disappeared with the nuisances, the moment I had been waiting for finally arrived.

I smiled brightly at Song Song.

“You’re hungry, right? How about steak at a nice restaurant for dinner?”

Song Song smiled back at me.

“I’m sorry, but I’m a vegetarian.”

“That’s strange. I thought you ate meat just fine yesterday. How about a salad bar?”

“I’m a carnivore.”

“…”

*I got rejected, right?*

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often used by students and people on tight budgets.
```
