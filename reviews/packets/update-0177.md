<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0177.txt",
      "sha256": "a3aa37e67c4a5bcd93e19be3ab82ccfdc7e4e9e77f3748a4062cb4dae5470379",
      "bytes": 17551
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9a9edd99ebd877c10353b631035d243187fa7097956c70fca88a6c72c8e596f3",
      "bytes": 5940
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "36f149d4be258ffb82ed40ffab5e34f78257985280722f04699e72d293bad04a",
      "bytes": 44580
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4733cc3cf2905f26fbc411974775a5d6040ed5a2e99ee3225b3f17b1c2d2cdf5",
      "bytes": 1591
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "21e43f866172bad835b4011fb9caad1cf4a7fe81f606d7549145698dd12f5f08",
      "bytes": 24938
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5a0763898bcc052775bcd90f27ef9a6699f68704c09429e83f166441b21e1f67",
      "bytes": 622
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "8f637dde9a4cb15b75ae12449ed9b53d89b42cd00c5ac2e8c6d41da7246584d1",
      "bytes": 3031
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3be60c97b5cd1c10648188fa627119d2896df17672b82760272e3dd68764277f",
      "bytes": 35421
    }
  ],
  "estimated_tokens": 32582
}
-->

# Durable State Update — Chapter 177

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 177. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 177. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 177,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 177,
    "continuity_sources": [177],
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
    "Jeok Cheongang is the nearly one-hundred-year-old Fire King of the Fire Gate Clan, a Supreme Peak master counted among the Ten Kings; his apparent Level 3 reading is false.",
    "Jeok Cheongang is secretive, cryptic, amused by unusual young martial artists, and quick to threaten violence during interrogation. He plans to reach Taiyuan and visit the Lower District Sect while concealing his identity, seeking an unidentified Peak master who mainly uses sword and palm techniques.",
    "Jeok Cheongang once fought Mae Jonghak for seven days and seven nights at Mount Jiuhua and drew; after Demonic Cultists burned Mount Jiuhua, he killed all one thousand attackers.",
    "Jin Taekyung is a Level 71 Peak Master with forty-five years of internal energy, Scorching Yang Qi, and seventy unassigned stat points.",
    "Jin Taekyung killed Jin Baekyang, the Blade of Flowers, and was rendered unconscious with an Internal Injury by Jeok Cheongang’s Flame Divine Palm.",
    "Taekyung revealed a huge supply of Ten-Thousand-Year Cold Iron to Jang Taebo, who committed to forging it into a divine weapon; Find the Master Artisan was completed. Jang Taebo is the retired former Guild Leader of the Ironcraft Guild and a renowned smith over eighty years old.",
    "Jang Taebo’s home was destroyed by the clash between Jeok Cheongang and Taekyung, ending his retirement.",
    "Cheongpung is Mae Jonghak’s grandson and disciple, has fought Jeok Cheongang using Huashan arts, and carries the unconscious Taekyung and Hyuk Mujin to the inn.",
    "Hyuk Mujin is a Level 50 First Rate martial artist, Captain of the Gatekeepers, and Taekyung’s subordinate in the reconnaissance squad.",
    "Jang-pal lives in Jang Family Village with his wife and daughter Hanga; they previously fed and sheltered Jeok Cheongang.",
    "The Datong Branches of the Jin Family of Taiyuan and the Lower District Sect tracked the Heavenly Wind Band before finding its annihilated force.",
    "Jin Baekyang, the Jin Family of Taiyuan’s Head Elder and Taekyung’s great-uncle, died in battle about two months ago and was buried in the family cemetery after Jin Wikyung overrode the family’s opposition.",
    "Jeok Cheongang deduced that Taekyung’s Scorching Yang Qi came from the Blazing Flame Divine Pill because the Fire Gate Clan’s Fire Gate Divine Technique has been preserved through one-person succession without leakage.",
    "Taekyung awakened after at least half a day unconscious with only a minor Internal Injury.",
    "Taekyung possesses Jopil’s Flame Divine Palm manual and Ten-Thousand-Year Cold Iron sword; the consumed Blazing Flame Divine Pill is inside his body.",
    "Jeok Cheongang and Cheongpung had been drinking downstairs for more than three shichen, and Jeok ordered Mujin to report Taekyung’s awakening.",
    "Jeok Cheongang stopped Taekyung and Mujin’s attempted escape from the inn and is confronting Taekyung.",
    "Jangcheon was an orphan rescued by Jeok Cheongang during an epidemic in Anhui Province. Jeok eventually accepted him as his Disciple despite his limited martial talent and physique.",
    "Jangcheon trained with extreme resolve, but later stagnated, visited a pleasure house while claiming to be in closed-door cultivation, and became the killer known as Jopil.",
    "The Azure Sky Sword King, one of the Ten Kings and Grand Family Head of the Nangong Family, reported Jangcheon’s killings to Jeok Cheongang; after the visitor left, Jeok detected the scent of blood."
  ],
  "continuity_sources": [
    176
  ],
  "open_questions": [
    "Who is the unidentified Peak master Jeok Cheongang seeks, and where is that person?",
    "Where can Taekyung find the Herb of Eternal Youth?",
    "Who is the unnamed giant leading the Heavenly Wind Band?",
    "What is the linked Quest generated after Find the Master Artisan?",
    "Who are the tall, handsome martial artists who came looking for Jeok Cheongang?",
    "Why does Qi Sense display Jeok Cheongang as Level 3 despite his Supreme Peak martial ability?",
    "What happened between Jeok Cheongang and Jangcheon after Jeok detected the scent of blood, and how did Jangcheon become Jopil?",
    "How will Jeok Cheongang respond to Taekyung’s possession of the Flame Divine Palm manual and consumption of the Blazing Flame Divine Pill?"
  ],
  "safe_through": 176,
  "temporary_decisions": [
    "Render 삼매진화 as “Samadhi True Fire”; render 정기신 as “essence, qi, and spirit,” 백염 as “white flames,” and 입신지경 as “a transcendent realm.”",
    "Render 어르신 as “elder” and 형님 as “big brother” when used for Jeok Cheongang.",
    "Render 명장 as “Master Artisan,” 장인을 찾아라 as “Find the Master Artisan,” and 가공되지 않은 만년한철 as “Unprocessed Ten-Thousand-Year Cold Iron.”",
    "Render 철기방 as “Ironcraft Guild” and 철기방주 as “Guild Leader of the Ironcraft Guild.”",
    "Render 항아 as “Hanga,” 장팔 as “Jang-pal,” 장가촌 as “Jang Family Village,” and 신령님 as “Mountain Spirit.”",
    "Render 반박귀진 as “Returning to Simplicity,” 이형환위 as “Shifting Form and Position,” 허공섭물 as “Seizing an Object Through Empty Space,” and 백련정강 as “Baekryeon Jeonggang.”",
    "Render 꼰대 as “boomer,” 꼰머 as “boomer-brain,” 국밥 as “gukbap” with a footnote, 작은 조부님 as “great-uncle,” 전사하셨습니다 as “He fell in battle,” and 열화신공 as “Fire Gate Divine Technique.”",
    "Render 장천 as “Jangcheon” meaning “Vast Sky”; 창천검왕 as “Azure Sky Sword King”; 태상가주 as “Grand Family Head”; 벌모세수 as “cleansing the sinews and washing the marrow”; 상단전 as “upper dantian”; and 무극 as “the Martial Extremity realm.”"
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
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이 첨사 | **Assistant Commissioner Li** | Address form for Li Feng |
| 홍 내관 | **Eunuch Hong** | Eunuch and Deputy Military Commissioner of Shanxi Province |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 육합검 | **Six Harmonies Sword** | Huashan sword technique known by Cheongpung. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 상청검 | **Supreme Clarity Sword** | Huashan sword technique listed among Cheongpung's knowledge. |
| 낙화추영장 | **Falling Flower Chasing Shadow Palm** | Huashan palm technique listed among Cheongpung's knowledge. |
| 산화무영수 | **Scattering Flowers Shadowless Hand** | Huashan hand technique listed among Cheongpung's knowledge. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 근위대 갑옷 세트 | **Royal Guard Armor Set** | Armor set Li Feng offers Cheongpung. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 상산왕의 증표 | **Prince Shangshan's Token** | Golden medallion awarded by Zhu Bao as the Quest Reward. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 금성전장 | **Golden Star Exchange** | Financial institution that issued the thousand-nyang bank draft. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 서악 | **Western Peak** | Name for Huashan among the Five Great Mountains. |
| 흑사파 | **Black Serpent Sect** | Dark-path gambling-den gang in Xi’an. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 십팔반병기 | **eighteen traditional weapons** | Training weapons displayed on a rack. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 찍고 땡 | **touch-and-go method** | Repeatedly reaching a destination and returning as an endurance exercise. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 진무량 | **Jin Muryang** | Founder of the Jin Family; legendary martial artist from roughly three hundred years earlier. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 태초 마을 | **Taecho Village** | Place named by Taekyung immediately after surviving the fall. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 낙안봉 | **Falling Goose Peak** | Huashan peak exceeding five hundred jang; Cheongpung climbed it as a child. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 검성 수련 간접 체험기 | **Sword Saint Training: A Secondhand Experience** | Cheongpung's Peak-grade cliff-training Quest. |
| 검성 수련 간접 체험기-2 | **Sword Saint Training: A Secondhand Experience—2** | Linked Quest generated after the first training Quest succeeds. |
| 초보 수련자 | **Beginner Trainee** | System Title upgraded after the tenth cliff climb. |
| 중급 수련자 | **Intermediate Trainee** | System Title received after Beginner Trainee is upgraded. |
| 황하방 | **Yellow River Gang** | Organization involved in a dispute with the Sogong Sect. |
| 소공문 | **Sogong Sect** | Sect involved in a dispute with the Yellow River Gang. |
| 남부상회 | **Southern Merchant Guild** | Merchant organization whose matter is reported to Jin Wikyung. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 내외당 | **Inner and Outer Halls** | The Jin Family's two internal administrative divisions. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 천근추 | **Thousand-Catty Drop** | Technique Cheongpung identifies when Taekyung lifts the spear shaft beneath his foot. |
| 일권복호 | **One Fist Subdues the Tiger** | Named form of the Crouching Tiger Fist. |
| 매화권 | **Plum Blossom Fist** | Huashan fist technique Cheongpung uses in sparring. |
| 천응조 | **Heavenly Eagle Claw** | Huashan claw technique used by Cheongpung. |
| 봉미혈 | **Fengwei acupoint** | Acupoint around the ribs targeted by Cheongpung. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 태극 1장부터 8장까지 | **Taegeuk Forms 1 through 8** | Standard taekwondo pattern sequence Taekyung copied as a child. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 오행매화보 | **Five-Element Plum Blossom Steps** | Footwork technique Cheongpung combines with Dark Fragrance Drift. |
| 백전백패 | **Hundred Battles, Hundred Losses** | Taekyung's proposed teasing nickname for Mujin. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 진라면 | **Jin Ramen** | Instant-noodle brand used in Taekyung's flavor joke. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |
| 매화오품지 | **Plum Blossom Five-Point Finger** | Five-finger technique Cheongpung uses during the duel. |
| 벽을 넘어서 | **Beyond the Wall** | System Quest generated during Taekyung's breakthrough. |
| 절정 고수 | **Peak Master** | System class awarded after Taekyung completes Beyond the Wall. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 텡게르 | **Tengger** | Sky deity invoked by Temur. |
| 대칸 | **Great Khan** | Title of the former ruler whose descendants Temur and Chinggen claim to be. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 흑사대 | **Black Sand Band** | Han-Chinese mounted-bandit force of one hundred. |
| 천풍단 | **Heavenly Wind Band** | Five-hundred-member northern plateau mounted-bandit force subordinate to Black Sand. |
| 천풍단주 | **Heavenly Wind Band Leader** | Leader operating under Black Sand's orders near Datong. |
| 하곡 | **Hequ** | Route and Jin Family branch targeted as the alliance's entry point into Shanxi. |
| 참마검 | **horse-chopping sword** | Heavy saber used by the Human Butcher; rendered descriptively. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 귀환자 | **Returnee** | System Title |
| 명가의 자제 | **Scion of a Prestigious Family** | System Title |
| 승부사 | **Gambler** | System Title |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 가공되지 않은 만년한철 | **Unprocessed Ten-Thousand-Year Cold Iron** | System Item |
| 장인을 찾아라 | **Find the Master Artisan** | System Quest |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 철기방주 | **Guild Leader of the Ironcraft Guild** | Title of the Ironcraft Guild’s leader; the current leader is Jang Taebo’s disciple. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 구방표국 | **Nine-Room Escort Bureau** | Escort Bureau that supplies Jang Taebo with a fifty-year-old He Shou Wu every four months. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 오십 년 묵은 하수오 | **Fifty-Year-Old He Shou Wu** | First Rate Spirit Herb shown in the System Item Window; can provide up to about two years of internal energy. |
| 불로초 | **Herb of Eternal Youth** | Spirit herb said to grant eternal youth and immortality. |
| 불로초를 찾아서 | **In Search of the Herb of Eternal Youth** | System Quest generated after Jang Taebo names the Herb of Eternal Youth. |
| 천검진인 | **Heavenly Sword True Person** | Taoist-style title of the current Sect Leader of Huashan, who once commissioned a sword from Jang Taebo. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 공청석유, 용의 발톱, 여의주 구하기 | **Get Gongcheong Seokyu, a Dragon’s Claw, and a Dragon Pearl** | Quest generated after Jang Taebo makes additional demands; Taekyung rejects it. |
| 천풍 | **Heavenly Wind** | Short form displayed on the Heavenly Wind Band's flag. |
| 장팔 | **Jang-pal** | Woodcutter who meets and helps the unnamed old man. |
| 장 씨 | **Jang** | Surname form used for the woodcutter Jang-pal. |
| 장가촌 | **Jang Family Village** | Clan village where Jang-pal lives. |
| 홍가촌 | **Hong Family Village** | Clan village said to be three hundred li from Jang Family Village. |
| 신령님 | **Mountain Spirit** | Jang-pal's mistaken address for the unnamed old man. |
| 장씨 | **Jang** | Unspaced source variant of 장 씨; surname form for Jang-pal. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 백련정강 | **Baekryeon Jeonggang** | Extremely hard steel used to forge Hyuk Mujin's sword. |
| 강자지존 | **Might Makes Right** | Murim principle invoked as the basis for Mae Jonghak's challenge. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 꼰머 | **boomer-brain** | Related slang term Cheongpung says has a similar meaning. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 부마도위 | **Imperial Son-in-Law** | Imperial title mentioned by Jang Taebo. |
| 천하오대세가 | **Five Great Families** | Expanded source form of 오대세가. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 벌모세수 | **cleansing the sinews and washing the marrow** | Jeok Cheongang’s constitution-improving technique. |
| 상단전 | **upper dantian** | Advanced dantian whose opening signifies entry into the Martial Extremity realm. |
| 무극 | **Martial Extremity realm** | Realm associated with opening the upper dantian. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |

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
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍 내관 | 이풍 | political_rivals | Assistant Commissioner Li | mock-friendly and probing | Uses 우리 이 첨사 and a superficially familiar tone while testing and provoking Li Feng. |
| 이풍 | 홍 내관 | political_rivals | Eunuch Hong / Deputy Military Commissioner | formal but sarcastic | Alternates between the official title and Eunuch Hong to mock his demand for familiarity. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 홍진 | 공일혁 | political_host_to_guest | Great Hero Gong | polite but cutting | Hong Jin uses the respectful title while dismissing Gong Ilhyuk and exposing his poor judgment. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 철우 | 백무성 | junior_disciple_to_senior_brother | Senior Brother | deferential | Uses 대사형 while answering Baek Museong. |
| 은향 | 백무성 | junior_disciple_to_senior_brother | Big Brother; Senior Brother | familiar and casual-polite | Repeatedly calls him 큰 오라버니 even after he insists on 대사형. |
| 홍가 | 장칠득 | older_martial_artist_to_junior_martial_artist | Little Brother Jang | familiar and casual | Hong calls Childeuk 장 아우 after inviting him to address Hong as hyung. |
| 장칠득 | 홍가 | junior_martial_artist_to_older_martial_artist | hyung | deferential, then familiar | Childeuk initially uses Senior and then adopts Hong's requested 형님 address. |
| 장칠득 | 진태경 | servant_to_third_young_master | Third Young Master | formal-deferential | Jang Childeuk addresses Taekyung as 삼공자님 while asking permission to report the dangerous training. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 위팽 | 유생 | senior_retainer_to_scholar | you | familiar and probing | Wipeng uses 자네 while asking the scholar for his assessment. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 테무르 | 인도 | hostile_strangers | you Han Chinese bastard | hostile and contemptuous | Temur insults the seated Han Chinese man before attempting to draw his curved saber. |
| 인도 | 테무르 | intimidating_rival_to_chieftain | friend | cold and taunting | The Human Butcher calls Temur a slow friend after forcing him to sit. |
| 인도 | 흑사 | rival_power_to_rival_power | Black Sand | blunt and familiar | Uses 흑사 while cutting off Black Sand's joking introduction. |
| 흑사 | 인도 | rival_power_to_rival_power | you | playful and taunting | Teases the Human Butcher about being called a butcher without showing fear. |
| 흑사 | 칭겐 | alliance_recruiter_to_recruited_chieftain | Chinggen | lightly teasing and probing | Identifies Chinggen by name while commenting on his composure and perceptiveness. |
| 흑사 | 노인 | subordinate_to_overwhelming_unknown_master | Elder, then big brother; both rejected | deferential and fearful | Black Sand first uses 어르신 and then 형님 while trying to placate the old man; the old man rejects both forms. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 장태보 | 항아 | elder_neighbor_to_child | Hanga | familiar and instructive | Calls the neighboring boy by name while correcting his speech and sending him home after dark. |
| 항아 | 장태보 | child_to_elder_neighbor | Grandpa | childlike-familiar | Repeatedly calls Jang Taebo 할부지. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 혁무진 | 항아 | visiting_adult_to_local_child | little one | coaxing and encouraging | Questions Hanga with an artificially kind smile and offers two food bundles. |
| 진태경 | 장태보 | younger_visitor_to_elder_master | Elder | polite and persistent | Taekyung repeatedly addresses Jang Taebo as 어르신 while requesting his assistance. |
| 장태보 | 진태경 | elder_master_to_younger_visitor | you | gruff and familiar | Jang Taebo uses 자네 while questioning and dismissing Taekyung. |
| 장태보 | 혁무진 | elder_smith_to_young_martial_artist | you / wet-behind-the-ears brat | gruff and insulting | Insults Mujin after Mujin whispers that Jang is senile. |
| 장태보 | 청풍 | elder_smith_to_young_martial_artist | you / lunatic | gruff and incredulous | Initially treats Cheongpung as a lunatic despite recognizing him as Mae Jonghak's disciple. |
| 장팔 | 노인 | stranger_to_elder | Mountain Spirit, then Elder | deferential and apologetic | Jang-pal initially mistakes the old man for a mountain spirit, then shifts to a respectful elder address. |
| 노인 | 장팔 | strangers | you | gruff and familiar | The old man uses 자네 while questioning Jang-pal and accepting his help. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 적천강 | 장태보 | strangers; visiting elder to local smith | Old Man Jang | blunt and familiar | Uses 장 노인 while confirming Jang Taebo’s identity. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 장천 | 적천강 | disciple_to_master | Master | deferential and pleading | Jangcheon repeatedly begs Jeok Cheongang to accept him as his Disciple. |
| 적천강 | 장천 | master_to_disciple | you / fool | blunt and gruff | Jeok rejects Jangcheon’s pleas, questions his choices, and threatens to send him down the mountain. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 조필     | **Jopil**          |
| 살성     | **Slaughter Saint**           | —              |
| 남궁세가   | **Nangong Family**               |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 176
- **Aliases:** Fire King
- **Role:** Nearly one-hundred-year-old wandering martial master and the Fire King; he visits Jang Taebo’s home, can detect Qi Sense, can cross more than ten jang in an instant, plans to reach Taiyuan and visit the Lower District Sect while concealing his identity, and once fought Sword Saint Mae Jonghak for seven days and seven nights to a draw at Mount Jiuhua before emerging from seclusion and annihilating one thousand Demonic Cultists there; after striking Jin Taekyung with the Flame Divine Palm, he deduces that Taekyung took the Blazing Flame Divine Pill and confronts him when he tries to flee the inn.
- **Personality:** Secretive, cryptic, sharp-eyed, amused by unusual young martial artists, and casually violent when dissatisfied with an answer.
- **Voice:** Sharp and ringing when calling out, then gruff, dryly teasing, and threatening during interrogation.
- **Relationships:** Visits Jang Taebo and tells him to check on the worried child living nearby; regards Jin Taekyung as an interesting fellow after detecting Qi Sense and interrogates him about the System; fought Mae Jonghak more than forty years ago and was close enough to be considered his kindred spirit; recognizes Cheongpung as Mae’s grandson and calls him a dependable grandson and Mae’s successor; rescued an orphan named Jangcheon during an Anhui epidemic, eventually accepted him as his Disciple, and later learned that Jangcheon became Jopil.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 176
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; Peak Master with forty-five years of internal energy and the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; possesses Jopil’s Flame Divine Palm manual and Ten-Thousand-Year Cold Iron sword; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 71 with 2,400 Fame (+250) and seventy unassigned stat points; completed the Find the Master Artisan Quest after securing Jang Taebo’s agreement to forge his Ten-Thousand-Year Cold Iron into a spear; can roughly copy observed martial forms and copied the Plum Blossom Fist after three days of sparring with Cheongpung; killed Jin Baekyang, the Blade of Flowers, and was rendered unconscious with an Internal Injury by Jeok Cheongang’s Flame Divine Palm
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 176
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 176
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan; dead by this chapter, having left behind the Supreme Peak martial art Flame Divine Palm; he was an orphan named Jangcheon whom Jeok Cheongang rescued after an epidemic in Anhui Province and eventually accepted as his Disciple
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

## Korean source

```text
＃177화



왜 몰랐을까?

그건 혈육처럼 기른 제자에 대한 믿음일 수도 있고, 무관심이었을 수도 있다. 그러나 그날 휘청이는 발걸음으로 산에 올라오던 장천의 몸에는 분명 혈향이 배어 있었다.



‘어디에 다녀오는 길이냐?’

‘아, 사부님.’



제자의 눈동자는 취기와 또 다른 무언가로 불그스름하게 달아올라 있었다.



‘아랫마을에 잠시 다녀왔습니다. 요새 마음이 싱숭생숭하여 술 한 잔 걸쳤지요.’

‘술이라. 그뿐이더냐?’

‘제 입으로 말씀드리기에는 좀. 하하하! 이런 모습을 보여 드려 죄송합니다.’



기녀들이 쓰는 독한 사향(麝香)이 코를 찔렀다. 그러나 그것은 위장을 위해 덧씌운 장막에 불과했다.

적천강은 장막 아래 숨겨진 엷은 혈향을 맡았다. 정마대전 이후 잊고 있던 죽음의 냄새, 살인자의 냄새였다.



‘기루……에 갔었느냐?’

‘역시 사부님을 속일 수는 없군요. 예, 불초 제자가 마음이 심란하여 여색을 탐했습니다.’



오랜만에 마주한 제자는 전혀 다른 사람이 되어 있었다.

무뚝뚝하고 웃음이 없던 소년에서, 아무렇지 않게 자신의 살인을 숨기는 넉살 좋은 살인자로.



‘한데 어쩐 일로 이 야심한 밤에 나와 계십니까? 폐관 수련에는 진전이 있으셨는지요?’

‘……네 얼굴을 본 지 오래된 것 같아 기다리고 있었다.’



무고한 양민 수십 명을 끔찍하게 살해했다고 했다.

천인공노할 죄를 저지른 제자다. 당장이라도 근맥을 끊고 단전을 폐하는 것이 옳았다. 스승이라면 그래야 했다.

하지만.



‘그렇군요. 저도 이렇게 사부님을 뵈니 참 좋습니다.’



빙긋 웃는 장천의 모습에 적천강은 말문이 막혔다. 분노도, 배신감도 들지 않았다. 그저 마음 깊숙한 곳에서 뭔가가 치밀어 올라 먹먹해졌다.

결국 그가 할 수 있었던 말은 하나밖에 없었다.



‘밤이 깊었구나. 이만 쉬어라.’



적천강의 말을 듣고 있던 진태경이 믿을 수 없다는 표정으로 물었다.

“설마 그걸로 끝입니까?”

“그 아이를 믿고 싶었다.”

“이미 다 알고 계셨잖아요. 조필, 아니 장천이 거짓말을 하고 있다는 것도.”

“알았지.”

“그런데도 놈을 놔뒀단 말입니까?”

“그래, 그런데도.”

노쇠한 목소리가 이어졌다.

“혈육이 있느냐?”

“네.”

“노부는 없다. 가장 오래된 기억을 떠올려 봐도 나는 혼자였고, 녀석도 마찬가지였지.”

적천강은 자신의 두 손을 내려다봤다. 검버섯과 주름으로 가득한 손에는 세월이 켜켜이 묻어 있었다.

“내 사부님은 엄한 분이셨다. 그분의 수련은 혹독하고 괴로웠지만 어린 시절의 나는 그것마저 좋았다. 누군가가 나를 생각해 주고, 함께한다는 사실이 기뻤으니까. 사부님은 내가 의지할 수 있는 유일한 사람이었다.”

하지만 스승과의 시간은 짧았다. 그는 다시 홀로 남겨졌고 외로움은 세월 속에서 천천히 무뎌졌다.

저잣거리에서 만두 하나를 지키기 위해 발버둥 치던 한 아이를 만나기 전까지는.

“그 아이가 의지할 사람은 나밖에 없었다. 천하가 손가락질하더라도 나만큼은 녀석을 믿어야 했다.”

어느 순간부터 적천강에게 있어 장천은 제자 그 이상의 존재가 되었다.

하나뿐인 아들이었고, 손자였다. 비록 피는 섞이지 않았지만 혈육 이상의 애정이 있었다.

“하지만 그 아이가 저지른 짓은 너무나도 끔찍했다. 그만 멈추게 만들어야 했지. 어떤 식으로든.”

그전에 제자의 만행을 직접 눈으로 확인하고 싶었다.

창천검왕이 직접 찾아왔다는 것은 이미 모든 심증과 물증이 갖춰져 있다는 뜻이었지만, 그것으로는 부족했다.

“해서 은밀히 뒤를 밟기 시작했다.”

그날 이후 적천강은 제자의 뒤를 쫓았다. 아직 절정의 벽을 넘어서지 못한 장천의 이목을 피하는 것은 쉬웠다.

한 번, 두 번, 열 번…… 처음 느꼈던 절망은 미행이 거듭될수록 엷어졌다.

장천은 여느 한량처럼 기루에 들러 술을 마시고 여자를 안을 뿐이었다. 불콰하게 취해 움막으로 돌아오면 무인의 모습으로 돌아와 성실하게 수련에 임했다.

모든 것들이 아무런 문제도 없어 보였다.

“문득 그런 생각이 들더군. 뭔가 착오가 있었던 것이 아닐까, 어쩌면 남궁세가와 창천검왕이 사람을 잘못 본 것이 아닐까 하는.”

진태경이 기가 찬다는 얼굴로 말했다.

“제 생각엔 적 대협께서 사람을 잘못 보신 것 같은데요.”

적천강이 허탈하게 웃었다.

“그래, 그랬지. 바보같이 애써 외면했던 거지.”

“그래서, 직접 확인하셨습니까?”

“…….”

적천강은 말없이 화주를 병째로 들이켰다.

천장이 흐릿하게 보이는 것은 술이 독해서가 아니라 생생하게 떠오르는 그날의 기억 때문이다.



* * *



푹, 푹, 푹.

짙은 어둠이 내리깔린 홍등가의 어느 뒷골목. 억눌린 신음과 뿜어져 나오는 핏줄기.

예리한 비수로 누군가의 사지를 찌르고 쑤셔 대던 복면인의 뒷모습은 누구보다 익숙했고, 그 어느 때보다 낯설었다.

‘……천아야.’

나지막한 부름에 비수를 쥔 손이 덜컥 굳는다. 천천히 고개를 돌린 복면인과 적천강의 시선이 부딪쳤다.

오랜만에 사부를 만난 제자의 눈매가 반달처럼 휘어졌다.

‘아, 사부님.’

‘지금, 지금 뭘 하는 게냐?’

‘뭘 하긴요. 보시는 대롭니다.’

장천이 히죽 웃으며 비수를 내리찍었다. 푹, 푹, 푹. 사지를 결박당한 중년인이 고통에 몸부림쳤다.

‘당장 그만두어라!’

‘왜 그만둬야 합니까?’

‘……지, 지금 뭐라 했느냐?’

‘오랜만에 나와 보니 별의별 놈들이 설치고 다니더군요. 같잖은 삼류 무공을 믿고 거들먹거리는 낭인, 살만 피둥피둥하게 오른 장사치들과 팔 수 있는 재산이라고는 몸밖에 없는 계집들. 요지경도 이런 요지경이 없습니다.’

장천이 새하얗게 웃었다.

‘이놈도 그중 하나일 뿐입니다. 이런 놈 하나 죽여 봤자 뭐가 문제겠습니까? 살아도 별 의미 없는, 두 발 달린 짐승일 뿐인데.’

적천강은 모든 것이 꿈처럼 느껴졌다. 지난 넉 달간 제자를 지켜보며 품었던 희망은 물거품처럼 사라진 후였다.

‘왜…… 왜 이런 짓을?’

‘제가 강하기 때문입니다.’

장천은 들뜬 목소리로 말을 이었다.

‘강자 지존. 사부님께서 가르쳐 주지 않으셨습니까? 무림은, 아니 천하는 그런 곳입니다. 약자는 강자에게 죽습니다.’

‘고작 그런 이유로 무고한 이들을 죽였느냐?’

‘무고하다니요. 사부님께서 그걸 어찌 아신단 말입니까?’

‘하면 네게 죽은 이들은 어떤 큰 죄를 지었단 말이냐.’

차라리 죽을죄를 지은 자들이었기를 바랐다.

세상 물정 모르고 소처럼 살던 순박한 양민들이 아니라, 그들의 고혈을 빨아먹는 악덕 상인들과 살인을 밥 먹듯이 저지르는 파락호였으면 했다.

하지만…….

‘그야 모르지요.’

‘……!’

‘뭐, 죄 없이 사는 사람이 어디 있겠습니까? 다만 그들은 운이 없었을 뿐입니다. 마침 제 눈에 띈 이놈도 마찬가지고요.’

적천강은 눈앞이 아득해지는 것을 느꼈다.

그가 피붙이처럼 사랑하는 제자는 이미 돌아오지 못할 강을 건넜다.

강 저편으로 넘어간 자들은 다시 돌아오지 못한다. 피에 젖은 살귀(殺鬼)가 되어 평생을 살아갈 것이다.

‘천아야.’

‘예, 사부님.’

십수 년 전, 저잣거리에서 만난 비쩍 마른 어린아이의 얼굴과 피에 젖은 청년의 얼굴이 겹쳐졌다.

‘도대체 무엇이 너를 이렇게 만들었느냐?’

‘그게 무슨 말씀이십니까?’

‘넌, 너는 이런 아이가 아니었다. 약자는 강자에게 죽는다고? 어떻게든 살기 위해 발버둥 치던 과거의 너를 잊었느냐?’

‘잊지 않았습니다. 그렇기에 지금의 제가 있는 거고요.’

‘아니다. 너는 착하고 성실한…….’

‘사부님.’

장천이 부드러운 목소리로 스승의 말을 잘라 냈다.

지금까지 단 한 번도 스승의 말을 끊거나 반박한 적 없는 제자다. 그러나 지금 장천의 입매에는 노골적인 비웃음마저 서려 있었다.

‘사부님을 처음 만났던 그 날을 똑똑히 기억합니다. 며칠을 내리 굶고 저잣거리를 헤매던 중 흙투성이가 된 만두를 주웠지요. 저와 비슷한 처지였던 놈들에게 짓밟히면서도 꾸역꾸역 입에 쑤셔 넣었습니다.’

‘맞다, 살기 위해서였다. 너 또한 한때 약자였다는 사실을 왜 기억하지 못하느냐!’

장천의 입꼬리가 비틀렸다.

‘왕팔, 홍소칠, 소우평.’

‘……?’

‘제게 만두를 뺏으려 했던 열다섯 명 중 셋입니다. 안타깝게도 나머지는 죽고 없더군요.’

제자의 입에서 흘러나온 세 사람의 이름.

그 의미는 명백했다. 그들은 이미 이 세상 사람이 아닐 것이다. 그리고 숨이 끊기는 그 순간까지 엄청난 고통을 겪어야 했을 것이다.

‘놈들은 절 기억하지 못했지만 저는 하루도 잊은 적이 없습니다. 십여 년 전 그날, 흙 묻은 만두를 씹으면서 깨달았으니까요. 이것이 세상이구나. 약자는 짓밟히고 강자는 짓밟는구나. 그러니 내가 강자가 되어야겠다. 강자의 권리를 누려야겠다.’

스산한 목소리로 그날의 다짐을 말하는 장천의 모습에 적천강은 깨달았다.

‘너, 너는.’

‘예. 저는 변한 적이 없습니다. 사부님을 처음 만난 그날부터 지금까지 단 한 번도.’

어둠 속에서 그의 흰 이빨이 드러났다. 장천은 낄낄 웃고 있었다.

‘짜릿했습니다. 처음에는 살려 달라고 애걸하더니 나중에는 죽여 달라고 울부짖더군요. 마침내 조용해지자 가슴 한구석이 허해지지 뭡니까. 기루에서 술을 진탕 마시고 여인을 안아도 그 느낌을 지울 수 없었습니다.’

타고난 살성(殺星)이 아닐 수 없다.

그 공허함을 채우는 방법은 오직 살인밖에 없다. 아마 숨이 끊기는 마지막 순간까지 장천은 살인을 멈추지 않을 것이다.

‘시기가 좋았습니다. 때마침 사부님께서는 수련에 힘쓰시느라 저를 방관하셨고, 덕분에 마음껏 활개 칠 수 있었으니까요.’

적천강은 차라리 귀를 막고 싶었다. 귀를 막고, 눈을 감고, 머릿속에 각인된 오늘의 기억을 지우고 싶었다.

혈육의 정으로 키우던 제자에 대한 배신감과 분노로 몸이 떨렸다.

그러나 그를 가장 힘들게 하는 것은 아직까지도 남아 있는 제자에 대한 애정이었다.

‘물론 저라고 마음이 편했던 건 아닙니다. 넉 달 전이었나? 일을 처리하고 돌아오니 사부님께서 기다리고 계셨지요. 평소와는 다른 모습을 보고 들켰다는 걸 깨달았습니다.’

‘그만하거라.’

‘저를 철석같이 믿으시는 사부님께서 갑자기 제 뒤를 밟았을 리는 없으니 누가 언질을 해 준 것이 분명한데…… 아, 남궁세가가 분명하군요.’

‘닥치라 했다!’

강대한 기파가 휘몰아쳤다. 지금까지 본 적 없던 스승의 진노에 장천이 눈을 동그랗게 떴다.

‘스승님?’

‘놈! 어찌 그 입으로 나를 스승이라 부르느냐! 네가 무슨 짓을 했는지 아직도 깨닫지 못했단 말이냐!’

‘왜 그러십니까? 설마 고작 이 정도 일로 하나뿐인 제자를 버리실 생각이십니까?’

‘고작? 지금 고작이라 했느냐?’

‘스승님은 제게 있어 아버님이나 마찬가지십니다. 천하 만민이 제 허물을 욕하더라도 스승님께서는 이해해 주실 거라 믿었습니다. 제 아버지시니까요.’

아버지. 그토록 듣고 싶었던 단어였건만.

적천강은 이를 악물었다.

‘틀렸다.’

‘틀렸다고요?’

장천이 희미하게 웃었다.

‘한데 왜 저를 당장 쳐 죽이지 않으십니까? 지금도, 지난 넉 달 동안에도 수없이 많은 기회가 있었는데 말입니다.’

‘그건!’

‘제 말이 틀립니까?’

적천강은 말문이 막혔다. 장천의 입에서 나온 말들은 모두 사실이었다. 애써 진실을 외면했고, 정당화시키려 애썼다.

그렇게 해서라도 제자를 믿고 싶었으니까.

그가 입을 연 것은 한참 후였다.

‘네 근맥을 자를 것이다.’

‘근맥이라. 그리고요?’

‘단전을 폐하겠다. 앞으로 남은 일생 동안 네가 지은 죄를 참회하며 지내게 될 것이다.’

‘죽을 때까지 면벽 수련이라. 생각만 해도 끔찍하군요.’

그러나 말과는 달리 장천의 얼굴에는 웃음기가 가득했다.

‘그런데 불초 제자가 잠시 한눈을 판 사이 본문의 문규(門規)가 바뀌기라도 했습니까? 이런 경우에는 볼 것도 없이 즉결 처분인 것으로 압니다만.’

‘……마지막 온정이다. 그러니 당장 그자를 내려놓고 물러서거라.’

장천이 중요한 사실을 잊고 있었다는 듯이 눈을 깜빡였다.

그의 품 안, 전신이 피에 흠뻑 젖은 중년 사내가 가쁜 숨을 이어 나가는 중이었다.

‘아, 이놈이 있었지요.’

서걱. 촤아아악.

적천강은 떨리는 눈빛으로 솟구치는 피분수를 바라봤다.

한 치의 망설임도 없는 손속. 목젖을 베인 사내는 몸을 부르르 떨다 이내 숨이 끊겼다.

‘이것이 네 답이냐?’

‘이미 늦었습니다. 살려 봤자 병신으로 남은 여생을 보내게 될 텐데, 차라리 깔끔하게 죽여 주는 게 더 낫지 않습니까?’

‘너는…… 더 이상 내가 알던 그 아이가 아니로구나.’

‘저는 사부님께서 알던 그 아이가 맞습니다. 처음부터 잘못 알고 계셨던 것뿐이지요.’

‘그만 되었다. 네 악행도 오늘까지니.’

‘절 정말 폐인으로 만들어 평생 면벽 수련만 시킬 생각이십니까?’

은은한 두려움이 묻어 나오는 제자의 얼굴.

적천강은 피가 배어 나오도록 주먹을 꽉 움켜쥐었다. 일 합, 단 일 합이면 장천을 이 세상에서 지울 수 있다.

그러나 스스로 그렇게 하지 못할 것임을 안다.

제자의 근맥을 끊고 무공을 폐하며 가두는 것만이 그가 할 수 있는 최선의 방법이었다.

‘후회하느냐?’

‘후회, 말입니까?’

‘그래. 후회.’

변하는 것은 아무것도 없겠지만 녀석의 입으로 듣고 싶었다.

그러나 다음 순간, 장천의 얼굴 위에서 두려움이 씻은 듯이 사라졌다.

‘안심했습니다.’

‘뭐라?’

‘보지도, 듣지도 못했지만 지난 넉 달 동안 저를 지켜보고 계시다는 건 알고 있었습니다. 그럼에도 제가 사부님의 눈앞에서 이런 짓을 벌인 이유가 뭐겠습니까?’

넋 나간 적천강의 눈동자에 장천의 얼굴이 비쳤다. 그는 여유로운 표정으로 말을 이었다.

‘사부님께서는 저를 죽이실 수 없습니다. 수십이 아니라 수백을 죽여도 마찬가집니다. 떠나기 전, 마지막으로 그걸 확인하고 싶었지요.’

‘떠나기 전이라니. 그게 무슨.’

‘자식의 허물을 탓하는 아비는 있어도 자식을 제 손으로 죽이는 아비는 세상천지 어디에도 없지요.’

‘……!’

‘감사합니다, 사부님. 저를 제자가 아니라 자식으로 키워 주셔서. 이런 자식을 끝까지 살리려고 노력해 주셔서. 덕분에 하나뿐인 생로(生路)가 열렸습니다.’

숨이 멎은 것처럼 굳어 버린 적천강에게 장천은 진심을 담아 큰절을 올렸다.

그리고 다시 고개를 들었을 때, 그의 입술에는 작고 흰 자기병 하나가 물려 있었다.

‘화골분(化骨粉)입니다.’

화골분, 살과 뼈를 녹여 버리는 맹독이다.

아무리 적은 양이라지만 입 안에서 깨진다면 대라신선이 와도 살릴 수 없다.

적천강은 노호성을 터트렸다.

‘장천! 네 이놈!’

‘방금 드린 절은…… 제 마지막 인사입니다. 저는 이 길로 떠나겠습니다. 멀리 떠나서 다시 돌아오지 않겠습니다.’

‘이대로 보내줄 성싶으냐!’

‘그럼 죽이십시오. 방법은 그것뿐입니다.’

‘……!’

‘죽이십시오.’

죽이십시오. 그것이 제자의 마지막 말이었다.



* * *



적천강은 눈을 깜빡였다. 아까부터 천장이 뿌옇다 싶더니, 볼을 타고 뭔가가 흘러내리는 중이었다.

“객잔이 낡았군. 비가 새.”

원단을 하루 앞둔 겨울밤의 일이었다.
```

## Final English reading copy

```markdown
# Chapter 177

*Why hadn't I known?*

It might have been the trust I placed in a Disciple I had raised like my own blood—or it might have been indifference. But there had unquestionably been a scent of blood clinging to Jangcheon when he staggered up the mountain that day.

“Where have you been?”

“Ah, Master.”

His eyes were red from drunkenness—and from something else.

“I went down to the village for a little while. I’ve been feeling restless lately, so I had a drink.”

“Drinking. Was that all?”

“It’s a little embarrassing to say it myself. Hahaha! I’m sorry you had to see me like this.”

The pungent musk courtesans used stung his nose. But that was merely a veil laid over the truth to conceal it.

Jeok Cheongang could smell the faint scent of blood hidden beneath it. It was the smell of death, the smell of a killer—the smell he had forgotten since the Great Faction War.

“You went to a pleasure house…?”

“As expected, I can’t fool you, Master. Yes. This useless Disciple was troubled and sought out women.”

The Disciple he met again after so long had become an entirely different person.

He had gone from a taciturn boy who never smiled to a smooth-talking killer who concealed his murders without the slightest concern.

“But what brings you out at this late hour? Have you made any progress in your closed-door cultivation?”

“…It felt like a long time since I’d seen your face, so I was waiting.”

He had apparently murdered dozens of innocent commoners in horrific ways.

His Disciple had committed a crime that made heaven and earth furious. The right thing to do would have been to sever his Sinews and Meridians and cripple his dantian at once. That was what a Master should do.

But—

“I see. I’m very glad to see you too, Master.”

At Jangcheon’s faint smile, Jeok Cheongang found himself unable to speak. He felt neither anger nor betrayal. Something simply welled up from deep within him and left him choked up.

In the end, there was only one thing he could say.

“It’s late. Go get some rest.”

Jin Taekyung listened to Jeok Cheongang and asked in disbelief,

“Wait. That’s it?”

“I wanted to believe in that child.”

“You already knew everything. You knew Jopil—or rather, Jangcheon—was lying.”

“I knew.”

“And you still let the bastard go?”

“Yes. Even so.”

The old man’s weary voice continued.

“Do you have any blood relatives?”

“Yes.”

“I have none. Even when I recall my earliest memory, I was alone. He was the same.”

Jeok Cheongang looked down at his hands. The hands covered in age spots and wrinkles bore the weight of the years in layer upon layer.

“My Master was a strict man. His training was harsh and painful, but I liked even that when I was young. I was happy that someone cared about me and stayed by my side. My Master was the only person I could rely on.”

But his time with his Master had been short. He was left alone once again, and over the years, his loneliness had slowly dulled.

That was how it had been until he met a child struggling desperately to protect a single dumpling in the marketplace.

“I was the only person that child could rely on. Even if all under heaven pointed fingers at him, I had to believe in him.”

At some point, Jangcheon became more than a Disciple to Jeok Cheongang.

He was his only son and his grandson. Their blood was not connected, but Jeok Cheongang loved him with an affection greater than blood.

“But what that child did was far too horrible. I had to make him stop. Somehow.”

Before that, he wanted to see his Disciple’s atrocities with his own eyes.

The fact that the Azure Sky Sword King had come in person meant that all the circumstantial and physical evidence was already in hand. But that alone was not enough.

“So I began secretly following him.”

From that day on, Jeok Cheongang followed his Disciple. It was easy to avoid Jangcheon’s notice, since he had not yet broken through the wall to the Peak realm.

Once, twice, ten times…

The despair he had felt at first grew fainter with every pursuit.

Jangcheon merely visited pleasure houses, drank, and embraced women like any other wastrel. When he returned to his hut flushed with drink, he resumed his identity as a martial artist and trained diligently.

Everything seemed perfectly normal.

“Then, suddenly, I began to wonder if there had been some mistake. Maybe the Nangong Family and the Azure Sky Sword King had simply misjudged him.”

Jin Taekyung stared at him in disbelief.

“I think you’re the one who misjudged him, Sir Jeok.”

Jeok Cheongang laughed hollowly.

“Yes. I did. Like a fool, I desperately turned away from the truth.”

“So did you confirm it yourself?”

“…”

Jeok Cheongang silently tipped back the bottle and drank straight from it.

The ceiling looked blurry—not because the liquor was strong, but because the memory of that day had risen vividly before his eyes.

* * *

Thud. Thud. Thud.

In a back alley of the red-light district, beneath the thick darkness of night, muffled groans mingled with spurts of blood.

The back of the masked man stabbing and prodding someone’s limbs with a sharp dagger was more familiar than anything—and more foreign than ever.

“…Jangcheon.”

At the quiet call, the hand holding the dagger abruptly froze. The masked man slowly turned his head, and his eyes met Jeok Cheongang’s.

The Disciple’s eyes curved like a crescent moon at the sight of his Master after so long.

“Ah, Master.”

“What… What are you doing?”

“What does it look like? Exactly what you see.”

Jangcheon grinned and drove the dagger down.

Thud. Thud. Thud.

The middle-aged man, his limbs bound, writhed in agony.

“Stop at once!”

“Why should I stop?”

“…W-What did you say?”

“It’s been a long time since I came down here, and all kinds of people are running wild. Wandering martial artists swaggering around because they know a few Third Rate martial arts, merchants with fat bulging from their bodies, and women whose only property they can sell is their own bodies. What a madhouse.”

Jangcheon smiled, showing all his teeth.

“This man is just one of them. What difference does it make if I kill one such person? He’s nothing more than a two-legged beast with no reason to live.”

Everything felt like a dream to Jeok Cheongang. The hope he had held while watching his Disciple for the past four months had already vanished like a bubble.

“Why… Why would you do something like this?”

“Because I’m strong.”

Jangcheon continued in an excited voice.

“Might makes right. Didn’t you teach me that, Master? Murim—or rather, the entire world—is like that. The weak die to the strong.”

“You killed innocent people for that reason?”

“Innocent? How do you know they were innocent, Master?”

“Then what great sin had those you killed committed?”

He had wanted to believe they had deserved death.

He had wanted them to be corrupt merchants who preyed on the blood and sweat of others, or ruffians who committed murder as easily as they ate—not simple commoners who knew nothing of the world and lived like oxen.

But…

“How should I know?”

“…!”

“Who in this world lives without sin? They were merely unlucky. This man who happened to catch my eye was the same.”

Jeok Cheongang felt the world grow distant before him.

The Disciple he loved like his own blood had already crossed a river from which there was no return.

Those who crossed to the other side could never come back. They would live out their entire lives as blood-soaked killing fiends.

“Jangcheon.”

“Yes, Master.”

The face of the emaciated child he had met in the marketplace more than a decade ago overlapped with the face of the blood-soaked young man before him.

“What on earth made you like this?”

“What do you mean?”

“You… You weren’t this kind of child. You say the weak die to the strong? Have you forgotten your past self, struggling desperately just to survive?”

“I haven’t forgotten. That’s why I am who I am now.”

“No. You were kind and diligent…”

“Master.”

Jangcheon cut him off in a gentle voice.

It was the first time the Disciple had ever interrupted or contradicted his Master. But now, even open mockery lingered at the corners of Jangcheon’s mouth.

“I remember the day I first met you very clearly. I had gone hungry for several days and was wandering through the marketplace when I found a dumpling covered in dirt. Even while the others, who were in the same situation as me, trampled me, I forced it into my mouth.”

“That’s right. You did it to survive. Why can’t you remember that you were once weak too?”

The corners of Jangcheon’s mouth twisted.

“Wangpal, Hong Sochil, So U-pyeong.”

“…?”

“They were three of the fifteen who tried to take my dumpling. Unfortunately, the rest were already dead.”

The three names that came from his Disciple’s mouth.

Their meaning was clear. Those three were no longer among the living. And until the moment their breathing stopped, they must have suffered tremendous pain.

“They didn’t remember me, but I never forgot them for a single day. That day, more than a decade ago, as I chewed that dirt-covered dumpling, I realized something. This is what the world is. The weak are trampled, and the strong do the trampling. So I must become strong. I must enjoy the rights of the strong.”

As Jangcheon spoke of the vow he had made that day in a bleak voice, Jeok Cheongang understood.

“You… You…”

“Yes. I never changed. Not once, from the day I first met you until now.”

His white teeth appeared in the darkness. Jangcheon was giggling.

“It was thrilling. At first, they begged me to let them live, but later they wailed for me to kill them. When they finally went quiet, I felt empty inside. Even after drinking myself senseless at a pleasure house and embracing a woman, I couldn’t get rid of that feeling.”

He was a born Slaughter Saint.

The only way to fill that emptiness was murder. Jangcheon would probably never stop killing until the moment his breath left his body.

“The timing was perfect. You happened to be so absorbed in your training that you neglected me, and thanks to that, I could run wild to my heart’s content.”

Jeok Cheongang wanted to cover his ears. He wanted to cover his ears, close his eyes, and erase the memory of that day, which had been branded into his mind.

His body trembled with betrayal and fury toward the Disciple he had raised with the affection of a blood relative.

But what tormented him most was the affection for his Disciple that still remained.

“Of course, it wasn’t as though I felt at ease either. Was it four months ago? I returned after taking care of some business and found you waiting for me. When I saw how different you were from usual, I realized I had been found out.”

“Stop.”

“There was no way you would suddenly follow me when you trusted me so completely, so someone must have tipped you off… Ah, it was obviously the Nangong Family.”

“I said shut up!”

A powerful wave of qi swept through the alley.

At the sight of his Master’s fury—something he had never seen before—Jangcheon’s eyes widened.

“Master?”

“You bastard! How dare you call me Master with that mouth? Have you still not realized what you’ve done?”

“Why are you acting like this? Surely you don’t intend to throw away your only Disciple over something this minor?”

“Minor? Did you just call this minor?”

“Master, you’re like a father to me. I believed that even if everyone under heaven cursed my faults, you would understand. Because you’re my father.”

Father.

It was the word Jeok Cheongang had wanted to hear so desperately.

He gritted his teeth.

“You’re wrong.”

“Wrong?”

Jangcheon smiled faintly.

“Then why don’t you strike me dead right now? You had countless chances, both now and throughout the past four months.”

“That’s—”

“Am I wrong?”

Jeok Cheongang was unable to speak. Everything Jangcheon had said was true. He had deliberately turned away from the truth and tried to justify it.

Because he wanted to believe in his Disciple, even if it took that.

Only after a long time did he finally open his mouth.

“I’ll sever your Sinews and Meridians.”

“My Sinews and Meridians. And then?”

“I’ll cripple your dantian. You’ll spend the rest of your life repenting for the crimes you committed.”

“Face-the-wall meditation until I die. That sounds terrifying.”

Despite his words, Jangcheon’s face was full of laughter.

“But did our sect’s rules happen to change while this useless Disciple was looking the other way? As I understand it, a case like this calls for immediate execution without further examination.”

“…This is my final mercy. Put that man down at once and step away.”

Jangcheon blinked as though he had forgotten something important.

In his arms, the middle-aged man—his entire body drenched in blood—was still struggling to breathe.

“Oh, right. This fellow was here.”

Slash.

A fountain of blood burst into the air.

Jeok Cheongang watched it with trembling eyes.

There had not been even a moment’s hesitation in Jangcheon’s hand. The man’s throat had been cut. He shuddered violently, then breathed his last.

“Is this your answer?”

“It’s already too late. Even if I saved him, he would spend the rest of his life crippled. Wouldn’t it be better to give him a clean death?”

“You… You’re no longer the child I knew.”

“I am exactly the child you knew, Master. You simply misunderstood me from the beginning.”

“Enough. Your evil deeds end today.”

“Do you really intend to cripple me and make me spend the rest of my life facing a wall?”

There was a faint trace of fear on his Disciple’s face.

Jeok Cheongang clenched his fist until blood seeped from his palm. One move—just one move—and he could erase Jangcheon from this world.

But he knew he could not bring himself to do it.

Severing his Disciple’s Sinews and Meridians, crippling his martial arts, and imprisoning him was the best he could do.

“Do you regret it?”

“Regret?”

“Yes. Regret.”

Nothing would change, but he wanted to hear the answer from Jangcheon’s own lips.

Yet in the next moment, all traces of fear vanished from Jangcheon’s face.

“I was relieved.”

“What?”

“I couldn’t see or hear you, but I knew you had been watching me for the past four months. Why else would I have done this right in front of your eyes?”

Jangcheon’s face was reflected in Jeok Cheongang’s vacant eyes. He continued speaking with a relaxed expression.

“You can’t kill me, Master. It wouldn’t matter if I killed not dozens but hundreds. Before I left, I wanted to confirm that one last time.”

“Before you leave? What are you talking about?”

“There may be fathers who blame their children for their faults, but there is no father anywhere in this world who kills his own child with his own hands.”

“…!”

“Thank you, Master. Thank you for raising me as your child rather than your Disciple. Thank you for trying to keep a child like me alive until the very end. Thanks to you, a single path to survival has opened for me.”

As Jeok Cheongang stood frozen, as though his breath had stopped, Jangcheon gave him a deep, sincere bow.

When he raised his head again, a small white porcelain vial was held between his lips.

“It’s Bone-Melting Powder.”

Bone-Melting Powder was a deadly poison that dissolved flesh and bone.

Even a tiny amount would be fatal if the vial shattered inside his mouth. Not even a celestial immortal could save him.

Jeok Cheongang let out a furious roar.

“Jangcheon! You bastard!”

“That bow I just gave you… was my final farewell. I’m leaving now. I’ll go far away and never return.”

“You think I’ll let you leave like this?”

“Then kill me. That’s the only way.”

“…!”

“Kill me.”

*Kill me.*

Those were his Disciple’s final words.

* * *

Jeok Cheongang blinked. The ceiling had seemed blurry for a while, but now something was running down his cheek.

“The inn is old. Rain must be leaking through.”

It had been the night before New Year’s Day.
```
