<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0096.txt",
      "sha256": "413d44c68cea59c68dae07679a95eba70c85fe68b3150cb31fc3258e0ff4397b",
      "bytes": 12937
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d50aa6b27f454e7c938db2322e2437962753f1e1489799e29c989ecd2b887d87",
      "bytes": 4916
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9f8665ee0d83e682a750e93eb3cb20e14f21e891644bd8bb594a737ab54a10d6",
      "bytes": 11390
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c33420ef78da66b1d97b54515bab55ac02a7c015b123fca70dc649eb25866241",
      "bytes": 23942
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "22ed1b9292d24a17dcfad62a32ce41a3a3c6285e68992e1774874c5ca2c2d109",
      "bytes": 9609
    }
  ],
  "estimated_tokens": 14266
}
-->

# Durable State Update — Chapter 96

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 96. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 96. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 96,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 96,
    "continuity_sources": [96],
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
    "The party sells The Minotaur's Labyrinth byproducts and Magic Gems to the Administration.",
    "Im Kkeokjeong warns that Sangdong Guild is powerful enough to threaten Peace Guild; Im Chunsoo ordered expanded surveillance of Taekyung through Sangdong's Audit Team.",
    "Im Changsoo transferred four billion won to Taekyung after Im Chunsoo learned about the transfers and beat him.",
    "Kim Jeonghee is Taekyung and Hayeon's mother; Taekyung's father died when a Gate opened downtown during the Great Cataclysm.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Taekyung is a C-rank Hunter reawakened from F-rank who defeated B-rank Minotaurs and can use the Jin Family's Cultivation Technique to perform Circulate Qi for Healing.",
    "Hayeon and Kim Jeonghee recovered substantially after Taekyung used Circulate Qi for Healing; Hayeon is considering dropping out after learning about his raid earnings.",
    "Taekyung's reality and Murim Inventories are separate.",
    "Peace Guild's Guild house remodeling is scheduled to finish in one week, and Taekyung is on paid vacation until then.",
    "Choi Minwoo and Butler Kim suspect Taekyung may be a third-awakening Hunter, but this remains unconfirmed.",
    "Taekyung agreed to buy the former family home for 3.38 billion won, paid a ten-percent deposit, and plans to remodel it and move after Hayeon's college entrance examination.",
    "Park Jihwang changed his name to Park Jihoon and is a Hunter in Team 1 of Myeongdong Guild; Taekyung judged Jihoon's strength comparable to or greater than Im Changsoo's.",
    "Hong Woojin is a B-rank mage and information broker investigating Taekyung through Familiars; he has severed both his Rice Weevil and Cat Familiar Links.",
    "Sangdong Guild's Team 1 Leader is its only A-rank Hunter besides Im Chunsoo, doubts reports of Taekyung's feats, and withholds Woojin's warning from Chunsoo; the Guild Master's and Team Leader's personal and account information is protected by a security Lock.",
    "Taekyung's Qi Sense reaches seventy meters and detected the fly Familiars in his home; after Woojin severed the Rice Weevil Link, no Familiar remained there at that time.",
    "Taekyung spent 350 million won at the Ilsan Store and stored the purchases in his Inventory.",
    "For a B-rank mage, Familiar connections reach up to 500 meters, with about 300 meters considered safe; forced Link severance causes physical distress and may cause mana backflow.",
    "Tiny Familiars evade most detection magic, so Taekyung concluded that their controllers had been nearby and decided to catch them himself.",
    "Hayeon is temporarily fostering an abandoned Level 2 Cat Familiar named Yeoreum; Taekyung knowingly allows it to remain while searching for the mage controlling it.",
    "Sangdong Guild's Security Team has assigned a B-rank leader, a C-rank Familiar mage, and four close-combat tracking and stealth Hunters to the current operation and is preparing another Cat Familiar."
  ],
  "continuity_sources": [
    95
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved.",
    "Whether Hayeon will actually drop out of school remains unresolved.",
    "Whether third-awakening Hunters exist and whether Taekyung is one remains unresolved.",
    "Why Hong Woojin is investigating Taekyung and what information he seeks remains unresolved.",
    "Whether Woojin's assignment and Sangdong Guild's Security Team operation share the same commissioning chain remains unresolved."
  ],
  "safe_through": 95,
  "temporary_decisions": [
    "Use Frozen for 프로즌, preserve the tiger-father/dog-son wordplay in 호부견자, and use ajumma for 아줌마.",
    "Use goshiwon for 고시원 with an explanatory footnote; use Hope Goshiwon for 희망 고시원.",
    "Use Minsu for 민수; render 운기요상 as Circulate Qi for Healing, 하급 포션 as Lesser Potion, and 상급 포션 as Superior Potion.",
    "Render 3차 각성자 as third-awakening Hunter, 3차 각성 as third awakening, 피의 일주일 as Bloody Week, and 전세 as jeonse lease.",
    "Render 사장님 as Boss in the real-estate context, including young Boss.",
    "Render 박지황/박지훈 as Park Jihwang/Park Jihoon, and 삼계탕 as samgyetang with an explanatory footnote.",
    "Render 1팀장 as Team 1 Leader, 기감 as Qi Sense, and 락 as Lock when referring to security restrictions.",
    "Render the fly and Familiar terminology as Housefly, Black Blow Fly, Green Bottle Fly, Familiar, Rice Weevil, Link, Store, Assistant Manager, Kim Seonhee, Ilsan, and Lafesta; use Yeoreum for 여름이 and Midsummer for 한여름."
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
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |

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
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 철수     | **Cheol Soo**      |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 평화 | **Peace Guild** | Guild name. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 링크 | **Link** | Mental connection between a mage and Familiar |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 95
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃96화



김준수는 상동 길드 보안팀 소속의 C급 헌터다.

원소 마법에는 재능이 쥐뿔도 없었지만 다행히 희귀하다는 정신계 마법사로 각성한 덕에 나름 잘나가는 인생을 살고 있었다.

‘집에 못 들어가는 것만 빼면.’

100평이 넘는 집을 갖고 있으면 뭐 하나. 상동 길드 유일의 패밀리어 마법사인 그는 일거리가 끊이질 않았다.

레이드 팀은 게이트 돌고 나면 퇴근이라도 하지, 보안팀은 그딴 거 없이 매번 달라지는 아지트에서 밤을 새야 한다.

“준수야, 밤샜냐?”

“네.”

김준수의 퀭한 얼굴을 본 보안팀의 동료가 혀를 찼다. 귀중한 패밀리어 마법사를 경호하기 위해 남아 있던 한 사람이다.

“고생 많다. 저 새끼는 어떻게 집 밖으로 한 발자국을 안 나오냐?”

“그러니까요. 며칠째 감시 중인데 지금까지 딱 두 번 나왔어요, 두 번. 고양시 쪽 부동산 한 번이랑 일산 스토어.”

“이래서 표적 대상은 흡연자인 게 좋은데. 걔들은 담배 피우러 나오기라도 하잖아.”

새로 구한 고양이를 패밀리어 삼아 밤새 아파트 동 입구에서 기다렸지만 표적은 꿈쩍도 하지 않았다.

유일한 사건이라면 기다림에 지쳐 야옹거리며 울다가 경비 아저씨한테 쫓겨날 뻔했던 것뿐이다.

“평화 길드? 보니까 규모도 작던데 레이드도 안 뛰나.”

“쟤들 지금 휴가래.”

“휴가요?”

“어. 2조에 있는 내 동기가 평화 길드 다른 애들 감시 중인데 다 쉬고 있다던데?”

“아…… 그쪽 상황은 어떻대요?”

“어제부로 철수. 여자 하나랑 아저씨 하난데 금방 끝났다더라. 팀장 반응 봐서는 그쪽에서 뭐 하나 건진 거 같긴 한데 잘은 모르겠고.”

“후우. 이쪽도 그냥 적당히 하고 철수하지.”

깊은 한숨을 내쉬는 김준수를 동료가 안쓰러운 표정으로 바라봤다.

“길드에 딱 한 명 있는 패밀리어 마법사를 특별히 붙인 이유가 있지 않겠어?”

“그래 봤자 C급 헌터인데, 이렇게까지 공들이는 건 좀 아니지 않아요?”

“어쩌겠냐. 까라면 까야 하는걸. 팀장이 어제처럼 쪼아 대도 그러려니 해.”

“적당히 쪼아 대야죠. 애초에 홍우진인가 하는 그 사람이랑 얘기해서 잘 협력했으면 진작 끝났을 문젠데.”

“길드장님께 보여 주고 싶은 거지. 우리 보안팀이 홍우진보다 훨씬 낫다. 내 리더십이 이렇게 뛰어나다. 안 그래도 슬슬 하반기 인사이동 시즌인데 팀장도 똥줄 탈 만하잖아.”

“……환장하겠네요.”

“환장하지.”

김준수는 머리라도 쥐어뜯고 싶은 마음이었지만 꾹 참았다. 그랬다가는 이제 겨우 봄철 새순처럼 돋아난 머리카락이 뽑혀 나갈지 모른다.

‘아, 의사가 스트레스받으면 탈모 악화된다고 했는데.’

그 쉬운 라이트 마법도 못 쓰는 민간인 의사지만 머리만 풍성하게 만들어 준다면 예수님으로 모실 수 있다.

‘그러고 보니 오늘은 머리가 별로 안 빠진 것 같기도 하고.’

김준수가 조심스럽게 정수리를 더듬으려던 그때였다.

- 표적 확인. 표적 확인. 이동 중!

무전기 너머로 들려오는 낮지만 긴박한 동료의 목소리.

방 안의 두 사람은 물론이고 옆방에서 코를 골고 있던 보안팀장까지 벌떡 일어났다.

추르릅. 입가의 침을 훔친 그가 외친다.

“야! 김준수!”

젠장. 아직 아침도 못 먹었는데.

패밀리어 마법 쓰면 머리 또 빠지는데!

‘씨바, 계약 끝나면 바로 길드 때려치운다.’

눈물을 삼킨 김준수가 마나를 끌어 올렸다. 머리가 뜨거워지며 의식이 빨려 들어간다.

‘충실한 종이여, 내 부름에 답하라. 링크!’

화악!

그리고 다음 순간, 차 밑에 엎드려 있던 새끼 고양이가 번쩍 눈을 떴다.

미야옹.



* * *



나는 걸음을 멈췄다. 울음소리와 함께 갑자기 불쑥 튀어나온 검은 털 뭉치 때문이다.



[Lv.2 고양이 - 패밀리어]



“…….”

또 고양이네. 이 자식들은 창의력이 이렇게 없나?

아, 하나 달라지긴 했다. 이놈은 털 색이 새까맣다.

미앙. 미야앙.

새끼치고는 제법 당찬 걸음으로 다가온 고양이가 내 슬리퍼에 온몸을 비비적거렸다. 시전자가 누군지는 몰라도 클럽에서 좀 놀아 본 솜씨다.

‘거참. 이런 식으로 관심받는 건 별론데.’

하지만 새로운 패밀리어의 등장 덕분에 새로운 사실을 짐작할 수 있었다.

‘이놈들, 한패가 아닌가?’

하루 간격으로 고양이처럼 눈에 띄는 패밀리어를 두 마리나? 결코 좋은 접근 방식이 아니다. 오히려 황급히 따라 한다는 느낌이 강했다.

냥!

관심을 가져 달라는 듯이 울어 대는 고양이의 모습에 나는 피식 웃었다.

“짜식, 귀엽네.”

이놈을 데려가야 하나, 말아야 하나…….

머리가 바쁘게 돌아가던 그때였다.

“고양이가 애교가 많네. 아저씨가 기르는 거예요?”

슬리퍼를 질질 끌며 다가온 한 남자. 40대 초반 정도로 보이는 얼굴은 지극히 평범했고 목 늘어난 티셔츠와 라면 국물이 묻은 축구 반바지는 친근하다.

“아뇨. 길고양이인 것 같은데 갑자기 애교를 부리네요.”

“이야, 이거 완전히 그거잖아. 개냥이.”

“그러게요. 어제도 그렇고, 이 동네 고양이들은 애교가 많나 봐요.”

“어제요?”

“네, 어제도 한 마리 주웠거든요. 개냥이로.”

“거 신기하네.”

남자가 반쯤 타들어 간 담배를 한 모금 빨았다.

“이렇게 보면 짐승들도 다 인연이 있는 것 같어. 좋은 주인이 될 것 같으니까 고양이가 애교도 부리고 하지.”

“에이, 좋은 주인은 무슨. 그냥 원래 이런 성격인 것 같은데요?”

“그런가? 야, 야, 이리 와 봐.”

아저씨의 손짓에도 고양이는 꿈쩍도 하지 않는다.

아니, 오히려 내 다리 사이로 파고들었다.

“허허. 이놈 봐라. 어린 게 벌써부터 사람을 가릴 줄 아네.”

내가 말없이 웃고만 있자 아저씨가 묻는다.

“그래서, 키우시려고?”

“글쎄요. 지금 급한 볼일이 있어서. 끝내고 왔을 때도 있으면 며칠 데리고 있어 보죠, 뭐.”

“그때까지 이놈이 여기 있을까 모르겠네. 그치, 나비야?”

에옹.

“얼마 안 걸려요. 요 앞에 부동산 가는 거라.”

“그래요? 참, 그쪽 젊은 양반은 처음 보는 분이시네. 나 여기 오래 살아서 어지간한 사람은 다 아는데. 부동산 가신다는 거 보니 새로 이사 오시는 분인가?”

“저는 따로 살아서요. 가족들 보러 어쩌다 한 번씩만 옵니다. 부동산은 잠깐 뭐, 일이 있어서요.”

“아아…….”

후우. 마지막 연기가 바람에 흩어진다. 담배꽁초를 바닥으로 튕긴 아저씨가 입을 열었다.

“이거 참, 내가 바쁜 사람 붙잡고 있었네. 마음 상한 건 아니죠?”

“전혀요.”

“그럼 다행이고. 다음에 만나면 알은체나 합시다. 이웃사촌끼리.”

내가 대답했다.

“네, 이웃사촌끼리.”

“그럼 먼저 갑니다. 날씨도 좋은데 동네나 한 바퀴 돌아야지.”

사람 좋은 웃음을 지은 아저씨가 걸음을 옮긴다. 휘적거리는 걸음으로 멀어지는 그의 뒷모습을 잠시 바라보며 생각했다.

‘연기 잘하네.’

야옹.

그래, 너도 있었지.

집을 나서자마자 연기자를 두 명이나 만났다. 길고양이와 이웃사촌이라는 탈을 쓴 연기자를.

“금방 올 테니까 여기서 얌전히 기다리고 있어라, 응?”

고양이가 무슨 소리냐는 듯 고개를 갸우뚱한다.

하지만 나는 알고 있다. 저 녀석이 내 말을 알아들었고, 몇 시간이 흘러도 이 자리에 있을 거라는 사실을.

그리고 하나 더.



[Lv.42 김권동]



우리 집 옆 동에는 헌터가 살지 않는다는 사실을.

‘역시 한패가 아니야.’

두 연기자의 등장은 짐작을 확신으로 바꾸기에 충분했다.

집 앞 부동산을 향하는 내 발걸음은 한층 더 가벼워져 있었다.



* * *



늦은 아침, 슬리퍼를 질질 끌며 콧노래를 부르는 후줄근한 차림의 중년인. 어디에서나 흔하게 찾아볼 수 있는 모습인 그는 코너를 돌자마자 담배 한 개비를 빼 물었다.

“어디 보자, 라이터가…….”

손은 느릿느릿 주머니를 뒤지지만 눈은 바쁘게 움직인다.

주위에 아무도 없는 것을 확인한 그가 라이터 대신 꺼낸 것은 초소형 무전기였다.

“연기 괜찮았어? 나 헌터 말고 배우나 할 걸 그랬나 봐. 어째 전투보다 연기를 더 잘해.”

- 나 팀장이다.

툭. 입에 물고 있던 담배가 떨어졌다. 덕분에 자유로워진 입이 벙긋거린다.

시바, 좆 됐네.

황급히 정신을 수습한 보안팀 소속 C급 헌터, 김권동이 대답했다.

“아, 예. 팀장님.”

- 이야, 김권동이 연기 잘하데? 길드 관두고 할리우드 가도 되겠더라.

“죄, 죄송합니다.”

- 쫄기는, 칭찬이야. 그건 그렇고 표적은 어때? 냄새 못 맡았겠지?

“제 생각으로는 그렇습니다.”

패밀리어 마법을 사용 중인 김준수를 통해 대화를 이미 들었을 텐데도 재확인하는 이유는 간단하다.

고양이의 시선으로는 표적의 모든 것을 명확하게 담을 수 없기 때문이다.

- 확실해? 100%?

“90%입니다.”

- 자식이, 90%가 확실한 거냐? 이럴 때는 자신감 있게 질러야지.

“섣부른 판단은 금물이니까요.”

김권동은 속으로 팀장을 욕했다.

‘자신 있게 지르면 뭐 해. 나중에 일 잘못되면 나한테 제일 먼저 지랄할 거면서.’

이런 식으로 빠져나갈 구멍은 만들어 둬야 한다. 김권동의 90%는 팀장의 10%가 더해져야 비로소 완성된다.

- 그런 모습 아주 보기 좋아. 다음 행동은 알지?

팀장의 기분 좋은 목소리는 이제야 100%가 됐다는 신호다.

김권동은 저 멀리서 걸어오는 주민을 피해 슬그머니 발길을 틀었다.

“예. 자연스럽게 주위 맴돌면서 관찰하겠습니다.”

- 그래, 특이 사항 생기면 바로바로 보고하고.

“예.”

- 그럼 수고.

1분 남짓 이루어진 둘의 대화는 아무도 듣지 못했다.

이번에는 진짜 라이터를 꺼내 담배에 불을 붙인 김권동이 연기를 깊이 들이마셨다.

“시발, 몬스터한테 죽는 것보다 폐암 걸려 죽는 게 더 빠르겠네.”



* * *



보안팀장이 바빠졌다. 외부 감시 인원은 총 셋. 남은 두 명에게 지시를 하달하고 만전을 기해야 한다.

“1번.”

- 1번 등장했습니다.

“전체 채널로 듣고 있었지? 표적이 가는 부동산은 어떻게 됐어?”

- 인근 상가에 두 개 있고, 두 곳 모두 도청 마법 장비 깔았습니다.

“잘했어. 표적 위치는?”

- 아직 안 보이는…… 아, 등장했습니다. 약 300m 밖에서 접근 중.

“자리 떠. 어차피 장비 깔았으니까 괜히 접촉할 필요 없어.”

- 예. 특이 사항 있으면 바로 보고하겠습니다.

“오케이. 2번은?”

- 현 위치에서 대기 중입니다.

무전기 너머로 들려오는 굵은 목소리.

근처 상가에 은신해 있던 또 다른 팀원의 대답에 보안팀장이 고개를 끄덕였다.

“이 자식 다른 길로 샐 수도 있으니까 잘 감시해.”

- 네.

은신, 추적 계열의 C급 헌터 넷과 패밀리어 마법사.

전투력은 떨어지지만 이 분야에서는 하나같이 풍부한 경험이 있는 베테랑들이다.

‘C급 헌터 하나한테 붙기에는 과분한 정도지.’

처음에는 약간의 경계심이 있었다. 표적에 관하여 길드장이 특별히 언질한 부분이 있었기 때문이다.

‘B급 게이트를 혼자 클리어했다고 했지, 아마.’

하지만 놈에 관한 정보를 모을수록, 지켜보면 지켜볼수록 전혀 아니라는 생각이 들었다. 의심에 종지부를 찍은 건 정보의 출처가 임창수라는 사실이다.

‘망나니 새끼가 맞아 죽기 싫어서 이빨 깐 거지.’

어디서나 볼 수 있는 평범한 C급 헌터.

그의 눈에 비친 진태경은 딱 그 정도였다.

삑.

- 표적, 부동산으로 들어갑니다.

감시하고 있던 팀원의 무전.

상동 길드 보안팀은 촉각을 곤두세웠다.
```

## Final English reading copy

```markdown
# Chapter 96

Kim Junsu was a C-rank Hunter belonging to Sangdong Guild’s Security Team.

He had not an ounce of talent for elemental magic, but fortunately, he had awakened as a rare type of mage—a mental mage—and was living a fairly successful life.

*Except for the fact that I can’t go home.*

What good was owning a house larger than 330 square meters? As the only Familiar mage in Sangdong Guild, he never ran out of work.

Raid teams at least got to go home after running a Gate, but the Security Team had no such luxury. They had to spend every night in a different hideout.

“Junsu, did you pull an all-nighter?”

“Yes.”

A colleague on the Security Team clicked his tongue when he saw Kim Junsu’s hollowed-out face. He was the one person who had stayed behind to protect their valuable Familiar mage.

“You’re working hard. How does that bastard manage not to step outside even once?”

“I know. We’ve been watching him for days, and he’s only gone out twice. Twice. Once to a real-estate office in Goyang and once to the Ilsan Store.”

“This is why it’s better when the target smokes. At least smokers come outside to have a cigarette.”

They had obtained a new cat to use as a Familiar and waited all night at the entrance of the apartment building, but the target had not budged.

The only incident was when the cat, exhausted from waiting, started meowing and was nearly chased away by a security guard.

“Peace Guild? It looked pretty small. Do they even go on raids?”

“They’re on vacation right now.”

“Vacation?”

“Yeah. A guy from Team 2 is watching the other members of Peace Guild, and apparently they’re all taking time off.”

“Ah… How’s that situation going?”

“They pulled out yesterday. There was one woman and one middle-aged man, but it ended quickly. Judging by the Team Leader’s reaction, it seems like they turned up something over there, but I don’t know the details.”

“Phew. We should just do enough to get by and pull out, too.”

His colleague looked at Kim Junsu with pity as he let out a deep sigh.

“There has to be a reason they specially assigned the Guild’s only Familiar mage, right?”

“He’s still only a C-rank Hunter. Don’t you think this is going a little overboard?”

“What can we do? When we’re told to do something, we have to do it. Even if the Team Leader hounds us like he did yesterday, we just have to put up with it.”

“He should hound us in moderation. This would’ve been over ages ago if he had just talked to that Hong Woojin guy and cooperated properly.”

“He wants to show the Guild Master. ‘Our Security Team is much better than Hong Woojin. My leadership is this outstanding.’ Besides, it’s almost time for the second-half personnel reshuffle. No wonder the Team Leader is sweating bullets.”

“…This is driving me insane.”

“It is.”

Kim Junsu wanted to tear his hair out, but he held himself back. If he did, the hair that had only just begun sprouting like fresh spring shoots might come right out.

*Ah, the doctor said stress makes hair loss worse.*

The doctor was a civilian who couldn’t even use the simple Light magic, but if he could give Kim Junsu a full head of hair, Junsu would worship him as Jesus.

*Come to think of it, maybe I haven’t lost much hair today.*

That was when Kim Junsu cautiously reached up to feel the crown of his head.

—Target confirmed. Target confirmed. Moving!

A low but urgent voice came through the radio.

The two men in the room—and even the Security Team Leader, who had been snoring in the next room—bolted upright.

Slurp. After wiping the drool from his mouth, the Team Leader shouted.

“Hey! Kim Junsu!”

*Damn it. I haven’t even eaten breakfast yet.*

*Using Familiar magic makes my hair fall out again!*

*Fuck this. I’m quitting the Guild the moment my contract ends.*

Swallowing back his tears, Kim Junsu drew up his mana. His head grew hot, and his consciousness was pulled inward.

*Faithful servant, answer my call. Link!*

Whoosh!

The next moment, a kitten lying beneath a car opened its eyes wide.

“Myaowww.”

* * *

I stopped walking.

A black ball of fur had suddenly popped out with a cry.

> **System**
>
> **Lv. 2 Cat—Familiar**

“…”

Another cat. Did these bastards have no creativity at all?

Well, one thing was different. This one’s fur was pitch-black.

“Miaow. Miaowww.”

The kitten approached with surprisingly confident steps for such a young creature, then rubbed its entire body against my slipper. Whoever had cast the spell clearly knew its way around a club.

*Man. I don’t like getting attention this way.*

But the appearance of this new Familiar allowed me to make a new guess.

*Could they be working together?*

Two conspicuous Familiars, both in the form of cats, appearing a day apart? It was hardly a good approach. If anything, it felt like someone had hurriedly copied the first attempt.

“Meow!”

The cat cried as if demanding my attention, and I let out a quiet laugh.

“You little thing. You’re cute.”

Should I take it with me or not…?

My mind was racing when—

“That cat’s pretty affectionate. Is it yours, sir?”

A man approached, dragging his slippers. He looked to be in his early forties, with an utterly ordinary face. His stretched-out T-shirt and soccer shorts stained with ramen broth gave him a friendly, familiar air.

“No. I think it’s a stray, but it suddenly started acting affectionate.”

“Wow, this is totally one of those. A dog-cat.”[^1]

“Exactly. Just like yesterday. I guess the cats in this neighborhood are pretty affectionate.”

“Yesterday?”

“Yeah, I picked up another one yesterday. It was a dog-cat, too.”

“That’s strange.”

The man took a drag from a half-burned cigarette.

“When you look at things like this, even animals seem to have connections with people. The cat’s acting affectionate because you look like you’d make a good owner.”

“Come on, what do you mean, a good owner? I think it just has this kind of personality.”

“Is that so? Hey, hey, come here.”

The cat did not move at the man’s beckoning.

No, it burrowed between my legs instead.

“Well, look at this one. Young as it is, it already knows how to pick its people.”

I only smiled without saying anything, so the man asked,

“So, are you planning to raise it?”

“I’m not sure. I have somewhere urgent to be right now. If it’s still here when I get back, I’ll keep it for a few days.”

“Who knows if it’ll still be here by then. Right, Nabi?”

“Mrow.”

“It won’t take long. I’m just going to the real-estate office right over there.”

“Really? Oh, come to think of it, I’ve never seen you before, young man. I’ve lived here a long time, so I know just about everyone. Since you’re going to a real-estate office, are you moving into the neighborhood?”

“I live somewhere else, so I only come by to see my family once in a while. I just have something to take care of at the real-estate office.”

“Ah…”

Phew. His final breath of smoke scattered in the wind. The man flicked his cigarette butt onto the ground and spoke.

“Well, look at me, holding up a busy man. You’re not offended, are you?”

“Not at all.”

“Then that’s good. If we meet again, let’s say hello. We’re neighbors, after all.”

I answered,

“Yes. We’re neighbors.”

“Then I’ll be off. The weather’s nice, so I should take a lap around the neighborhood.”

The man gave me a good-natured smile and started walking. I watched his retreating back for a moment as he moved away with a loose, swinging gait.

*He’s good at acting.*

“Meow.”

Right. You’re here, too.

The moment I left the house, I met two actors. Actors wearing the guises of a stray cat and a neighbor.

“I’ll be back soon, so wait here quietly, okay?”

The cat tilted its head as if it had no idea what I was talking about.

But I knew. I knew that it understood me—and that it would still be sitting here even after several hours had passed.

And there was one more thing.

> **System**
>
> **Lv. 42 Kim Gwondong**

There wasn’t a Hunter living in the building next to ours.

*So they aren’t working together.*

The appearance of the two actors was enough to turn my suspicion into certainty.

My steps grew lighter as I headed toward the real-estate office in front of the house.

* * *

Late in the morning, a middle-aged man in shabby clothes dragged his slippers along while humming. He was such an ordinary sight that he could be found anywhere. The moment he turned the corner, he pulled out a cigarette and placed it between his lips.

“Let’s see. Where’s my lighter…”

His hand moved slowly as it rummaged through his pocket, but his eyes were moving busily.

After confirming that no one was nearby, he pulled out something else instead of a lighter: a miniature radio.

“Was the acting okay? Maybe I should’ve become an actor instead of a Hunter. I’m better at acting than fighting.”

—It’s me, the Team Leader.

Plop.

The cigarette fell from his mouth. His now-free lips moved soundlessly.

*Shit. I’m screwed.*

The C-rank Hunter Kim Gwondong, a member of the Security Team, hurriedly pulled himself together and answered.

“Ah, yes, Team Leader.”

—Kim Gwondong’s pretty good at acting, huh? You could quit the Guild and go to Hollywood.

“I-I’m sorry.”

—Don’t get scared. It’s a compliment. Anyway, how’s the target? He didn’t smell anything, right?

“I don’t think so.”

The reason the Team Leader asked again, despite having already heard the conversation through Kim Junsu, was simple.

A cat’s eyes could not capture everything about the target clearly.

—Are you sure? One hundred percent?

“Ninety percent.”

—You little shit, is ninety percent certain? At times like this, you’re supposed to say it confidently and go for it.

“Jumping to conclusions is dangerous.”

Kim Gwondong cursed the Team Leader inwardly.

*What good does it do me to say it confidently? If something goes wrong later, you’ll be the first one to chew me out.*

He had to leave himself an escape route like this. Kim Gwondong’s ninety percent would only be complete once the Team Leader added his ten percent.

—That attitude of yours is exactly what I like to see. You know what to do next, right?

The Team Leader’s pleasant voice was a sign that he had finally reached one hundred percent.

Kim Gwondong subtly changed direction to avoid a resident approaching from far away.

“Yes. I’ll naturally circle around the area and keep watch.”

—Right. Report immediately if anything unusual happens.

“Yes.”

—Then keep up the good work.

The conversation between the two men lasted a little over a minute, and no one heard it.

This time, Kim Gwondong took out a real lighter and lit his cigarette. He inhaled deeply.

“Fuck. Looks like lung cancer’s going to kill me faster than a monster.”

* * *

The Security Team Leader got busy. There were three external surveillance personnel in total. He had to give instructions to the other two and make sure everything was in place.

“Number One.”

—Number One here.

“You were listening on the all-team channel, right? What about the real-estate office the target is heading to?”

—There are two in the nearby shopping district, and we’ve installed eavesdropping-magic Equipment in both.

“Good. Where’s the target?”

—We haven’t seen him yet… Ah, there he is. He’s approaching from about 300 meters away.

“Leave your position. We already installed the Equipment, so there’s no need to make contact for no reason.”

—Yes. I’ll report immediately if anything unusual happens.

“Okay. Number Two?”

—Waiting at my current position.

A deep voice came through the radio.

The Security Team Leader nodded at the reply from another team member hiding in a nearby shop.

“That bastard might take another route, so keep a close eye on him.”

—Yes.

Four C-rank Hunters specializing in stealth and tracking, along with a Familiar mage.

Their combat power was low, but every one of them was a veteran with extensive experience in this field.

*It’s overkill for one C-rank Hunter.*

At first, he had been somewhat wary. The Guild Master had given them a special warning about the target.

*They said he cleared a B-rank Gate alone, I think.*

But the more information he gathered about the man, the more he watched him, the more he felt that was not the case at all. The fact that the information had come from Im Changsoo finally put an end to his doubts.

*That good-for-nothing bastard made it all up because he didn’t want to get beaten to death.*

An ordinary C-rank Hunter whom one could find anywhere.

That was all Jin Taekyung was in his eyes.

Beep.

—Target entering the real-estate office.

A report came over the radio from the team member keeping watch.

Sangdong Guild’s Security Team went on full alert.

[^1]: A Korean term for a cat that acts like a dog—friendly and affectionate.
```
