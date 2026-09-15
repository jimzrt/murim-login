<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0119.txt",
      "sha256": "ae19e0acb0e346d00c298eb882b1f9976c3e64b34618e0cf55cdb22dd92bfb07",
      "bytes": 14109
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ef5171b1ab250977b241266c09d6bd244309a5f36b6c2ed34704bf49ed831a7b",
      "bytes": 3120
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "805d0d0c2124435a568932abf05bdb3bee6e94919341010e9d24082e38171393",
      "bytes": 18576
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "c06c0f6f11b6ce49702fac761cb2c4ff52d5513023ccd064e3c15188d21550be",
      "bytes": 724
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "357e357a9bc69be03fa8052a714a28449dc2617fd1f56c45ae765ef058245294",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "2d0e3d92c294935c87408dc4c2e40b4799b330422d4fa5e22bbdaedc92711fa6",
      "bytes": 1326
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "0676e9a60fb726cc903e46dc05e7075f5b2331e458c83da2a8c41cad94db34d7",
      "bytes": 8154
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "3b53f20cc728ff44e1f6c69c560f244e8d660ff9be16312587bf6d27b5551655",
      "bytes": 749
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "24a32748dab0bc4ac43ca9dea2e5d3d63ade412153b659f858439d4e0207cd7e",
      "bytes": 1126
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "d5428bc7ed9de2c30cb46e3d515a5e2eae573e3e2cca3f5e9f505d61023ed6fc",
      "bytes": 2314
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "05f382e9d41e20017da3ef8a0906bf0c8e1fdf371061791e6e550bbdbb8d6de0",
      "bytes": 17236
    }
  ],
  "estimated_tokens": 19850
}
-->

# Durable State Update — Chapter 119

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 119. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 119. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 119,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 119,
    "continuity_sources": [119],
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
    "Cheol Mubaek was critically injured after Pung Yang defeated him using a Temporary Strength Pill.",
    "Pung Yang possesses the Crimson Blood martial arts and has reached the Peak realm through them and the Temporary Strength Pill.",
    "Pung Yang can temporarily manifest imperfect Sword Force and can maintain powerful Body-Protecting Qi after taking the pill.",
    "Pung Yang has reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers.",
    "Jin Mukyung is a young Peak-level swordsman known as the Heaven Shaking Sword.",
    "Jin Taekyung is a First Rate martial artist who uses One Annihilation with his iron spear.",
    "Jin Mukyung's visible duel with Pung Yang ended in Mukyung's favor, but Pung Yang's concealed throwing knives left Mukyung unconscious.",
    "Pung Yang killed more than ten Mount Heng Sword Sect martial artists after incapacitating Mukyung.",
    "Pung Yang plans to take both Jin brothers and obtain the Jin Family of Taiyuan's martial arts formulas.",
    "Jin Taekyung has taken the Blazing Flame Divine Pill, temporarily gaining Scorching Yang Qi and raising his internal energy from fifteen to forty-five years.",
    "The Blazing Flame Divine Pill's energy may kill Taekyung if he cannot control it, and the System has created the Divine Pill Absorption Quest.",
    "The pill's temporary energy increase lets Taekyung read and evade Pung Yang's attacks more effectively.",
    "Pung Yang knows the Temporary Strength Pill is a secret legacy of demonic, heterodox arts and has taken it several times.",
    "Pung Yang cut Taekyung's iron spear to less than half its length, but Taekyung learned his attack pattern.",
    "At the confrontation's current endpoint, Pung Yang has raised Body-Protecting Qi and Taekyung has produced a dagger."
  ],
  "continuity_sources": [
    118
  ],
  "open_questions": [
    "Can Jin Taekyung survive and control the Blazing Flame Divine Pill's fire qi?",
    "Can Taekyung defeat Pung Yang before the pill's energy overwhelms him?",
    "Can Taekyung's dagger penetrate Pung Yang's Body-Protecting Qi?",
    "Will Jin Mukyung recover from the five concealed throwing knives?",
    "Can Lee Seowol and the Mount Heng Sword Sect survive Pung Yang's resumed assault?",
    "Will Pung Yang obtain the Jin Family's martial arts formulas?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What lasting consequences will the Blazing Flame Divine Pill have if Taekyung survives?"
  ],
  "safe_through": 118,
  "temporary_decisions": [
    "Render 일류 초입 as early First Rate.",
    "Render 잠력단 as Temporary Strength Pill.",
    "Render 호신강기 as Body-Protecting Qi.",
    "Render 격산타우 as Striking the Ox Across the Mountain.",
    "Render 북망산 as Mount Beimang with a burial-ground footnote.",
    "Render 열화신단 as Blazing Flame Divine Pill.",
    "Render 반 갑자 as half a jiazi, clarified as thirty years.",
    "Retain Narye tagon for 나려타곤 with a footnote explaining the idiom."
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
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |

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
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |

## Exact glossary matches

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 사형     | **Senior Brother**                           |
| 사숙     | **Martial Uncle**                            |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 118
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 115
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 118
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang but was then incapacitated by five concealed throwing knives
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 117
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 117
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 118
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and can temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; has reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 115
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃119화



푹!

손끝을 타고 흐르는 찌릿한 전율. 지금까지 수천, 수만 번도 넘게 느낀 익숙한 감각이다.

‘들어갔구나.’

확신과 동시에 놈의 옆구리에 박아 넣은 비수를 비틀자 풍양의 입에서 비명이 터져 나왔다.

“크아아악!”

비수에 의한 고통도 있겠지만 지금의 일격으로 만만치 않은 내상(內傷)을 입었을 것이다. 미처 완성되지도 못하고 연기처럼 흩어지는 호신강기가 그 증거다.

‘아슬아슬했어.’

풍양의 본능은 보통이 아니었다. 정말 찰나의 순간, 호신강기가 완성되기 직전에 비수가 박히지 않았다면 오히려 내가 당했을 것이다.

“컥!”

풍양이 검은 핏물을 토하며 팔을 뻗었다. 순간 컴컴한 소매 안에서 빛이 번쩍 솟구친다.

쐐애애액!

나는 순간적으로 한 걸음 물러나며 고개를 젖혔다. 풍양의 소매에서 튀어나온 비수 한 자루가 아슬아슬하게 콧날을 스쳐 간다.

‘위험했다.’

물러서지 않았다면 콧날이 아니라 목젖에 박혔을 거다.

앞서 풍양이 비도술을 사용하는 것을 본 덕분에 피할 수 있었다. 나는 혀를 내밀어 콧날을 타고 흐르는 핏물을 날름 받아마셨다.

“고맙다. 안 그래도 목말랐는데.”

“이 쥐새끼 같은 놈이……!”

거리를 벌린 풍양이 이를 갈았다.

“처음부터 이걸 노린 거였나?”

“응. 아프지?”

“기다려라, 백배로 돌려줄 테니.”

“우리 사이에 뭘 또 그렇게까지. 안 갚아도 돼.”

“이이이익!”

놀리는 맛이 제법 쏠쏠하다. 저놈이 화병으로 죽어 주면 참 고맙겠는데 그럴 일은 없겠지.

‘좋은 기회였는데.’

도발로 풍양을 끌어들이는 데까지는 성공했지만 완전히 끝장내는 것은 실패했다. 열화신단을 복용했다지만 아직 나와 풍양의 격차는 컸다.

그리고 무엇보다.

‘슬슬 힘들어지네.’

전신이 불덩이처럼 뜨겁다. 처음부터 통제할 수 없었던 30년의 열양지기는 이제 제멋대로 날뛰는 중이다.

기존의 공력으로 억눌러도 될까 말까인데, 아예 고삐를 놓은 상태로 풍양과 접전을 벌였더니 점차 악화되어 가고 있었다.

‘젠장, 열화신단이 아니라 잠력단이었으면 좋았을 텐데.’

열화신단과 잠력단은 애당초 제조된 목적부터가 다르다.

잠재된 힘을 한계치까지 끌어 올리는 일시적 각성제라고 해야 되나? 비유하자면 한약과 각성제의 차이라고 할 수 있겠다.

‘저놈은 부작용도 없나. 더럽게 쌩쌩하네.’

내심 부러운 마음으로 풍양을 바라본 그때였다.

“쿨럭.”

어, 이것 봐라?

짧은 기침하는 풍양의 눈에, 순간 흰자위가 비쳤다.

시종일관 온통 핏빛처럼 붉었던 눈동자가 저렇게 변한 이유는 아무리 생각해 봐도 하나밖에 없다.

‘잠력단의 효력이 떨어지고 있다.’



* * *



풍양은 당황했다. 그는 자신의 몸에서 일어나는 이상 신호를 곧바로 알아차렸다.

‘벌써?’

잠력단의 효력은 한 시진 남짓. 한데 고작 반 시진이 지난 지금, 전신에서 용솟음치던 힘이 점차 사그라지고 있다.

느껴지지 않던 피로가 둔중하게 어깨를 짓누르고, 멀게 느껴지던 통증이 신경을 건드렸다.

“쿨럭.”

거기에 적지 않은 내상까지.

기침에 섞여 나온 검붉은 핏물에 풍양은 입술을 깨물었다.

‘힘을 너무 소진했어.’

잠력단은 가진 힘을 두 배, 혹은 그 이상으로 끌어 올리는 귀물이지만 그만큼의 대가가 따른다.

일시적으로 강대한 힘을 얻는 대신 신체 능력이 저하되고, 복용자의 신체가 받쳐 주지 않는다면 효능이 사라진다.

‘잠력단을 연이어 복용한 게 문제였다.’

항산호 철무백에 이어 태원진가의 어린놈들까지. 잠력단을 먹지 않았다면 진작 죽었을 테지만 그 대가를 알고 있는 풍양으로서는 후폭풍이 두려웠다.

‘지금 상태대로라면 잠력단의 효능은 길어 봤자 한 식경…….’

한 식경, 그 안에 승부를 봐야 한다.

마지막 남은 잠력단은 결코 쓰여선 안 된다. 연이어 세 개를 복용한다면 목숨이 위험할 수도 있다.

“한 식경이라…….”

작게 중얼거린 풍양이 남아 있는 사냥감들을 노려봤다.

“그 정도면 충분하지.”

언뜻 드러난 흰자위가 다시 핏빛으로 채워졌다.



* * *



착각이었나?

풍양이 다시 고개를 들었을 때, 놈의 눈은 붉었고 전신에서는 감당 못 할 기파가 쏟아져 나왔다.

“단칼에 죽여 주마.”

나는 놈의 곡도를 주시하며 입을 열었다.

“무공 구결 필요하다면서?”

“네가 아니라도 상관없다. 내가 굳이 진무경을 살려 둔 이유가 뭐라고 생각하지?”

“사랑해서.”

“천지신명께 맹세컨대…… 네 혓바닥은 반드시 잘라 주마.”

풍양이 곡도를 치켜세운 다음 순간이었다.

쐐애애액! 탁!

강맹한 기세로 날아온 철시(鐵矢)를 붙잡은 풍양이 눈살을 찌푸렸다.

“죽고 싶은 놈들이 널렸군. 아니, 이번에는 년인가?”

화살의 주인이 천천히 걸어와 내 옆에 섰다. 솜털처럼 가벼운 발걸음과 내 어깨에 닿을까 말까 한 신장. 이 급박한 와중에도 순간 시선을 뺏길 만큼 아름다운 외모.

항산검문주 이소월이 내게 작은 목소리로 속삭였다.

“우리가 시간을 벌게요.”

‘우리’라는 건 이소월을 포함한 살아남은 항산검문의 무인들이었다. 고작 열 명. 엄청난 격전에서 최후까지 버틴 이들답게 하나같이 일류 고수들이지만 상대가 풍양이라면 결과는 불 보듯 뻔하다.

‘전멸.’

이들이 나선다고 한들 얼마나 시간을 벌 수 있을까? 오히려 내게는 방해가 될 공산이 컸다. 냉정하지만 그게 현실이다.

나는 고개를 가로저었다.

“그렇다고 달라지는 건 없을 겁니다.”

“함께 싸우자는 이야기가 아니에요.”

“그럼.”

“형님을 데리고 도망쳐요.”

풍양과 우리의 거리는 고작 십여 장(30m) 남짓. 아무리 작게 말해도 절정 고수인 놈이 못 들었을 리 없다.

“뭐, 도망을 쳐? 크하하하!”

터져 나오는 풍양의 폭소에도 이소월은 아랑곳하지 않고 말을 이었다.

“촌각에 불과하겠지만 시간을 벌어 드릴게요. 최대한 멀리 도망치세요.”

나는 성문 밖으로 시선을 던졌다. 여기서부터 문까지는 약 백 장(300m)의 거리. 얼마 떨어지지 않은 곳에는 월화와 혁무진, 그리고 우리를 태울 말이 있다.

‘시도해 볼 만한 일이야.’

지금도 열화신단에 의해 내상을 입고 있지만 어느 정도는 버틸 만하다. 젖 먹던 힘까지 쥐어짠다면 진무경을 업는다 해도 탈출 가능성이 있다.

하지만…….

‘이들은 죽는다.’

단언컨대, 단 한 명도 예외는 없다. 앞서 이소월이 말한 ‘우리’에는 문주인 자신도 포함되어 있으니 그녀도 죽음을 각오하고 나선 것이다.

‘어째서?’

항산검문과 태원진가는 악연이다. 비록 대장로의 술수에 놀아났다고 해도 서로가 서로를 죽이고, 각자 수많은 피를 흘렸다. 그런데 이소월은 나를 구하려 한다.

자신과 수하들의 목숨을 바쳐서까지.

“그런 얼굴로 볼 필요 없어요. 심사숙고 끝에 내린 결론이니까. 대신 부탁 하나만 해도 될까요?”

내가 물었다.

“그 부탁이 뭡니까?”

“우리를 대신해서 원수를 갚아 주는 것.”

이소월이 서늘한 눈빛으로 풍양을 응시했다.

“저놈을 죽여 주면 돼요. 누구보다 잔인하게.”

한 사람의 죽음을 위해 열 사람이 목숨을 버렸다.

말 한마디, 한마디에 이소월이 품은 원한이 느껴진다. 내가 할 말을 잃은 그때, 비웃음을 띠고 우리를 지켜보던 풍양이 입을 열었다.

“제법 맹랑한 생각을 했다만, 그럴 일은 없을 게다. 너희는 여기서 모두 뼈를 묻을 테니까.”

항산검문의 무인 중 하나가 외쳤다.

“닥쳐라, 이 악독한 놈!”

퍽-!

다음 순간, 무인이 고개가 넘어갔다. 그의 이마에는 풍양이 쥐고 있던 철시가 박혀 있었다.

“사형!”

뒤늦게 터진 비명을 들으며 풍양이 빙긋 웃었다.

“안 그래도 비수가 다 떨어진 참이었는데……. 고맙네, 문주.”

이소월이 입술을 깨물었다.

“가요, 어서!”

나는 크게 심호흡했다. 이미 어떻게 해야 할지는 모두 머릿속에 그려 놓았다.

진무경이 쓰러져 있는 곳까지는 불과 이십여 장(60m). 내상을 감수하고서라도 최대한 공력을 일으켜 업고 달리면 성문까지는 금방이다.

아마 그때쯤에는 풍양에게 따라잡힐지도 모르지만, 이들이 조금만 더 시간을 벌어 준다면 살 수 있다.

‘돌아갈 수 있어.’

진위경이 있는 태원진가로, 어머니와 하연이가 기다리는 집으로 돌아갈 수 있다. 지금 후일을 기약한다면 풍양은 비교도 안 될 만큼 강해져서 돌아올 자신도 있다.

‘그럼 된 거야.’

깊게 심호흡한 나는 이소월을 향해 돌아섰다.

“원수는 갚을 겁니다. 반드시.”

아주 잠깐, 그녀가 웃었다고 생각한 것은 착각일까?

그것은 너무 찰나였고, 다시 본 이소월의 얼굴에는 굳은 결의만이 남아 있었다.

“가세요. 어서.”

그 말이 신호탄이었다. 항산검문의 무인들이 악에 받친 고함과 함께 돌격했다. 그 선두에 이소월이 있었다.

‘그래, 가야지.’

나는 전신의 모든 공력을 끌어 올렸다. 열양지기가 남긴 내상으로 인해 날카로운 통증과 함께 코에서 검붉은 피가 흘렀지만 참았다. 잠깐, 아주 잠깐이면 된다.

‘인벤토리 오픈, 창 장착.’

서늘한 창대가 손아귀에 잡힌다.

그리고 한 번의 발 구름.

쿵.

나는 화살처럼, 아니 화살보다 빠른 속도로 쏘아졌다.

진무경이 아닌 풍양에게로. 놈의 활짝 웃는 얼굴이 보였다.

“그래, 이렇게 나와야지!”

“닥쳐, 이 개새끼야.”

“으하하하!”

풍양의 곡도는 그 어느 때보다 거대했다. 붉은 도기를 한껏 머금은 그것이 나를 향해 휘둘러졌다.

쏴아아악!

바람이 터져 나가고 공기마저 지워지는 듯했다.

나는 철창을 으스러져라 움켜쥐었다.

‘제발, 단 한 번만.’

15년의 공력을 모두 창으로 흘려보냈다. 어깨와 허리를 한껏 젖히고 내 모든 걸 쏘아 보낸다.

‘일섬.’

구구구궁-!

거대한 도기와 와류의 충돌.

하늘이 갈라지는 듯한 굉음이 세상을 가득 메웠다. 휘몰아치는 바람 사이로 똑똑히 보였다.

콰아아아!

붉은 도기 앞에서 산산이 흩어지는 백색 와류. 거대한 기의 결정체는 일섬을 완전히 분쇄했다. 풍양이 희열에 찬 얼굴로 속삭였다.

“여기까지다.”

다음 순간, 창을 타고 솟구친 풍양의 공력이 나를 후려쳤다.

쾅! 아득한 고통과 이명(耳鳴)이 파도처럼 밀려온다.

띠링.



- [내상]을 입었습니다! 상태가 매우 심각합니다!

- [열양지기]가 폭주 중입니다!

- [중상]을 입었습니다! 모든 능력치가 크게 하락합니다!



연이어 울리는 시스템 알림, 항산검문 무인들의 고함, 이소월의 비명, 그리고 풍양의 웃음까지.

‘끝이구나.’

의지와는 상관없이 다리에 힘이 풀린 찰나, 억센 손아귀가 내 목을 틀어쥐었다.

“컥. 커헉.”

“제법이었다. 촌각만 늦었더라면 네가 이겼을지도 모르지.”

풍양이 이를 드러내며 웃었다. 놈의 눈동자에서 붉은 기운이 서서히 사라지고 있었다.

젠장, 더럽게 아깝네.

소리 내서 말하고 싶었지만 핏물이 가득 찬 탓에 그조차도 쉽지 않았다.

“천지신명께 맹세했었지. 반드시 네 혓바닥을 뽑겠다고.”

그런 말을 했었나? 이젠 내가 누구인지도 가물가물하다.

풍양이 다른 한 손으로 내 입을 벌렸다. 핏물로 흠뻑 젖은 혀를 잡아당기는 거친 손가락이 느껴진다.

“흐어…….”

“그 주둥이를 나불거릴 때는 이렇게 될 줄 몰랐나. 응?”

“흐아, 흐하하아.”

“으하하! 뭐라 지껄이는 거냐? 마지막 유언이라도 남기게 해 주랴?”

풍양이 껄껄 웃으며 혓바닥을 놔 주자 비로소 말을 할 수 있게 되었다. 나는 핏물을 꿀꺽 삼키며 말했다.

“짜.”

“뭐?”

“더럽게 짜다고.”

“그게 무슨 개소리냐?”

무슨 소리긴.

네 손가락 맛을 보고 약간 정신이 돌아왔다는 소리지.

나는 혼미한 정신으로 중얼거렸다.

‘인벤토리 오픈, 아무거나 소환.’

띠링.



- [아무거나]라는 아이템을 찾을 수 없습니다. 인벤토리에 보관된 것 중 가장 오래된 아이템부터 소환합니다.

- [이름 없는 검]이 소환되었습니다.



이름 없는 검? 그게 뭐였더라.

‘뭐든 어때.’

나는 마지막 힘을 끌어올려 손에 든 검을, 호신강기가 서린 풍양의 가슴을 향해 찔러 넣었다. 그건 결말이 뻔한 발악이었다.

‘빌어먹을 호신강기.’

하지만 이걸로 됐다. 더 이상 후회는 없으니까.

고개가 스르륵 내려가던 그 순간이었다.

푹-!

띠링.



- [이름 없는 검]이 특정 조건을 만족합니다.

- [만년한철]이 [호신강기]를 파괴했습니다.



……응?
```

## Final English reading copy

```markdown
# Chapter 119

*Thud!*

A tingling tremor ran through my fingertips. It was a familiar sensation, one I had felt thousands, tens of thousands of times before.

*It went in.*

At the same time as that certainty struck me, I twisted the dagger buried in Pung Yang’s side. A scream burst from his mouth.

“Graaaargh!”

The dagger itself must have caused excruciating pain, but that blow had also inflicted a serious internal injury. The Body-Protecting Qi that had failed to fully form before scattering like smoke was proof enough.

*That was close.*

Pung Yang’s instincts were extraordinary. If the dagger hadn’t pierced him in that fleeting moment, just before his Body-Protecting Qi was completed, I would have been the one in trouble.

“Guh!”

Pung Yang spat out dark blood and reached out with one arm. In that instant, a flash of light burst from inside his pitch-black sleeve.

*Shweeeeeek!*

I instinctively took a step back and tilted my head. A dagger shot from Pung Yang’s sleeve and narrowly grazed the bridge of my nose.

*That was dangerous.*

If I hadn’t stepped back, it would have struck my throat instead of my nose.

I was only able to evade it because I had seen Pung Yang use throwing knives earlier. I stuck out my tongue and licked up the blood running down the bridge of my nose.

“Thanks. I was thirsty anyway.”

“You little rat bastard…!”

Pung Yang widened the distance between us and ground his teeth.

“Was this what you were aiming for from the beginning?”

“Yeah. Does it hurt?”

“Wait. I’ll pay you back a hundredfold.”

“There’s no need to go that far between friends. You don’t have to pay me back.”

“Grrrrrgh!”

Teasing him was surprisingly satisfying. It would be nice if he died of rage, but there was no chance of that happening.

*It was a good opportunity.*

I had succeeded in drawing Pung Yang in by taunting him, but I had failed to finish him off completely. Even after taking the Blazing Flame Divine Pill, the gap between Pung Yang and me was still enormous.

And more importantly—

*This is getting difficult.*

My entire body was hot as a furnace. The thirty years of Scorching Yang Qi that I hadn’t been able to control from the beginning was now running wild of its own accord.

It would have been touch and go even if I’d tried to suppress it with my existing internal energy, but I’d fought Pung Yang at close quarters with the reins completely off, and my condition was steadily worsening.

*Damn it. I wish this had been a Temporary Strength Pill instead of the Blazing Flame Divine Pill.*

The Blazing Flame Divine Pill and the Temporary Strength Pill had been created for entirely different purposes.

Was the Temporary Strength Pill a stimulant that temporarily awakened latent power and raised it to its limit? To put it simply, the difference was like that between traditional herbal medicine and a stimulant.

*Does that bastard not have any side effects? He’s annoyingly full of energy.*

I was looking at Pung Yang with a trace of envy when—

“Cough.”

Oh? What was this?

For an instant, the whites of Pung Yang’s eyes showed through during his short cough.

His eyes had been completely blood-red the entire time. No matter how I thought about it, there could only be one reason for this change.

*The Temporary Strength Pill is losing its effect.*

* * *

Pung Yang was flustered. He immediately recognized the abnormal signs appearing in his body.

*Already?*

The Temporary Strength Pill’s effect lasted a little over one shichen. Yet now, after barely half a shichen had passed, the power that had been surging through his entire body was gradually fading.

Fatigue he hadn’t felt before pressed heavily down on his shoulders, and pain that had seemed distant began to prick at his nerves.

“Cough.”

On top of that, he had suffered a considerable internal injury.

Pung Yang bit his lip as dark-red blood came out with his cough.

*I’ve expended too much strength.*

The Temporary Strength Pill was a wondrous object that could draw out twice, or even more than twice, the strength a person possessed—but it demanded an equal price.

In exchange for temporarily granting tremendous power, it weakened the body’s physical abilities. If the user’s body could not support it, the effect would disappear.

*Taking the Temporary Strength Pills one after another was the problem.*

First the Tiger of Mount Heng, Cheol Mubaek, and then the young brats from the Jin Family of Taiyuan. If he hadn’t taken the pills, he would have died long ago, but Pung Yang knew the price he would have to pay and feared the aftermath.

*At this rate, the Temporary Strength Pill’s effect will last only one meal’s time longer at most…*

He had to settle the battle within that time.

He must not use the last Temporary Strength Pill. Taking three in succession could put his life at risk.

“One meal’s time…”

Pung Yang muttered under his breath and glared at the remaining prey.

“That’s more than enough.”

The whites of his eyes disappeared again, filled once more with blood-red light.

* * *

Had I been mistaken?

When Pung Yang raised his head again, his eyes were red, and an overwhelming aura poured from his entire body.

“I’ll kill you with a single stroke.”

I watched his curved saber and opened my mouth.

“I thought you needed the martial arts formulas.”

“It doesn’t have to be you. Why do you think I went to the trouble of keeping Jin Mukyung alive?”

“Because you love him.”

“I swear by the gods of heaven and earth… I will cut out your tongue.”

The next moment, Pung Yang raised his curved saber.

*Shweeeeeek! Clang!*

Pung Yang caught an iron arrow flying toward him with tremendous force and frowned.

“There are plenty of bastards who want to die. Or is it a bitch this time?”

The owner of the arrow slowly walked over and stood beside me. Her footsteps were light as down, and her height barely reached my shoulder. Even in this desperate situation, her beauty was enough to steal my gaze for an instant.

The Sect Leader of the Mount Heng Sword Sect, Lee Seowol, whispered to me in a low voice.

“We’ll buy you some time.”

*We* meant the surviving martial artists of the Mount Heng Sword Sect, including Lee Seowol. There were only ten of them. As befitted those who had survived until the end of such a brutal battle, every one of them was a First Rate master, but against Pung Yang, the outcome was obvious.

*They’ll all be wiped out.*

How much time could they buy even if they stepped forward? They were more likely to get in my way. It was coldhearted, but that was reality.

I shook my head.

“That won’t change anything.”

“We’re not saying we’ll fight alongside you.”

“Then?”

“Take your brother and run.”

The distance between Pung Yang and us was only a little over ten zhang—about thirty meters. No matter how quietly she spoke, there was no way a Peak master like him hadn’t heard her.

“What, run? Hahahaha!”

Despite Pung Yang’s booming laughter, Lee Seowol continued speaking without flinching.

“It may only be for a fleeting moment, but we’ll buy you time. Run as far away as you can.”

I turned my gaze toward the fortress gate. It was about one hundred zhang—three hundred meters—from here. Wolhwa, Hyuk Mujin, and the horses waiting to carry us were not far beyond it.

*It’s worth trying.*

I was already suffering internal injuries from the Blazing Flame Divine Pill, but I could still endure them to some extent. If I squeezed out every last bit of strength I had, I might be able to escape even while carrying Jin Mukyung on my back.

But…

*They’ll die.*

Every last one of them. Not a single exception.

Lee Seowol herself was included in the *we* she had mentioned. She had stepped forward prepared to die as well.

*Why?*

The Mount Heng Sword Sect and the Jin Family of Taiyuan were bitter enemies. Even if they had been manipulated by the Head Elder’s schemes, they had killed one another, and both sides had shed a great deal of blood.

And yet Lee Seowol was trying to save me.

She was willing to sacrifice her own life—and the lives of her subordinates—to do it.

“You don’t need to look at us like that. I reached this conclusion after careful consideration. In return, may I ask you for one thing?”

I asked her,

“What is it?”

“Aveng​e us in our place.”

Lee Seowol stared at Pung Yang with icy eyes.

“Kill that man. As cruelly as possible.”

Ten people were throwing away their lives for one person’s death.

I could feel the hatred Lee Seowol held in every word she spoke. Just as I was rendered speechless, Pung Yang, who had been watching us with a mocking smile, opened his mouth.

“That’s a bold idea, but it won’t happen. You’ll all bury your bones here.”

One of the Mount Heng martial artists shouted.

“Shut up, you vicious bastard!”

*Thwack!*

The next moment, the martial artist’s head jerked back. The iron arrow Pung Yang had been holding was embedded in his forehead.

“Senior Brother!”

As the belated scream rang out, Pung Yang smiled.

“I was just about out of throwing knives, too… Thank you, Sect Leader.”

Lee Seowol bit her lip.

“Go! Hurry!”

I took a deep breath. I had already drawn out every step in my mind.

Jin Mukyung had fallen only about twenty zhang—sixty meters—from here. If I drew out as much internal energy as possible, ran while carrying him on my back, and endured the internal injuries, I could reach the fortress gate quickly.

Pung Yang would probably catch up to me by then, but if these people bought me just a little more time, I could survive.

*I can go back.*

I could return to the Jin Family of Taiyuan, where Jin Wikyung was, and to the home where my mother and Hayeon were waiting. If I lived to fight another day, I was confident I could return much stronger—strong enough to make Pung Yang seem insignificant by comparison.

*That’s enough.*

After taking another deep breath, I turned toward Lee Seowol.

“I’ll avenge you. I swear.”

For the briefest instant, did Lee Seowol smile?

It was so fleeting that I might have imagined it. When I looked again, only firm resolve remained on her face.

“Go. Hurry.”

Her words were the starting signal. The Mount Heng martial artists charged with furious shouts, Lee Seowol at the front.

*Yes. I have to go.*

I drew up every last bit of internal energy in my body. Sharp pain tore through me as the internal injuries left by the Scorching Yang Qi sent dark-red blood flowing from my nose, but I endured it.

It only had to last a moment. A very brief moment.

*Inventory open, equip spear.*

The cool shaft of the spear settled into my grip.

Then I pushed off once.

*Boom.*

I shot forward like an arrow—no, faster than an arrow.

Not toward Jin Mukyung, but toward Pung Yang. I could see his broad smile.

“That’s more like it!”

“Shut up, you son of a bitch.”

“Ha-ha-ha-ha!”

Pung Yang’s curved saber was larger than ever before. Brimming with red saber qi, it swung toward me.

*Whoooosh!*

The wind exploded, and even the air seemed to vanish.

I gripped the iron spear until it felt as though it might crumble in my hands.

*Please. Just this once.*

I poured all fifteen years of my internal energy into the spear. Drawing back my shoulder and waist as far as I could, I sent everything I had flying forward.

*One Annihilation.*

*Rumble-rumble-rumble!*

A gigantic mass of saber qi collided with the vortex.

A thunderous roar filled the world, as though the sky itself were splitting apart. Through the raging wind, I saw it clearly.

*Kaboom!*

The white vortex shattered into pieces before the red saber qi. The massive concentration of qi completely pulverized One Annihilation.

Pung Yang whispered with an ecstatic expression,

“This is as far as you go.”

The next moment, Pung Yang’s internal energy surged along the spear and hammered into me.

*Boom!*

Blinding pain and ringing ears rolled over me like waves.

*Ding.*

> **System**
> - You have suffered **Internal Injury**! Your condition is extremely serious!
> - **Scorching Yang Qi** is running wild!
> - You have suffered a **Severe Injury**! All stats have dropped significantly!

System notifications rang out one after another, mixed with the shouts of the Mount Heng martial artists, Lee Seowol’s scream, and Pung Yang’s laughter.

*It’s over.*

The instant my legs gave out despite my will, a powerful hand clamped around my throat.

“Guh. Guhh.”

“That was fairly impressive. If I’d been only a moment slower, you might have won.”

Pung Yang bared his teeth in a grin. The red light in his eyes was slowly fading.

*Damn it. I was so damn close.*

I wanted to say it aloud, but my mouth was full of blood, making even that difficult.

“I swore by the gods of heaven and earth, didn’t I? I swore I’d pull out your tongue.”

Had he said that? By now, even who I was had become hazy.

Pung Yang pried open my mouth with his other hand. I felt his rough fingers tugging on my blood-soaked tongue.

“Ghh…”

“When you were flapping that mouth, didn’t you know this would happen? Huh?”

“Ghaa… hahahaa.”

“Hahaha! What the hell are you mumbling? Shall I let you leave some last words?”

Pung Yang laughed heartily and released my tongue. Only then could I speak. I swallowed the blood in my mouth and said,

“Salty.”

“What?”

“It’s insanely salty.”

“What kind of bullshit is that?”

*What do you think?*

*I’m saying the taste of your fingers brought me back to my senses a little.*

I muttered through my fading consciousness.

*Inventory open, summon anything.*

*Ding.*

> **System**
> - No item named **Anything** can be found. The oldest item stored in your inventory will be summoned first.
> - The **Unnamed Sword** has been summoned.

*The Unnamed Sword? What was that again?*

*Whatever.*

I gathered up the last of my strength and thrust the sword in my hand toward Pung Yang’s chest, which was shrouded in Body-Protecting Qi.

It was a futile last-ditch attack with an obvious conclusion.

*Damn Body-Protecting Qi.*

But this was enough. I had no regrets left.

It was at that moment, as my head slowly drooped—

*Thud!*

*Ding.*

> **System**
> - The **Unnamed Sword** satisfies a specific condition.
> - **Ten-Thousand-Year Cold Iron** has destroyed **Body-Protecting Qi**.

…Huh?
```
