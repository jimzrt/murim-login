<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0094.txt",
      "sha256": "589153965b1f5aa44fe9daedbf319a2716f41c2bfe93b6aab628447d9da137f3",
      "bytes": 13305
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "88ab09f0da7c102fa47cc71d36fbaaea958aedc5f239cc0ff58b908ac3e62c49",
      "bytes": 4902
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a0a5963251181c3ec49eba4e01928e60f739fc2e7f771a71dd850e4ff9288281",
      "bytes": 11191
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "22ed1b9292d24a17dcfad62a32ce41a3a3c6285e68992e1774874c5ca2c2d109",
      "bytes": 9609
    }
  ],
  "estimated_tokens": 14307
}
-->

# Durable State Update — Chapter 94

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 94. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 94. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 94,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 94,
    "continuity_sources": [94],
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
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild.",
    "Im Chunsoo is Sangdong Guild's A-rank Guild Master and founder, known as Frozen; he ordered expanded surveillance of Taekyung through Sangdong's Audit Team.",
    "Im Changsoo transferred the promised four billion won to Jin Taekyung after Im Chunsoo learned about his transfers and beat him.",
    "Kim Jeonghee is Taekyung and Hayeon's mother; she secretly worked in a restaurant kitchen for over a year and quit after the owner insulted and attacked Taekyung.",
    "Taekyung's father died when a Gate opened downtown during the Great Cataclysm.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Taekyung is a C-rank Hunter who reawakened from F-rank, defeated B-rank Minotaurs, and can use the Jin Family's Cultivation Technique to perform Circulate Qi for Healing on others.",
    "Hayeon and Kim Jeonghee recovered substantially after receiving Circulate Qi for Healing from Taekyung; Hayeon also asked whether she could drop out of school after learning about his raid earnings.",
    "Taekyung's reality and Murim Inventories are separate.",
    "Peace Guild's Guild house remodeling is scheduled to finish in one week, and Taekyung is on paid vacation until then.",
    "Choi Minwoo and Butler Kim suspect that Taekyung may be a third-awakening Hunter; the possibility remains unconfirmed.",
    "Sangdong Guild is monitoring Peace Guild and has marked Taekyung as a major target; Choi has not warned him because he wants Sangdong's investigation to reveal more.",
    "Taekyung agreed to buy a meaningful former family home for 3.38 billion won, paid a ten-percent deposit, and plans to remodel it and move after Hayeon's college entrance examination.",
    "Park Jihwang changed his name to Park Jihoon and is now a Hunter in Team 1 of Myeongdong Guild; Taekyung judged Jihoon's strength comparable to or greater than Im Changsoo's.",
    "Hong Woojin is a B-rank mage and information broker investigating Taekyung through Familiars; he severed his rice-weevil Familiar's Link in this chapter and plans more direct surveillance.",
    "Sangdong Guild's Team 1 Leader is the Guild's only A-rank Hunter besides Im Chunsoo and doubts the report of Taekyung's feats, while withholding Woojin's warning from Chunsoo.",
    "Peace Guild's Guild Master and Team Leader have personal and account information protected by a security Lock reportedly imposed by an upper agency.",
    "Taekyung's Qi Sense reaches seventy meters and detected the fly Familiars in his home; after Woojin severed the rice-weevil Link, Taekyung confirmed that no Familiar remained.",
    "Taekyung visited the Ilsan Lafesta Store and began ordering boxes of low-rank Hunter weapons to fill his Inventory."
  ],
  "continuity_sources": [
    93
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved.",
    "Whether Hayeon will actually drop out of school remains unresolved.",
    "Whether third-awakening Hunters exist and whether Taekyung is one remains unresolved.",
    "Why Hong Woojin is investigating Taekyung and what information he seeks remains unresolved.",
    "Whether Sangdong Guild sent the Familiars observing Taekyung remains unresolved.",
    "What Familiar form Hong Woojin will use for his next surveillance attempt remains unresolved."
  ],
  "safe_through": 93,
  "temporary_decisions": [
    "Use Frozen for 프로즌, preserve the tiger-father/dog-son wordplay in 호부견자, and use ajumma for 아줌마.",
    "Use goshiwon for 고시원 with an explanatory footnote; use Hope Goshiwon for 희망 고시원.",
    "Use Minsu for 민수; render 운기요상 as Circulate Qi for Healing and 하급 포션 as Lesser Potion.",
    "Render 3차 각성자 as third-awakening Hunter, 3차 각성 as third awakening, 피의 일주일 as Bloody Week, and 전세 as jeonse lease.",
    "Render 사장님 as Boss in the real-estate context, including young Boss.",
    "Render 박지황/박지훈 as Park Jihwang/Park Jihoon, and 삼계탕 as samgyetang with an explanatory footnote.",
    "Render 1팀장 as Team 1 Leader, 기감 as Qi Sense, and 락 as Lock when referring to security restrictions.",
    "Render 집파리, 검정파리, 금파리, and 패밀리어 as Housefly, Black Blow Fly, Green Bottle Fly, and Familiar; use Rice Weevil for 쌀벌레, Link for 링크, Store for 스토어, Assistant Manager for 대리, Kim Seonhee for 김선희, Ilsan for 일산, and Lafesta for 라페스타."
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

| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |

## Listed compact profiles

(No chapter-safe profiles matched.)

## Korean source

```text
＃94화



“3억 5천만 원입니다.”

계산하는 직원의 목소리도 떨리고, 카드를 건네는 내 손도 떨린다.

세상에, 3억 5천만 원이라니. 개처럼 일하던 시절의 3년 치 연봉을 불과 한 시간 만에 다 써 버렸다.

‘아냐. 좋게 생각하자.’

감시자들로부터 가족을 지키기 위해 쓰는 돈이다.

어차피 돈은 앞으로 계속 벌면 되고, 오늘 산 물건들은 두고두고 쓸 수 있다.

삑.

- 승인이 완료되었습니다.

“결제 완료했습니다.”

덕분에 이 아가씨만 로또 맞았군. 입이 귀에 걸린 김희선 대리에게 카드를 돌려받았다.

“그럼 끝난 거죠?”

“아, 주소를 알려 주시면 저희가 배송해 드립니다.”

“괜찮아요. 바로 가 볼 데가 있어서.”

배송은 무슨. 사람들의 시선에서 벗어나는 즉시 인벤토리에 보관하면 끝이다.

‘시스템이 이럴 때 편리하단 말이야.’

그런 생각을 하며 쇼핑백을 양손 가득 받아 들었다. 물론 그냥 종이 쇼핑백이 아니다. 오우거 가죽으로 만들었다는 질기고 튼튼한 가죽 쇼핑백이다. 사은품으로 받은 건데 기쁘기는커녕 속이 쓰리다.

“그럼 수고하세요.”

“다음에 꼭! 다시 찾아 주십시오.”

“……아, 네.”

허리를 직각으로 푹 숙이며 내미는 그녀의 명함을 건네받았다.

실적에 미친 자, 그의 이름은 판매 사원.



* * *



근처 화장실에 들러 스토어에서 산 물건들을 인벤토리에 수납한 뒤 택시를 잡았다. 운전면허를 못 딴 게 후회되는 요즘이다.

“일산 A아파트로 가 주세요.”

조수석에 앉자마자 스마트폰을 꺼내 정보를 검색했다.

검색어는…….

‘패밀리어.’

검색 버튼을 누르기가 무섭게 관련 정보가 촤르륵 떴다.

일반인들은 보지 못하는, 헌터 인증을 해야만 열람 가능한 정보도 상당수였는데, 그중 제법 시선을 끄는 제목이 하나 있었다.



유머X 패밀리어 마법 쓰지 마라. 탈모 왔다.



그야말로 영혼을 울리는 제목이다. 클릭 안 할 수가 없지.

‘아, 여기 올라온 글이었네.’

글이 게시된 사이트는 유명한 국내 헌터 커뮤니티였다.

해당 게시글은 월간 베스트에 조회수가 10만, 댓글이 2천 개가 넘어가는 위엄을 보였다.

‘어디 한 번 읽어 볼까.’

클릭!



유머X 패밀리어 마법 쓰지 마라. 탈모 왔다.



현직 B급 마법사다.

나름 짬밥 좀 먹었고 프리랜서 헌터로 짭짤하게 돈 벌고 있다. 정확한 스펙을 밝히지 못하는 건 양해 바람.

아무튼 이 글을 쓰게 된 이유는 제목 그대로다.

나 패밀리어 마법 때문에 탈모빔 맞았다…….

아직 20대인데 정수리는 2천 년 된 미라랑 동기 동창이다, 시발 거.

태클 거는 새끼들 있을까 봐 미리 말해 두는데 우리 집안은 대대로 풍성충이다. 일제 강점기 때 찍은 증조할아버지 사진도 봤는데 조선의 라푼젤임.

각설하고, 패밀리어 마법. 이거 진짜 양날의 검이다.

나처럼 법사 하는 애들은 알 건데 정신계 마법이 흔한 게 아니거든. 민간인들도 기술 하나 배우면 먹고는 살잖아.

법사한테는 정신계가 딱 그래. 이거 하나 있으면 어떻게든 잘 먹고 잘 산다.

근데 시발, 머리가 빠져. 계속 빠져.

여기 상급 포션으로 머리 감아 본 놈 있냐? 난 해 봤다.

머리 한 번 감는데 몇천만 원을 썼다고 미친 놈들아. 그 정도로 별 지랄을 다 해 봤는데 그것도 잠깐이야.

하다 하다 안 돼서 민간 의사 찾아갔더니 이 새끼가 한숨 푹 내쉬면서 그러더라.

정신계 마법사시죠?

진짜 토씨 한 글자 안 틀리고 저랬음. 깜짝 놀라서 어떻게 알았냐고 물었더니 리얼 소름 돋는 얘기 해 주더라.

정신계 법사 중 90퍼 이상이 탈모고, 특히 그중에서도 난이도가 있는 패밀리어 마법 쓰는 놈들은 100퍼센트래.

머리를 존나 혹사시키니까 어느 순간부터 풍성충도 탈모충이 된다는 거지.

처음에는 무슨 헛소리를 하는 거지 싶었는데 알아보니까 사실이더라고.

부랴부랴 정신계 법사 카페 가입해서 나 같은 놈 있는지 찾아봤는데 뭔 카페 회원 100명 중에 98명이 탈모야.

내 상황 듣더니 이미 늦었다고, 포션 그거 일시적으로 세포 회복시켜 주는 거라 자주 쓰면 모발 세포만 죽는대.

카페 게시판에 진료 후기 써 주면 등업 시켜 준다는 거 쌩 까고 탈퇴 후 나만의 치료법을 찾고 있다…….

세줄 요약.

1. 정신계 마법사 좋다. 근데 그 대신 머리 빠짐.

2. 포션 써 봤자 헛수고다. 차라리 탈모 방지 샴푸에 민간 병원을 가라. 모발은 마음과 간절함으로 치료해야지, 마법으로 치료하려고 하면 안 됨.

3. 난 포기하지 않는다.

그럼 이만.



“…….”

다 읽고 나니 눈앞이 뿌옇게 흐려진다. 항상 부러워했던 마법사들, 다 가졌을 것 같던 그들에게도 이런 고충이 있었다니.

“손님, 괜찮으세요?”

“전 괜찮…… 으흡.”

“왜 그러세요?”

“아, 아닙니다. 괜찮아요.”

이 상황에 하필이면 택시 아저씨도 대머리다. 나는 죄인의 심정으로 스마트폰을 향해 고개를 떨궜다.

게시글 아래 2천 개가 넘어가는 댓글이 보인다.



익명#232 : 한 줄 요약해 주라.

└ 작성자 : [심한 욕설로 블라인드 처리된 댓글입니다.]



익명#112 : 첫 댓글 사람 새끼 맞냐? 난 울었다. 응원할게 힘내.

└ 작성자 : 고맙다...



익명#1512 : 다른 건 모르겠고 두 번째 댓글도 탈모인인 듯. 근데 쭉 읽어 보니까 돈 많이 버는 것 같던데 모발 좀 없어도 되지 않냐. 가발 좋은 거 쓰면 되잖아.

└ 작성자 : [심한 욕설로 블라인드 처리된 댓글입니다.]



익명#4885 : 와, 패밀리어 법사를 여기서 보네. 너희가 몰라서 그렇지 작성자 리얼 귀족임. 같은 B급이어도 수입 면으로는 비교가 안 된다. 대우도 그렇고.

└ 작성자 : 돈 많으면 뭐 하냐. 머리가 없는데.

└ 익명#4885 : 생각해 보니까 그러네.

└ 작성자 : 위로해 줄 거면 끝까지 해, 이 새끼야.

.

.

.

운영자 : 축하드립니다! 인기 게시글로 선정되셨습니다!

└ 익명#5252 : ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ 익명#8984 : ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ 작성자 : 이걸 웃어야 되냐 말아야 되냐.

└ 익명#2652 : 지금 모발이 없는데 웃음이 나와?

└ 작성자 : [심한 욕설로 블라인드 처리 된 댓글입니다.]



작성자 : 열화와 같은 성원 고맙다. 월간 베스트 찍고 명예의 전당 가게 생겼네. 혹시 궁금한 점 있으면 아래로 댓글 달아라. 지금 일 중이긴 한데 틈틈이 들어와서 대답해 줌.

└ 익명#9665 : 프리랜서라고 했는데 주로 어떤 일 함?

└ 작성자 : 말이 좋아서 프리랜서지 하는 일은 흥신소랑 비슷해. 일급 범죄자(물론 헌터) 추적도 해 봤고 졸부 집 불륜 사건도 맡아 봤다.

└ 익명#915 : 오... 많이 벌겠네. 수입 얼마나 되냐.

└ 작성자 : 그거야 어떤 의뢰냐에 따라 다르지. 그래도 몇 년 일해서 서울에 건물 하나 올렸다. 지금 사는 집도 내 명의로 된 거고.

└ 익명#5252 : 집 인증해 봐.

└ 작성자 : 일 중이라 밖에 나와 있어. 나중에 제대로 인증할 테니까 그때 봐라.

└ 익명#9882 : 일 중인 거랑 뭔 상관이냐. 패밀리어 어차피 원격 조종 아님?

└ 작성자 : 아무리 원격 조종이어도 거리 제한이 있지 병신아. 넌 미국 여행 가서도 너희 집 와이파이 쓰냐?

└ 익명#9882 : ㅈㅅ

└ 작성자 : 패밀리어 연결 거리는 최대 500미터가 한계야. 조금씩 거리 늘리고는 있는데 힘들더라. 강제로 링크 해제되면 속 울렁거리고 토할 것 같음. 마나 역류 위험도 있고.

└ 익명#9882 : 그럼 500미터 안에는 무조건 있어야겠네.

└ 작성자 : ㅇㅇ 안전하게 작업하려면 한 300미터? 혹시 모를 사태를 대비해야 되니까. 아마 대부분이 그럴 거야.



댓글들을 쭉 읽어 내리다가 멈칫했다.

지금 뜻하지 않게 중요한 정보를 발견한 것 같은데?

‘500m를 벗어나면 패밀리어와의 연결이 끊긴다고?’

최대 거리가 그 정도고 안전한 작업을 위해서는 300m라니.

즉, 작성자의 댓글이 사실이라면 어제 패밀리어를 부린 놈들은 우리 집에서 얼마 떨어지지 않은 곳에 있었다는 뜻이다.

‘그리고 머리가 벗겨져 있겠지. 완전히 대머리거나.’

가발을 쓰고 있을 가능성이 농후하지만 알고 있어서 나쁠 건 없다.

나는 그 후로도 계속 패밀리어 마법에 관한 정보를 검색했고, 몇 가지 사실을 정리할 수 있었다.

‘B급 마법사 기준 패밀리어 연결 거리는 최대 500m. 안전 거리 300m. 패밀리어가 죽을 경우 강제로 링크가 해제되며 시전자도 약간의 타격을 입는다.’

그리고 하나 더, 왜 굳이 몸값 비싼 패밀리어 마법사로 나를 감시하는지도 깨달았다.

‘뭐야, 이거. 초소형 패밀리어는 어지간한 탐지 마법에도 안 걸린다고?’

예를 들자면 그런 거다. 탐지 마법은 그물이고, 파리나 쌀벌레 같은 소형 패밀리어는 그물에 걸리지 않을 만큼 작으니 걸릴 리가 없다.

물론 그것까지 잡아내는 최상급 탐지 마법이 내장된 제품도 있긴 한데 찾아보니 여름 특가로 5억 5천이란다.

“…….”

도대체 어느 부분에서 여름 특가인지 모르겠다. 가뜩이나 앞으로 돈 나갈 구석도 많은데 5억은 얼어 죽을.

‘직접 잡아야 할 이유가 하나 더 늘었군.’

문득 다른 길드원들에게도 생각이 미쳤다. 과연 패밀리어가 우리 가족에게만 붙었을까?

사주한 범인의 정확한 정체도 아직 모른다. 상동 길드는 유력한 용의자일 뿐이다.

“8천 4백 원이요.”

“아, 네. 여기요.”

택시비를 지불하고 차에서 내렸다. 항상 똑같았던 아파트 단지 입구가 오늘은 좀 낯설다.

목구멍에 걸린 가시처럼, 감시자의 존재가 거슬렸다.

‘최 팀장한테 연락을 해 봐야 되나.’

스마트폰에 저장된 그의 번호를 보며 고민하던 그때였다.

“오빠!”

낯익은 초록색 추리닝에 동그란 안경. 떡 진 머리를 뒤로 질끈 묶은 백조 한 마리가 날 보며 손을 흔든다.

“어, 으응.”

“뭐야, 그 반응은?”

“왠지 밖에서는 알은척하고 싶지 않다고 해야 할까. 부끄럽다고나 할까…….”

“하나뿐인 여동생이 부끄러워? 어?”

“옷이나 사 입어라. 지난번에 백화점에서 산 옷은 놔뒀다 뭐 하고 또 추리닝이야?”

“오빠나 잘해. 맨날 비슷한 옷만 입고 다니는 주제에.”

하연이의 일침에 순간 할 말을 잃었다. 불과 한두 시간 전에 3억을 결제했는데 입고 있는 옷은 아직도 청바지와 티셔츠뿐이다. 27년 동안 박혀 있던 소시민의 묵은 때가 덜 벗겨진 모양이다.

“아, 아무튼. 어디 가는 길이야?”

“어디 가냐고? 편의점!”

방금까지만 하더라도 뚱해 있던 하연이가 이번엔 실실 웃기 시작한다.

얘가 왜 이래? 난 떨떠름한 목소리로 물었다.

“왜 이렇게 신났냐? 편의점 털어 올 생각에 벌써부터 가슴이 두근거려?”

“털어 오긴 무슨. 참치 통조림 사 올 건데.”

“참치 통조림? 오늘 점심 참치 김치찌개야?”

“아니! 아닌데!”

“……오늘 왜 이래, 진짜? 술 마셨어?”

“오빠도 얘 보면 그렇게 될걸.”

내 반응에도 평소와 달리 히죽거리기만 하던 하연이가 추리닝 지퍼를 내리고 품 안에서 뭔가를 꺼내 들었다. 하얗고 노란, 조그마한 털 뭉치 하나가 손바닥 안에서 꼬물거린다.

야오옹.

“……새끼 고양이?”

“귀엽지? 아까 분리수거 하러 갔는데 누가 박스에 버려 놨더라고. 기르고 싶은 사람 기르라고.”

“…….”

“어떤 놈이 버렸는지 몰라도 불쌍하잖아. 얘는 뭔 죄야? 안 그래, 오빠?”

“……그래. 동물이 무슨 죄냐.”

“엄마한테 허락받아서 잠깐이라도 임시 보호 하기로 했어. 오빠도 괜찮지?”

“나?”

“응, 우리 김 여사가 장남한테 껌뻑 죽잖아. 오빠 허락도 받으라는데 이따 들어가서 말 좀 잘 해 주라.”

“글쎄.”

“뭐야. 어릴 땐 동물 좋아했잖아.”

좋아했지. 아니, 지금도 좋아한다. 하지만 하연이의 손바닥에 얌전히 안겨 있는 이 녀석은…….



[Lv.2 고양이 – 패밀리어]



좀, 다르다.
```

## Final English reading copy

```markdown
# Chapter 94

“Three hundred fifty million won.”

The employee’s voice trembled as she ran the payment, and so did my hand as I handed over the card.

*Good lord. Three hundred fifty million won?* I had just spent three years’ worth of salary from back when I worked like a dog in barely an hour.

*No. Let’s look on the bright side.*

This was money spent to protect my family from the people watching us.

I could keep earning money from now on, anyway, and I could use the things I bought today for a long time.

Beep.

- Approval complete.

“Your payment has gone through.”

Thanks to me, this young lady was the only one who had hit the lottery. I took my card back from Assistant Manager Kim Seonhee, whose smile stretched from ear to ear.

“So that’s everything, right?”

“Ah, if you give us your address, we can have everything delivered.”

“That’s all right. I have somewhere to go right now.”

Delivery, my ass. The moment I got out of everyone’s sight, I could just store everything in my Inventory.

*The System sure is convenient at times like this.*

Thinking that, I accepted the shopping bags until both my hands were full. Of course, they weren’t ordinary paper bags. They were tough, sturdy leather shopping bags supposedly made from ogre hide. They had been free gifts, but instead of feeling happy, they just made my stomach hurt.

“Take care.”

“Please come back next time! We look forward to seeing you again.”

“…Ah, yes.”

I accepted the business card she held out while she bent at the waist at a perfect right angle.

*One obsessed with sales figures. Their name: salesperson.*

* * *

I stopped by a nearby restroom and stored the things I had bought at the Store in my Inventory before hailing a taxi. These days, I regretted never getting my driver’s license.

“Please take me to Apartment A in Ilsan.”

The moment I sat in the passenger seat, I pulled out my smartphone and started searching for information.

The search term was…

*Familiar.*

The moment I pressed the search button, related information came streaming onto the screen.

There was quite a bit of information that ordinary people couldn’t see and that required Hunter certification to access. One title in particular caught my eye.



No Joke: Don’t Use Familiar Magic. It Made My Hair Fall Out.



It was a title that resonated with my soul. There was no way I could not click it.

*Ah, so this was where it was posted.*

The post was on a famous domestic Hunter community site.

It had been selected as a monthly best post, with over one hundred thousand views and more than two thousand comments.

*Let’s see what it says.*

Click!



No Joke: Don’t Use Familiar Magic. It Made My Hair Fall Out.



I’m a currently active B-rank mage.

I’ve been in the business for a while and make decent money as a freelance Hunter. Please understand that I can’t reveal my exact specifications.

Anyway, the reason I’m writing this post is exactly what the title says.

I got hit by a hair-loss beam because of Familiar magic…

I’m still in my twenties, but the top of my head is classmates with a two-thousand-year-old mummy. Goddamn it.

Before anyone starts nitpicking, let me say this in advance: My family has always been blessed with thick hair. I even saw a photograph of my great-grandfather taken during the Japanese occupation, and he looked like Rapunzel of Joseon.

Anyway, back to Familiar magic. This stuff is a real double-edged sword.

Any of you guys who are mages will know this, but mental magic isn’t exactly common. Even civilians can make a living once they learn a skill.

For a mage, mental magic is exactly like that. If you have this one thing, you can live well no matter what.

But fuck, your hair starts falling out. It keeps falling out.

Anyone here ever tried washing their hair with a Superior Potion? I have.

You crazy bastards, I spent tens of millions of won washing my hair just once. I tried every kind of crazy shit imaginable, but even that only worked for a little while.

When none of it worked, I went to a regular doctor, and the bastard let out a long sigh and said:

“You’re a mental-magic mage, aren’t you?”

He said it exactly like that, without getting a single word wrong. I was shocked and asked how he knew, and then he told me something genuinely horrifying.

More than ninety percent of mental-magic mages suffer from hair loss, and the rate is one hundred percent among those who use the more difficult Familiar magic.

Apparently, because we overwork our brains like crazy, even people with thick hair turn into bald people at some point.

At first, I thought, *What the hell is he talking about?* But I looked into it, and it turned out to be true.

I hurriedly joined a mental-magic mage café and searched for people like me, only to find that ninety-eight of its one hundred members suffered from hair loss.

After hearing about my situation, they told me it was already too late. Potions only restore cells temporarily, so using them too often just ends up killing your hair-follicle cells.

I ignored the café’s promise to upgrade my membership if I wrote a review of my medical consultation, quit, and am searching for my own treatment method…

Three-line summary.

1. Mental-magic mage is great. But you lose your hair instead.

2. Potions are useless. Use hair-loss-prevention shampoo and go to a regular hospital instead. Hair must be treated with heart and desperation, not magic.

3. I will not give up.

That’s all.



“…”

After reading the entire thing, my vision grew blurry. So even the mages I had always envied, the people who seemed to have everything, had their own hardships.

“Are you all right, sir?”

“I’m fine… Hngh.”

“What’s wrong?”

“Ah, it’s nothing. I’m fine.”

Of all things, the taxi driver happened to be bald, too. Feeling like a sinner, I lowered my head toward my smartphone.

Below the post, I found more than two thousand comments.



Anonymous#232: Give us the one-line summary.

└ Author: [Comment hidden due to severe profanity.]



Anonymous#112: Is the person who made the first comment even human? I cried. I’ll be rooting for you. Hang in there.

└ Author: Thanks…



Anonymous#1512: I don’t know about the rest, but the second commenter seems to be suffering from hair loss, too. But after reading the whole thing, it sounds like you make a lot of money. Can’t you live without some hair? Just wear a good wig.

└ Author: [Comment hidden due to severe profanity.]



Anonymous#4885: Wow, I’m seeing a Familiar mage here. You guys don’t know this, but the author is a real aristocrat. Even among B-ranks, your income is incomparable. So is the way you’re treated.

└ Author: What good is having money when you don’t have any hair?

└ Anonymous#4885: Now that you mention it, you’re right.

└ Author: If you’re going to comfort me, see it through, you son of a bitch.

.

.

.



Moderator: Congratulations! You’ve been selected as a popular post!

└ Anonymous#5252: LMAOOOOOOOOOO

└ Anonymous#8984: LMAOOOOOOOOOOOOOOOOOOOOOOOOOO

└ Author: Am I supposed to laugh at this or not?

└ Anonymous#2652: You don’t have any hair and you still feel like laughing?

└ Author: [Comment hidden due to severe profanity.]



Author: Thanks for the overwhelming support. Looks like I’m about to make the monthly best list and enter the Hall of Fame. If you have any questions, leave them below. I’m working right now, but I’ll drop in and answer them whenever I get a chance.

└ Anonymous#9665: You said you’re a freelancer. What kind of work do you mainly do?

└ Author: Freelancer is a nice way of putting it. What I do is similar to running a private detective agency. I’ve tracked high-level criminals—Hunters, of course—and I’ve also taken on an affair case at a nouveau riche family’s house.

└ Anonymous#915: Oh… You must make a lot. How much do you earn?

└ Author: That depends on the job, obviously. Still, after working for a few years, I put up a building in Seoul. The house I live in now is also under my name.

└ Anonymous#5252: Show us proof of your house.

└ Author: I’m outside working right now. I’ll properly verify it later, so wait until then.

└ Anonymous#9882: What does working have to do with it? Familiars are remote-controlled anyway, aren’t they?

└ Author: Even remote control has a range limit, you idiot. Do you use the Wi-Fi at your house while traveling in the United States?

└ Anonymous#9882: Sorry.

└ Author: The maximum distance for a Familiar connection is five hundred meters. I’m increasing the distance little by little, but it’s difficult. If the Link is forcibly severed, my stomach starts churning and I feel like I’m going to throw up. There’s also a risk of mana backflow.

└ Anonymous#9882: So you always have to stay within five hundred meters.

└ Author: Yeah. To work safely, maybe three hundred meters? You have to prepare for anything that might happen. Most people probably do the same.



I was scrolling through the comments when I suddenly stopped.

It seemed I had unintentionally discovered some important information.

*The connection with a Familiar is severed if it goes beyond five hundred meters?*

The maximum distance was that much, and the safe working distance was three hundred meters.

In other words, if the author’s comments were true, then the people who had controlled the Familiars yesterday had been somewhere not far from my house.

*And they’d be going bald, too. Maybe completely bald.*

There was a strong possibility they were wearing wigs, but knowing that couldn’t hurt.

I continued searching for information about Familiar magic and was able to organize a few facts.

*For a B-rank mage, the maximum Familiar connection distance is five hundred meters. The safe distance is three hundred meters. If a Familiar dies, the Link is forcibly severed, and the caster also takes a slight hit.*

And I realized one more thing: why they had gone out of their way to use an expensive Familiar mage to watch me.

*What? Tiny Familiars don’t get caught by most detection magic?*

It was like this: detection magic was a net, while tiny Familiars like flies and rice weevils were too small to get caught in it.

Of course, there were products with built-in top-of-the-line detection magic capable of detecting even those, but when I looked them up, they cost five hundred fifty million won as part of a summer special.

“…”

I had no idea which part of that was supposed to be a summer special. I already had plenty of places where money would be going from now on. Five hundred million won, my ass.

*That’s one more reason I have to catch them myself.*

My thoughts suddenly turned to the other Guild members, too. Had Familiars been attached only to my family?

I still didn’t know the exact identity of the person who had commissioned this. Sangdong Guild was only the prime suspect.

“That’ll be 8,400 won.”

“Ah, yes. Here you go.”

I paid the taxi fare and got out. The entrance to the apartment complex, which had always looked exactly the same, seemed a little unfamiliar today.

The presence of the watcher bothered me like a thorn lodged in my throat.

*Should I contact Team Leader Choi?*

I was looking at his number saved on my smartphone when—

“Oppa!”

A familiar “swan”[^1] in a green tracksuit and round glasses, her greasy hair tied tightly back, waved at me.

[^1]: In Korean slang, a “swan” is an unemployed woman.

“Oh, y-yeah.”

“What’s with that reaction?”

“I guess I’d rather not acknowledge knowing you in public. You could say I’m embarrassed…”

“Are you embarrassed by your one and only little sister? Huh?”

“Go buy some clothes. What are you doing wearing a tracksuit again when you left the clothes you bought at the department store last time at home?”

“You should worry about yourself. You’re one to talk, when you go around wearing the same kinds of clothes every day.”

Hayeon’s pointed remark left me speechless for a moment. I had paid three hundred million won only an hour or two ago, but I was still wearing nothing but jeans and a T-shirt. Apparently, the old grime of being an ordinary little citizen, caked on over twenty-seven years, had not yet completely washed off.

“W-Well, anyway. Where are you headed?”

“Where am I going? The convenience store!”

Hayeon, who had been sulking until just now, began grinning foolishly.

*What’s gotten into her?*

I asked in a bemused voice.

“Why are you so excited? Is your heart already pounding at the thought of raiding the convenience store?”

“Who’s raiding anything? I’m going to buy canned tuna.”

“Canned tuna? Are we having tuna kimchi stew for lunch today?”

“No! We’re not!”

“…What’s with you today, seriously? Did you drink?”

“You’ll be like this, too, when you see this little one.”

Despite my reaction, Hayeon only continued to grin strangely, unlike her usual self. Then she lowered the zipper of her tracksuit and pulled something out from inside her clothes.

A tiny ball of white and yellow fur wriggled in her palm.

“Meeoow.”

“…Is that a kitten?”

“Cute, right? I went out to sort the recycling earlier, and someone had abandoned it in a box. It had been left there for anyone who wanted to raise it.”

“…”

“I don’t know what kind of bastard abandoned her, but she’s pitiful, isn’t she? What did it ever do to deserve that? Right, Oppa?”

“…Yeah. Animals haven’t done anything wrong.”

“I got Mom’s permission to foster it, even if it’s only for a little while. You’re okay with it, too, right?”

“Me?”

“Yeah. Our Mom melts for her eldest son, you know. She told me to get your permission, too, so put in a good word for me when we go inside later.”

“We’ll see.”

“What? You liked animals when you were little.”

I did. I still did, in fact. But this little thing sitting quietly in Hayeon’s palm was…

> **System**
>
> Lv. 2 Cat—Familiar

A little different.
```
