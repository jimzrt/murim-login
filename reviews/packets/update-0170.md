<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0170.txt",
      "sha256": "d54a3c8e9372e5688ab2e680af9639b57ff79ff1879371d14a6bf4692b882224",
      "bytes": 14292
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2ab4c917a9cf388e1f9b55453092daf717a31060d75b79ce51bccad1457d4742",
      "bytes": 5456
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "23e315af2cbaa3d9619953bbec66b35b91d8349b1e9c38a4cc5906898e9ddc0c",
      "bytes": 42639
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "f8a5cbc843f87456cb5241ab410a35e83521089190cec56a2450a63416d17bd0",
      "bytes": 543
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "827fe80de20fd72af32357b3dd366be91011c2bfb624b612839dda396402c45f",
      "bytes": 5558
    },
    {
      "path": "characters/Jang Taebo.md",
      "sha256": "af75a2a18d9834b3ce2b1872e9073f3fdee819e80328efa2268666a3237596d1",
      "bytes": 1033
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4f40f32f199dec639bb9e8e7d682a8b22da34e6cb650f471a02aeb23d9831393",
      "bytes": 33413
    }
  ],
  "estimated_tokens": 29296
}
-->

# Durable State Update — Chapter 170

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 170. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 170. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 170,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 170,
    "continuity_sources": [170],
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
    "The unnamed old man is a Supreme Peak master nearing one hundred years old whose old age causes increasingly long periods of unconsciousness; he delayed its effects for roughly twenty years with two jiazi of internal energy and can use Samadhi True Fire and overwhelmingly potent Scorching Yang Qi.",
    "The old man is searching for an unidentified Peak master who mainly uses a sword and palm techniques; Black Sand attempted to manipulate his senility to obtain his martial arts, but the old man killed Black Sand with a single palm while Chinggen and Temur survived.",
    "The old man left the Northern Gaoyuan for Datong on the Shanxi–Gaoyuan border and said he would return in about a month.",
    "Jin Taekyung is a Level 71 Peak Master with forty-five years of internal energy and seventy unassigned stat points.",
    "Taekyung completed the Find the Master Artisan Quest after Jang Taebo agreed to personally forge his Ten-Thousand-Year Cold Iron into a spear; a linked Quest was generated.",
    "Jang Taebo is the retired former Guild Leader of the Ironcraft Guild and a renowned smith over eighty years old who spent a full jiazi at the forge.",
    "Jang Taebo has lived anonymously near Jeongyang for more than ten years, refuses commissions, and now agrees to personally forge Taekyung's weapon after seeing his enormous supply of Ten-Thousand-Year Cold Iron.",
    "Jang Taebo receives a fifty-year-old He Shou Wu from the Nine-Room Escort Bureau every four months; its leader owes him a favor.",
    "The current Guild Leader of the Ironcraft Guild is Jang Taebo's disciple, learned by watching Jang Taebo work, and the guild has close ties to the Nine Sects and One Gang.",
    "Taekyung seeks information about the Fire King and will consult Jin Wikyung before deciding whether to learn the Flame Divine Palm.",
    "Hyuk Mujin knows that Taekyung obtained the Flame Divine Palm martial arts manual after the Eight Spring Gorge battle and once offered it to him.",
    "Wipeng has recognized that Taekyung crossed the wall and reached the Peak realm.",
    "Wipeng reported unusual mounted-bandit activity near Datong.",
    "More than four hundred Heavenly Wind Band mounted bandits led by an unnamed giant turned south to attack and plunder the Jin Family of Taiyuan before an unidentified old man confronted them.",
    "Cheongpung joined Taekyung and Mujin on the journey to Jeongyang and has never seen a blacksmith before.",
    "Hanga is a local boy living near Jang Taebo and Jang Taebo's only conversational companion.",
    "The System generated In Search of the Herb of Eternal Youth after Jang Taebo named the Herb of Eternal Youth, and Taekyung rejected it.",
    "The Datong Branches of the Jin Family of Taiyuan and the Lower District Sect were established about one month ago and had tracked the Heavenly Wind Band for nearly half a month before finding its annihilated force.",
    "The unnamed old man annihilated the Heavenly Wind Band, primarily using Scorching Yang Qi; the Heavenly Wind Band Leader survived nearly two days, identified the attacker as an old man, and then died.",
    "The old man met the woodcutter Jang-pal on an unnamed mountain, accepted his rice ball, and is being carried toward Jang Family Village."
  ],
  "continuity_sources": [
    169
  ],
  "open_questions": [
    "Who is the unnamed Supreme Peak master, and what is his relationship to the Peak master he seeks?",
    "Who is the unidentified Peak master being sought, and where is that person?",
    "Where can Taekyung find the Herb of Eternal Youth?",
    "Is the Fire King alive or dead, and where can he be found?",
    "Who is the unnamed giant leading the Heavenly Wind Band?",
    "Who is the unidentified old man who confronted and annihilated the Heavenly Wind Band?",
    "What is the linked Quest generated after Find the Master Artisan?"
  ],
  "safe_through": 169,
  "temporary_decisions": [
    "Render 삼매진화 as “Samadhi True Fire.”",
    "Render 정기신 as “essence, qi, and spirit,” 백염 as “white flames,” and 입신지경 as “a transcendent realm.”",
    "Render 어르신 as “elder” and 형님 as “big brother” when Black Sand addresses the old man, preserving the old man's rejection of both forms.",
    "Render 명장 as “Master Artisan,” 장인을 찾아라 as “Find the Master Artisan,” 가공되지 않은 만년한철 as “Unprocessed Ten-Thousand-Year Cold Iron,” 하수오 as “He Shou Wu,” and 오십 년 묵은 하수오 as “Fifty-Year-Old He Shou Wu.”",
    "Render 철기방 as “Ironcraft Guild” and 철기방주 as “Guild Leader of the Ironcraft Guild.”",
    "Render 오향장육 as “five-spice pork,” 집성촌 as “clan village,” 야장 as “smith,” 항아 as “Hanga,” 여의주 as “dragon pearl,” and 신병이기 as “divine weapon.”",
    "Render 구방표국 as “Nine-Room Escort Bureau,” 영초 as “Spirit Herb,” 불로초 as “Herb of Eternal Youth,” 불로초를 찾아서 as “In Search of the Herb of Eternal Youth,” and 공청석유, 용의 발톱, 여의주 구하기 as “Get Gongcheong Seokyu, a Dragon’s Claw, and a Dragon Pearl.”",
    "Render 천풍 as “Heavenly Wind,” 장팔 as “Jang-pal,” 장가촌 as “Jang Family Village,” 홍가촌 as “Hong Family Village,” and 신령님 as “Mountain Spirit.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 노부      | **this old man / I**                                            |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 평화 | **Peace Guild** | Guild name. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 장가촌 | **Jang Family Village** | Clan village where Jang-pal lives. |
| 홍가촌 | **Hong Family Village** | Clan village said to be three hundred li from Jang Family Village. |

## Listed compact profiles

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 167
- **Aliases:** None
- **Role:** Local village boy who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 168
- **Aliases:** None revealed
- **Role:** Level 50 First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; has accepted Jin Taekyung’s invitation to train alongside Taekyung and Cheongpung in Taekyung’s private training ground
- **Personality:** Young, disciplined, persistent, and possessed of clear martial talent; suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jang Taebo.md

# Jang Taebo (장태보)

- **Safe through:** Chapter 168
- **Aliases:** None
- **Role:** Former Guild Leader of the Ironcraft Guild and one of the world’s renowned smiths; spent a full jiazi working at the forge before retiring and living anonymously for more than ten years in a village near Jeongyang, where he refuses commissions despite remaining a sturdy man in his eighties; after seeing Taekyung’s enormous supply of Ten-Thousand-Year Cold Iron, he agrees to personally forge Taekyung’s spear.
- **Personality:** Blunt, cantankerous, solitary, and proud; values an untroubled retirement and protects his anonymity, while quietly caring for the neighboring boy Hanga.
- **Voice:** Curt, gruff, and dryly teasing; rejects requests with flat finality.
- **Relationships:** His disciple is the current Guild Leader of the Ironcraft Guild; neighboring boy Hanga is his only conversational partner, and Jang Taebo gives him candy while pretending annoyance.

## Korean source

```text
＃170화



‘낡고, 작군.’

그것이 장가촌을 본 노인의 첫 소감이었다.

천천히 흔들리는 지게에 앉아 드문드문 늘어선 가옥들을 바라보던 그가 아무도 알아들을 수 없을 만큼 작은 목소리로 덧붙였다.

“……그리고 평화롭고.”

세월이 흐르긴 한 모양이다. 별거 아닌 풍경에도 몸이 느슨해지고 마음 한구석이 간질거린다.

마치 이십여 년 전의 그 날처럼.

‘그 녀석을 거둘 때도 그랬지.’

문득 오래전 만난 한 아이가 눈앞을 스쳐 지나간다.

평소 같았으면 철전이라도 좀 던져 주거나 무시하고 지나쳤을 텐데, 그날은 평소와 달랐다.

스스로 노환(老患)에 걸렸다는 것을 깨달은 직후이기 때문일까?

간절하게 내민 그 손의 주인을 바라보다가, 자신도 모르게 한마디를 내뱉었더랬다.



‘함께 가겠느냐?’



“어르신. 다 왔습니다.”

나무꾼 장 씨의 목소리에 노인은 불현듯 정신을 차렸다.

어느새 그들은 작은 집 앞에 멈춰 있었다. 나뭇단을 얼기설기 엮어 만든 울타리 안에서 자그마한 뭔가가 불쑥 튀어나왔다.

“아빠!”

“어이쿠, 우리 딸!”

기껏해야 예닐곱 살이나 됐을까, 어린 계집아이가 도도도 뛰어오더니 제 아비의 다리에 철썩 달라붙는다.

지게 위에서 가볍게 뛰어내린 노인이 그 모습을 물끄러미 바라봤다.

“자네 자식인가?”

“아, 예. 맞습니다. 항아야, 인사드려라. 이분은…….”

그러고 보니 아직 노인의 이름도 모른다.

말꼬리를 흐리는 장 씨를 향해 노인이 손을 내저었다.

“통성명은 무슨. 일 없네.”

장 씨가 멋쩍게 웃던 그때, 반짝거리는 눈망울로 노인을 올려다보던 항아가 타박타박 걸어와 그의 앙상한 허벅지를 쳤다.

“할부지!”

“응?”

“할부지는 이름이 뭐야?”

“모른다. 나도 잊었다.”

노인에게는 귀찮음을 피하기 위해 내뱉은 대답이었지만, 장 씨에게는 달랐다.

‘이름도 기억 못 할 정도로 정신이 온전치 못하구나.’

순박한 산골 사람인 그는 이 노인이 퍽 안쓰럽게 느껴졌다.

자식들에게도 버림받고, 거적이나 다름없는 옷을 걸친 채 이대로 거리를 활보하게 둘 수는 없었다.

“어르신, 우선 식사라도 하시지요. 금방 자리를 마련하겠습니다.”

“됐네. 아까 얻어먹은 걸로도 족해.”

“그래도…….”

“찾을 사람이 있어. 시간이 많이 지체돼서 이러니 양해해 주게.”

말을 마친 노인이 멈칫했다.

양해? 입에서 흘러나온 그 단어가 낯설다.

평생 거칠 것 없이 살았던 자신이다. 모두가 노인을 두려워했고 우러러봤다. 내로라하는 무림의 명숙들도 그의 앞에서는 꼬리를 말았다.

한데 만난 지 반 시진도 되지 않은 이 촌부에게는 이런 말이 쉽게 나온다.

‘늙었군. 확실히 늙었어.’

당혹스러워하는 노인의 소맷자락을 누군가 잡아당겼다.

고개를 내려 보니 통통한 젖살이 실룩거린다.

“누구 찾아? 항아 사람 찾는 거 잘해.”

“……그러냐?”

“웅! 어제도 옆옆옆 집에 사는 장 씨 할부지 찾아 줬어.”

“그거 잘했구나.”

“찾았더니 맛있는 거 줬어. 배 터지게 먹었어.”

뜻 모를 소리를 하더니 허리춤에 척 손을 얹었다. 그 표정이 제법 근엄하기까지 하다.

“그리고 사람은 밥을 먹어야 힘을 써. 할부지 나이에는 무쇠를 씹어 먹어도 돼.”

“하, 항아야!”

“으하하하!”

노인은 모처럼 시원하게 웃었다. 이렇게 웃어 본 것이 언제였던가, 족히 십 년은 넘었지 싶다.

웃음을 그친 그가 동글동글한 머리통을 쓰다듬었다.

“그래, 네 말이 맞다. 노부는 무쇠도 씹어 먹을 수 있지.”

“응. 내 말은 항상 맞아.”

뿌듯한 웃음을 지은 항아가 소맷자락을 잡아 집 안으로 이끄는 것을, 노인은 못 이기는 척 따라갔다.

천하장사가 덤벼도 꿈쩍 안 할 그였지만 오늘만큼은 예외다. 무엇보다…….

‘썩 나쁘지 않군.’

이 상황이 은근히 마음에 들었다. 모처럼 평범한 노인이 된 것 같기도 했다.

방 안에 들어서자 곧 장 씨의 부인이 밥상을 내왔다.

“찬이 변변치 않네요.”

그녀의 말처럼 음식은 단출했다. 몇 가지 나물과 잡곡밥. 나름 대접한다고 내온 고깃국은 색도 희멀겋고 맛도 심심했다.

그러나 정성껏 차린 음식이었다. 한눈에 봐도 넉넉한 형편이 아닌 그들은 밥상머리를 차지한 추레한 늙은이를 불청객이 아닌 손님으로 맞아 주었다.

‘거 참.’

노인은 묘한 기분에 휩싸인 채 식사를 끝마쳤다. 항아가 눈을 반짝이며 물었다.

“할부지. 맛있었어?”

“그래, 근래 먹어 본 것 중 가장 맛있었다.”

“그치? 울 엄마가 우리 마을에서 요리 제일 잘해.”

“……그러냐?”

“응!”

그 정도는 아니던데. 노인은 하고 싶은 말을 꿀꺽 삼키고 고개를 주억거렸다.

지금 식사는 맛으로 먹은 게 아니다. 정성으로 먹은 거지.

반면 항아는 그런 줄도 모르고 신이 나서 계속 떠들어 댔다.

“옆옆옆 집 사는 장씨 할부지도 가끔 우리 집 와서 밥 먹어. 어제는 내가 얻어먹었지만. 헤헤.”

흐뭇하게 딸을 지켜보던 장 씨가 말했다.

“항아 이 녀석, 또 어르신 댁에 갔더냐?”

“응, 어제 할부지가 맛있는 거 줬어. 다른 오라버니들도.”

“내가 어르신께 폐 끼치지 말라고 몇 번이나…… 그런데 오라버니들이라니?”

장가촌은 작은 마을이다. 몇 안 되는 젊은이들은 외지로 나가거나 풍운의 꿈을 안고 무림 문파에 투신했다.

남은 이들은 각자 가정을 꾸려서 항아가 오라버니라고 부를 만한 이는 거의 없다고 봐야 한다. 그런데 오라버니라니.

“처음 보는 사람이더냐?”

“으응. 키 크고, 잘생기고, 먹을 것도 이따만큼 많이 줬어. 그래서 내가 할부지 찾아 줬어.”

“찾아 줘? 그들이 어르신을 찾고 있었느냐?”

“몰라. 그냥 할부지를 찾던데? 허리에 막대기도 차고 있는 멋있는 오라버니들이었어.”

“허리에 막대기…… 검?”

무림인, 무림인이 틀림없다.

같은 생각을 떠올린 장 씨 부부의 얼굴이 심각해졌다.

그들 같은 평범한 양민들에게 있어 무림인이란 두려움의 대상이다.

불과 몇 달 전 벌어진 태원진가와 항산검문의 전쟁 당시에도 얼마나 두려움에 떨었던가?

한데 정체를 알 수 없는 무림인들이 지척에 와 있다. 그리고 하나뿐인 딸이 그들과 얽혔다.

장 씨는 초조한 얼굴로 입을 열었다.

“그래서 어찌 되었느냐?”

“데려갔더니 할부지가 소리 질렀어.”

“그, 그 오라버니들이 누구인지는 들었고?”

“들었는데, 까먹었어!”

해맑은 대답이었지만 부모의 가슴에는 먹구름이 꼈다. 장 씨가 황급히 자리에서 일어났다.

“가 봐야겠소. 어르신께서 무슨 봉변이라도 당했을지 몰라.”

“항아 아버지!”

“당신은 여기서 항아랑 있으시오. 살짝 보고만 올 테니까 걱정 말고.”

말과는 달리 방 한구석에 기대어 놓은 도끼를 챙긴다. 기겁한 부인이 만류하려던 그 순간이었다.

“앉아 있게.”

“예?”

“아, 귀 막혔나? 앉으라고.”

잠자코 앉아 있던 노인이 몸을 일으킨다. 앙상한 무릎에서 우두둑, 하는 소리가 들렸다.

“밥도 든든하게 먹었겠다. 산책이나 할 겸 다녀오겠네. 이참에 밥값도 하고.”

멍하니 노인을 바라보던 장 씨가 허탈하게 웃었다.

“어르신께서 갈 곳이 못 됩니다.”

“그 반대지. 그곳은 자네가 갈 곳이 못 돼.”

“여기에 계십시오. 금방 돌아오겠습니다.”

“돌아올 수는 있고?”

노인이 알 수 없는 표정으로 장 씨를 응시했다.

깊고 가라앉은, 심유(深幽)한 눈빛을 마주한 그는 숨이 멎는 듯했다.

“만약 놈들이 조금, 아주 조금이라도 질이 나쁜 놈이라면 자네는 돌아올 수 없을 걸세. 아이를 아비 없이 키울 생각인가?”

눈빛은 찰나의 섬광처럼 빛났다가 사그라졌다.

아무 일도 없었다는 듯 허리를 두드린 노인이 장 씨를 향해 손을 뻗었다.

“이리 주게.”

단지 그뿐이었다. 그러나 장 씨는 뭔가에 홀린 사람처럼 노인에게 도끼를 건네주었다.

“잘 관리했군. 이건 나무를 팰 때만 쓰는 게 좋아.”

날이 선 도끼날을 가만히 들여다보던 노인이 항아를 향해 씩 웃었다. 분위기를 감지한 아이의 커다란 눈망울은 어느새 축축하게 젖어 들어 있었다.

“왜 울상인 것이냐?”

“내가, 항아가 잘못한 것 같아서. 항아가 잘못했어요.”

“그래, 이번에는 네가 잘못한 것이 맞다.”

서러운 울음이 터져 나오려던 그때, 솜이불처럼 푹신하고 부드러운 목소리가 이어졌다.

“그러니 다음부터는 이런 일이 벌어지지 않도록 각별히 주의하여라. 부모님 말씀 잘 듣고. 알겠느냐?”

“으응…… 그런데 할부지.”

“말해 보거라.”

“할부지는 돌아올 수 있어?”

노인은 피식 새어 나오는 웃음을 참을 수 없었다.

“물론. 무쇠도 씹어 먹는 나이인데 뭘 못 할까.”

그때, 잠깐 넋이 나가 있던 장 씨는 정신이 번쩍 들었다.

아무리 그래도 그렇지, 노환을 앓는 노인에게 도끼를 넘겨주다니. 뭔가 홀려도 단단히 홀린 모양이었다.

지금이라도 바로 잡아야 한다.

“어르신, 어서 도끼 이리 주십시오. 이건, 이건 말도 안 됩니…….”

다음 순간, 장 씨는 말을 잇지 못하고 입을 딱 벌렸다. 도저히 믿을 수 없는 광경이 눈앞에 펼쳐졌기 때문이었다.

오독, 오도독.

도끼날이 부러지고 있었다. 물렁한 닭 뼈도 못 씹을 것 같은 누런 이빨이 움직일 때마다, 매일 정성 들여 벼린 도끼날이 똑똑 끊어졌다.

“이, 이게 무슨.”

“자네 아이, 사람 보는 눈이 있더군. 아주 정확했어.”

경악하는 장 씨의 뇌리에 얼마 전 나누었던 노인과의 대화가 스쳐 지나갔다.



‘여기에는 왜 이리 집성촌이 많아? 반 시진 전에도 홍가촌인가 뭔가 하는 게 있더만.’

‘홍가촌이요? 홍가촌은 이곳에서 족히 삼백 리는 떨어져 있을 텐데요. 혹시 다른 곳과 착각하신 것 아닙니까?’

‘내가 겨우 반 시진 전의 일도 기억 못 하는 천치로 보이는가?’



장 씨는 그제야 깨달았다.

지금까지 노인이 했던 모든 말이 거짓이 아니었음을.

그는 평범한 노인이 아니다. 반 시진에 삼백 리를 걷고, 무쇠도 씹어 먹을 수 있는 노인은 평범할 수 없다.

이런 기사(奇事)를 부릴 수 있는 것은 오직 그들뿐이다.

“무림인…….”

다리를 후들거리는 장 씨에게 노인이 물었다.

“그래, 놈들이 어디 있다고?”



* * *



장태보의 입술 사이로 환희에 찬 목소리가 흘러나왔다.

“천하제일의 신병이기(神兵利器)를 만들어 주지.”

띠링.



- 퀘스트 임무를 성공했습니다.

- 퀘스트, [장인을 찾아라]를 성공적으로 완료했습니다.

- 연계 퀘스트가 생성되었습니다.



“…….”

시바, 이럴 줄 알았으면 진작 보여 줄걸. 혁무진도 어이가 없다는 얼굴. 아니, 자세히 보니 경악한 표정이다.

“저, 저게 다 만년한철이라고요?”

나는 턱을 긁적였다. 내가 뭘 알겠어. 그냥 시스템이 만년한철이라고 하니까 그렇구나, 하는 거지.

“어, 그럴걸.”

“아니, 그럴걸이 아니잖습니까!”

“그러게.”

사실 나도 당황스럽다.

앞서 장태보가 만년한철이 있다는 말을 듣고도 별 반응이 없길래 윗물에서 노는 놈들은 만년한철은 기본 템이구나. 그렇게 생각했거든.

그런데 알고 보니…….

‘음료수에 사과향 10퍼센트 첨가. 뭐 그런 건가.’

천하제일의 광물이라더니, 조금씩 떼서 날에 붙일 정도라면 엄청나게 귀하긴 한 모양이다.

다들 만년한철 5퍼센트, 10퍼센트 첨가물을 쓸 때 나만 100퍼센트를 쓸 수 있다는 것도 엄청난 이점이다.

템빨로 먹고 들어간다는 거니까.

“이거라면, 이거라면 내 필생의 역작을 만들 수 있을 걸세.”

장태보가 감격에 못 이겨 몸을 부르르 떤다.

방금 전까지 심드렁하게 튕기던 그 노인네가 맞나 싶을 정도다. 물론 일이 잘 풀렸으니 나야 좋지만.

“이런 엄청난 양의 만년한철을 도대체 어디서 얻었나?”

“비밀입니다.”

“호, 혹시 만년한철이 대량으로 파묻힌 광산이라도 발견한 겐가!”

장태보의 눈이 하이빔마냥 번쩍거렸다. 자신에게는 더 이상 필요한 게 없다더니 지금은 아주…….

“내게 알려 주게!”

나는 냉정하게 고개를 가로저었다. 광산의 위치 따위 모를뿐더러, 사실대로 알려 줄 수도 없다.

“안 됩니다.”

“제발! 내가 이렇게 부탁하겠네!”

“어, 어어, 왜 이러세요?”

이제는 바짓가랑이를 붙잡고 매달린다. 눈동자에는 수십 년 간 외길을 걸어온 장인의 혼이 불타고 있다.

“이보게에-!”

“아이고, 진짜!”

황급히 장태보의 손을 떼어 낸 그 순간.

“여기가 옆옆옆 집에 사는 장씨 할부지…… 니미럴. 그새 옮았네. 아무튼 장 노인 댁이오?”

카랑카랑한 목소리가 고막을 찔렀다.
```

## Final English reading copy

```markdown
# Chapter 170

*Old and small.*

That was the old man’s first impression of Jang Family Village.

Sitting on the slowly swaying wooden carrying frame and gazing at the houses scattered sparsely across the village, he added in a voice so quiet that no one could make out the words,

“…And peaceful.”

It seemed the years had passed after all. Even an insignificant view like this made his body relax and a corner of his heart itch.

Just like that day, twenty-some years ago.

*It was the same when I took that child in.*

Suddenly, a child he had met long ago flashed before his eyes.

Under normal circumstances, he would have tossed the child a few iron coins or simply ignored them and walked on. But that day had been different.

Perhaps it was because he had just realized that he had developed an illness of old age?

He had looked at the owner of that desperately outstretched hand and, without realizing it, spoken a single sentence.

*Will you come with me?*

“Elder, we’re here.”

The woodcutter’s voice brought the old man back to his senses.

They had stopped in front of a small house. Something small suddenly popped out from behind a loosely woven fence made of bundles of branches.

“Dad!”

“Oh, my daughter!”

The little girl, no more than six or seven years old, came pattering over and clung tightly to her father’s leg.

The old man lightly jumped down from the carrying frame and gazed at the scene.

“Is she your child?”

“Ah, yes. That’s right. Hanga, greet him. This gentleman is…”

Come to think of it, he did not even know the old man’s name.

When Jang-pal trailed off, the old man waved his hand.

“No need for names. It’s nothing.”

Just then, Hanga, who had been gazing up at the old man with sparkling eyes, came toddling over and smacked his bony thigh.

“Grandpa!”

“Hm?”

“What’s your name, Grandpa?”

“I don’t know. I’ve forgotten it too.”

The old man had only said it to avoid the annoyance, but Jang-pal took it differently.

*He’s not sound of mind enough to remember even his own name.*

A simple mountain man, Jang-pal felt terribly sorry for the old man.

He could not leave someone who had apparently been abandoned by his children to wander the streets in clothes barely better than rags.

“Elder, why don’t you at least have a meal first? I’ll prepare a place right away.”

“No need. What I ate earlier was enough.”

“Even so…”

“There’s someone I need to find. I’ve already been delayed for quite some time, so I ask for your understanding.”

After finishing his sentence, the old man stopped.

*Understanding?*

The word that had slipped from his mouth felt unfamiliar.

He had lived his entire life without anything holding him back. Everyone had feared and revered him. Even the renowned masters of Murim had tucked their tails between their legs in his presence.

And yet, with this humble villager he had known for less than half a shichen, such words came easily.

*I’ve grown old. I’m definitely old.*

Someone tugged at the old man’s sleeve as he stood there, bewildered.

When he looked down, he saw chubby baby fat quivering in motion.

“Who are you looking for? Hanga is good at finding people.”

“…Is that so?”

“Uh-huh! Yesterday, I found Grandpa Jang from the house three houses over.”

“You did well.”

“When I found him, he gave me something tasty. I ate until I thought my stomach would burst.”

After saying something incomprehensible, she planted a hand on her waist. Her expression was almost solemn.

“And people have to eat to have strength. At Grandpa’s age, you can chew iron and eat it.”

“H-Hanga!”

“Ha ha ha!”

The old man laughed heartily for the first time in a long while. When was the last time he had laughed like this? It must have been more than ten years ago.

After his laughter faded, he patted Hanga’s round head.

“Yes, you’re right. This old man can chew iron and eat it.”

“Uh-huh. I’m always right.”

With a proud smile, Hanga grabbed his sleeve and led him into the house. The old man followed, pretending he had no choice.

Even if the strongest man under heaven had attacked him, he would not have budged. But today was an exception. More importantly…

*This isn’t so bad.*

He rather liked the situation. It almost felt as though he had become an ordinary old man for once.

As soon as they entered the room, Jang-pal’s wife brought out a meal.

“I’m sorry the side dishes aren’t much.”

Just as she said, the food was simple: a few kinds of namul and mixed-grain rice. The meat soup they had served to make the meal more special was pale and bland.

But everything had been prepared with care. It was obvious at a glance that they were not well-off, yet they welcomed the shabby old man occupying their table as a guest rather than an unwelcome intruder.

*Well, now.*

The old man finished the meal with a strange feeling in his heart. Hanga asked him with sparkling eyes,

“Grandpa, was it tasty?”

“Yes. It was the most delicious thing I’ve eaten lately.”

“Right? My mom cooks the best in the whole village.”

“…Is that so?”

“Uh-huh!”

*It wasn’t that good.*

The old man swallowed the words he wanted to say and nodded.

He had not eaten the meal for its flavor. He had eaten it for the care that went into preparing it.

Hanga, unaware of that, continued chattering excitedly.

“Grandpa Jang from three houses over sometimes comes to our house to eat too. Yesterday I ate at his house, though. Hee hee.”

As Jang-pal watched his daughter fondly, he asked,

“Hanga, you went to the elder’s house again?”

“Uh-huh. Grandpa gave me something tasty yesterday. The other older brothers did too.”

“How many times have I told you not to bother the elder? But what do you mean, older brothers?”

Jang Family Village was a small place. The few young people had either left for other regions or joined Murim sects with dreams of making their fortunes in the martial world.

Those who remained had all started families of their own, so there were hardly any men Hanga could call older brothers. And yet she had mentioned older brothers.

“Were they people you’d never seen before?”

“Uh-huh. They were tall and handsome, and they gave me this much food. So I found Grandpa for them.”

“You found him? Were they looking for the elder?”

“I don’t know. They were just looking for Grandpa. They were cool older brothers with sticks hanging from their waists.”

“Sticks hanging from their waists… Swords?”

They were martial artists. There was no doubt about it.

The faces of Jang-pal and his wife grew serious as they reached the same conclusion.

To ordinary civilians like them, martial artists were objects of fear.

How terrified had they been only a few months ago, during the war between the Jin Family of Taiyuan and the Mount Heng Sword Sect?

And now, unidentified martial artists had come right next door. Worse, their only daughter had become involved with them.

Jang-pal spoke with an anxious expression.

“So what happened?”

“When I took them to Grandpa, he shouted.”

“D-Did you hear who those older brothers were?”

“I heard them, but I forgot!”

Her answer was bright and innocent, but dark clouds gathered over her parents’ hearts. Jang-pal hurriedly rose from his seat.

“I need to go. The elder might have suffered some kind of misfortune.”

“Hanga’s father!”

“You stay here with Hanga. I’ll just sneak over and take a look, so don’t worry.”

Despite his words, he picked up the axe propped in a corner of the room. His horrified wife was about to stop him when—

“Sit down.”

“What?”

“Are your ears clogged? I said sit down.”

The old man, who had been sitting quietly, stood up. His bony knees gave a loud crack.

“I’ve eaten a hearty meal. I’ll take a walk while I’m at it. Consider it payment for the food.”

Jang-pal stared blankly at the old man before giving a hollow laugh.

“Elder, that isn’t a place you can go.”

“It’s the opposite. It’s a place you can’t go.”

“Please stay here. I’ll be back soon.”

“Will you be able to come back?”

The old man stared at Jang-pal with an unreadable expression.

When Jang-pal met those deep, sunken, unfathomable eyes, it felt as though his breath stopped.

“If they’re even a little—just a little—bad, you won’t be able to return. Do you mean to leave your child to grow up without a father?”

The old man’s eyes flashed like a streak of light, then faded.

As though nothing had happened, he patted his lower back and held out a hand toward Jang-pal.

“Give that here.”

That was all.

And yet Jang-pal handed the axe to the old man like someone under a spell.

“You’ve taken good care of it. It’s best to use this only for chopping wood.”

The old man calmly examined the sharp axe blade, then grinned at Hanga. Sensing the atmosphere, the child’s large eyes had already grown wet.

“Why the gloomy face?”

“I think Hanga did something wrong. Hanga was wrong.”

“Yes, this time you were in the wrong.”

Just as a sorrowful cry was about to burst from her, the old man’s voice continued, soft and gentle as a cotton quilt.

“So from now on, pay special attention to make sure something like this doesn’t happen again. Listen to what your parents say. Do you understand?”

“Uh-huh… But, Grandpa.”

“Go on.”

“Will Grandpa come back?”

The old man could not hold back the small laugh that escaped him.

“Of course. I’m old enough to chew iron. What could I possibly be unable to do?”

At that moment, Jang-pal, who had been briefly dazed, suddenly came to his senses.

No matter how you looked at it, he had handed an axe to an old man suffering from an illness of old age. He must have been thoroughly bewitched.

He had to correct this right now.

“Elder, please give me the axe. This, this is ridiculous—”

The next moment, Jang-pal could not finish his sentence. He stood there with his mouth hanging open, because an utterly unbelievable sight had unfolded before his eyes.

Crunch. Crunch.

The axe blade was breaking.

Each time the old man’s yellow teeth moved—teeth that looked incapable of chewing even soft chicken bones—the axe blade Jang-pal had carefully sharpened every day snapped apart piece by piece.

“W-What is this?”

“Your child has a good eye for people. She was exactly right.”

A conversation he had shared with the old man not long ago flashed through Jang-pal’s horrified mind.

*Why are there so many clan villages around here? Less than half a shichen ago, there was something called Hong Family Village or whatever.*

*Hong Family Village? Hong Family Village should be at least three hundred li from here. Are you perhaps confusing it with somewhere else?*

*Do I look like some idiot who can’t even remember something that happened less than half a shichen ago?*

Only then did Jang-pal realize that none of the old man’s words had been lies.

He was not an ordinary old man. Someone who could walk three hundred li in half a shichen and chew iron could not possibly be ordinary.

Only martial artists could perform such extraordinary feats.

“A martial artist…”

The old man asked Jang-pal, whose legs were trembling,

“So where are they?”

* * *

A voice filled with joy escaped between Jang Taebo’s lips.

“I’ll make you the greatest divine weapon under heaven.”

Ding!

> **System**
>
> - Quest objective complete.
> - Quest *Find the Master Artisan* has been successfully completed.
> - A linked Quest has been generated.

“…”

*Shit. If I’d known this would happen, I would’ve shown him sooner.*

Hyuk Mujin looked dumbfounded too. No—looking more closely, he looked horrified.

“Is all of that Ten-Thousand-Year Cold Iron?”

I scratched my chin. What did I know? The System said it was Ten-Thousand-Year Cold Iron, so I simply assumed it was.

“Yeah, probably.”

“No, you can’t just say ‘probably’!”

“I know.”

To be honest, I was flustered too.

When Jang Taebo had shown no reaction after hearing that I possessed Ten-Thousand-Year Cold Iron, I had assumed that people in the upper circles treated Ten-Thousand-Year Cold Iron as basic gear.

But as it turned out…

*Is it like a drink with ten percent apple flavoring added?*

They called it the greatest mineral under heaven, and judging by how people only shaved off tiny pieces to attach to a blade, it really must be incredibly rare.

While everyone else had to use weapons with five or ten percent Ten-Thousand-Year Cold Iron added, I could use one made with one hundred percent.

That was an incredible advantage.

It meant I could rely on my gear to give me a head start.

“With this—with this, I can create the masterpiece of my lifetime.”

Jang Taebo trembled all over, overcome with emotion.

It was hard to believe he was the same old man who had been so indifferent and dismissive only moments ago. Of course, I was happy things had worked out.

“Where on earth did you get such an enormous amount of Ten-Thousand-Year Cold Iron?”

“It’s a secret.”

“H-Have you perhaps discovered a mine where a massive amount of Ten-Thousand-Year Cold Iron was buried?”

Jang Taebo’s eyes flashed like high beams. He had said he no longer needed anything, but now he was—

“Tell me!”

I coldly shook my head. I did not even know where the mine was, and I could not tell him the truth anyway.

“No.”

“Please! I’ll beg you like this!”

“W-Wait, what are you doing?”

Now he was clinging to my trouser leg. The spirit of an artisan who had walked a single path for decades burned in his eyes.

“Come on!”

“Oh, for crying out loud!”

Just as I hurriedly pried Jang Taebo’s hands away—

“Is this the house of Grandpa Jang, who lives three houses over…? Damn it. It’s rubbed off on me already. Anyway, is this Old Man Jang’s place?”

A sharp voice stabbed at my eardrums.
```
