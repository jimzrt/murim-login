<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0105.txt",
      "sha256": "6a075cb4c8ef9aacc7f0e11b6bc792d307747dcdb1af7d614e6d343d854d64c0",
      "bytes": 12694
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9c5b0b244fa118662dc4e59210f2c5aa8f76133c02626faf9accaad88f017950",
      "bytes": 4195
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "692027e51686d9b04d792e51f56eaa4c36f520cd74dd0e6d9b5822eb290134f7",
      "bytes": 13845
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "adbef2112f17fd96741acc9bbedad96d3d7d4aa5e1fb8c3c8f3896621e9e5aea",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "5a75c78be482cf4cf0bda0ba7a5bd08944a13ce2f90c6b10578de33b7eb1aad7",
      "bytes": 8154
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "28279b783a7eb88c5c4bccb19789c29a04a1b817bb9d0b1806af2de53f04ac05",
      "bytes": 3101
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "6276a696ab2122bbd26b5bd78d1cc363ae7273273c7de7befa65ae803cd65441",
      "bytes": 4604
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "e02ae977311ea891974d7f397bb25febcc94446e96cf6c5aa69a5ede8c188c3f",
      "bytes": 2200
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4829e8f06f0b432ad12e37721fdb83cc281fbf9ec4fc74c8c79be81676435b85",
      "bytes": 13416
    }
  ],
  "estimated_tokens": 16645
}
-->

# Durable State Update — Chapter 105

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 105. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 105. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 105,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 105,
    "continuity_sources": [105],
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
    "Sangdong Guild's Security Team was assigned to surveil Jin Taekyung; the property being used as its surveillance base remains unidentified.",
    "Choi Byungil led the failed operation against Taekyung and was defeated with the other field Hunters; the Security Team faces written discipline, a pay cut, and possible dismissal.",
    "Kim Junsu is the Security Team's sole Familiar mage, and Hong Woojin is an outside B-rank Familiar mage hired by Team Leader 1.",
    "Seong Jinho is Taekyung's thirty-year-old civilian goshiwon manager and sworn-brother-like friend in Bucheon.",
    "Im Chunsoo is a Level 75 A-rank ice mage and Guild Master of Sangdong Guild.",
    "Kim Hwajong is a Level 80 mage and former Hunter Training Center instructor; he trained Im Chunsoo, who was a Class 25 trainee assigned to the 28th Regiment, First Battalion, Second Company.",
    "The reason Kim Hwajong arrived at the confrontation remains unknown, as does why he now works as a butler.",
    "Team Leader 1 assesses Taekyung as a top-tier B-rank or A-rank Hunter.",
    "Taekyung owns a two-story detached house in Goyang intended as his family's home and will live there alone until Hayeon finishes her college entrance exam.",
    "Logout is active, so Taekyung no longer needs the capsule to travel between the modern world and Murim.",
    "Seong Jinho unexpectedly emerged from Taekyung's capsule inside the new house after Taekyung logged into Murim; how and why he entered remains unknown.",
    "Taekyung, Mukyung, and Hyuk Mujin have reached Honju and are staying at the Phoenix Inn's private residence.",
    "Mukyung is a Peak master and uses a superficially learned heat-yang technique to warm Hyuk Mujin.",
    "Taekyung must deliver the Jin Family of Taiyuan's Lunar New Year invitation to the weakened Mount Heng Sword Sect, now led by Lee Seowol, his uncomfortable former accuser.",
    "Hyuk Mujin is a First Rate martial artist from a tenant-farmer family, Captain of the Jin Family's Gatekeepers, deputy squad leader of White Tiger Hall's reconnaissance squad, and a candidate to become the next Master of the Gatekeeper Pavilion.",
    "Jin Wikyung gave Mujin fifty silver nyang for the journey and ordered the travelers to use good lodging and meals because they had no attendants.",
    "Mukyung considers enduring hunger a form of training, while Taekyung's appetite causes Mujin severe financial anxiety.",
    "A group of martial artists at the Phoenix Inn ruined Taekyung's soup and provoked him; Taekyung punched the first aggressor.",
    "The unnamed Phoenix Inn proprietress was told that the Sleeping Dragon of Shanxi subdued six martial artists and went to see him."
  ],
  "continuity_sources": [
    104
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong, despite his former instructor status and exceptional ability, now works as a butler remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol will react to the invitation remains unknown.",
    "What will result from the Phoenix Inn fight, and why the unnamed proprietress recognizes the Sleeping Dragon of Shanxi, remain unknown."
  ],
  "safe_through": 104,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술.",
    "Keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you while preserving his blunt senior voice.",
    "Render 김화종's 춘수 as Chunsoo and 교관님 as Instructor.",
    "Render 1번 훈련생 as Trainee Number One.",
    "Render 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year.",
    "Render 봉황객잔 as Phoenix Inn and 계용옥미갱/계용옥미앵 as chicken-and-corn soup."
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
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |

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
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 지부장    | **Branch Leader**                            |
| 산서지부장  | **Shanxi Branch Leader**                     |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 104
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 104
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 103
- **Aliases:** Blood Wolf Sword
- **Role:** Sect Leader of the Mount Heng Sword Sect; Lee Seogeun’s father
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; leader of the Mount Heng Sword Sect

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 103
- **Aliases:** Ghost Sword
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 70
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, and quietly amused; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃105화



콰직!

악취 나는 주둥이에 주먹을 꽂는 순간 직감했다. 저놈이 앞으로 먹을 수 있는 건 계용옥미갱뿐이라는 걸.

쿠당탕! 쾅!

일직선으로 튕겨 나간 첫 번째 놈은 몸이 땅에 닿기도 전에 정신을 잃었다.

31레벨. 일류 초입에 든 무인이지만 내 주먹을 피할 수는 없었다.

“시발놈이 어디서 입 냄새를 풍겨, 밥맛 떨어지게.”

순간 객잔의 모든 소리가 멎었다. 그러나 그건 아주 잠깐에 불과했다.

“광수가 당했다!”

“이 애새끼가!”

“죽여!”

차차창!

일제히 뽑혀 나온 다섯 개의 곡도. 살기로 번들거리는 다섯 쌍의 눈동자. 비명과 함께 객잔의 손님들이 흩어진다.

문득 방금 쓰러진 놈에게서 나던 피비린내가 생각났다.

‘허, 이놈들 봐라?’

살인에 익숙한 놈들이다. 먼저 시비를 건 주제에 병장기를 꺼내는 걸 주저하지 않는 모습만 봐도 알 수 있다.

“너네 뭐 하는 놈들이냐?”

“저승사자.”

대답과 동시에 놈들이 달려들었다. 네 개의 곡도가 사지를, 남은 하나는 가슴을 정확히 노리고 찔러 들어온다.

쉬쉬쉭!

느리다. 다섯 놈 중 일류가 하나, 이류가 넷.

날 어떻게 해 보겠다는 생각은 야무졌지만 발은 느리고 정면에서 펼친 도의 그물은 허술하다.

“다음부터는 최소한 포위라도 해라.”

친절한 조언과 함께 놈들을 향해 양손을 떨쳤다. 아주 짧은 순간, 인벤토리에서 소환된 단검 두 자루가 허공을 갈랐다.

쉬쉭!

단검 투척. 무림에서는 비도술이라고 하나?

실전용으로 배운 적은 없지만 괜찮다. 날이건, 자루건 우선 맞기만 하면 되니까.

빡! 털썩.

그래, 저렇게.

검 자루에 이마가 깨진 한 놈이 비명도 못 지르고 그대로 고꾸라졌다. 그럼 다른 하나는?

캉!

“어디서 얕은수를!”

운이 좋은 건지, 생각보다 눈이 좋은 건지 용케 막았다.

나는 놈을 향해 활짝 웃어 주었다.

“그 단검이 네 단검이냐?”

“네놈이 던져 놓고 무슨 개소리냐!”

“정직한 아이로구나. 상으로 둘 다 주마.”

뻑, 뻑!

“꺼흑. 분명 손이 비었…….”

털썩.

“내 단검은 무한 증식이란다.”

태원진가에서 출발하기 전에 무기 창고에 먼저 들르길 잘했다.

빈손으로 들어가서 빈손으로 나왔지만 지금 인벤토리에는 전리품으로 노획한 병장기 수십 개가 쌓여 있다.

“이, 이게 무슨.”

눈 깜짝할 사이에 벌어진 일. 남은 세 놈이 달려들다 말고 주춤거리며 물러났다.

“안 와? 그럼 내가 간다?”

“자, 잠깐, 소협! 저희가 무례를 저질렀습니다. 정중하게 사과드리고 변상을…….”

태세 전환 하는 속도 봐라.

방금만 해도 애새끼 운운하던 놈들이 소협은 무슨.

“사과?”

“예, 예!”

“필요 없어!”

나는 주먹을 불끈 쥐고 놈들을 향해 달려들었다. 이런 놈들을 처리하는 데에는 무공도 필요 없다.

“제기랄, 쳐!”

쉬이익!

옆으로 한 걸음.

정수리를 향해 일직선으로 내리 찍히는 곡도를 피했다. 이어 비어 있는 옆구리에 일권(一拳)을 내지른다.

우드득.

헉, 억눌린 신음과 함께 쓰러지는 놈을 뒤로하고 다음 상대를 향해 달려들었다. 머리 위로 35레벨이라 적힌 시스템창이 보인다.

“놈!”

쐐애액!

일류 고수답게 제법 무공을 익힌 티가 난다. 군더더기 없는 동작과 정확히 급소를 노리고 휘둘러지는 곡도.

하지만…….

‘압도적인 힘과 속도 앞에서는 무용지물이지.’

레벨과 공력이 낮을 뿐, 능력치로 따지자면 일류를 아득하게 뛰어넘은 나다. 거기다 더해 무림에서 쌓은 전투 경험까지. 이놈은 결코 내 상대가 될 수 없다.

콰직!

초점이 사라진 눈동자. 미처 끝까지 휘두르지 못한 곡도가 손아귀에서 미끄러진다.

철그렁.

이 모든 광경을 지켜본 마지막 한 놈은 반쯤 넋이 나갔다.

“조, 조장이 고작 일 합 만에…… 넌 누구냐?”

“통성명은 내 주먹이랑 해야지. 자, 얘는 오른손이라고 해. 너는?”

불끈 쥔 오른 주먹을 들고 다가서자 놈이 허공에 곡도를 붕붕 휘둘러 댔다.

“오, 오지 마!”

“부탁은 공손히 해야지.”

“오지 마십시오!”

“이걸 진짜 하네.”

그래도 저렇게까지 공손하게 부탁하는데 들어줘야지.

내가 걸음을 멈추자 놈의 얼굴에 화색이 돈다.

“가, 감사합니다! 앞으로 착하게 살겠습니다!”

“뭘 감사까지. 그리고 착하게 안 살아도 돼.”

“예?”

“개과천선이라는 게 그렇게 쉽게 되는 게 아니거든. 안 그러냐, 무진아?”

어느새 놈의 뒤에 서 있던 혁무진이 대답했다.

“그럼요.”

“헉!”

헛숨을 들이켜며 돌아봤지만 이미 늦었다. 혁무진이 손에 든 나무 의자를 녀석의 정수리로 있는 힘껏 내리찍는 중이니까.

빡!

둔중한 소리와 함께 마지막 한 놈이 쓰러진다. 혁무진이 의자를 내려놓으며 중얼거렸다.

“고맙고, 미안하다.”

“저런 놈들한테 뭐가 고마워?”

“그런 게 있습니다.”

어째 상당히 건방진 눈빛인데, 저거.

오랜만에 한 대 쥐어박을까 고민하고 있던 그때 쓰러진 놈들의 품을 뒤지던 혁무진이 고개를 갸웃거렸다.

“어라? 조장님, 이놈들 좀 수상한데요?”

“뭐가?”

“이것 좀 보세요.”

혁무진이 한 놈의 소매를 쓱 걷어 올리자 마치 인두로 지진 듯한 흉터가 드러난다. 아니, 단순한 흉터가 아니다.

이건 마치…….

“문신?”

조잡하고 야만적이지만 분명 그건 일종의 문신이었다. 달리는 말의 형태를 한.

“이놈 하나만 그런 거 아냐?”

“모르겠습니다. 아직 다 확인해 본 게 아니라서.”

“다른 놈들도 확인해 봐.”

“옙.”

혁무진이 기절한 놈들을 한곳에 모아 상의를 벗겼다. 팔뚝, 가슴, 목. 위치는 조금씩 달라도 하나같이 말 문신을 새겼다.

‘어떤 단체에 소속되어 있다는 건데…….’

단순한 불량배가 아니라는 사실은 알고 있었다. 일류 고수가 둘이나 포함되어 있는 데다가 마지막 한 놈이 무심코 흘렸던 단어가 마음에 걸렸기 때문이다.

‘분명히 조장, 이라고 했었지.’

다른 문파에 소속된 무인들? 아니다. 그런 것치고는 풍기는 기세가 거칠고 복장도 통일되어 있지 않았다.

차라리 제법 규모가 있는 낭인 집단일 가능성이 크다.

‘말 문신, 말 문신이라.’

그때 문득, 어떤 단어가 뇌리를 스쳤다. 항산검문과의 전쟁 당시 처음으로 들었던 이름이다.

“마적(馬賊)?”

내 중얼거림에 어디선가 대답이 들려왔다.

“북쪽 고원(高原)에는 수십 개의 마적단이 있답니다. 이천백이 그들을 고용한 건 큰 실수였어요.”

나른하면서도 고혹적인 목소리의 주인을 찾아 고개를 돌렸다. 2층으로 통하는 계단 위, 얼굴에 면사를 드리운 한 여인이 서 있었다.

“오랜만이네, 우리 공자님.”

우리 공자님?

그 한마디를 듣는 순간, 여인의 정체를 알 수 있었다.

‘월화.’

바로 그녀다.



* * *



나와 혁무진이 안내된 곳은 봉황객잔의 최상층에 있는 객실이었다. 말이 객실이지, 층 전체를 쓰는 거라 일종의 펜트하우스라고 해야 맞겠다.

“이곳에 사내를 들이는 건 처음이네요. 그것도 둘씩이나.”

은은한 불빛에 물든 월화의 미소는 눈부셨다. 첫 만남 때부터 느꼈지만 진짜 팜므파탈이 따로 없다.

이미 몇 번 만난 적이 있는 나도 속이 울렁거릴 정도인데, 혁무진은 말할 것도 없었다.

“사, 삼생의 영광입니다.”

“…….”

이 새끼 눈 풀린 것 보소. 아주 제대로 뻑이 간 모양인데.

혁무진을 향해 싱긋 웃어 보인 그녀가 내게로 시선을 던졌다.

“진 공자는 잘 지냈어요? 아, 이제는 예전처럼 공자님이라고 부를 수도 없으려나?”

월화의 짓궂은 표정을 보니 무슨 말이 나올지 충분히 예상이 간다. 나는 황급히 손을 내저었다.

“그냥 편하게 부르세요. 예전처럼.”

“음, 그럼 잠룡 공자 어때요?”

“……끔찍한데요.”

“어머, 왜? 산서잠룡, 멋있잖아요. 약관에 그 정도 무명(武名)을 얻었으면 좀 더 자랑스러워해도 될 텐데.”

산서잠룡이나, 불꽃 카리스마 태경이나 오십보백보다. 내 표정을 본 월화가 키득거리며 곰방대를 물었다.

“농담이에요. 하여간 진 공자는 놀리는 재미가 있어서 좋다니까.”

“저어, 끼어들어서 죄송합니다만.”

약간 정신이 돌아온 혁무진이 나와 월화를 번갈아 본다.

“혹시 두 분이 어떤 사이신지?”

“알 거 없어.”

구구절절 설명하기에는 좀 쪽팔린 관계다. 칼같이 잘라 내며 월화를 향해 눈짓했다. 대충 장단 맞춰 달라는 신호.

그녀도 눈치 빠르게 알아듣고 고개를 끄덕였다.

“우리 가게 단골손님이었어요. 지금은 아니지만.”

“…….”

알아듣긴 개뿔이.

하긴, 진위경과 위팽 앞에서도 스스럼없던 그녀가 이제 와서 감추는 것도 웃기긴 하다.

한편 월화의 대답에 혁무진은 제대로 이해하지 못했는지 반신반의하는 얼굴이었다.

“그 가게라는 게 봉황객잔을 말씀하시는 겁니까?”

“아니? 이건 부업이고. 본업은 따로 있죠. 나처럼 아름답고 매력 있는 여인만이 할 수 있는 일.”

“그럼 혹시…….”

“젊은 무사님이 생각하는 그게 맞을걸?”

“기루?”

“정답.”

혁무진의 눈이 커졌다.

“소문으로만 듣던 봉황객잔의 여주인이 기녀였다니.”

“무사님, 말조심하셔야겠어요. 듣는 입장에서는 기분이 별로거든.”

“기분 나빴다면 사과하겠소. 허나 지금 소저의 언행도 그리 좋게 보이지만은 않는구려.”

갑자기 정색하는 녀석의 모습에 내가 더 당황했다.

“야, 너 왜 그래?”

“조장, 아니 공자님은 태원진가의 직계이십니다. 설령 천하제일미(天下第一美)라 해도 공자님께 이리 소홀히 대할 수는 없는 법. 본가의 식솔로서 좌시할 수 없어 나선 것입니다.”

“아까는 삼생의 영광이라며.”

“……아무튼, 한낱 기녀가 어찌 공자님께. 억!”

시원하게 뒤통수를 후려갈긴 내가 입을 열었다.

“하오문 산서지부장이셔.”

“하오문 산서지부장이건 뭐건, 예? 뭐요?”

“귀 막혔냐? 하오문 산서지부장님이시라고. 이번 항산검문과의 전쟁에서 아주, 매우, 결정적인 도움을 주신.”

“난 괜찮아요, 진 공자.”

월화가 슬픈 듯이 눈을 내리깔았다.

“어차피 한낱 기녀일 뿐이니까.”

잠시 침묵하던 혁무진이 고개를 숙였다.

“소저, 아니 지부장님. 사죄드리겠…….”

“그럼 입 다물고 있어요.”

“옙.”

월화가 실소를 흘렸다.

“재밌는 수하를 뒀네요.”

어물전 망신은 꼴뚜기가 시킨다더니, 태원진가 망신은 혁무진 저 자식이 다 시키는구나. 쪽팔려서 얼굴도 제대로 못 쳐다보겠다.

“……제가 다 죄송하네요.”

“공자가 사과할 건 아니죠. 뭐, 아주 틀린 말도 아니고.”

시원시원하게 넘어가 주니 다행이다.

담배 연기를 내뿜은 월화가 입을 열었다.

“항산검문에 가는 길이죠?”

“네.”

“목적이 뭔지 물어봐도 될까요?”

“이미 알고 있지 않습니까?”

산서성 제일의 정보통이 바로 그녀다. 어떻게 알았는지 물어볼 필요조차 없었다.

“나는 진 공자가 직접 말해 주길 바랐는데…… 섭섭하네요.”

“공과 사는 뚜렷해야죠.”

“야박하긴. 그럼 제의 하나만 해도 될까요? 거래라고 해도 좋고.”

“들어 보고 결정하겠습니다.”

월화가 곰방대를 툭툭 털었다.

“같이 가요. 항산검문.”

“네?”

이게 뭔 소리야.
```

## Final English reading copy

```markdown
# Chapter 105

Crack!

The instant my fist sank into that foul-smelling snout, I knew.

The only thing that bastard would be able to eat from now on was chicken-and-corn soup.

Crash! Bang!

The first man shot backward in a straight line and lost consciousness before his body even hit the ground.

Level 31. He was a martial artist at the entry level of First Rate, but he still couldn’t dodge my punch.

“Where the hell do you get off stinking up the place with your breath and ruining my appetite?”

Every sound in the inn stopped.

But only for a moment.

“Gwangsu’s down!”

“You little brat!”

“Kill him!”

Shing, shing, shing!

Five curved sabers were drawn at once. Five pairs of eyes gleamed with killing intent. The inn’s guests scattered with screams.

I suddenly remembered the smell of blood coming from the man who had just fallen.

*Huh. Look at these bastards.*

They were used to killing. I could tell just from the fact that they had started the fight and still hadn’t hesitated to draw their weapons.

“What kind of people are you?”

“The Grim Reaper.”

The answer came at the same time as their attack.

Four curved sabers stabbed straight at my limbs, while the remaining one aimed precisely for my chest.

Whoosh, whoosh, whoosh!

Too slow.

One of the five was First Rate. The other four were Second Rate.

Their confidence in taking me down was impressive, but their feet were slow, and the net of sabers they spread from the front was full of gaps.

“Next time, at least try surrounding someone.”

Along with that friendly advice, I flicked both hands toward them.

For a very brief moment, two daggers summoned from my Inventory cut through the air.

Whoosh!

*Throwing daggers. Is that what they call it in Murim—flying-dagger arts?*

I had never learned it for actual combat, but it didn’t matter. Whether they were hit by the blade or the hilt, a hit was a hit.

Crack! Thud.

Yes, just like that.

One man’s forehead split open against the hilt of a dagger, and he crumpled without even managing to scream.

What about the other one?

Clang!

“What a cheap trick!”

Whether he was lucky or had better eyes than I expected, he had somehow blocked it.

I gave him a wide smile.

“Is that dagger yours?”

“You threw it at me, so what kind of bullshit are you talking about?”

“What an honest child. As a reward, I’ll give you both of them.”

Thud, thud!

“Ghk. But your hands were clearly empty—”

Thud.

“My daggers multiply infinitely.”

It had been a good idea to stop by the armory before leaving the Jin Family of Taiyuan.

I had gone in empty-handed and come out empty-handed, but my Inventory was now filled with dozens of weapons looted as spoils.

“What… what is this?”

It had all happened in the blink of an eye. The remaining three stopped in the middle of their charge, hesitated, and backed away.

“Not coming? Then I’ll go to you.”

“W-Wait, Young Hero! We were rude. We sincerely apologize and will compensate you—”

Look at how quickly they changed tactics.

Just a moment ago, they had been calling me a brat. Now they were calling me Young Hero.

“An apology?”

“Yes, yes!”

“Don’t need it!”

I clenched my fist and charged at them. I didn’t need martial arts to deal with trash like this.

“Damn it, attack!”

Whoosh!

One step to the side.

I dodged the curved saber that came crashing straight down toward the top of my head, then drove a single punch into the exposed side of his body.

Crunch.

Leaving the man who collapsed with a strangled groan behind me, I charged at the next opponent.

Above his head, I saw a System window displaying Level 35.

“You bastard!”

Whoosh!

As befitted a First Rate expert, he had clearly learned a fair amount of martial arts. His movements were clean, and the curved saber was swung with precision toward my vital points.

But…

*All of that is useless before overwhelming strength and speed.*

My level and internal energy were low, but in terms of stats, I far surpassed First Rate. On top of that, I had all the combat experience I had built up in Murim.

This man could never be my opponent.

Crack!

The focus vanished from his eyes. The curved saber slipped from his grip before he could finish his swing.

Clang.

The last man, who had watched everything unfold, was half out of his mind.

“T-The squad leader fell in a single exchange… Who are you?”

“You should exchange names with my fist. Here, this one’s called Right Hand. And you?”

I approached with my right fist clenched. The man swung his curved saber wildly through the air.

“D-Don’t come any closer!”

“You should make a request more politely.”

“Please, don’t come any closer!”

“You really did it.”

Since he had asked so politely, I supposed I had to honor his request.

When I stopped walking, color returned to the man’s face.

“T-Thank you! I’ll live a good life from now on!”

“No need to thank me. And you don’t have to live a good life.”

“Huh?”

“Turning over a new leaf isn’t something that happens so easily. Isn’t that right, Mujin?”

Hyuk Mujin was standing behind the man before I knew it.

“Of course.”

“Hic!”

The man sucked in a startled breath and turned around, but it was already too late.

Hyuk Mujin was in the middle of bringing the wooden chair in his hands down on the top of the man’s head with all his strength.

Crack!

With a heavy thud, the last man collapsed. Hyuk Mujin set the chair down and muttered,

“Thank you, and I’m sorry.”

“What are you thanking those bastards for?”

“There are things.”

That look in his eyes was awfully cocky.

I was wondering whether I should give him a smack after such a long time when Hyuk Mujin, who had been searching through the fallen men’s clothes, tilted his head.

“Huh? Squad Leader, these men are suspicious.”

“What about them?”

“Look at this.”

Hyuk Mujin rolled up one man’s sleeve, revealing a scar that looked as though it had been branded into the flesh.

No, it wasn’t simply a scar.

It looked like…

“A tattoo?”

It was crude and savage, but it was definitely a kind of tattoo.

A running horse.

“Is this the only one with it?”

“I don’t know. I haven’t checked all of them yet.”

“Check the others.”

“Yes, sir.”

Hyuk Mujin gathered the unconscious men in one place and stripped off their shirts.

Their arms, chests, and necks. The locations differed slightly, but every one of them had a tattoo of a horse.

*So they belong to some kind of organization…*

I already knew they weren’t simple thugs. Two of them were First Rate masters, and I couldn’t stop thinking about the word the last man had let slip without meaning to.

*He definitely said captain, didn’t he?*

Martial artists belonging to another sect?

No. Their aura was too rough for that, and their clothing wasn’t uniform.

It was more likely that they belonged to a fairly large group of wandering martial artists.

*A horse tattoo. A horse tattoo…*

Then a word suddenly flashed through my mind.

It was a name I had first heard during the war with the Mount Heng Sword Sect.

“Mounted bandits?”

Someone answered my mutter from somewhere nearby.

“There are dozens of mounted-bandit groups on the northern plateau. It was a great mistake for Lee Cheonbaek to hire them.”

I turned toward the owner of the languid yet alluring voice.

A woman stood on the stairs leading to the second floor, a veil draped across her face.

“Long time no see, our Young Master.”

*Our Young Master?*

The moment I heard those words, I knew who she was.

*Wolhwa.*

It was her.



* * *



Hyuk Mujin and I were led to a guest room on the top floor of the Phoenix Inn.

Calling it a guest room didn’t really do it justice. We had the entire floor to ourselves, so it was more accurate to call it a penthouse.

“It’s my first time bringing a man here. And two of them, no less.”

Wolhwa’s smile, bathed in the soft light, was dazzling.

I had felt it from the moment we first met, but there really was no better example of a femme fatale.

Even though I had met her several times already, my stomach still churned whenever I looked at her.

Hyuk Mujin was beyond saving.

“It’s an honor beyond three lifetimes.”

“……”

Look at that bastard’s unfocused eyes.

He was completely smitten.

Wolhwa gave him a bright smile before turning her gaze toward me.

“Have you been well, Young Master Jin? Ah, I suppose I can’t call you Young Master the way I used to anymore?”

Judging from Wolhwa’s mischievous expression, I could easily guess what she was about to say.

I hurriedly waved my hands.

“Just call me whatever you like. Like before.”

“Hmm. Then how about Young Master Sleeping Dragon?”

“……That’s horrible.”

“Why? Sleeping Dragon of Shanxi sounds wonderful. If you’ve earned that much martial fame at such a young age, you could stand to be a little prouder.”

Sleeping Dragon of Shanxi or Flaming Charisma Taekyung—they were equally terrible.

Seeing my expression, Wolhwa chuckled and put her long-stemmed tobacco pipe to her lips.

“I’m only joking. Anyway, teasing Young Master Jin is so much fun.”

“Excuse me for interrupting.”

Hyuk Mujin had finally regained some of his senses. He looked back and forth between Wolhwa and me.

“May I ask what kind of relationship the two of you have?”

“None of your business.”

It was too embarrassing to explain our relationship in detail.

I cut him off sharply, then glanced at Wolhwa. It was a signal asking her to play along.

She immediately understood and nodded.

“He used to be a regular at my establishment. Not anymore, though.”

“……”

Like hell she did.

Still, it was a little ridiculous for her to hide it now. She had been completely open about it in front of Jin Wikyung and Wipeng.

Hyuk Mujin, meanwhile, seemed only half-convinced by Wolhwa’s answer.

“By ‘establishment,’ do you mean the Phoenix Inn?”

“No. This is just a side business. My real profession is something only a beautiful and charming woman like me can do.”

“Then perhaps…”

“It’s probably what you’re thinking, Young Martial Artist.”

“A pleasure house?”

“Correct.”

Hyuk Mujin’s eyes widened.

“So the proprietress of the Phoenix Inn, whom I had only heard about in rumors, was a courtesan.”

“Young Martial Artist, you should watch your words. It’s unpleasant to hear that from the other side.”

“If I offended you, I apologize. However, your words and behavior don’t exactly appear in a favorable light either.”

The sudden change in his expression caught me even more off guard.

“Hey, what’s with you?”

“Squad Leader—no, Young Master—is a direct descendant of the Jin Family of Taiyuan. Even the most beautiful woman under heaven cannot treat the Young Master so casually. As a retainer of our family, I could not stand by and let it happen.”

“A moment ago, you said it was an honor beyond three lifetimes.”

“……In any case, how could a mere courtesan treat Young Master—”

Smack!

I gave him a satisfying whack on the back of the head and opened my mouth.

“She’s the Shanxi Branch Leader of the Lower District Sect.”

“Whether she’s the Shanxi Branch Leader or not, huh? What?”

“Are your ears clogged? I said she’s the Shanxi Branch Leader of the Lower District Sect. She gave us extremely—very, very—decisive help in the recent war with the Mount Heng Sword Sect.”

“I’m fine, Young Master Jin.”

Wolhwa lowered her eyes sadly.

“I’m only a mere courtesan, after all.”

Hyuk Mujin was silent for a moment before bowing his head.

“Young Lady—no, Branch Leader. I apologize—”

“Then keep your mouth shut.”

“Yes, ma’am.”

Wolhwa let out a quiet laugh.

“You have an interesting subordinate.”

They say the squid is what disgraces the fish market. In the same way, that bastard Mujin was doing all the disgracing for the Jin Family of Taiyuan.

I was too embarrassed to look Wolhwa in the eye.

“……I apologize for all of this.”

“You’re not the one who needs to apologize, Young Master. And he wasn’t entirely wrong.”

Thankfully, she let it slide without a fuss.

After exhaling a stream of smoke, Wolhwa spoke.

“You’re on your way to the Mount Heng Sword Sect, aren’t you?”

“Yes.”

“May I ask what your purpose is?”

“You already know, don’t you?”

She was the greatest source of information in all of Shanxi. There was no need to ask how she knew.

“I wanted Young Master Jin to tell me himself, though. I’m disappointed.”

“Business and personal matters should be kept separate.”

“How cold. Then may I make you a proposal? You can call it a deal, if you prefer.”

“I’ll decide after I hear it.”

Wolhwa tapped the ash from her pipe.

“Let’s go together. To the Mount Heng Sword Sect.”

“What?”

What the hell was she talking about?
```
