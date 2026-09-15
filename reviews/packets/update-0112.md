<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0112.txt",
      "sha256": "cc139115c2ba518071cced9254e85ee9a67732ec7166ee1df47bd44114adf859",
      "bytes": 14613
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e980e85fc0b072473131496ba9a5b8150cb0a2ef17776f36e2295bf91b008b2c",
      "bytes": 5292
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a0746fb402dce170764e151f3f77b1eb6d6bbd874752dcc6b16c0681c2b9d348",
      "bytes": 16396
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "2489211d2b58c888c73b76de2fddb83c052e51416ce25da0d31373b3dd9b19a8",
      "bytes": 724
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "73f5171380a89f4862376c813ada0c493aa66f1b08c990b6c2490cd3088ef9fb",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e4400c12eaabb735c19ee3c41e24a2f568f202098f26c7455425eb989da2362f",
      "bytes": 24117
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "599818f57ccd1ea887d385fd60d73b909b20824b72f0c59ac6052e7a069bf946",
      "bytes": 3231
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "a86576093b00db31b4aa1b25fa1a69e9fcb638d8826223b27abd9be535e8f850",
      "bytes": 749
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "0a0b7596c8830dedb8273a263969491c188e37ddd72bb01c6e98b6eff8da2544",
      "bytes": 563
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "079f31258d8a35d65fc2c0ca7a78d698dae5ec85bd69b4f56c2f9b1dc7a8f7cc",
      "bytes": 15617
    }
  ],
  "estimated_tokens": 19417
}
-->

# Durable State Update — Chapter 112

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 112. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 112. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 112,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 112,
    "continuity_sources": [112],
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
    "Jin Taekyung, Jin Mukyung, Hyuk Mujin, and Wolhwa are riding toward the Mount Heng Sword Sect; their exhausted horses have been replaced with at least ten fresh horses taken from defeated Red Wind Band mounted bandits.",
    "Taekyung's displayed Quest time limit fell from 16:25:32 to 15:59:13 after six hours elapsed during the journey.",
    "The Red Wind Band has more than one hundred remnants scattered throughout northern Shanxi as ambush forces; Pung Yang is replenishing forces on the plateau and moving south while sending remaining subordinates north.",
    "Pung Yang is an early Peak master whose saber arts and throwing-knife techniques have reached a high realm; Cheol Mubaek suspects that his insidious forms derive from demonic, heterodox martial arts.",
    "Cheol Mubaek and Pung Yang have already clashed once; Pung Yang withdrew with a minor internal injury, and Cheol Mubaek currently has the advantage in a life-and-death duel between them.",
    "The Mount Heng Sword Sect is being attacked by a force close to three hundred from both directions, while the sect has fewer than half that number even after recalling martial artists from its branches; morale is low.",
    "Lee Seowol's mother, father Lee Cheonbaek, and two older brothers are dead, leaving her as the last surviving blood relative of Lee Cheonbaek and the new Sect Leader of the Mount Heng Sword Sect.",
    "Lee Cheonbaek had planned to link Lee Seowol to Jin Taekyung to provoke an unbearable scandal while the Strange Hero of Shanxi and Jin Mukyung were absent, treating that moment as the best opportunity to wage war against the Jin Family of Taiyuan.",
    "Cheol Mubaek urged Lee Seowol to escape, but she refused and declared that remaining and surviving as Sect Leader was her own choice.",
    "Lee Seowol estimates Mount Heng's chance of victory at ten percent immediately and fifty percent or more if reinforcements arrive.",
    "A messenger pigeon from the Lower District Sect's Jeongyang Branch arrived four hours earlier with notice that four reinforcements were coming, including Jin Mukyung and Jin Taekyung.",
    "The Quest concerning the Mount Heng Sword Sect is graded Peak and requires Taekyung to deliver an invitation to the Jin Family during the upcoming Lunar New Year.",
    "The Quest requires Taekyung to reach the Mount Heng Sword Sect within twenty-two hours, and being late is irreversible.",
    "Taekyung is Level 55, and Hyuk Mujin is Level 38 after rising from Level 20 over roughly two months."
  ],
  "continuity_sources": [
    111
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation and why he now works as a butler despite his former instructor status and exceptional ability remain unknown.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol and Mount Heng will respond to the merger proposal, and what compensation or territorial concession Wolhwa will receive, remain unresolved.",
    "What final outcome will follow Cheol Mubaek and Lee Seowol's assertion of authority inside the damaged main hall remains unresolved.",
    "Whether Pung Yang truly learned demonic, heterodox martial arts remains unconfirmed."
  ],
  "safe_through": 111,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술 and keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you; 김화종's 춘수 and 교관님 as Chunsoo and Instructor; 1번 훈련생 as Trainee Number One; and 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year; 봉황객잔 as Phoenix Inn; 계용옥미갱 and 계용옥미앵 as chicken-and-corn soup; and 곡도 as curved saber.",
    "Render 마적 and 마적단 as mounted bandits and mounted-bandit groups; 적풍단 as Red Wind Band; 적풍단주 as Red Wind Band Leader; and 토호단 as Earth Tiger Band.",
    "Render 초일류 as master beyond First Rate; preserve Wolhwa's Young Master forms for Taekyung and Young Hero Jin for Mukyung; render 관제묘 as Guandi Temple and 흑도 as dark-path figures; render 소월 as Seowol and 철 숙부 as Uncle Cheol.",
    "Render 오색귀 as Five-Colored Ghosts, 이삼 as Lee Sam, 전서응 as messenger hawk, and 대형 as Boss.",
    "Render 추종향 as tracking scent, 대동 as Datong, 풍양 as Pung Yang, 춘삼 as Chunsam, 철검대주 as Iron Sword Squad Leader, 대항산검문 as great Mount Heng Sword Sect, and 대동지부 as Datong Branch.",
    "Render 절정 as Peak, 절정 초입 as early Peak, 일류 as First Rate, 일격 as One Strike, 단주 as Leader, 아가씨 as Young Lady, 문주님 as Sect Leader, 반 시진 as one hour, 산서괴협 as Strange Hero of Shanxi, 녹림맹주 as Green Forest Alliance Leader, 장강수로맹주 as Alliance Leader of the Yangtze River Channel League, and 사마외도 as demonic, heterodox arts."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 이소광    | **Lee Seogwang**   |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 111
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 111
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 111
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 111
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 111
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 111
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band; commands a force of at least two hundred mounted bandits
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃112화



마적이 백주대낮에 대로를 활보한다?

평소라면 결코 있을 수 없는 일이다. 가장 먼저 인근의 무림 문파가 나설 것이고 그다음은 관아의 병졸들이 제압할 것이다.

그러나 마적들의 숫자가 수백에 달한다면, 그들을 토벌해야 할 무림 문파조차 압도한다면 관아의 벼슬아치도 눈을 감고 귀를 막을 수밖에 없다.

바로 지금처럼.

“저, 저놈들 마적 아니여?”

“놈이라니, 자네 목숨이 세 개쯤 되나? 그 악명 높다는 적풍단이잖아.”

“그 적풍단? 얼마 전에 항산검문이랑 붙어서 깨진 것 아니었나?”

“그런 줄 알았지. 한데 이번에는 좀 다른가 보더라고. 벌써 저잣거리에 항산검문이 멸문지화를 면치 못할 거라는 소문이 파다해.”

“그래도 깜냥이 있는데 설마하니 마적들 따위한테…….”

“어허, 그 입! 맨 앞에 가는 저 사내가 풍양이라고, 적풍단 두목인데 절정 고수라더군.”

“뭣이, 절정 고수?”

“그래, 마적이라고 무시할 게 못 된다니까. 듣기로는 무공만 강한 게 아니라 머리도 아주 비상하다던데.”

양민들의 두려움 섞인 웅성거림이 풍양과 휘하 마적들의 귓속을 파고들었다.

풍양의 오른편에서 말을 몰던 수하가 넌지시 말을 건넸다.

“저놈들의 주둥이를 찢어 놓을까요?”

“그리하고 싶으냐?”

“단주께서 허락해 주신다면 저 두 놈부터 처리한 다음 마을 전체를 불바다로 만들지요.”

“늙은이들은 죽이고, 젊은 놈들은 사로잡고, 여인들은 겁탈하겠다?”

“흐흐, 저 같은 놈들한테야 늘 하던 일 아닙니까. 어차피 항산검문 놈들은 지금쯤 겁을 잔뜩 집어먹고 담벼락 뒤에 숨어 있을 터인데.”

“그렇겠지. 모든 힘을 끌어모은 일전을 준비 중일 것이다.”

“그래 봤자 계란으로 바위 치깁니다. 단주께서 항산검문 놈들을 쓸어 버리고 그 자리를 차지하시는 건 기정사실이죠.”

“그래서 허락하지 않는 것이다.”

“예?”

풍양은 어리둥절한 수하의 반응에 너털웃음을 터트렸다.

하나같이 생각이 짧고 천성이 잔인하다. 그래서 마적이 된 것이고, 풍양이 그들을 곁에 두는 이유이기도 했다.

‘다루기가 쉬우니까.’

웃음을 그친 그가 입을 뗐다.

“대동지부를 몰살시킨 것은 전쟁의 일부다. 그러나 지금 양민들을 건드렸다가는 태원진가가 끼어들 구실을 만들어 주는 것밖에 안 돼.”

“그놈들이 산서성의 주인이라도 된답니까?”

“아직은 아니지만 머지않아 그리되겠지. 그전에 항산검문을 집어삼키고 개처럼 넙죽 엎드려 있어야 하지 않겠느냐?”

“저어, 단주님 말씀을 의심하는 건 아닙니다만…… 태원진가 같은 정파 놈들이 우리 같은 마적들을 좋게 보겠습니까?”

“마적? 누가 마적이냐?”

“예?”

“지난번에 보니 항산검문주의 미색(美色)이 대단하더구나.”

눈을 껌뻑거리던 풍양의 수하는 마침내 뜻을 알아차리고 입꼬리를 말아 올렸다.

“혼기가 꽉 찼으니 지아비를 맞이해야 하겠군요.”

“멸문지화와 혼인. 둘 중 하나를 택해야겠지.”

“그럼 적풍단은……?”

“알맹이를 취하고 껍데기는 뒤집어써야지. 어디 보자, 다른 놈들에 비해 네가 그나마 얼굴이 멀쩡하니 수문각주를 시켜 주마.”

“으하하! 목숨을 다 바쳐 충성하겠습니다.”

수하의 웃음소리를 들으며 풍양은 고삐를 움켜쥐었다.

‘마침내 여기까지 왔다.’

냉철한 성격의 소유자인 그였지만 야망을 향해 한 걸음 다가섰다는 생각에 가슴이 뛰었다.

오래전의 기억이 새록새록 떠올라 눈앞을 스친다.

‘벌써 이십 년이 훌쩍 넘었군.’

마적이 되는 길은 생각 이상으로 쉽고 간단했다. 제 발로 찾아가거나, 잡히거나. 풍양의 경우에는 후자였다.

어린 시절 죄를 지어 관아로 압송되어 가던 도중에 마적단의 습격을 받은 것이 인생의 전환점이었다.



‘두목, 여기 어린놈도 있는데요?’

‘응? 비쩍 곯아서 팔아 봤자 몇 푼 받지도 못하겠네. 꼬마야, 소매치기라도 하다가 걸렸냐?’

‘아뇨. 사람을 죽여서요.’

‘사람을 죽였다고? 네 나이가 몇인데?’

‘열셋이요.’

‘죽인 이유는?’

‘사흘 동안 굶었는데 왕초가 만두를…….’

‘만두? 동냥질한 걸 뺏긴 거냐? 그럼 눈 돌아갈 만하지.’

‘그게 아니라요. 배는 고프고, 동냥질할 힘도 없고. 앞에서는 만두를 먹으니까.’

‘……그래서 죽였다?’

‘뺏어 먹는 게 빠를 것 같아서요.’

‘야, 이놈 풀어 주고 뭐라도 먹여. 오늘부터 우리 식구다.’



풍양은 그날부로 마적이 됐다. 천애 고아로 유리걸식하던 그는 눈치가 비상했고 머리 회전도 빨랐다.

사흘에 한 끼를 먹을까 말까 했던 과거에 비하면 마적 생활은 풍요로웠다.

약탈? 살인? 고작 열세 살에 만두를 먹고 싶다는 이유로 살인을 저질렀던 풍양에게는 당연히 해야 할 일에 불과했다.



‘허 참, 내가 마적질만 십 년 넘게 했는데 너 같은 놈은 처음 본다. 죄책감이라는 게 없는 놈 같아.’

‘왜요? 전 마적이잖아요.’

‘자식이. 보통은 그게 아니라니까. 차차 익숙해지는 거지, 처음부터 능숙한 놈은 없다고.’

‘두목도 그러셨어요? 전 쉽던데.’

‘쉽다, 쉽다라……. 이거 범 새끼를 키우는 게 아닌가 싶긴 한데, 나한테 무공 한 수 배워 볼 테냐?’

‘무공이요?’

‘그래, 무공. 너야 아직 어린 나이니까 근골과 무재만 좀 받쳐 준다면 충분히 고수가 될 수 있을 게다.’

‘그럼 오늘부터 사부라고 부를게요.’

‘사제지간은 염병, 됐으니까 지금처럼만 해.’



사제지간을 맺지 않은 건 잘한 일이었다. 일 년 후, 두목은 일류 고수에게 목이 잘려 죽었고 풍양은 새로운 마적단에 둥지를 틀었다.



‘광칠이 밑에 있었다고?’

‘예. 배불리 먹여 주시기만 하면 충성을 바치겠습니다.’

‘눈치는 제법 있어 보이는군. 어린놈이라고 봐주는 거 없으니까 알아서 잘 따라와라.’



고원은 치열했다. 상단을 잘못 건드렸다가 마적단 전체가 몰살되는 일도 있었고 마적단들끼리의 알력 다툼도 끊이질 않았다. 그러나 풍양은 매번 살아남았고, 점점 강해졌다.

그의 나이 이립(而立)이 되었을 때, 무공은 일류에 접어들었고 제법 규모 있는 마적단의 조장 자리를 꿰찰 수 있었다.

‘하지만 딱 거기까지였지.’

힘의 법칙은 어디에나 적용되는 법.

고원도 결국 강자가 지배하는 무림의 일부분이었다.

풍양에게는 원대한 야망과 뛰어난 머리가 있었지만, 우두머리에 걸맞은 무력을 갖추지는 못했다.

‘삼류 무공의 한계.’

풍양의 무재는 뛰어났다.

어린 시절 명문 정파에 입문하여 훌륭한 내공심법과 무공을 익혔다면 진즉 절정의 벽을 넘어섰을지도 모른다.

그러나 거지 소굴에서 자라고 고원의 마적들에게 삼류 무공을 배운 그의 한계는 명확했다.

‘천운(天運)이 따르지 않았다면 지금도 제자리걸음이었겠지.’

풍양의 입가에 진한 웃음이 맺혔다.

삼 년 전, 그날을 기점으로 풍양의 인생은 송두리째 바뀌었다. 마적단의 일개 조장에서 고원의 한 축을 움직이는 적풍단의 단주, 그리고 이제는 무림 문파를 집어삼킬 차례다.

“단주!”

수하의 외침에 풍양은 상념에서 깨어났다. 저 멀리, 성벽처럼 높게 쌓아 올린 돌담이 마침내 모습을 드러내고 있었다.

‘항산검문.’

자신과 적풍단의 새로운 보금자리를 바라보던 풍양의 시선에 한 사람이 들어왔다. 멀리 떨어진 거리에서도 느껴지는 불같은 기세.

‘항산호 철무백.’

항산검문을 취하기 위해서는 반드시 넘어야 할 벽.

비록 지난번에는 약간의 손해를 보고 물러났지만…….

‘오늘은 다르지.’

풍양은 무의식적으로 품 안을 더듬었다. 단단한 목갑을 확인한 그의 웃음이 더더욱 진해졌다.

“단주, 명령을.”

“포위해라. 개미 새끼 한 마리 빠져나가지 못하도록. 그다음에 사자를 보내.”

멸문과 혼인.

항산검문에게 주어진 선택지는 두 개뿐이다.

“오늘 해가 지기 전에 항산검문을 손에 넣을 것이다.”



* * *



“놈들이 본 문을 빈틈없이 에워쌌습니다!”

“그 숫자가 이백이 훌쩍 넘어갑니다!”

“문주, 부디 결단을.”

상석에 앉아 있던 이소월은 침착한 얼굴로 입을 열었다.

“병력 배치는 끝났나요?”

“백여 명 중 절반은 문을 막고 나머지는 방패와 활로 무장시켰습니다.”

말이 백여 명이지, 실은 그것에 한참 못 미친다는 사실을 대전의 모두가 알고 있었다.

지난밤 항산검문의 중진 몇이 가족과 자신들을 따르는 수하들을 데리고 줄행랑을 쳤기 때문이다.

“철 숙부, 제가 따로 말씀드린 건 어떻게 됐나요?”

“네 말대로 조치해 두었다.”

이소월의 계책은 다름 아닌 기름이었다. 장원 곳곳에 마차 열 대 분량의 기름을 골고루 뿌려 놓았다.

잘 마른 건초 더미로 덮어 두었으니 불이 닿기만 해도 사방이 불바다로 변할 것은 자명했다.

‘동귀어진이라도 할 셈인가?’

철무백은 걱정스러웠지만 말을 아꼈다. 그가 오랜 세월 지켜봤던 이소월은 아주 어린 시절부터 언제나 침착하고 총명한 아이였다.

“하루, 딱 하루만 버티면 됩니다. 태원진가의 지원군이 오고 있으니 그때까지만 시간을 끌면 충분히 승산이 있어요.”

“태, 태원진가에서 지원군을 보냈습니까?”

“산서잠룡과 진천검이 직접 오고 있다는군요.”

대전에 모인 이들의 얼굴이 한층 밝아졌다. 진천검 진무경이야 이미 중원에서도 명성이 자자한 무공의 천재고, 산서잠룡 진태경은 떠오르는 샛별이다.

그가 항산검문과의 전쟁을 통해서 명성을 얻었다는 사실은 껄끄럽지만 한 편이라고 생각하니 천군만마가 따로 없다.

무엇보다…….

“풍양이 아무리 간 큰 놈이라고 해도 태원진가의 직계를 상대로 검을 겨누진 못할 겁니다.”

“……그렇겠죠.”

이소월은 내심 씁쓸했다. 얼마 전만 하더라도 태원진가와 어깨를 나란히 하던 항산검문이다.

산서 북부를 호령하던 무림 문파가 이제는 마적단을 상대로도 버티는 것에 주력해야 한다니.

‘오늘 일은 결코 잊지 않는다.’

입술을 질끈 깨문 그 순간이었다.

대전 문이 열리고 수문각의 무사가 헐레벌떡 뛰어와 외쳤다.

“문주님, 적들이 사자를 보내왔습니다!”

“사자?”

“예. 직접 만나 뵙고 전해 드릴 말이 있다고…….”

이소월은 망설임 없이 고개를 끄덕였다.

일각이라도 전투를 늦출 수 있다면 뭐든지 해야 한다.

“들여라.”

수문각 무사가 물러난 지 얼마 되지 않아 적풍단의 사자가 대전으로 안내되었다. 썩은 이를 드러내며 히죽 웃은 그가 과장되게 허리를 굽혔다.

“대항산검문의 문주님을 뵙소.”

다분히 조롱 섞인 태도였지만 중진들은 물론이고 불같은 성격인 철무백도 분노를 참았다. 앞서 이소월의 신신당부가 있었기 때문이다.

“무슨 일로 사자를 보냈지?”

“거, 먼 길 온 사람한테 탁주라도 한 사발 주고 물어봐야 하는 것 아니…… 헉.”

적풍단의 사자는 말을 잇지 못하고 몸을 부르르 떨었다.

분노를 참지 못한 철무백이 한 걸음 앞으로 나서며 엄청난 기세를 내뿜었기 때문이다.

“탁주가 그리 먹고 싶더냐?”

깊게 가라앉은 음성에 사자가 정신없이 고개를 흔들었다.

“아, 아닙니다. 목이 말라서 허, 헛소리를 그만.”

“철 숙부. 그만하세요.”

“……흥, 헛소리 그만하고 말이나 전해라.”

간신히 철무백의 기세에서 풀려난 사자가 더듬더듬 입을 열었다.

“다, 단주께서 말씀하시길, 무익한 전쟁은 멈추고 이제 우의를 다지자 하십니다.”

“우의?”

항산검문의 중진들은 자신의 귀를 의심했다.

전대 문주인 이천백을 배신하고 소문주 이소광마저 죽인 것이 누구인가? 심지어 바로 얼마 전에는 대동지부의 식솔들을 몰살시키기까지 하지 않았던가.

그러나 이소월의 반응은 달랐다. 그녀는 놀란 기색도 없이 사자를 똑바로 응시했다.

“거절한다면?”

“멸문지화를 면치 못할 거라 하셨습니다.”

“사람들을 살리고 싶으면 혼인 예물로 항산검문을 통째로 바치라는 뜻이군.”

“저, 저는 거기까지는 잘…….”

이쯤 되니 대전 안의 사람들도 풍양이 전한 ‘우의’의 의미를 알아차릴 수 있었다. 모두가 분노했지만 그중 가장 빠르게 움직인 사람은 항산호 철무백이었다.

퍽!

말 그대로 찰나의 순간, 십여 장의 거리를 뛰어넘은 철무백의 일 권이 사자의 가슴에 박혔다. 가공할 열기를 머금은 붉은 권기(拳氣)가 가슴뼈를 박살 내고 피와 살을 태웠다.

“꺼허어어.”

마지막 단말마와 함께 사자의 눈동자에서 빛이 사라졌다.

놈의 가슴에서 주먹을 뽑아낸 철무백이 이소월을 향해 몸을 돌렸다.

“백번 죽어 마땅한 놈이었다.”

“저도 같은 생각이에요. 다만…….”

천천히 자리에서 일어난 이소월이 말을 이었다.

“이제 싸움을 피할 수 없겠군요.”

반 시진 후, 항산검문의 모두는 사방에서 울리는 뿔피리 소리를 들을 수 있었다.
```

## Final English reading copy

```markdown
# Chapter 112

Mounted bandits openly riding down the main road in broad daylight?

Under normal circumstances, it would be unthinkable. The nearest Murim sect would be the first to act, followed by the soldiers from the local authorities.

But if there were hundreds of mounted bandits—enough to overwhelm even the Murim sect that was supposed to suppress them—the officials could only close their eyes and cover their ears.

Just like now.

“Ar-aren’t those mounted bandits?”

“Don’t call them ‘those guys.’ Do you have three lives or something? They’re the infamous Red Wind Band.”

“The Red Wind Band? Weren’t they defeated by the Mount Heng Sword Sect not long ago?”

“That’s what we thought. But this time seems different. Rumors are already spreading through the marketplace that the Mount Heng Sword Sect won’t escape total destruction.”

“Still, the sect has some ability. Surely they won’t lose to mere mounted bandits…”

“Hey, watch your mouth! The man riding at the front is Pung Yang, the leader of the Red Wind Band. They say he’s a Peak master.”

“What? A Peak master?”

“Yeah. You can’t dismiss them just because they’re mounted bandits. I hear he isn’t merely strong in martial arts—he’s exceptionally clever, too.”

The commoners’ fearful whispers wormed their way into Pung Yang’s ears and those of his mounted bandits.

A subordinate riding on Pung Yang’s right spoke softly.

“Shall I rip those bastards’ mouths apart?”

“Do you want to?”

“If the Leader permits it, I’ll deal with those two first, then turn the entire village into a sea of flames.”

“You’ll kill the old men, capture the young men, and rape the women?”

“Heh heh. Isn’t that what men like us always do? The Mount Heng Sword Sect bastards are probably cowering behind their walls by now, scared out of their wits.”

“They probably are. They’ll be preparing for a final battle by gathering every bit of strength they have.”

“It won’t matter. That’ll just be eggs thrown at a rock. It’s a foregone conclusion that the Leader will wipe out the Mount Heng Sword Sect and take its place.”

“That is why I won’t permit it.”

“What?”

Pung Yang burst into a hearty laugh at his subordinate’s bewildered reaction.

They were all shallow-minded and cruel by nature. That was why they had become mounted bandits—and why Pung Yang kept them close.

*Because they’re easy to handle.*

When his laughter subsided, he spoke.

“Destroying the Datong Branch was part of the war. But if we harm commoners now, all we’ll accomplish is giving the Jin Family of Taiyuan an excuse to intervene.”

“Are they the rulers of Shanxi or something?”

“Not yet. But they will be soon enough. Before that happens, shouldn’t we swallow the Mount Heng Sword Sect and lie flat like dogs?”

“Um, Leader, I’m not doubting your judgment, but… would orthodox factions like the Jin Family of Taiyuan really look favorably on mounted bandits like us?”

“Mounted bandits? Who’s a mounted bandit?”

“What?”

“Last time, I noticed that the Sect Leader of the Mount Heng Sword Sect was quite beautiful.”

Pung Yang’s subordinate blinked several times before finally understanding. The corners of his mouth curled upward.

“She’s of marriageable age, so she’ll need to take a husband.”

“She has two choices: total destruction or marriage.”

“Then what will happen to the Red Wind Band…?”

“We’ll take the heart of it and wear the outer shell. Let’s see… Compared to the others, your face is at least presentable. I’ll make you Master of the Gatekeeper Pavilion.”

“Ha ha ha! I’ll devote my life to serving you!”

As he listened to his subordinate’s laughter, Pung Yang tightened his grip on the reins.

*At last, I’ve made it this far.*

He was a cold and levelheaded man, but his heart pounded at the thought that he had taken another step toward his ambition.

Memories from long ago flickered before his eyes.

*It’s been well over twenty years already.*

Becoming a mounted bandit had been easier and simpler than he had expected. There were only two ways: go looking for them or get caught by them. In Pung Yang’s case, it had been the latter.

When he was young, he had committed a crime and was being taken to the local authorities when a mounted-bandit group attacked. That had been the turning point of his life.

*“Boss, there’s a little one here, too.”*

*“Hm? He’s so skinny that we wouldn’t get more than a few coins for him even if we sold him. Kid, did you get caught pickpocketing?”*

*“No. I killed someone.”*

*“You killed someone? How old are you?”*

*“Thirteen.”*

*“Why did you kill him?”*

*“I hadn’t eaten for three days, and the boss had dumplings…”*

*“Dumplings? Did he take away what you begged for? That would be enough to make anyone snap.”*

*“No. I was hungry, and I didn’t have the strength to beg. He was eating dumplings right in front of me.”*

*“…So you killed him?”*

*“I thought it would be faster to take them and eat them.”*

*“Hey, let this kid go and feed him something. He’s one of us from today.”*

Pung Yang became a mounted bandit that day.

An orphan abandoned by the world, he had wandered from place to place begging for food. He was exceptionally perceptive and quick-witted.

Compared to his past, when he had barely eaten a meal every three days, life as a mounted bandit was lavish.

Robbery? Murder?

To Pung Yang, who had committed murder at the age of thirteen simply because he wanted to eat dumplings, such things were nothing more than what had to be done.

*“Good grief. I’ve been a mounted bandit for more than ten years, but I’ve never seen anyone like you. It’s as if you don’t have a conscience.”*

*“Why? I’m a mounted bandit.”*

*“Kid, that’s not how it works. You gradually get used to it. No one is skilled from the very beginning.”*

*“Were you like that too, Boss? It was easy for me.”*

*“Easy, easy… I’m starting to wonder if I’m raising a tiger cub. How about learning a thing or two about martial arts from me?”*

*“Martial arts?”*

*“Yes, martial arts. You’re still young, so if your bones and martial talent are up to the task, you could become a master.”*

*“Then I’ll call you Master from today onward.”*

*“Master and disciple, my ass. Forget it. Just keep doing what you’re doing now.”*

Not forming a master-disciple relationship had been a wise decision.

A year later, his boss was beheaded and killed by a First Rate master, and Pung Yang found a new nest in another mounted-bandit group.

*“You were under Gwangchil?”*

*“Yes. If you feed me well, I’ll swear my loyalty to you.”*

*“You seem reasonably sharp. I won’t go easy on you because you’re young, so keep up on your own.”*

The plateau was brutal.

There were times when an entire mounted-bandit group was wiped out after attacking the wrong merchant caravan. The struggles for power between mounted-bandit groups never stopped, either.

But Pung Yang survived every time, growing stronger with each passing year.

By the time he turned thirty, his martial arts had entered the First Rate realm, and he managed to seize the position of squad leader in a mounted-bandit group of considerable size.

*But that was as far as I got.*

The law of strength applied everywhere.

The plateau was ultimately just another part of the Murim, where the strong ruled.

Pung Yang possessed grand ambitions and an exceptional mind, but he lacked the martial power befitting a leader.

*The limit of Third Rate martial arts.*

Pung Yang’s martial talent was extraordinary.

If he had entered a prestigious orthodox sect as a child and learned an excellent internal cultivation technique and martial arts, he might have crossed the wall to Peak long ago.

But he had grown up in a beggar’s den and learned Third Rate martial arts from the mounted bandits of the plateau. His limitations were clear.

*If heaven’s fortune hadn’t favored me, I’d probably still be standing in the same place.*

A deep smile settled over Pung Yang’s lips.

Three years ago, on that day, his life had changed completely. He had gone from being a mere squad leader in a mounted-bandit group to the leader of the Red Wind Band, one of the powers moving the plateau—and now it was time to swallow a Murim sect.

“Leader!”

Pung Yang snapped out of his thoughts at his subordinate’s shout.

Far in the distance, stone walls piled high like a fortress had finally come into view.

*The Mount Heng Sword Sect.*

As Pung Yang gazed at his and the Red Wind Band’s new home, one person entered his sight. Even from this distance, he could feel the man’s fiery aura.

*The Tiger of Mount Heng, Cheol Mubaek.*

A wall he would have to overcome in order to take the Mount Heng Sword Sect.

Although he had withdrawn after suffering a slight loss last time…

*Today will be different.*

Pung Yang unconsciously felt inside his robes. After confirming the hard wooden case there, his smile deepened.

“Leader, your orders?”

“Surround them. Don’t let even a single ant escape. Then send an envoy.”

Total destruction or marriage.

The Mount Heng Sword Sect had only two choices.

“I’ll have the Mount Heng Sword Sect in my hands before sunset.”

* * *

“They’ve surrounded our sect without leaving a gap!”

“Their numbers are well over two hundred!”

“Sect Leader, please make a decision!”

Seated in the place of honor, Lee Seowol calmly opened her mouth.

“Are the troops deployed?”

“Of the hundred or so men, half are blocking the sect entrance. The rest have been armed with shields and bows.”

Everyone in the main hall knew that “a hundred or so” was a generous estimate. In truth, they had far fewer than that.

Several of the Mount Heng Sword Sect’s senior figures had fled the previous night, taking their families and the subordinates who followed them.

“Uncle Cheol, what happened with what I asked you to do?”

“It has been arranged as you instructed.”

Lee Seowol’s plan involved oil.

They had spread enough oil to fill ten wagons evenly throughout the estate.

They had covered it with piles of well-dried hay, so it was obvious that the entire area would turn into a sea of flames the moment fire touched it.

*Does she intend for us to perish together with them?*

Cheol Mubaek was worried, but he kept his thoughts to himself. In all the years he had watched Lee Seowol, she had always been calm and clever, even from a very young age.

“We only need to hold out for one day. Exactly one day. Reinforcements from the Jin Family of Taiyuan are on their way, so we have a good chance of winning if we can stall them until then.”

“R-reinforcements from the Jin Family of Taiyuan?”

“I hear the Sleeping Dragon of Shanxi and the Heaven Shaking Sword are coming in person.”

The faces of everyone gathered in the main hall brightened.

The Heaven Shaking Sword, Jin Mukyung, was already renowned throughout the Central Plains as a martial arts genius, while the Sleeping Dragon of Shanxi, Jin Taekyung, was a rising star.

It was uncomfortable that he had earned his fame through a war against the Mount Heng Sword Sect, but knowing that he was now on their side made it feel as though they had gained a thousand troops.

Above all else…

“No matter how bold Pung Yang is, he won’t dare raise his sword against a direct descendant of the Jin Family of Taiyuan.”

“…That’s true.”

Lee Seowol felt bitter inside.

Not long ago, the Mount Heng Sword Sect had stood shoulder to shoulder with the Jin Family of Taiyuan.

Now, a Murim sect that had once commanded northern Shanxi had to focus all its strength on merely holding out against a mounted-bandit group.

*I will never forget what happened today.*

Just then, she bit down hard on her lip.

The doors to the main hall opened, and a martial artist from the Gatekeeper Pavilion came running in, shouting.

“Sect Leader, the enemy has sent an envoy!”

“An envoy?”

“Yes. He says there’s something he wishes to tell you in person…”

Lee Seowol nodded without hesitation.

If they could delay the battle by even a single moment, they had to do everything they could.

“Bring him in.”

Not long after the Gatekeeper Pavilion martial artist withdrew, the Red Wind Band’s envoy was escorted into the main hall.

He exposed his rotten teeth in a crooked grin and bowed deeply in an exaggerated manner.

“I pay my respects to the Sect Leader of the great Mount Heng Sword Sect.”

His attitude was clearly mocking, but the senior figures—and even Cheol Mubaek, whose temper was as fierce as fire—suppressed their anger. Lee Seowol had repeatedly warned them to do so beforehand.

“Why did you send an envoy?”

“Well, shouldn’t you give someone who has come such a long way a bowl of rice wine before asking—gasp.”

The Red Wind Band’s envoy was unable to finish his sentence and began trembling violently.

Cheol Mubaek, unable to contain his anger, had taken one step forward and released an overwhelming aura.

“Do you want rice wine that badly?”

At the deep, heavy voice, the envoy frantically shook his head.

“N-no, sir. I was thirsty, so I said something stu—stupid.”

“Uncle Cheol. That’s enough.”

“…Hmph. Stop talking nonsense and deliver your message.”

Barely freed from Cheol Mubaek’s aura, the envoy stammered.

“T-the Leader says we should stop this pointless war and now cement our friendship.”

“Friendship?”

The senior figures of the Mount Heng Sword Sect doubted their own ears.

Who had betrayed the previous Sect Leader, Lee Cheonbaek, and killed even the Young Sect Leader, Lee Seogwang? And hadn’t they massacred the families and dependents of the Datong Branch only a short while ago?

But Lee Seowol’s reaction was different. Without the slightest hint of surprise, she stared straight at the envoy.

“And if we refuse?”

“He said you won’t escape total destruction.”

“So he means that if we want to save our people, we must offer the Mount Heng Sword Sect in its entirety as a wedding gift.”

“I-I don’t know about anything beyond that…”

At this point, everyone in the main hall understood the meaning of the “friendship” Pung Yang had offered.

All of them were furious, but Cheol Mubaek was the quickest to act.

*Thud!*

In the literal blink of an eye, Cheol Mubaek crossed more than ten *jang* and drove one punch into the envoy’s chest.

The red fist aura carrying horrifying heat shattered his chest bones and burned his blood and flesh.

“Ghuuuh…”

With one final death rattle, the light vanished from the envoy’s eyes.

Cheol Mubaek pulled his fist from the man’s chest and turned toward Lee Seowol.

“He deserved to die a hundred times over.”

“I think so, too. But…”

Lee Seowol slowly rose from her seat and continued.

“We can no longer avoid the fight.”

One hour later, everyone in the Mount Heng Sword Sect heard the sound of horn calls ringing out from all directions.
```
