<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0095.txt",
      "sha256": "9322da49892a1e70fdce469c0ca6813327851064de9ef398e039d79595f96ad4",
      "bytes": 13967
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a2728a02cf936174771f8ff6f8de6c4977012f4a0d875f2e0f2be8c5e9dd4f02",
      "bytes": 5181
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b719c1138bf5c03923c24ed7e302816dd450d14b93c4de3974e9111bae24a6b3",
      "bytes": 11319
    },
    {
      "path": "characters/Jin Hayeon.md",
      "sha256": "3a25a2df48663fa746b6c4f5990e1a66531b1386f68e056f5acffd1678a7fa5e",
      "bytes": 1425
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e80a0fa2902a8a73d8190bad7b3ab954c64495c51b35ba4a8e44a43379b3892c",
      "bytes": 23942
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "22ed1b9292d24a17dcfad62a32ce41a3a3c6285e68992e1774874c5ca2c2d109",
      "bytes": 9609
    }
  ],
  "estimated_tokens": 14909
}
-->

# Durable State Update — Chapter 95

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 95. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 95. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 95,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 95,
    "continuity_sources": [95],
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
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild; Im Chunsoo, its A-rank Guild Master and founder known as Frozen, ordered expanded surveillance of Taekyung through Sangdong's Audit Team.",
    "Im Changsoo transferred the promised four billion won to Jin Taekyung after Im Chunsoo learned about his transfers and beat him.",
    "Kim Jeonghee is Taekyung and Hayeon's mother; Taekyung's father died when a Gate opened downtown during the Great Cataclysm.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Taekyung is a C-rank Hunter who reawakened from F-rank, defeated B-rank Minotaurs, and can use the Jin Family's Cultivation Technique to perform Circulate Qi for Healing on others.",
    "Hayeon and Kim Jeonghee recovered substantially after receiving Circulate Qi for Healing from Taekyung; Hayeon also asked whether she could drop out of school after learning about his raid earnings.",
    "Taekyung's reality and Murim Inventories are separate.",
    "Peace Guild's Guild house remodeling is scheduled to finish in one week, and Taekyung is on paid vacation until then.",
    "Choi Minwoo and Butler Kim suspect that Taekyung may be a third-awakening Hunter; the possibility remains unconfirmed.",
    "Taekyung agreed to buy a meaningful former family home for 3.38 billion won, paid a ten-percent deposit, and plans to remodel it and move after Hayeon's college entrance examination.",
    "Park Jihwang changed his name to Park Jihoon and is now a Hunter in Team 1 of Myeongdong Guild; Taekyung judged Jihoon's strength comparable to or greater than Im Changsoo's.",
    "Hong Woojin is a B-rank mage and information broker investigating Taekyung through Familiars; he severed his rice-weevil Familiar's Link and plans more direct surveillance.",
    "Sangdong Guild's Team 1 Leader is the Guild's only A-rank Hunter besides Im Chunsoo and doubts the report of Taekyung's feats, while withholding Woojin's warning from Chunsoo.",
    "Peace Guild's Guild Master and Team Leader have personal and account information protected by a security Lock reportedly imposed by an upper agency.",
    "Taekyung's Qi Sense reaches seventy meters and detected the fly Familiars in his home; after Woojin severed the rice-weevil Link, Taekyung confirmed that no Familiar remained.",
    "Taekyung spent 350 million won at the Ilsan Store and stored the purchases in his Inventory.",
    "For a B-rank mage, Familiar connections reach up to 500 meters, with about 300 meters considered safe; forced Link severance causes physical distress and may cause mana backflow.",
    "Tiny Familiars evade most detection magic, leading Taekyung to conclude that the people who controlled the Familiars near his home yesterday were nearby and to decide he has another reason to catch them himself.",
    "Hayeon found an abandoned level-two Cat Familiar and received Kim Jeonghee's permission to foster it temporarily; Taekyung recognized it through the System."
  ],
  "continuity_sources": [
    94
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved.",
    "Whether Hayeon will actually drop out of school remains unresolved.",
    "Whether third-awakening Hunters exist and whether Taekyung is one remains unresolved.",
    "Why Hong Woojin is investigating Taekyung and what information he seeks remains unresolved.",
    "Whether Sangdong Guild sent the Familiars observing Taekyung remains unresolved.",
    "Who controls the Cat Familiar and whether it is connected to the surveillance remains unresolved."
  ],
  "safe_through": 94,
  "temporary_decisions": [
    "Use Frozen for 프로즌, preserve the tiger-father/dog-son wordplay in 호부견자, and use ajumma for 아줌마.",
    "Use goshiwon for 고시원 with an explanatory footnote; use Hope Goshiwon for 희망 고시원.",
    "Use Minsu for 민수; render 운기요상 as Circulate Qi for Healing, 하급 포션 as Lesser Potion, and 상급 포션 as Superior Potion.",
    "Render 3차 각성자 as third-awakening Hunter, 3차 각성 as third awakening, 피의 일주일 as Bloody Week, and 전세 as jeonse lease.",
    "Render 사장님 as Boss in the real-estate context, including young Boss.",
    "Render 박지황/박지훈 as Park Jihwang/Park Jihoon, and 삼계탕 as samgyetang with an explanatory footnote.",
    "Render 1팀장 as Team 1 Leader, 기감 as Qi Sense, and 락 as Lock when referring to security restrictions.",
    "Render 집파리, 검정파리, 금파리, and 패밀리어 as Housefly, Black Blow Fly, Green Bottle Fly, and Familiar; use Rice Weevil for 쌀벌레, Link for 링크, Store for 스토어, Assistant Manager for 대리, Kim Seonhee for 김선희 and the source variant 김희선, Ilsan for 일산, and Lafesta for 라페스타."
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
| 진하연    | **Jin Hayeon**    |
| 홍우진    | **Hong Woojin**   |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 링크 | **Link** | Mental connection between a mage and Familiar |

## Listed compact profiles

### Jin Hayeon.md

# Jin Hayeon (진하연)

- **Safe through:** Chapter 53
- **Aliases:** Hayeon; Taekyung’s younger sister
- **Role:** High-school senior preparing for the college entrance exam
- **Personality:** Sharp-tongued, academically gifted, impatient with Taekyung’s evasions, and warmer beneath the teasing
- **Voice:** Bratty, fast, blunt sibling banter; turns brighter when discussing school and her interests
- **Relationships:** Taekyung’s younger sister; daughter of Taekyung’s mother

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 93
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃95화



‘후후후. 성공이다.’

홍우진은 득의양양하게 웃었다. 그는 표적 대상의 일거수일투족을 감시하며 모든 정보를 읽어 내는 베테랑이다.

진태경의 여동생이 동물, 그중에서도 특히 고양이에 환장한다는 정보는 특히 유용했다.

“야옹아, 대답해 봐. 집 들어오니까 좋지?”

침투는 자연스러웠고, 성공적이었다. 새끼 고양이의 몸 안에 들어간 홍우진이 기쁨의 포효를 내질렀다.

미야오옹.

“꺄, 귀여워! 오빠, 방금 들었어? 들었어?”

“응. 들었다.”

“이런 귀여운 생물체를 두고 어떻게 그렇게 무심할 수가 있어? 사람이야?”

“그럼 내가 짐승이냐?”

문제는 진태경, 저놈이다.

아무리 감정이 메마른 사람이라고 해도 귀여운 동물, 특히 조그마한 새끼 앞에서는 마음이 말랑말랑해지기 마련인데…….

“옆으로 좀 비켜 봐. TV 화면 가리고 있잖아.”

이놈은 그딴 거 없다. 사하라 사막보다 건조한 감수성에 여동생, 진하연이 구시렁거렸다.

“어휴, 사람이 삭막해도 정도가 있지. 안 그래, 여름아?”

“여름이?”

“응. 여름에 태어났으니까 한여름. 이름 예쁘지?”

“한여름은 무슨. 덩치 보니까 3개월은 되어 보이는데 늦봄에 태어났으니까 늦봄이라고 하든가.”

“……그게 말이야, 방구야? 아무튼 얘 이름은 오늘부터 여름이야. 그치, 여름아?”

야오옹.

홍우진 입장에서는 진하연이 일등 공신이다. 덕분에 일이 술술 풀리고 있었다.

“꺄악! 대답했어! 여름이 방금 언니한테 대답한 거 맞죠? 그렇죠?”

미야옹.

“으헉, 내 심장!”

후후, 다루기 쉬운 녀석 같으니라고. 몇 번 울어 주기만 해도 아주 자지러진다.

‘이래서 여고생들이란…… 아니지, 내 패밀리어 선택이 탁월했던 거지.’

홍우진이 흐뭇하게 웃고 있던 그때.

멀뚱히 TV만 보고 있던 진태경이 한마디를 툭 던졌다.

“걔 수컷 아냐?”

“응? 그거야…….”

“아직 모르지?”

“그러고 보니 확인을 안 했어.”

“까 봐. 확인해 보자.”

어라?

일이 요상하게 돌아간다. 비록 몸은 고양이지만 홍우진은 혈기왕성한 청년. 진태경의 커다란 손이 다가오자 문득 수치심이 몰려왔다.

‘더러운 사내놈이 내 거기를 본다고?’

정확히 말하자면 홍우진의 몸은 아니다. 종(種)이 다른 만큼 신체 구조도 다르다.

그러나 패밀리어 마법은 시전자와 패밀리어가 모든 것을 공유한다. 그렇다 보니 기분이 더러워지는 건 어쩔 수 없었다.

‘절대 안 돼!’

홍우진은 황급히 진하연의 품속으로 파고들었다.

야오오옹.

“어머, 얘가 싫어하는 거 같은데?”

“원래 세상이 그래. 하고 싶은 거만 하면서 사는 사람이 어디 있어?”

“여름이는 고양이잖아.”

“고양이도 마찬가지야. 뜨신 사료에 간식으로 통조림 하나라도 얻어먹으려면 이 정도는 감수해야지.”

저런 미친놈. 고양이 성별 한번 확인해 보겠다고 말도 안 되는 소리를 지껄이네. 홍우진은 이를 갈며 유일한 희망인 진하연에게 매달렸다.

그녀의 팔에 온몸을 비비며 애처로운 눈빛을 발사하자 진하연의 눈동자가 스르륵 풀린다.

“어떡해. 귀여워서 미칠 것 같아.”

“그래, 귀여우니까 한번 까 보자.”

“다음에 해. 애가 무서워하잖아.”

“기분 탓이야.”

“여름이가 오빠 싫어하는 것 같다니까.”

타이밍에 맞춰 신음 한번 흘려 주는 게 포인트다.

끼양. 끼으응.

“봐 봐. 맞지?”

“……그럼 어쩔 수 없지.”

“괜히 애 억지로 만지고 그랬단 봐라. 새끼 고양이들은 예민해서 신경 써 줘야 한단 말이야.”

됐다. 당장 위기는 넘겼다. 진태경 이 녀석, 세상 혼자 사는 또라이 같아도 가족에게는 약한 놈이었다.

이미 상동 길드 측에서 건네준 사전 정보를 모두 숙지한 홍우진은 자신이 한 수 앞을 내다보고 있다고 생각했다.

‘이래서 정보가 중요하지. 넌 나한테 이미 걸려들었어.’

그러나 홍우진이 차마 몰랐던 사실이 있었다.

“동생아.”

“응?”

“용돈 더 안 필요하니?”

“……지금 나를 돈으로 매수해서 우리 여름이를 막, 농락하겠다 이거야?”

“어. 10만 원.”

“콜. 그 대신 너무 싫어하지 않게 살살 해야 돼?”

“내 방 책상에 지갑 있으니까 가져가.”

“꺅!”

미야옹?

총알처럼 사라지는 진하연의 뒷모습에 홍우진은 어이없는 마음을 담아 울음을 토해 냈다.

귀여워서 미칠 것 같다며? 우리 여름이라며?

‘저런 되바라진 것을 봤나.’

언제는 간이고 쓸개고 다 빼 줄 것처럼 굴더니 고작 10만 원에 우리 여름이를 버려?

그러나 자본주의 사회의 현실에 한탄하고 있을 틈 따위는 더 이상 주어지지 않았다.

“자, 이제 나랑 놀자.”

덥석.

번개 같은 속도로 사지를 결박한 진태경의 징글맞은 웃음.

홍우진은 절박한 심정으로 비명을 내질렀다.

‘놔! 놔, 이 새끼야!’

하악! 하아아악!

털을 바짝 세운 하악질 소리에 진태경의 지갑을 뒤지던 유일한 희망이 반응했다.

“오빠!”

“어, 10만 원 더 빼 가라.”

“고마워!”

야, 야!

유일한 희망이 자본주의의 노예로 타락했다!

충격이 채 가시기도 전에 진태경의 뜨거운 숨결이 훅 밀려왔다.

“우리 여름이, 고추 좀 볼까?”

절체절명의 순간.

‘링크(Link) 해제!’

미야오오옹!

구슬픈 울음소리와 함께 새끼 고양이의 몸에서 힘이 쭉 빠져나갔다.

그리고 어두컴컴한 어딘가에서 눈을 뜬 홍우진이 숨을 토해 냈다.

“푸하악!”

헌터 일을 시작하고 크고 작은 백여 건의 의뢰를 처리했지만 지금처럼 생명의 위협을 느낀 적은 처음이다.

소름이 오소소 돋은 팔뚝을 내려다본 그가 헛구역질을 시작했다.

“우욱.”

속이 울렁거리고 머리가 지끈지끈했다.

갑작스러운 링크 해제의 부작용이다. 미리 준비해 놓은 포션을 냉수처럼 들이켜고 나서야 홍우진은 한숨 돌릴 수 있었다.

“진태경, 이 개새끼 진짜…….”

처음으로 의뢰를 받은 게 후회되는 순간이었다.



* * *



[Lv.2 고양이]



“갔네, 갔어.”

나는 혀를 쯧쯧 차며 새끼 고양이를 놔주었다. 3개월이나 됐을까. 손바닥 두 개를 합친 것보다 작은 녀석이 어리둥절한 얼굴로 뒷걸음질 쳤다.

미야옹.

내 방을 나오던 하연이가 그 광경을 발견했다.

“우리 여름이한테 못된 짓 한 거 아니지?”

“그 여름이를 20만 원에 팔아넘긴 게 너고?”

“……흠. 흠.”

“됐다. 어휴, 주워 와도 꼭 저런 걸 주워 와서.”

“뭐래, 얘가 얼마나 귀여운데.”

“그게 아니라…… 아니다. 말을 말자.”

일일이 설명하기에는 길고 복잡한 얘기다. 설명해 줄 생각도 없고.

어떤 음흉한 놈이 고양이 몸 안에 들어가 우리를 관찰하고 있다고 말해 봐라. 얼마나 불안해할지 안 봐도 뻔한데. 지금 벌어지고 있는 일들을 가족들이 알아서는 안 된다.

‘어차피 나도 허락한 일이고.’

패밀리어를 집에 들인 이유는 하연이가 부탁해서, 엄마가 허락해서가 아니다.

‘내가 원해서지.’

누구의 의뢰인지는 몰라도 놈들은 당장 쫓아낸다 해도 계속해서 시도할 것이다.

패밀리어의 형태가 지난번처럼 벌레든, 오늘처럼 고양이든 그건 상관없다.

내가 패밀리어의 정체를 이미 알고 있으며, 언제든지 쳐 낼 수 있다는 사실이 중요하다.

‘분명 이 근방이야.’

집으로부터 최대 500m. 그 안에 패밀리어를 조종하는 마법사가 있다. 그놈을 털면 분명히 연결 고리가 나올 거다.

‘일단 아구창에 주먹 한 대 꽂고 물어봐야지.’

어차피 불법으로 민간인 사찰을 한 놈이니 때려도 신고 못 할 게 뻔하다. 제대로 손봐 줄 생각에 벌써 주먹이 근질거렸다.

‘감히 누구 집에서 깔짝대?’

오랜만의 휴가까지 방해받고 심지어 이 자식들 덕분에 쓴 돈도 3억이 훌쩍 넘어간다. 여러모로 손해 보는 장사가 아닐 수 없다.

잔뜩 구겨진 얼굴로 TV를 보고 있는데, 하연이가 슬금슬금 눈치를 살피며 입을 열었다.

“오빠, 화났어?”

“아니. 화날 게 뭐가 있어.”

“내가 미안해.”

“……왜 이러냐? 무서워지려고 하네.”

농담이 아니라 진짜다. 패밀리어를 처음 발견했을 때보다 더 놀랐다. 얘가 이런 말도 할 줄 알았나?

나는 진지하게 물었다.

“어디 아파?”

“아니 뭐, 그냥.”

“그럼 배고파?”

“그게 아니고…….”

뭔가 말하려던 하연이가 멈칫한 순간, 어디선가 꼬르륵 소리가 들려왔다.

나는 아니고. 엄마는 잠깐 볼일 보러 나가셨고.

“너 배고프지.”

“음, 살짝?”

“그래, 배고파서 헛소리까지 나오는구나. 내 지갑 어디 있는지 알지? 너 먹고 싶은 거 다 시켜.”

“진짜?”

“응. 10만 원 한도 내에서.”

“와, 돈 벌더니 통 커졌네. 우리 오빠.”

살다 살다 우리 오빠 소리도 들어 보는구나. 하연이가 중학생일 때 이후로 처음 듣는 말이라 소름이 돋았다.

“너 패밀리어지, 이 새끼야!”

“무슨 헛소리야. 암튼 그럼 10만 원 선에서 막 시킨다?”

“어, 아니네. 그래. 다 시켜.”

“남은 돈은?”

“……너 나한테 돈 맡겨 놨니?”

“다다익선.”

당당한 하연이의 모습에 기가 찼지만 한편으로는 기뻤다.

지금까지 용돈 달라는 소리 한번 없던 녀석이다. 입고 다니는 옷이나 평소 상태만 봐도 길거리에서 종종 마주치는 또래 애들에 비하면 한참 수수했다.

‘애늙은이 같은 녀석.’

생각해 보면 하연이는 어릴 때부터 그랬다. 쉽게 울지도 않았고 솔직하게 감정을 표현하는 일도 적었다. 지금 같은 성격이 된 것은 오히려 고등학교에 입학한 이후다.

가끔은 어리광을 피워도 될 텐데…… 너무 일찍 철이 들었다.

‘어쩌면 나보다도 훨씬.’

그래서 그런가? 녀석의 행동과 말이 하나도 얄밉지 않다. 오히려 기특하고 기뻤다.

“그래, 다 가져라, 다 가져.”

“진짜?”

“어.”

내 말에 하연이가 방긋 웃었다.

“다행이다. 괜히 미안할 뻔했네.”

“미안할 게 뭐가 있어.”

“아까 오빠 지갑에서 30만 원 빼 갔거든.”

“……어?”

“그런데 오빠가 10만 원 선에서 먹고 남은 거 다 가지라고 하니까 마음이 편해지네.”

“잠깐만, 내가 20만 원 가져가라고 하지 않았냐?”

“우발적 사고였어.”

“……우발적 범죄 아니냐?

아까 했던 말 취소.

콧노래를 부르며 방으로 들어가는 뒷모습이 얄밉기 짝이 없다.



* * *



상동 길드 보안팀장은 눈살을 찌푸렸다.

“고양이 패밀리어?”

“네, 확실합니다.”

단호한 목소리로 대답한 사람은 보안팀 소속이자 길드 유일의 패밀리어 마법사다. 헌터 등급은 C급에 불과하지만 희귀한 정신계 마법사라 보안팀의 핵심 멤버이기도 했다.

“표적의 여동생이 고양이 덕후랍니다. 빈틈을 잘 노렸어요.”

“분위기 파악 안 되냐? 지금 내 앞에서 그 새끼 칭찬이 나와?”

“죄, 죄송합니다.”

“1팀장님이 그러더라. 홍우진이가 전화해서 우리 때문에 바로 들킬 뻔했다고 지랄했대.”

“…….”

“뭐 따지고 보면 그 새끼도 우리 편이긴 하지. 근데 프리랜서한테 밀리면 되겠냐? 길드장님이 각별하게 신경 쓰고 계신 거 몰라?”

이번 일에 투입된 인원은 그를 포함해 총 여섯. 그중 하나는 패밀리어 마법사고 나머지 넷은 추적과 은신에 특화된 근접 헌터들, 마지막으로 팀장 본인은 B급 헌터였다.

“너희가 뭘 착각하나 본데…… 우리 C급 헌터 하나 털어 보자고 온 거 아니다.”

보안팀장은 험악한 얼굴로 팀원들을 응시했다.

이번 건은 길드장이 직접 지시한 일이다. 무조건 지시한 것 그 이상의 성과를 내야만 했다.

“잘하자. 이거 길드장님 직통이야. 너희 여기서 끝날 거야? 보너스도 받고 승진도 해야지.”

팀원들은 말없이 고개를 숙였다.

보너스와 승진이 가장 간절한 사람이 바로 보안팀장이다. 은퇴 시기가 슬슬 다가오는 중년 가장의 히스테리는 이제 와선 하루 이틀 일이 아니었다.

“그리고 너.”

보안팀장이 패밀리어 마법사를 지목했다.

“너도 고양이 해.”

“고양이요? 그건 이미 저쪽에서 했는데.”

“그럼? 괜히 컨트롤도 안 되는 초소형 패밀리어로 발연기 하다가 지난번처럼 뒤질래?”

“…….”

“시키는 대로 해. 여자애가 고양이 덕후라며?”

까면 까야지, 별수 있나. 한바탕 성질을 부린 보안팀장이 나간 뒤 패밀리어 마법사는 곧장 스마트폰을 켜서 검색을 시작했다.

틱. 틱. 틱.

[일산 고양이 분양]

“……이것도 영수증 처리해 주려나?”
```

## Final English reading copy

```markdown
# Chapter 95

*Heh heh heh. Success.*

Hong Woojin smiled smugly. He was a veteran at monitoring his targets’ every move and extracting every bit of information from them.

The information that Jin Taekyung’s younger sister was crazy about animals—cats in particular—had been especially useful.

“Meow-meow, answer me. You like being inside the house, don’t you?”

The infiltration had been natural and successful. Inside the kitten’s body, Hong Woojin let out a roar of joy.

“Miaowww.”

“Ahh, so cute! Oppa, did you hear that just now? You heard it, right?”

“Yeah. I heard it.”

“How can you be so indifferent to such a cute little creature? Are you even human?”

“Then what am I, a beast?”

The problem was Jin Taekyung.

Even the most emotionally dried-up person tended to soften in front of a cute animal, especially a tiny one, but…

“Move over a little. You’re blocking the TV.”

This guy had none of that. His sensitivity was drier than the Sahara Desert, and his younger sister, Jin Hayeon, grumbled.

“Good grief, there’s a limit to how bleak a person can be. Right, Yeoreum?”

“Yeoreum?”

“Yeah. Born in summer, so Midsummer. Pretty, right?”

“What do you mean, Midsummer? Judging by the size, the kitten looks about three months old. That would mean it was born in late spring, so call it Late Spring or something.”

“…Is that supposed to be a joke or what? Anyway, this kitten’s name is Yeoreum from today onward. Right, Yeoreum?”

“Mrowww.”

From Hong Woojin’s perspective, Jin Hayeon was his greatest asset. Thanks to her, everything was going smoothly.

“Ahh! Yeoreum answered! You just answered your big sister, didn’t you? Didn’t you?”

“Miaow.”

“Eek, my heart!”

*Heh. What an easy one to handle.* All it took was a few meows, and she practically melted.

*This is why high-school girls are… No, wait. It’s because my choice of Familiar was excellent.*

Hong Woojin was grinning contentedly when—

Jin Taekyung, who had been staring blankly at the TV, casually tossed out a remark.

“Isn’t that one male?”

“Huh? Well, that…”

“We don’t know yet, do we?”

“Come to think of it, I haven’t checked.”

“Let’s take a look. We can find out.”

Huh?

Things were taking a strange turn. His body might have been a cat’s, but Hong Woojin was a vigorous young man. When Jin Taekyung’s large hand approached, a sense of shame suddenly washed over him.

*That filthy bastard is going to look at my junk?*

Strictly speaking, it wasn’t Hong Woojin’s body. Since the species were different, the physical structures were different, too.

However, Familiar magic made the caster and the Familiar share everything. There was no helping the disgust he felt.

*Absolutely not!*

Hong Woojin hurriedly burrowed into Jin Hayeon’s arms.

“Mrowww.”

“Oh my, I don’t think the kitten likes that.”

“That’s how the world works. Who gets to live doing only what they want?”

“But Yeoreum’s a cat.”

“Cats are the same. If you want warm feed and even a can of treats, you have to put up with this much.”

What a lunatic. He was spouting ridiculous nonsense just because he wanted to check a cat’s sex. Grinding his teeth, Hong Woojin clung to his only hope, Jin Hayeon.

He rubbed his entire body against her arm and gave her a pitiful look. Her eyes slowly softened.

“What am I going to do? Yeoreum’s so cute I could die.”

“Yeah, very cute. So let’s take a look.”

“Do it next time. You’re scaring the kitten.”

“That’s just your imagination.”

“I told you, Yeoreum doesn’t like you, Oppa.”

The key was to let out a groan at exactly the right moment.

“Mnyaa. Mngh.”

“See? I’m right, aren’t I?”

“…Then I can’t help it.”

“Don’t you dare force the kitten to let you handle it. Kittens are sensitive, so you have to be careful with them.”

Good. He had gotten past the immediate crisis. Jin Taekyung seemed like a lunatic who lived in his own world, but he was weak when it came to his family.

Having fully absorbed all the background information Sangdong Guild had given him, Hong Woojin thought he was one step ahead.

*This is why information matters. You’ve already fallen right into my trap.*

But there was one fact Hong Woojin had never imagined.

“Hey, Sis.”

“Yeah?”

“Do you need more spending money?”

“…Are you trying to bribe me so you can mess with our Yeoreum?”

“Yeah. A hundred thousand won.”

“Deal. But you have to be gentle so she doesn’t hate you too much, okay?”

“My wallet’s on the desk in my room. Go get it.”

“Eek!”

“Miaow?”

Jin Hayeon disappeared like a bullet. Hong Woojin let out a cry filled with disbelief.

*You said she was so cute you could die. You called her our Yeoreum!*

*What a shameless little brat.*

One minute she had acted ready to give Yeoreum anything, and now she was abandoning “our Yeoreum” for a mere hundred thousand won?

But he was given no time to lament the realities of a capitalist society.

“Come on. Let’s play.”

He grabbed him.

Jin Taekyung restrained all four of his limbs with lightning speed and smiled horribly.

Hong Woojin screamed desperately.

*Let go! Let go, you son of a bitch!*

“Hiss! Hissss!”

The kitten’s fur stood on end as Hong Woojin hissed, catching the attention of his only hope as she rummaged through Jin Taekyung’s wallet.

“Oppa!”

“Yeah, take another hundred thousand won.”

“Thanks!”

*Hey! Hey!*

His only hope had become a slave to capitalism!

Before the shock had even worn off, Jin Taekyung’s hot breath swept over him.

“Our Yeoreum, shall we take a look at your little peepee?”

At that desperate, life-or-death moment—

*Sever Link!*

“Miaowww!”

With a sorrowful cry, all the strength drained out of the kitten’s body.

Then Hong Woojin opened his eyes somewhere dark and let out a breath.

“Puhack!”

Since starting work as a Hunter, he had handled more than a hundred large and small assignments, but this was the first time he had ever felt his life was in danger.

He looked down at his forearms, which were covered in goose bumps, and began to gag.

“Urgh.”

His stomach churned, and his head throbbed.

It was a side effect of the sudden Link severance. Only after he gulped down the potion he had prepared in advance like cold water could Hong Woojin finally catch his breath.

“Jin Taekyung, you fucking bastard…”

It was the moment he first regretted ever accepting the assignment.

* * *

> **System**
>
> **Lv. 2 Cat**

“There he goes.”

Clicking my tongue, I let the kitten go. Was it three months old? The little thing, smaller than my two joined palms, backed away with a bewildered expression.

“Miaow.”

Hayeon was leaving my room when she spotted what had happened.

“You didn’t do anything mean to our Yeoreum, did you?”

“And you’re the one who sold Yeoreum for 200,000 won?”

“…Ahem. Ahem.”

“Whatever. Good grief. Whenever you pick something up, it has to be something like that.”

“What are you talking about? Look how cute Yeoreum is.”

“That’s not what I meant… Never mind. Forget it.”

It was a long and complicated story to explain one detail at a time. Besides, I had no intention of explaining it.

If I told her that some sinister bastard had entered the body of a cat and was watching us, it was obvious how anxious she would become. My family couldn’t find out about what was happening.

*Besides, I was the one who had allowed it.*

The reason I had let a Familiar into the house wasn’t because Hayeon had asked or because Mom had given her permission.

*It was because I wanted it.*

I didn’t know who had hired them, but even if I drove them off now, they would keep trying.

It didn’t matter whether the Familiar took the form of an insect like last time or a cat like today.

What mattered was that I already knew what the Familiar was and could swat it away whenever I wanted.

*They’re definitely somewhere around here.*

Within 500 meters of the house. Somewhere inside that radius was a mage controlling the Familiar. If I roughed him up, I was sure I’d find the connection.

*First, I’ll punch him in the mouth, then ask some questions.*

He had illegally surveilled a civilian, so there was no way he could report me even if I beat him. Just thinking about teaching him a proper lesson made my fists itch.

*How dare they snoop around someone’s house?*

They had interrupted my first vacation in a long time, and thanks to these bastards, I had already spent well over 300 million won. In every respect, this was a losing proposition.

I was watching TV with my face twisted into a scowl when Hayeon cautiously watched my reaction and spoke.

“Oppa, are you mad?”

“No. What is there to be mad about?”

“I’m sorry.”

“…What’s gotten into you? You’re starting to scare me.”

I wasn’t joking. I was more startled than when I had first discovered the Familiar. Since when could she say something like that?

I asked seriously.

“Are you sick?”

“No, it’s just…”

“Then are you hungry?”

“That’s not it…”

Just as Hayeon hesitated, apparently about to say something, a stomach growled from somewhere.

It wasn’t mine. Mom had stepped out to run an errand.

“You’re hungry.”

“Mm, a little?”

“Right. You’re so hungry you’re starting to spout nonsense. You know where my wallet is, right? Order anything you want to eat.”

“Really?”

“Yeah. Up to 100,000 won.”

“Wow, now that you’re making money, you’ve gotten generous, Oppa.”

In all my life, I never thought I’d hear her call me “our Oppa.” It was the first time I’d heard it since Hayeon had been in middle school, and it gave me goose bumps.

“You’re the Familiar, you little bastard!”

“What are you talking about? Anyway, can I order whatever I want as long as it’s under 100,000 won?”

“Yeah. No, wait. Fine. Order everything you want.”

“What about the money left over?”

“…Did you leave your money with me?”

“More is better.”

I was dumbfounded by Hayeon’s shamelessness, but at the same time, I was happy.

She had never once asked me for spending money. Even judging by the clothes she wore and her usual appearance, she was far more modest than the kids her age I occasionally saw on the street.

*What an old soul.*

Come to think of it, Hayeon had been like that since she was little. She rarely cried, and she didn’t often express her feelings honestly. Her current personality had only developed after she entered high school.

*She ought to be allowed to act spoiled once in a while… She grew up too soon.*

*Maybe even much sooner than I did.*

Maybe that was why. None of her actions or words annoyed me in the slightest. If anything, I found her admirable, and I was happy.

“Fine. Take it all. Take everything.”

“Really?”

“Yeah.”

Hayeon beamed at my words.

“That’s a relief. I almost felt bad for nothing.”

“What’s there to feel bad about?”

“I took 300,000 won from your wallet earlier.”

“…Huh?”

“But when you said I could have whatever was left after eating within the 100,000-won limit, I felt better.”

“Hold on. Didn’t I tell you to take 200,000 won?”

“It was an accident.”

“…Don’t you mean a crime of opportunity?”

I take back what I said earlier.

The sight of her back as she hummed her way into her room couldn’t have been more irritating.

* * *

The head of Sangdong Guild’s Security Team frowned.

“A Cat Familiar?”

“Yes, I’m certain.”

The person who answered in a firm voice was a member of the Security Team and the Guild’s only Familiar mage. He was only a C-rank Hunter, but he was also a core member of the Security Team because mental mages were rare.

“The target’s younger sister is a cat fanatic. Hong Woojin took advantage of that opening perfectly.”

“Can’t you read the room? You’re praising that bastard in front of me?”

“I-I’m sorry.”

“Team 1 Leader said Hong Woojin called and went ballistic, saying he nearly got exposed because of us.”

“…”

“Come to think of it, that bastard is technically on our side, too. But can we afford to be outdone by a freelancer? Don’t you know the Guild Master is taking a special interest in this?”

Six people had been assigned to this operation, including the Security Team Leader. One was the Familiar mage, four were close-combat Hunters specializing in tracking and stealth, and the Team Leader himself was a B-rank Hunter.

“I think you’re under a misconception… We didn’t come here just to dig up dirt on one C-rank Hunter.”

The Security Team Leader glared at his team with a menacing expression.

The Guild Master had personally ordered this operation. They had to produce results that went beyond the direct order, no matter what.

“Let’s do this properly. This came straight from the Guild Master. Are you going to let your careers end here? You want bonuses and promotions, don’t you?”

The team members silently lowered their heads.

The person most desperate for a bonus and promotion was the Security Team Leader himself. The hysteria of a middle-aged family man whose retirement was slowly approaching was nothing new by this point.

“And you.”

The Security Team Leader pointed at the Familiar mage.

“You do the cat, too.”

“The cat? They already did that over there.”

“What, then? Are you going to put on another pathetic performance with a tiny Familiar you can’t even control and die like last time?”

“…”

“Do as you’re told. The girl’s a cat fanatic, isn’t she?”

If they wanted a cat, he had to use a cat. What else could he do?

After the Security Team Leader stormed out, the Familiar mage immediately turned on his smartphone and began searching.

Tap. Tap. Tap.

> **Ilsan Cat Adoption**

“…Do you think this will count as a business expense?”
```
