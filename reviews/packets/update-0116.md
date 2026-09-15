<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0116.txt",
      "sha256": "4c4a7660016894296e04c7b12320bdbef74a604f58072b943544b0c8518eefca",
      "bytes": 13512
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "59430804c65ebc8e34b7fd2b32fe5df59f536876ff2b9ff8c85943fae511cbf3",
      "bytes": 1809
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5479195f26221d6953fdb4d1c02e8c2a80343bad8bae36b9e2b042cb2c669a1a",
      "bytes": 17193
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "39280f430090a39af7479ef08dcfb180e63a5485ed3300c5f7cd4a1a4359e766",
      "bytes": 724
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "97922821c9eceb6ca2dbe668054f0a5468b7a6ac678570a53021401485a76e39",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fa9fd3dd3124a131c32511406a73c7d135c7c4064ce2c503433fbe2c150cce4c",
      "bytes": 24117
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "63f1146826e92543ad20aa75e144f2b9e6b0a9af5e5662f375638e3e1bc586f5",
      "bytes": 3231
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "19c2efad0a216ac1011a3de5fe9851c4a54950a780ac04f49168ecf470e51541",
      "bytes": 749
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "d3c9377e6663ee347406fa37d3a3bda9e3da09e43124bc913701d8e74e0b3761",
      "bytes": 684
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c2fe066986c06714739eb6def0749dfcbd0ed24110775fd03ef26ee9342cb610",
      "bytes": 16692
    }
  ],
  "estimated_tokens": 18763
}
-->

# Durable State Update — Chapter 116

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 116. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 116. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 116,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 116,
    "continuity_sources": [116],
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
    "Cheol Mubaek personally protected Lee Seowol during the Red Wind Band's assault and was critically wounded after Pung Yang defeated him alone.",
    "Pung Yang has used the Temporary Strength Pill, a rare power-enhancing pill, and suffers substantial aftereffects from it.",
    "Lee Seowol agreed under coercion to marry Pung Yang in exchange for the survival of the Mount Heng Sword Sect's captured martial artists and Cheol Mubaek.",
    "Jin Mukyung and Jin Taekyung entered the Mount Heng fortress and attacked Pung Yang and the Red Wind Band.",
    "Jin Mukyung is stronger than Pung Yang; Taekyung is killing the mounted bandits around him.",
    "Pung Yang plans to take control of the Mount Heng Sword Sect and build a larger orthodox faction under its name.",
    "The battle between the Jin brothers and Pung Yang is unresolved."
  ],
  "continuity_sources": [
    115
  ],
  "open_questions": [
    "What is the origin and full effect of the Temporary Strength Pill?",
    "Can Jin Taekyung and Jin Mukyung defeat Pung Yang and rescue Lee Seowol and Cheol Mubaek?",
    "Will Lee Seowol's coerced agreement be carried out or overturned?",
    "Whether the Mount Heng Sword Sect will survive the continuing assault remains unresolved."
  ],
  "safe_through": 115,
  "temporary_decisions": [
    "Render 일류 초입 as early First Rate.",
    "Retain shichen and explain three shichen as six hours in context.",
    "Render 화시 as fire arrow, 쇠뇌 as crossbow, and 충차 as battering ram.",
    "Render 수라멸권 as Shura Annihilating Fist.",
    "Render 항산권문 as Mount Heng Fist Sect.",
    "Render 벽곡단 as fasting pills.",
    "Render 잠력단 as Temporary Strength Pill and explain its literal meaning in a footnote."
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
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |

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
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 무신     | **Martial God**               | —              |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 115
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 115
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 115
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 115
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 115
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 115
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃116화



진무경의 검기가 풍양의 등을 가른 순간, 나는 생각했다.

‘이 싸움, 이겼어.’

절정 고수들의 생사결은 어떻게 될지 짐작하기 어렵다.

그러나 아직 절정에 이르지 못한 내가 보기에도 진무경과 풍양의 격차는 확실했다.

‘진무경이 강한 건지, 아니면 풍양이 생각했던 것보다 약했던 건지.’

앞서 항산호 철무백과의 싸움에서 힘을 전부 소진했던 걸까?

중요한 건 진무경이 압도적인 우세를 점하고 있다는 사실이다.

서걱, 촤아악!

“으아악!”

수하들을 방패 삼아 뒤로 몸을 빼는 풍양, 거침없이 베어 나가며 추격하는 진무경. 푸른 검기를 피해 적풍단의 마적들이 사방으로 흩어지자 홀로 남은 풍양의 모습이 드러났다.

‘끝났다.’

내심 주먹을 불끈 움켜쥔 그때였다. 놈의 손에 들려 있는 붉은 단환이 눈에 들어온 것은.

‘잠깐, 붉은 단환?’

철무백이 말했던 바로 그것이다. 머릿속 경고등이 울림과 동시에 풍양이 단환을 한입에 털어 넣었다.

그 틈을 놓치지 않고 진무경의 푸른 검기가 놈의 정수리를 향해 내리꽂혔다.

쉬이이잉! 서걱!

허공에 흩뿌려지는 핏물, 깊게 베인 어깨.

비틀거리며 물러나는 한 사람은 다름 아닌…… 진무경이다.

나는 눈을 깜빡거렸다.

‘방금 도대체…….’

무슨 일이 일어난 거지?

내 의문에 시스템이 응답했다.

띠링.



- 돌발 퀘스트가 생성되었습니다.



퀘스트



[잠력단]

현재 적풍단주 풍양은 잠력단(暫力丹)을 복용하여 비정상적인 힘을 얻은 상태입니다. 그를 쓰러트리고 항산검문을 구원하십시오.

* 이소월의 사망 시 퀘스트는 실패합니다!



등급 : 초절정

제한 : 진태경

임무 : [Lv.??? 풍양]을 저지, 혹은 승리 (미완료)

보상 : ???

실패 : ???





자그마치 초절정 등급의 퀘스트. 내용을 빠르게 훑어보니 저놈이 강해진 이유를 알 수 있었다.

“잠력단? 이거 설마.”

나는 입을 딱 벌리고 풍양을 바라봤다.

놈은 처음과 많이 달라진 모습이었다. 온통 핏빛으로 물든 눈동자. 소매 아래로 드러난 피부엔 핏줄이 불뚝 섰고 근육은 터질 것 같다. 거기에 다가가기도 두려울 만큼 막대한 기파까지.

‘빼박이네.’

아니, 시바…….

절정 고수라는 새끼가 치사하게 도핑을 해?



* * *



“크흐흐흐.”

풍양은 낮은 웃음을 흘렸다.

전신에서 용솟음치는 힘과 활력! 머리는 그 어느 때보다 뜨겁게 달아올랐고 시야에 들어오는 모든 것들이 나약하고 하찮게 느껴졌다.

거기에 더해 단전에서 끓어오르는 공력까지.

‘이것이 잠력단의 힘이다.’

일시적으로 갖고 있는 힘을 두 배, 아니 그 이상으로 끌어내는 미지의 단환. 누가, 어떻게 만들었는지는 풍양 자신도 모른다. 그건 말 그대로 하늘이 내린 기연이었으니까.

‘적혈십이검(赤血十二劍). 적혈심법(赤血心法). 그리고 잠력단 다섯 알이 담긴 목곽 하나.’

광활한 고원에 숨겨진 수많은 무덤 중 하나. 그곳에서 누가 남겼는지 모를 절정 비급과 잠력단을 발견한 순간, 풍양은 기연을 만났음을 깨달았다.

이런 보물은 아무와도 나눌 수 없다는 사실도.

‘그 시절로 열 번을 돌아간다 해도 같은 선택을 했겠지.’

수하들을 죽이고 기연을 독차지한 풍양은 아무도 찾지 않는 비처에서 수련을 시작했다. 그리고 불과 이 년 만에 절정의 경지에 올랐다.

비상식적인 성장 속도와 불쑥불쑥 솟구치는 살기에 사마외도(邪魔外道)의 무공을 익혔다는 걸 깨달았지만 그에게는 아무런 상관도 없었다.

‘이곳은 무림이다!’

힘이 곧 법칙인 세상에서 정, 사, 마를 논하는 것이 우스웠다. 고원으로 돌아온 풍양은 금방 두각을 드러내기 시작했다.

다른 마적들과는 확연히 다른 비상한 두뇌와 뛰어난 무공.

폭력과 보상을 적절히 이용하는 용인술로 빠른 속도로 수하들을 휘어잡았다. 물론 그에게도 위기가 없었던 것은 아니다.

그러나 풍양에게는 아무에게도 보여 주지 않은 귀물이 있었다.

‘그때 처음 잠력단의 효능을 알았지.’

일당백? 고작 그 정도가 아니다.

잠력단을 복용한 그는 고원에서 그 누구도 당해 낼 자가 없는 무적의 고수였다.

새로운 경쟁자를 제거하려던 대형 마적단 두 곳이 하루아침에 궤멸당했다. 풍양이 이끄는 적풍단이 그 자리를 차지한 것은 자연스러운 수순이었다.

‘하지만 딱 거기까지.’

사마외도의 무공은 속성으로 빠르게 익히는 것이 가능한 대신 깊이가 얕았다. 그 단점을 정종 무공으로 보완하려던 찰나 눈에 띈 곳이 바로 태원진가와 항산검문이다.

용과 호랑이의 싸움. 풍양은 누가 쓰러지든 상관없었다.

처음에는 이천백에게 태원진가의 무공을 약속받고 고용됐는데…… 일이 꼬여 지금에까지 왔다.

‘처음 항산검문을 쳤을 때 잠력단을 썼어야 했는데.’

항산검문은 언제든지 다시 쳐 굴복시킬 수 있지만 잠력단은 다시 구할 수 없다.

차라리 그때 잠력단을 복용했다면 이미 항산검문의 주인이 되어 있었을지도 모를 일이다.

“뭐, 이것도 나쁘지는 않구나. 태원진가와 항산검문의 무공을 모두 얻게 되었으니 말이다.”

어깨의 혈도를 짚어 상처를 지혈한 진무경이 입을 열었다.

“처음부터 그게 목적이었나? 난 또 웬 마적 놈 하나가 정파 대협 흉내가 내고 싶어서 안달이 난 줄 알았지.”

“대협? 오늘 진천검과 산서잠룡을 잡아 죽이면 마두 정도는 되겠지. 으하하하!”

“네깟 놈이 마두는 무슨. 그리고 그럴 일은 없으니까 걱정 마라.”

“철무백은 사지를 부러트려 놨지. 네놈은 말하는 본새가 글러 먹었으니 팔다리 두 개는 잘라야겠다.”

“아, 그래? 이건 내 아우가 자주 하는 말인데…….”

진무경이 가래를 탁 뱉었다.

“좆이나 까 잡숴.”

쉭!

이가 숭숭 나간 청강검은 볼품없어 보였지만 푸른 검기가 덧씌워지니 천하제일의 명검으로 돌변했다.

쐐애애애액! 쉬쉬쉬슁!

빗발치는 검기가 사방을 가르고 베었다. 끔찍한 비명이 여기저기서 터져 나왔지만 진무경은 검을 멈추지 않았다.

미처 피하지 못하고 휘말린 마적들의 비명일 뿐, 그가 원하는 목소리의 주인은 손쉽게 검을 피해 내고 있었기 때문이다.

“역시 진천검, 검 끝이 제법 날카롭군.”

진무경은 번개 같은 속도로 풍양의 허리를 베어 갔다.

쩡! 검기에 휩싸인 진무경의 검과 풍양의 곡도가 격돌하자 굉음이 터져 나왔다.

“사술 따위로 강해진 놈한테 들으니 기분이 더러운데.”

“중요한 사실은 강해졌다는 거지. 그 대단하다는 항산호가 나한테 몇 초나 버텼을 것 같나?”

“몰라.”

쉬이익!

이번에는 안면이다. 팔, 가슴, 배, 옆구리, 다리를 향해 쏟아지던 검격이 돌연 위로 쭉 솟구쳤다.

순간 황급히 고개를 뺀 풍양의 뺨 위로 검날이 아슬아슬하게 비껴갔다.

치이익.

그러나 예리한 풍압마저 피할 수는 없었다. 바람이 할퀴고 간 뺨에서 핏물이 뚝뚝 떨어졌다.

말없이 물러난 풍양이 상처를 확인하고 이를 갈았다.

“……이 어린놈이.”

진무경은 살기 어린 목소리에도 담담하게 입을 열었다.

“그래서?”

“뭐?”

“그래서 철 대협이 너한테 몇 초를 버텼나?”

진무경을 뚫어져라 노려보던 풍양이 대답했다.

“백 초.”

“나는 어떨까?”

“이백 초. 그 안에 끝내 주마.”

“그럴 능력은 되고?”

“사지를 자르기 전에 혀부터 뽑아야겠군. 아까부터 듣고 있자니 기분이 더러워.”

“내 아우와 싸우지 않은 걸 고맙게 여겨라. 저놈이 네 상대였으면 넌 이미 귀 막고 자결했어. 사람 놀리는 데는 도가 튼 놈이거든.”

“산서잠룡이? 그럼 저놈도 같이 뽑아야겠군.”

“……음. 그건 살짝 괜찮은 것 같기도 하고.”

“헛소리 그만하고 검을 들어라. 그래야 촌각이라도 더 발버둥 치다가 뒈지지.”

풍양의 붉은 눈동자가 요사스럽게 반짝인 순간, 늘어트린 곡도에서 막대한 공력이 솟구쳤다.

화아아악!

공력을 어떠한 매개체에 불어넣어 유형화시킬 수 있는 것을 검기(劍氣)라 한다. 그러나 잠력단을 복용한 풍양은 지금 이 순간, 그 경지를 뛰어넘었다.

“검강(劍罡)…….”

초절정 고수. 이른바 무신이라 불리는 자들의 상징.

비록 깨달음이 받쳐 주지 못한 탓에 진정한 검강이라 부를 수는 없지만, 그가 절정의 극에 다다랐다는 것은 분명했다.

“거참.”

진무경은 헛웃음을 흘렸다. 과연 풍양이 수련만으로 저 경지에 다다르려면 몇 년이 필요했을까. 십 년? 이십 년?

하지만 조그마한 붉은 단환 하나가 풍양으로 하여금 그 세월을 건너뛰게 만들었다. 무리(武理)에 대한 고민, 끊임없는 수련과 피땀. 그 모든 것을 뛰어넘도록.

“어떤 개 같은 놈이 저딴 걸 만들어서…….”

츠츠츠츠.

진무경의 검에서도 검기가 솟아올랐다. 풍양이 가소롭다는 듯이 말했다.

“이백 초를 버티면 살려 주마.”

“응, 좆 까.”

후우우웅!

천지를 가를 듯이 내리꽂히는 검강을 바라보며, 진무경은 문득, 자신이 건방진 막내아우를 닮아 간다는 생각이 들었다.

‘그런데 이놈은 뭐 하느라 이렇게 안 와?’

콰과과광!



* * *



구구구궁.

지진이라도 난 것처럼 지면이 흔들렸다. 삼십 장 밖에서 도대체 무슨 싸움을 하는 건지 몰라도 하나는 알겠다.

‘가면 안 돼.’

농담이 아니라 저 싸움에 끼었다가는 죽을 것 같다.

절정 고수 싸움에 일류 등 터지는 꼴을 직접 겪고 싶진 않거든. 그리고 무엇보다…….

쉭, 서걱!

“꺼어어어.”

이쪽도 충분히 힘들다. 이 정도면 일당백은 아니어도 일당칠십 정도는 되겠지. 나는 쏟아지는 핏물을 뒤집어쓴 채로 미친 듯이 무기를 휘둘렀다.

슈왁!

옆구리를 노리고 찔러 들어오려는 기병창을 붙잡고 그대로 당겼다. 등 뒤에서 도를 내리찍던 놈의 배에 박아 넣고 창대를 수도(手刀)로 내리친다.

우지직!

“허억!”

“다음부턴 철창 써. 무겁고 튼튼한 걸로. 스쿼트도 할 수 있고 얼마나 좋냐.”

덕담과 함께 마적의 턱을 후려갈겼다. 턱뼈가 으스러지는 소리와 함께 놈의 몸에서 힘이 빠져나간다.

쐐애액!

‘목, 옆구리, 다리.’

세 방향에서 내질러지는 단검은 눈으로 보지 않아도 읽을 수 있었다.

어떻게 이렇게 하나같이 느리고 뻔한지. 그리고 이 짧은 순간에 대응을 생각하고 실행에 옮길 수 있는 내 자신이 새삼 놀랍다.

타탁. 콰직!

인벤토리에 무기를 넣어 자유로워진 손으로 목과 옆구리를 찔러 오는 녀석들의 손목을 잡는 동시에 부러트리고 뒷발을 쭉 뻗었다.

짤막한 비명과 둔탁한 타격감은 적에게 정확히 명중했다는 증거다.

‘더, 더, 더.’

점점 더 손이 빨라지고 소리가 멀어진다. 나를 가득 둘러싼 적들의 몸을 스칠 때마다 인벤토리에서 불러들인 무기들이 나타났다가 사라진다. 찍고, 베고, 휘두르고. 부쉈다.

몇 명이나 쓰러트렸을까? 어느 한순간, 멀리 밀려나 있던 소음이 한 번에 찾아왔다.

털썩.

“끄으윽.”

“커헉.”

죽은 자들은 차가운 흙바닥에 얼굴을 처박은 채 미동이 없고, 살아남은 자들은 뒹굴며 신음한다. 죽지도, 다치지도 않은 이십여 명의 마적들은 나를 피해 뒷걸음질 쳤다.

“사, 산서잠룡…….”

한 걸음, 두 걸음.

겁에 질린 그들은 내가 다가선 만큼 물러났다. 아직 뒤에 성난 적들이 남아 있다는 사실을 잊은 채로.

쐐애애액! 퍼걱!

“죽여! 마적 놈들을 모조리 죽여라!”

“이 개새끼들!”

최후까지 살아남아 항전하던 항산검문의 무인들이다.

눈이 벌겋게 충혈되어 달려드는 그들의 기습에 마적들이 도미노처럼 쓰러졌다.

“크아아악!”

“제, 제발 살려……!”

온 사방이 온통 시체와 핏물, 신음으로 넘쳐흘렀다.

오늘 이곳에서 죽은 마적들이 몇 명이나 될까? 이백? 삼백? 모르겠다.

내가 아는 건, 한 사람이 죽기 전까지 이 전투는 끝나지 않을 거라는 사실이다.

‘풍양.’

저 치사한 약쟁이 놈을 처리해야 할 시간이다.

“…….”

할 수 있겠지? 할 수 있을 거야. 아마도…….
```

## Final English reading copy

```markdown
# Chapter 116

The moment Jin Mukyung’s Sword Energy split Pung Yang’s back, I thought,

*This fight is won.*

It was hard to predict the outcome of a life-and-death duel between Peak masters.

But even to me, someone who had yet to reach the Peak realm, the difference between Jin Mukyung and Pung Yang was obvious.

*Is Jin Mukyung really that strong, or was Pung Yang weaker than I thought?*

Had he exhausted all his strength in his earlier fight with Cheol Mubaek, the Tiger of Mount Heng?

What mattered was the fact that Jin Mukyung held an overwhelming advantage.

Slice! Shraaak!

“Gaaaaah!”

Pung Yang retreated, using his subordinates as shields, while Jin Mukyung pursued him without hesitation, cutting his way through them. As the mounted bandits of the Red Wind Band scattered in all directions to avoid the blue Sword Energy, Pung Yang was revealed standing alone.

*It’s over.*

That was when I clenched my fist in triumph.

Then I saw the red pill in his hand.

*Wait. A red pill?*

It was the very thing Cheol Mubaek had mentioned. At the same moment the warning bells began ringing in my head, Pung Yang tossed the pill into his mouth.

Jin Mukyung didn’t miss the opening. His blue Sword Energy plunged toward the crown of Pung Yang’s head.

Shiiiiing! Slice!

Blood sprayed through the air. One shoulder was cut deeply.

The person staggering backward was none other than Jin Mukyung.

I blinked.

*What the hell just…*

What had happened?

The System answered my question.

> **System**
>
> A sudden Quest has been generated.
>
> **Quest**
>
> **Temporary Strength Pill**
>
> Red Wind Band Leader Pung Yang has taken a Temporary Strength Pill (暫力丹) and is currently empowered by abnormal strength. Defeat him and save the Mount Heng Sword Sect.
>
> *The Quest will fail if Lee Seowol dies!*
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Task:** Stop or defeat **Lv.??? Pung Yang** (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

A Quest with a Grade of Supreme Peak.

I skimmed through the details and immediately understood why that bastard had grown so strong.

“Temporary Strength Pill? Don’t tell me…”

I gaped at Pung Yang.

He looked completely different from before. His eyes had turned completely bloodred. Veins bulged beneath the skin exposed below his sleeves, and his muscles looked ready to burst. On top of that, the sheer force radiating from him made it frightening to even approach.

*There’s no mistaking it.*

No, fuck…

A fucking Peak master, cheating by doping?

* * *

“Heh-heh-heh.”

Pung Yang let out a low laugh.

Power and vitality surged throughout his body. His head burned hotter than ever, and everything in his field of vision seemed weak and insignificant.

The internal energy boiling in his dantian only added to the sensation.

*So this is the power of the Temporary Strength Pill.*

It was an unknown red pill capable of drawing out twice the strength a person currently possessed—no, even more than that—for a limited time. Pung Yang himself didn’t know who had made it or how.

It was, quite literally, a fortuitous encounter bestowed by the heavens.

*The Crimson Blood Twelve Swords. The Crimson Blood Cultivation Technique. And a wooden case containing five Temporary Strength Pills.*

Among the countless tombs hidden on the vast plateau, Pung Yang had discovered a Peak-level martial arts manual and the Temporary Strength Pills in one of them. The moment he found the Peak-level manual and Temporary Strength Pills left behind by an unknown person, he realized he had encountered a great opportunity.

He also realized that such treasures could not be shared with anyone.

*Even if I went back to that time ten times, I would have made the same choice.*

Pung Yang killed his subordinates and kept the fortuitous encounter for himself, then began training in a hidden refuge that no one ever visited. In only two years, he reached the Peak realm.

The absurd speed of his growth and the killing intent that surged from him at unpredictable moments made him realize he had learned demonic, heterodox arts.

But it didn’t matter to him.

*This is the Murim!*

In a world where strength was the law, arguing over whether something was orthodox, heterodox, or demonic was laughable. After returning to the plateau, Pung Yang quickly began to distinguish himself.

His intelligence was far beyond that of the other mounted bandits, and his martial arts were exceptional.

By using violence and rewards in just the right measure, he quickly bent his subordinates to his will. Of course, he had faced crises as well.

But Pung Yang possessed a wondrous treasure he had never shown to anyone.

*That was when I first learned what the Temporary Strength Pill could do.*

One against a hundred? It was far beyond that.

After taking a Temporary Strength Pill, he became an invincible master whom no one on the plateau could withstand.

Two major mounted-bandit groups that had tried to eliminate their new competitor were wiped out overnight. It was only natural that the Red Wind Band, led by Pung Yang, would take their place.

*But that was as far as I could go.*

Demonic, heterodox arts could be learned quickly through shortcuts, but they lacked depth. Just as Pung Yang was trying to make up for that weakness with orthodox martial arts, two places caught his eye: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

A battle between a dragon and a tiger.

Pung Yang didn’t care which one fell.

At first, Lee Cheonbaek had hired him with the Jin Family of Taiyuan’s martial arts promised as payment…

But things had become complicated, leading him to this point.

*I should have used a Temporary Strength Pill when I first attacked the Mount Heng Sword Sect.*

He could attack the Mount Heng Sword Sect again and force it to submit whenever he wanted.

But he could never obtain another Temporary Strength Pill.

If he had taken one back then, he might already have become the master of the Mount Heng Sword Sect.

“Well, this isn’t bad either. I’ll obtain the martial arts of both the Jin Family of Taiyuan and the Mount Heng Sword Sect.”

Jin Mukyung, who had pressed an acupoint on his shoulder to staunch the bleeding, spoke.

“Was that your goal from the beginning? I thought some mounted-bandit bastard was desperate to play at being a Great Hero of the orthodox faction.”

“A Great Hero? If I kill the Heaven Shaking Sword and the Sleeping Dragon of Shanxi today, I might at least become a demon lord. Wahaha!”

“You? A demon lord? Don’t make me laugh. And you don’t have to worry about that happening.”

“I broke all four of Cheol Mubaek’s limbs. Your way of speaking is beyond saving, so I’ll have to cut off two of yours.”

“Oh, really? This is something my younger brother says often…”

Jin Mukyung spat out a wad of phlegm.

“Go fuck yourself.”

Whoosh!

The blue-steel sword was missing so many pieces from its edge that it looked pathetic. But once blue Sword Energy coated it, it transformed into the finest sword in the world.

Shraaaaak! Shishishiiing!

Sword Energy rained down, cutting through everything around them. Horrible screams erupted from all directions, but Jin Mukyung did not stop swinging his sword.

They were merely the screams of mounted bandits who had been caught in the attack after failing to evade it. The person whose voice Jin Mukyung actually wanted to hear was easily avoiding his sword.

“As expected of the Heaven Shaking Sword. The edge of your sword is fairly sharp.”

Jin Mukyung moved with lightning speed and slashed toward Pung Yang’s waist.

Clang!

When Jin Mukyung’s Sword Energy-wreathed blade collided with Pung Yang’s curved saber, a thunderous boom rang out.

“It’s disgusting hearing that from someone who grew stronger through sorcery.”

“The important thing is that I grew stronger. How many moves do you think that supposedly incredible Tiger of Mount Heng lasted against me?”

“I don’t know.”

Whoosh!

This time, the attack came for his face. Sword strikes poured toward his arms, chest, stomach, side, and legs before suddenly shooting straight upward.

Pung Yang hurriedly pulled his head back. The blade skimmed past his cheek by the narrowest margin.

Sizzle.

But he couldn’t avoid even the sharp pressure of the wind. Blood dripped from the cheek the wind had raked.

Pung Yang retreated without a word, checked the wound, and ground his teeth.

“…You little brat.”

Despite the murderous voice, Jin Mukyung calmly opened his mouth.

“So?”

“What?”

“So how many seconds did Sir Cheol last against you?”

Pung Yang glared at Jin Mukyung for a long moment before answering.

“A hundred moves.”

“What about me?”

“Two hundred moves. I’ll finish you before then.”

“Do you have what it takes?”

“Before cutting off your limbs, I should pull out your tongue first. Listening to you has been pissing me off for a while now.”

“Be grateful you didn’t have to fight my younger brother. If he were your opponent, you’d have already plugged your ears and killed yourself. He’s an expert at making fun of people.”

“The Sleeping Dragon of Shanxi? Then I suppose I should pull his tongue out too.”

“…That actually sounds kind of appealing.”

“Enough nonsense. Raise your sword. That way, you can struggle for even a moment longer before you die.”

The moment Pung Yang’s red eyes gleamed with an eerie light, immense internal energy surged from his lowered saber.

Fwoooosh!

When internal energy was infused into a medium and given tangible form, it was called Sword Energy.

But after taking the Temporary Strength Pill, Pung Yang had now surpassed that realm.

“Sword Force…”

A Supreme Peak master.

It was the symbol of those known as Martial Gods.

Though his enlightenment was insufficient for it to be called true Sword Force, there was no doubt that he had reached the absolute pinnacle of the Peak realm.

“Well, damn.”

Jin Mukyung let out a hollow laugh.

How many years would Pung Yang have needed to reach that realm through training alone? Ten years? Twenty?

But a tiny red pill had allowed him to leap over all those years—the contemplation of martial principles, the endless training, the blood and sweat.

It had let him surpass all of it.

“What kind of son of a bitch made something like that…”

Tsssss.

Sword Energy rose from Jin Mukyung’s sword as well. Pung Yang spoke with open contempt.

“Last two hundred moves, and I’ll let you live.”

“Yeah, go fuck yourself.”

Fwoooosh!

As he watched the Sword Force plunge down as though it meant to split heaven and earth, Jin Mukyung suddenly thought that he was beginning to resemble his insolent youngest brother.

*But what is that guy doing, taking so long to get here?*

KABOOOOM!

* * *

Rumble, rumble, rumble.

The ground shook as though an earthquake had struck.

I had no idea what kind of battle was taking place thirty jang away, but I knew one thing.

*I can’t go over there.*

I wasn’t joking. If I got caught up in that fight, I felt like I would die.

I had no desire to personally experience what happened when a First Rate got its back broken between Peak masters. And more importantly…

Whoosh! Slice!

“Gueeegh.”

This side was hard enough already.

At this point, I might not be a match for a hundred men, but I had to be good for at least seventy.

I swung my weapon like a madman, drenched in the blood pouring down around me.

Shwaaak!

I caught the cavalry spear thrusting toward my side and pulled it toward me. I drove it into the stomach of the man who had been bringing his saber down behind me, then chopped the shaft with the edge of my hand.

Crack!

“Gasp!”

“Use an iron spear next time. Something heavy and sturdy. You can even do squats with it. How great is that?”

Along with the friendly advice, I slammed my fist into the mounted bandit’s jaw. His body went limp as his jawbone shattered.

Shraaaaak!

*Throat, side, leg.*

I could read the daggers thrusting toward me from three directions without even looking at them.

How could every one of them be so slow and predictable?

I was also genuinely amazed by myself. In that brief moment, I could think of a response and put it into action.

Tap. Crack!

I put my weapon into my Inventory, freeing one hand. As I simultaneously caught the wrists of the men stabbing toward my throat and side and broke them, I kicked backward with my leg fully extended.

Their short screams and the dull impact were proof that I had struck them exactly where I intended.

*More. More. More.*

My hands gradually grew faster, and the sounds around me grew more distant.

Every time I brushed against the bodies of the enemies surrounding me, weapons summoned from my Inventory appeared and vanished.

Stabbed, slashed, swung.

Broke.

How many had I brought down?

At some point, the noise that had been pushed far away came rushing back all at once.

Thud.

“Ggh…”

“Urgh.”

The dead lay motionless with their faces buried in the cold dirt. The survivors rolled around, groaning. The twenty or so mounted bandits who had escaped death and injury took several steps backward to get away from me.

“T-the Sleeping Dragon of Shanxi…”

One step. Two steps.

Terrified, they retreated as I advanced, forgetting that furious enemies were still behind them.

Shraaaaak! Thud!

“Kill them! Kill every last mounted bandit!”

“You fucking bastards!”

They were martial artists of the Mount Heng Sword Sect who had survived and fought to the bitter end.

Caught by the bloodshot-eyed men’s surprise attack, the mounted bandits fell like dominoes.

“Kyaaaagh!”

“P-please, spare me…!”

Everywhere I looked, the ground overflowed with corpses, blood, and groans.

How many mounted bandits had died here today? Two hundred? Three hundred?

I didn’t know.

What I did know was that this battle would not end until one person died.

*Pung Yang.*

It was time to deal with that cheating, pill-popping bastard.

“…”

*I can do this, right? I should be able to. Probably…*
```
